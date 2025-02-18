from flask import Flask, request, jsonify
from flask_cors import CORS  # Ensure this is included

app = Flask(__name__)
CORS(app)  # Enables CORS for frontend integration

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    handle = data.get("handle")
    email = data.get("email")

    if not handle or not email:
        return jsonify({"error": "Handle and email are required"}), 400

    # Placeholder response for now
    result = {
        "platform": "Instagram" if "instagram" in handle else "Website",
        "summary": "Your engagement rate is good, but you should post more frequently!",
        "details": {"suggestion": "Increase posting frequency and use relevant hashtags."}
    }
    
    return jsonify(result)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Ensure it's running on all interfaces
