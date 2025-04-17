import requests
import csv
import time
import os

# Set up request URL and Query
url = "https://leetcode.com/graphql/"
query = """
query userProgressQuestionList($filters: UserProgressQuestionListInput) {
  userProgressQuestionList(filters: $filters) {
    totalNum
    questions {
      translatedTitle
      frontendId
      title
      titleSlug
      difficulty
      lastSubmittedAt
      numSubmitted
      questionStatus
      lastResult
      topicTags {
        name
        nameTranslated
        slug
      }
    }
  }
}
"""

def load_cookie(cookie_path="./cookies.txt"):
    if not os.path.exists(cookie_path):
        raise FileNotFoundError(f"Cookie file not found at {cookie_path}")
    with open(cookie_path, "r") as f:
        return f.read().strip()

def extract_csrftoken(cookie_str):
    for part in cookie_str.split(";"):
        if "csrftoken" in part:
            return part.split("=")[1].strip()
    return ""

def fetch_questions_by_page(page, limit=50):
    """Fetch questions by page number"""
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/progress/?page={page}",
        "x-csrftoken": csrf_token,
        "cookie": cookie_str,
        "User-Agent": "Mozilla/5.0"
    }
    
    payload = {
        "operationName": "userProgressQuestionList",
        "variables": {
            "filters": {
                "skip": (page - 1) * limit,
                "limit": limit
            }
        },
        "query": query
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def save_to_csv(questions, filename="solved_problems.csv"):
    fieldnames = [
        "Id", "Title", "Title Slug", "Difficulty", "Status", 
        "Last Submitted", "Submitted Count", "Last Result", "Topic Tags"
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for q in questions:
            # Convert topic tags list to a string
            topic_tags = ", ".join([tag["name"] for tag in q.get("topicTags", [])])
            
            writer.writerow({
                "Id": q.get("frontendId", ""),
                "Title": q.get("title", ""),
                "Title Slug": q.get("titleSlug", ""),
                "Difficulty": q.get("difficulty", ""),
                "Status": q.get("questionStatus", ""),
                "Last Submitted": q.get("lastSubmittedAt", ""),
                "Submitted Count": q.get("numSubmitted", ""),
                "Last Result": q.get("lastResult", ""),
                "Topic Tags": topic_tags
            })

# Load cookie and extract csrf token
cookie_str = load_cookie()
csrf_token = extract_csrftoken(cookie_str)

# Initialize variables
all_questions = []
page = 1
limit = 50
last_page_count = -1

print("Starting to fetch LeetCode problems...")

while page <= 100:
    print(f"Fetching page {page}...")
    
    data = fetch_questions_by_page(page, limit)
    
    # Check if the data structure is correct
    if "data" not in data or "userProgressQuestionList" not in data["data"] or "questions" not in data["data"]["userProgressQuestionList"]:
        print(f"Failed to fetch questions or unexpected data structure: {data}")
        break
    
    questions = data["data"]["userProgressQuestionList"]["questions"]
    current_page_count = len(questions)
    
    # If no questions returned or the same questions as the previous page (reached the end)
    if not questions or current_page_count == 0:
        print("No more questions to fetch.")
        break
    
    # If we got the same number of results as the previous page, we might have reached the end
    if current_page_count == last_page_count:
        # Check first item to see if it's the same as the previous page
        if len(all_questions) >= current_page_count and questions[0]["frontendId"] == all_questions[-current_page_count]["frontendId"]:
            print("Reached the last page of results.")
            break
    
    all_questions.extend(questions)
    last_page_count = current_page_count
    
    # Add a short delay between requests
    time.sleep(1)
    page += 1

print(f"\nFetched a total of {len(all_questions)} problems.")
save_to_csv(all_questions)