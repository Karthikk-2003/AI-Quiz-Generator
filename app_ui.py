import gradio as gr
import subprocess
import requests
from quiz_logic import generate_quiz
from pdf_exporter import export_quiz_to_pdf

ollama_process = None

# --- Ensure Ollama Model is Running ---
def ensure_ollama_running():
    global ollama_process
    try:
        response = requests.get("http://localhost:11434")
        if response.status_code == 200:
            return True
    except:
        pass

    try:
        ollama_process = subprocess.Popen("ollama run mistral", shell=True)
        return True
    except Exception as e:
        print(f"Failed to start Ollama: {e}")
        return False

# --- Generate and Display Quiz ---
def generate_and_display_quiz(topic, num_questions):
    global ollama_process

    if not ensure_ollama_running():
        return "⚠️ Could not start Ollama. Please ensure it's installed.", gr.update(visible=False), *[gr.update(visible=False)] * 10, gr.update(visible=False), []

    try:
        quiz = generate_quiz(topic, num_questions)
        if not quiz:
            return "❌ Failed to generate quiz. Try again.", gr.update(visible=False), *[gr.update(visible=False)] * 10, gr.update(visible=False), []

        display = "\n\n".join([
            f"Q{i+1}: {q['question']}\n" +
            "\n".join([f"  {opt}: {q['options'][opt]}" for opt in q['options']])
            for i, q in enumerate(quiz)
        ])

        radio_updates = [gr.update(visible=(i < num_questions)) for i in range(10)]

        return display, gr.update(visible=True), *radio_updates, gr.update(visible=True), quiz

    except Exception as e:
        return f"❌ Error: {e}", gr.update(visible=False), *[gr.update(visible=False)] * 10, gr.update(visible=False), []

    finally:
        if ollama_process:
            try:
                ollama_process.terminate()
                ollama_process = None
            except Exception as e:
                print(f"Error stopping Ollama: {e}")

# --- Export to PDF ---
def download_pdf(quiz_data):
    if not quiz_data:
        return None
    return export_quiz_to_pdf(quiz_data)

# --- Evaluate Quiz ---
def evaluate_quiz(*user_answers_and_state):
    *user_answers, quiz_data = user_answers_and_state

    if not quiz_data:
        return "⚠️ No quiz data found. Generate a quiz first."

    correct = sum(
        1 for i, q in enumerate(quiz_data)
        if i < len(user_answers) and user_answers[i] == q['answer']
    )
    return f"✅ You scored {correct} out of {len(quiz_data)}"

# --- Gradio Interface ---
with gr.Blocks(title="AI Quiz Generator") as app:
    quiz_state = gr.State([])

    gr.Markdown("# 🤖 AI Quiz Generator\nGenerate topic-based quizzes using your local AI model!")

    with gr.Row():
        topic = gr.Textbox(label="Enter Topic", placeholder="e.g., Machine Learning")
        num_questions = gr.Slider(1, 10, value=5, step=1, label="Number of Questions")

    with gr.Row():
        generate_btn = gr.Button("🚀 Generate Quiz")
        pdf_btn = gr.Button("📄 Download PDF", visible=False)

    quiz_output = gr.Textbox(lines=20, label="Generated Quiz", interactive=False)

    with gr.Accordion("📝 Take the Quiz", open=False):
        answers = {
            str(i): gr.Radio(["A", "B", "C", "D"], label=f"Q{i+1}", visible=False)
            for i in range(10)
        }
        submit_btn = gr.Button("✅ Submit Answers", visible=False)
        result_output = gr.Textbox(label="Your Score", interactive=False)

    # --- Events ---
    generate_btn.click(
        fn=generate_and_display_quiz,
        inputs=[topic, num_questions],
        outputs=[
            quiz_output,
            pdf_btn,
            *[answers[str(i)] for i in range(10)],
            submit_btn,
            quiz_state
        ]
    )

    pdf_btn.click(
        fn=download_pdf,
        inputs=[quiz_state],
        outputs=gr.File()
    )

    submit_btn.click(
        fn=evaluate_quiz,
        inputs=[answers[str(i)] for i in range(10)] + [quiz_state],
        outputs=result_output
    )

app.launch(server_name="127.0.0.1", server_port=7860, share=False, inbrowser=True)
