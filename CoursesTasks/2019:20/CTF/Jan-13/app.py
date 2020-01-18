#!/usr/bin/env python

import os
import json

from Crypto.Util.number import getPrime
from Crypto.Cipher import AES

from flask import Flask, request, session, redirect, url_for, render_template


app = Flask(__name__)
key = os.urandom(32)
cipher = AES.new(key, AES.MODE_ECB)

pad = lambda x: x + chr(16 - (len(x) % 16)) * (16 - (len(x) % 16))


with open('flag.txt') as f:
    flag = f.read().strip()

with open('config.json', 'r') as json_data:
    config = json.load(json_data)


def encrypt(text):
    return cipher.encrypt(pad(text)).encode('hex')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        message = request.form.get('message')
        cipher_text = encrypt(message + flag)
        return render_template('index.html', data=cipher_text)


if __name__ == '__main__':
    app.config = dict(app.config, **config)
    app.secret_key = config['secret_key']
    app.threaded = True
    app.processes = 50
    app.run(host=config['host'], port=config['port'])
