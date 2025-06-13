import requests
import json

# --- Prompt Template for Quiz Generation ---
def build_prompt(topic, num_questions):
    return f"""
You are a quiz-making AI. Generate {num_questions} multiple-choice questions on the topic: {topic}.

Each question should have 4 options labeled A, B, C, and D. Indicate the correct answer as one of these letters.

Respond only in this JSON format:
[
  {{
    "question": "Question text?",
    "options": {{
      "A": "Option A text",
      "B": "Option B text",
      "C": "Option C text",
      "D": "Option D text"
    }},
    "answer": "A"
  }},
  ...
]
"""

# --- Generate Quiz using Ollama Mistral ---
def generate_quiz(topic, num_questions):
    prompt = build_prompt(topic, num_questions)

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:
            response_text = response.json().get("response", "").strip()

            # Try to find the first valid JSON array in the response
            try:
                start = response_text.find("[")
                end = response_text.rfind("]") + 1
                if start != -1 and end != -1:
                    quiz_json = response_text[start:end]
                    return json.loads(quiz_json)
            except json.JSONDecodeError:
                print("Error decoding JSON response.")
                return None

        else:
            print(f"Error: Status Code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error during quiz generation: {e}")
        return None
