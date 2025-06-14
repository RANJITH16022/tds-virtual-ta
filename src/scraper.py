import json

# Simulated data (replace with real scraping later)
def scrape_discourse_posts(start_date, end_date, discourse_url, output_file='discourse_data.json'):
    posts = [
        {
            "title": "GA5 Question 8 Clarification",
            "content": "Use the model mentioned in the question.",
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
            "created_at": "2025-02-01"
        },
        {
            "title": "GA5 Question 8 Clarification",
            "content": "Use a tokenizer like tiktoken.",
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
            "created_at": "2025-02-01"
        }
    ]
    with open(output_file, 'w') as f:
        json.dump(posts, f)
    print(f"Saved {len(posts)} posts to {output_file}")

if __name__ == '__main__':
    scrape_discourse_posts('2025-01-01', '2025-04-14', 'https://discourse.onlinedegree.iitm.ac.in')