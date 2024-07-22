from flask import Flask, render_template, request, jsonify
from main import load_knowledge_base, find_best_match, get_answer_for_question, save_knowledge_base

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    if request.method == "POST":
        data = request.get_json()
        user_input = data["question"]
        knowledge_base = load_knowledge_base('knowledge_base.json')
        if knowledge_base is None:
            return jsonify({"answer": "Tôi không thể trả lời câu hỏi này. Vui lòng thử lại sau."})
        best_match = find_best_match(user_input, knowledge_base.keys())
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            return jsonify({"answer": f"{answer}"})
        else:
            return jsonify({"answer": "Xin lỗi. Tôi không biết câu trả lời. Bạn có thể hỏi tôi câu khác được không?"})

if __name__ == "__main__":
    app.run(debug=True)

