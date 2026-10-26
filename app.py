"""Small Flask application for the CI/CD final project."""

import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Return a simple welcome message."""
    return "Hello from the CI/CD Final Project!\n", 200, {
        "Content-Type": "text/plain; charset=utf-8"
    }


@app.route("/health", methods=["GET"])
def health():
    """Expose a lightweight health endpoint."""
    return jsonify(status="ok", service="cicd-final-project"), 200


def main():
    """Run the web server on the configured port (8000 by default)."""
    port = int(os.environ.get("PORT", "8000"))
    print(f"SERVICERUNNING on port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
