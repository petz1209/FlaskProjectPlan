from flask import current_app as app


@app.route("/api")
def api_index():
    return {"var": "hello world"}