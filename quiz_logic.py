import requests
import json

# --- Prompt Template Builder ---
def build_prompt(topic, num_questions):
    return f"""
You are a quiz-generating AI. Create {num_questions} high-quality multiple-choice questions about the topic: "{topic}".

Each question must:
- Be factually correct and concise
- Have 4 options (A, B, C, D)
- Clearly mention the correct option (A/B/C/D)

Only reply in this JSON format:
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
""".strip()

# --- Internal function to contact Ollama API ---
def call_model_api(prompt, model_name="gemma:2b", timeout=60):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False
            },
            timeout=timeout
        )

        if response.status_code != 200:
            print(f"[ERROR] API call failed with status code: {response.status_code}")
            return None

        raw_output = response.json().get("response", "").strip()

        # Extract JSON from response
        start_idx = raw_output.find("[")
        end_idx = raw_output.rfind("]") + 1
        if start_idx == -1 or end_idx == 0:
            print("[ERROR] JSON structure not found in model output.")
            return None

        json_str = raw_output[start_idx:end_idx]
        return json.loads(json_str)

    except json.JSONDecodeError as json_err:
        print(f"[ERROR] Failed to decode JSON: {json_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"[ERROR] Request failed: {req_err}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

    return None
