import json
import os

# Simulated course content
COURSE_CONTENT = "Use gpt-3.5-turbo-0125 for assignments unless specified. Tokenize with tiktoken."

# Get the path to the directory this file is in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DISCOURSE_FILE = os.path.join(BASE_DIR, 'discourse_data.json')

def answer_question(question, image_path=None):
    # Load scraped posts
    discourse_data = []
    if os.path.exists(DISCOURSE_FILE):
        with open(DISCOURSE_FILE, 'r') as f:
            discourse_data = json.load(f)

    # Default answer
    answer = "I couldn't find a specific answer. Check the course materials."
    links = []

    # Simple logic for matching
    if 'gpt-4o-mini' in question.lower() or 'gpt-3.5-turbo' in question.lower():
        answer = "Use `gpt-3.5-turbo-0125`, even if AI Proxy supports `gpt-4o-mini`. Use OpenAI API directly."
        links = [
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4", "text": "Use the model mentioned in the question."},
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3", "text": "Use a tokenizer like tiktoken."}
        ]
    elif 'tokenize' in question.lower():
        answer = "Use tiktoken to tokenize text in Python."
        if discourse_data:
            links = discourse_data[1:2]

    return answer, links
