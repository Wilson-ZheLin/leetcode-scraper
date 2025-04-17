# LeetCode Scraper

A simple Python script to extract your LeetCode problem history and export it to a CSV file.

## Example Output:

| Id  | Title                   | Title Slug             | Difficulty | Status | Last Submitted      | Submitted Count | Last Result | Topic Tags                  |
|-----|-------------------------|------------------------|------------|--------|---------------------|----------------|-------------|----------------------------|
| 1   | Two Sum                 | two-sum                | Easy       | AC     | 2023-05-15 13:24:25 | 5              | Accepted    | Array, Hash Table          |
| 53  | Maximum Subarray        | maximum-subarray       | Medium     | AC     | 2023-06-02 09:15:30 | 3              | Accepted    | Array, Dynamic Programming |
| 200 | Number of Islands       | number-of-islands      | Medium     | AC     | 2023-06-10 22:18:45 | 2              | Accepted    | DFS, BFS, Union Find       |
| ... | ...                     | ...                    | ...        | ...    | ...                 | ...            | ...         | ...                        |

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Copy your LeetCode cookies to `cookies.txt` file
   - Login to LeetCode in your browser
   - Open developer tools (F12 or right-click > Inspect)
   - Go to Network tab
   - Refresh the page and select any request to LeetCode
   - Find the Cookie in Headers section and copy its content to cookies.txt
2. Run the script:
   ```
   python leetcode_scraper.py
   ```
3. The script will generate a CSV file with all your problem data