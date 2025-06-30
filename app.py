from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

# Option 1: get from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Option 2: Or hardcode (not recommended)
# api_key = "your_actual_api_key_here"

client = OpenAI(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_input = request.form["prompt"]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
