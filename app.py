import os
from flask import Flask
app = Flask(__name__)

@app.route("/", defaults={'path':''})
@app.route("/<path:path>")
def main_handler(path):
    return "You're on {}! {}.".format(os.getenv('ENV', 'not-set'), os.getenv('HELLO_MESSAGE', 'Default hello message!'))

@app.route("/health")
def healthcheck():
    return '{"status": "ok"}', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
