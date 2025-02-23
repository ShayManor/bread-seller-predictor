from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


from ask_ai import ask_ai
from flask import jsonify

@app.route("/get_feedback", methods=["POST"])
def get_feedback():
    data = request.get_json()
    essay = data.get("essay", "").strip()
    
    if not essay:
        return jsonify({"error": "No essay provided"}), 400
    
    prompt = f"Please provide constructive feedback to improve the following essay:\n\n{essay}"
    feedback = ask_ai(prompt)
    
    return jsonify({"feedback": feedback})


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "templates/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
