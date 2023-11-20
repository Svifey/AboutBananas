from flask import Flask
import os
app = Flask(__name__)

app_root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    index_path = os.path.join(app_root, 'index.html')
    return open(index_path).read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)