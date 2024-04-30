from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/get_file', methods=['GET'])
def get_file():
    with open('data.txt', 'r') as file:
        content = file.read()
    return jsonify({'file_content': content})

@app.route('/post_file', methods=['POST'])
def post_file():
    data = request.get_json()  # Get JSON data from the request
    content = data.get('content')  # Extract the 'content' field from JSON data
    with open('data.txt', 'w') as file:
        file.write(content)  # Write content to the file
    return jsonify({'message': 'File updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)