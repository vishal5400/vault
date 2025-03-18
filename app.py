from flask import Flask, render_template, jsonify, request
import json
import os
app = Flask(__name__)

token = "asdf123a"

def read_json_file(secret_file):
    with open(secret_file, 'r') as file:
        return json.load(file)

def write_json_file(secret_file, data):
    with open(secret_file, 'w') as file:
        json.dump(data, file, indent=4)

def encript(data_file, name):
    enp=f"openssl enc -aes-256-cbc -salt -in {data_file} -out {name}.enc -pass pass:{token}"
    return (os.system(enp))

def dip(name, file):
    di= f"openssl enc -d -aes-256-cbc -in {name}.enc -out {file} -pass pass:{token}"
    return (os.system(di))

@app.route('/create', methods=['GET'])
def create():
    password = request.args.get('password')
    if password == token:
        secret_file = request.args.get('secret_file')
        os.system(f'touch {secret_file}')
        return jsonify({"Created": "File Created"}), 200

@app.route('/list', methods=['GET'])
def list():
    password = request.args.get('password')
    if password == token:
        lists = os.listdir()
        return jsonify(lists), 200


@app.route('/secret', methods=['GET'])
def secret():
    password = request.args.get('password')
    if password == token:
        file_enc = request.args.get('file_name')
        base_name, extension = os.path.splitext(file_enc)
        dir = os.getcwd()
        file_path = os.path.join(dir, base_name)
        dip(file_path, base_name)

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = json.load(file)
                response = jsonify(content)
                os.remove(file_path)
                return response


@app.route('/update', methods=['PUT'])
def update_json():
    password = request.args.get('password')
    if password == token:
        secret_file = request.args.get('file_path')
        new_data = request.get_json()
        dip(secret_file, secret_file)
        existing_data = read_json_file(secret_file)
    
        existing_data.update(new_data)
        write_json_file(secret_file, existing_data)
        encript(secret_file, "data-encript" )
        os.remove(secret_file)
        return jsonify({"Updated": "Data updated"}), 200


if __name__ == '__main__':
    app.run(debug=True)