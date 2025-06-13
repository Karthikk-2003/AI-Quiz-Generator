from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os

# --- Export Quiz to PDF ---
def export_quiz_to_pdf(quiz_data):
    # Create a temporary file path for the PDF
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "quiz_output.pdf")

    # Create PDF canvas
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    y = height - 40
    line_height = 18

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Generated Quiz")
    y -= 30

    # Quiz Content
    c.setFont("Helvetica", 12)
    for idx, q in enumerate(quiz_data):
        question_text = f"Q{idx + 1}: {q['question']}"
        c.drawString(40, y, question_text)
        y -= line_height

        for opt_key, opt_value in q['options'].items():
            option_text = f"   {opt_key}: {opt_value}"
            c.drawString(50, y, option_text)
            y -= line_height

        answer_text = f"   ✅ Answer: {q['answer']}"
        c.drawString(50, y, answer_text)
        y -= line_height + 10

        # Add a new page if needed
        if y < 60:
            c.showPage()
            y = height - 40
            c.setFont("Helvetica", 12)

    c.save()
    return file_path
