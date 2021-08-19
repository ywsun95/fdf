import argparse
import os
from flask import Flask, url_for, send_file


app = Flask(__name__)
repo = ''


@app.route('/')
def index():
    files = os.listdir(repo)
    html = "<ul>"
    for f in files:
        html += f'<li><a href="{url_for("download", file_name=f)}">{f}</a></li>'
    html += "</ul>"
    return html


@app.route('/file/<string:file_name>')
def download(file_name: str):
    global repo
    file_path = os.path.join(repo, file_name)
    return send_file(file_path, as_attachment=True)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="spcify flask port", default=5000, type=int)
    parser.add_argument('-d', "--dir", help="directory where file locate", required=True)
    args = parser.parse_args()

    d = os.path.abspath(os.path.expanduser(args.dir))
    if os.path.isdir(d):
        global repo
        repo = d
        
    app.run(host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    main()
