# 🐍 LeetCode Scraper

A simple Python script to extract your LeetCode problem history and export it to a CSV file.

## Installation and Usage

1. Clone this repository

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Copy your LeetCode cookies to `cookies.txt` file
   - Login to LeetCode in your browser
   - Open developer tools (F12 or right-click > Inspect)
   - Go to Network tab
   - Refresh the page and select any request to LeetCode
   - Find the Cookie in Headers section and copy its content to cookies.txt

4. Run the script:
   ```
   python leetcode_scraper.py
   ```
   
5. The script will generate a CSV file with all your problem data

## Example Output:

| Id | Title | Title Slug | Difficulty | Status | Last Submitted | Submitted Count | Last Result | Topic Tags |
|----|-------|------------|------------|--------|----------------|-----------------|-------------|------------|
| 42 | Trapping Rain Water | trapping-rain-water | HARD | SOLVED | 2025-04-12T | 32 | AC | Array, Two Pointers, DP, Stack |
| 200 | Number of Islands | number-of-islands | MEDIUM | SOLVED | 2025-04-12T | 11 | AC | Array, DFS, BFS, Union Find, Matrix |
| 68 | Text Justification | text-justification | HARD | SOLVED | 2025-04-12T | 13 | AC | Array, String, Simulation |
| 994 | Rotting Oranges | rotting-oranges | MEDIUM | SOLVED | 2025-04-12T | 48 | AC | Array, Breadth-First Search, Matrix |
| 51 | N-Queens | n-queens | HARD | SOLVED | 2025-04-12T | 14 | AC | Array, Backtracking |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
