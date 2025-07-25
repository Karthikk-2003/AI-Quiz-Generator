import time
from quiz_logic import call_model_api, build_prompt

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# --- Topic-based Smart Model Selection ---
def select_model_by_topic(topic):
    topic_lower = topic.lower()
    if "math" in topic_lower or "calculation" in topic_lower:
        return "mistral"  # Better logical reasoning
    elif "history" in topic_lower or "general knowledge" in topic_lower:
        return "gemma:2b"
    elif "programming" in topic_lower or "python" in topic_lower:
        return "mistral"
    else:
        return "gemma:2b"  # Default fallback

# --- Enhanced Quiz Generator with Retry ---
def generate_quiz(topic, num_questions, model_name=None):
    """
    Generates a quiz using the selected or user-defined model.
    Retries up to MAX_RETRIES times if quiz generation fails.
    """
    model = model_name if model_name else select_model_by_topic(topic)
    prompt = build_prompt(topic, num_questions)

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"[INFO] Attempt {attempt}: Generating quiz using model '{model}'...")
        quiz_data = call_model_api(prompt, model_name=model)

        if quiz_data:
            print(f"[SUCCESS] Quiz generated on attempt {attempt}.")
            return quiz_data
        else:
            print(f"[WARNING] Attempt {attempt} failed. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)

    print("[ERROR] All attempts failed. Could not generate quiz.")
    return None

# Optional wrapper for UI usage
def generate_quiz_with_retry(topic, num_questions, model_name):
    return generate_quiz(topic, num_questions, model_name)
