"""A small Flask application for the Coursera CI/CD final project."""

import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Return the welcome message."""
    return "Hello from the CI/CD Final Project!\n", 200, {
        "Content-Type": "text/plain; charset=utf-8"
    }


@app.route("/health", methods=["GET"])
def health():
    """Return a JSON health response."""
    return jsonify(status="ok", service="cicd-final-project"), 200


def main():
    """Run the application on port 8000 unless PORT is configured."""
    port = int(os.environ.get("PORT", "8000"))
    print(f"SERVICERUNNING on port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
