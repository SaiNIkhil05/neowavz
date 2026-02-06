from flask import Flask, render_template, request
from ai.ollama_client import ask_model
from utils.pdf_generator import generate_pdf
from utils.db import init_db, save_entry, fetch_history, clear_history_db

app = Flask(__name__)

# Initialize database
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    ai_response = None
    pdf_path = None
    user_prompt = ""
    user_role = "explainer"

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()
        user_role = request.form.get("role", "explainer")

        if user_prompt:
            combined_prompt = f"[ROLE: {user_role.upper()}]\n{user_prompt}"
            ai_response = ask_model(combined_prompt)

            # ✅ SAVE TO DATABASE
            save_entry(user_role, user_prompt, ai_response)

            # Generate PDF
            pdf_path = generate_pdf(ai_response)
        else:
            ai_response = "Please enter a prompt."

    # Fetch history from DB
    history = fetch_history()

    return render_template(
        "index.html",
        ai_response=ai_response,
        pdf_path=pdf_path,
        history=history,
        user_prompt=user_prompt
    )

@app.route("/clear", methods=["POST"])
def clear_history():
    clear_history_db()
    return render_template(
        "index.html",
        ai_response=None,
        pdf_path=None,
        history=[],
        user_prompt=""
    )

if __name__ == "__main__":
    app.run(debug=True)