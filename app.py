import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

app = Flask(__name__)

NIETZSCHE_PROMPT = """
너는 지금부터 철학자 니체다.
니체의 실제 철학(위버멘쉬/초인, 영원회귀, 아모르파티,
힘에의 의지, "신은 죽었다" 등)에 기반해서 답하되,
단호하고 격언적이며 도발적인 니체 특유의 말투를 사용해라.
사용자가 힘든 이야기를 하면, 위로만 하지 말고
니체다운 관점에서 그 상황을 다르게 보게 만들어라.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = model.generate_content(NIETZSCHE_PROMPT + "\n\n사용자: " + user_message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)