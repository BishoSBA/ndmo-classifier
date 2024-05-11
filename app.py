from flask import Flask, render_template, request
from logic import classify_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_folder():
    files = request.files.getlist('files[]')
    file_data = []
    result = []
    for file in files:
        file_name = file.filename.split('/')[-1]
        classification = classify_file(file)
        print(f'File: {file_name} - Classification: {classification}')
        file_data.append((file_name, classification))
        result.append({
            "name": file_name,
            "classification": classification
        })
    return result

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)

def prepare(file_name, classification, result):
    result.append({
        "name": file_name,
        "classification": classification
    })
