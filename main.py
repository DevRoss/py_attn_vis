#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/07/24 12:26:23
@Author  :   rossliang 
@Contact :   rossliang@tencent.com
@Desc    :   None
'''

from argparse import ArgumentParser

from flask import Flask, jsonify, render_template, request, redirect, url_for
import json

app = Flask(__name__)  # 实例化app对象
# app.config["JSON_AS_ASCII"] = False
data_path = 'attn_vis_data.json'


def read_file_to_dict(path):
    d = {}
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            d[i] = line.strip()
    return d


labels = ["X", "O", "[START]", "[END]", "B-address", "B-company", 'B-government', 'B-works', 'B-name',
          'B-organization', 'B-position', 'B-scene', "I-address",
          "I-company", 'I-government', 'I-works', 'I-name',
          'I-organization', 'I-position', 'I-scene',
          "S-address", "S-company", 'S-government', 'S-works',
          'S-name', 'S-organization', 'S-position',
          'S-scene']

data = read_file_to_dict(data_path)


@app.route('/')
def index():
    return redirect(url_for('load_page', page=1))


@app.route('/<int:page>')
def load_page(page=None):
    json_d = json.loads(data[page - 1])
    return render_template('index.html',
                           data=json_d,
                           page=page,
                           page_num=len(data))


if __name__ == "__main__":
    app.run(host='0.0.0.0',  # 任何ip都可以访问
            port=8000,  # 端口
            debug=True)
