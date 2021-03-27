from application.config.routes import app

if "__main__" == __name__:
    # app.run(port=8080)
    app.run(debug=True, port=8080)
