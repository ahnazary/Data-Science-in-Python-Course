import csv
import io

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/result",methods= ["POST","GET"])
def result():
    inputJSON = request.get_json()
    if len(inputJSON.keys()) == 1:
        return {"key": "invalid entry"}

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

@app.route("/result2",methods= ["POST","GET"])
def result2():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    # print("file contents: ", file_contents)
    # print(type(file_contents))
    print(csv_input)
    for row in csv_input:
        print(row)

    stream.seek(0)
    result = transform(stream.read())

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response

if __name__ == '__main__':
    app.run(debug=True, port=2000)