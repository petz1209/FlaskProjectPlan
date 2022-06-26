from app import create_app


if __name__ == '__main__':
    this_app, port = create_app()
    if port == 5001:
        this_app.run(host="0.0.0.0", port=port, debug=True)
    else:
        this_app.run(host="0.0.0.0", port=port)
