"""
Simple web application — intentionally contains security vulnerabilities
for testing the ASPM Quality Gate mechanism.
"""

from flask import Flask, request

app = Flask(__name__)

# ── Intentional vulnerability: CWE-95 Improper Neutralization of Directives
# Bandit will flag this as B307 (eval) — CRITICAL severity
@app.route("/calculate")
def calculate():
    expr = request.args.get("expr", "")
    result = eval(expr)          # <-- CRITICAL: eval(user_input)
    return {"result": result}


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)          # <-- HIGH: debug=True in production
