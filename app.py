from flask import Flask, request, jsonify, session
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = "super-secret-key-change-this"
# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ----------------------------
# HEALTH CHECK
# ----------------------------
@app.route("/")
def home():
    return jsonify({"message": "PDF SaaS Backend Running"})


# ----------------------------
# SET SESSION FROM FRONTEND
# (after login in Supabase JS)
# ----------------------------
@app.route("/set-session", methods=["POST"])
def set_session():
    data = request.json
    access_token = data.get("access_token")

    if not access_token:
        return jsonify({"error": "No token provided"}), 400

    # Get user from Supabase
    user = supabase.auth.get_user(access_token)

    if not user or not user.user:
        return jsonify({"error": "Invalid session"}), 401

    session["user"] = user.user.id

    return jsonify({
        "message": "Session set successfully",
        "user_id": user.user.id
    })


# ----------------------------
# GET CURRENT USER
# ----------------------------
@app.route("/me")
def me():
    user_id = session.get("user")

    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    return jsonify({"user_id": user_id})


# ----------------------------
# LOGOUT
# ----------------------------
@app.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})


if __name__ == "__main__":
    app.run(debug=True)