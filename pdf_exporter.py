import os
import tempfile
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# --- Export Quiz to PDF ---
def export_quiz_to_pdf(quiz_data):
    """
    Exports quiz questions with user answers and correct answers to a PDF.
    Returns the absolute path to the generated PDF.
    """
    try:
        # Create unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quiz_{timestamp}.pdf"
        file_path = os.path.join(tempfile.gettempdir(), filename)

        # Setup PDF canvas
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        y = height - 40
        line_height = 18

        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(40, y, "Quiz Results")
        y -= 30
        c.setFont("Helvetica", 12)

        for idx, q in enumerate(quiz_data):
            # Question
            question_text = f"Q{idx + 1}: {q.get('question', 'Unknown Question')}"
            c.drawString(40, y, question_text)
            y -= line_height

            # Options
            for opt_key, opt_value in q.get("options", {}).items():
                c.drawString(50, y, f"   {opt_key}: {opt_value}")
                y -= line_height

            # Correct & User Answer
            correct_ans = q.get("answer", "")
            user_ans = q.get("user_answer", "Not answered")

            c.drawString(50, y, f"   Correct Answer: {correct_ans}")
            y -= line_height

            if user_ans != "Not answered":
                result = "Correct" if user_ans == correct_ans else "Wrong"
                c.drawString(50, y, f"   Your Answer: {user_ans}   →   {result}")
                y -= line_height
            else:
                c.drawString(50, y, "   Your Answer: Not Answered")
                y -= line_height

            y -= line_height  # Space after each question

            # Start new page if space is low
            if y < 100:
                c.showPage()
                y = height - 40
                c.setFont("Helvetica", 12)

        c.save()
        return file_path

    except Exception as e:
        print(f"[ERROR] Failed to export PDF: {e}")
        return None
