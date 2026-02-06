from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(text: str, filename: str = "ai_response.pdf") -> str:
    os.makedirs("static", exist_ok=True)
    file_path = os.path.join("static", filename)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 40
    for line in text.split("\n"):
        c.drawString(40, y, line)
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    return file_path