from flask import Flask

class Views:
    def __init__(self, app):
        self.app = app

    @app.route("/")
    def index(): 
        return "hello world"

if __name__ == "__main__":
    a = Flask(__name__)
    v = Views(a)
    a.run()
