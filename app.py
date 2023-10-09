from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    headers_dict = dict(request.headers)

    if request.method == 'POST':
        if not request.is_json:
            body = request.data.decode('utf-8')  
            response = {
                "headers": headers_dict,
                "body": body
            }
            return jsonify(response)
        
        body = request.json
        response = {
            "headers": headers_dict,
            "body": body
        }
        return jsonify(response)

    elif request.method == 'GET':
        body = request.args.to_dict()
        response = {
            "headers": headers_dict,
            "body": body
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
