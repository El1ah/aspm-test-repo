# ===== ASPM SECURITY FIX =====
# Vulnerability: flask_debug_true
# CWE: CWE-94  Severity: HIGH  Risk: 7/10
# Ensure that `debug=True` is never used in a production environment. The debug mode should be conditionally set based on the application's environment. A common and secure practice is to use environment variables to control this setting.
# 
# For example, modify your `app.py` as follows:
# 
# ```python
# import os
# 
# # ... (your existing Flask app setup)
# 
# if __name__ == "__main__":
#     # Check if the FLASK_ENV environment variable is set to 'development'
#     # Default to False (production-safe) if not explicitly set to development
#     debug_mode = os.environ.get('FLASK_ENV') == 'development'
#     app.run(debug=debug_mode)
# ```
# 
# Then, when deploying to production, ensure that `FLASK_ENV` is not set to `development` (or is set to `production`). When developing locally, you can set `export FLASK_ENV=development` in your terminal before running the app.
# ===== END ASPM SECURITY FIX =====

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
