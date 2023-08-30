from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!!!!'


@app.route('/incoming', methods=['POST'])
def incoming():
    print("post req")
    return Response(status=200)