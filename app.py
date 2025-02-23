from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


from ask_ai import ask_ai
from flask import jsonify
import csv
from io import StringIO

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    try:
        stream = StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)
        header = next(csv_input)
        data = list(csv_input)
        sales_data = "\n".join([",".join(row) for row in data])
        prompt = f"Here is the daily bread sales data:\n{header[0]},{header[1]}\n{sales_data}\nPredict how much bread to produce tomorrow to keep up with demand."
        prediction = ask_ai(prompt)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "templates/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
