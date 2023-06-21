from flask import Flask

app = Flask(__name__) # creates flask object and links to this module

@app.route("/") # call this function whenever user visits the root (/) page
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port = 5000, debug = True)