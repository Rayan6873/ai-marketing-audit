from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    handle = data.get("handle")
    email = data.get("email")

    if not handle or not email:
        return jsonify({"error": "Handle and email are required"}), 400

    # Placeholder analysis logic
    result = {
        "platform": "Instagram" if "instagram" in handle else "Website",
        "summary": "Your engagement rate is good, but you should post more frequently!",
        "details": {"suggestion": "Increase posting frequency and use relevant hashtags."}
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
