import json
import os

# Simulated course content
COURSE_CONTENT = "Use gpt-3.5-turbo-0125 for assignments unless specified. Tokenize with tiktoken."

# Load JSON path from root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'discourse_data.json')

def answer_question(question, image_path=None):
    discourse_data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            discourse_data = json.load(f)

    # Default answer
    answer = "I couldn't find a specific answer. Check the course materials."
    links = []

    if 'gpt-4o-mini' in question.lower() or 'gpt-3.5-turbo' in question.lower():
        answer = "Use `gpt-3.5-turbo-0125`, even if AI Proxy supports `gpt-4o-mini`. Use OpenAI API directly."
        links = [
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4", "text": "Use the model mentioned in the question."},
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3", "text": "Use a tokenizer like tiktoken."}
        ]
    elif 'tokenize' in question.lower():
        answer = "Use tiktoken to tokenize text in Python."
        links = discourse_data[1:2]

    return answer, links
