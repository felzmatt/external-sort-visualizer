import sys
import json
from algorithm.sort_algorithm import Sort

import csv
from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

def customSort(data, field, position):
    # Sort the data based on the specified field and position
    sorted_data = sorted(data, key=lambda x: x[field][position])
    return sorted_data

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    # Check if the POST request has a file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    F = int(request.form['F'])  # Access the F field as an integer
    P = int(request.form['P'])  # Access the P field as an integer

    # Check if the file is a CSV file
    if file and file.filename.endswith('.csv'):
        data = []

        # Read the CSV file and extract data
        reader = csv.reader(file.stream.read().decode("UTF-8").splitlines())
        for row in reader:
            data.append(row)
        print(len(data))
        print(data[0])
        # Call the custom sorting function
        sorter = Sort(F=F, P=P, csvdata=data)
        sorter.sort()
        history = sorter.export_json()
        # Return the JSON response with appropriate content type
        return Response(history, mimetype='application/json')
        # return jsonify(history)
        # return jsonify({"status":data})

    return jsonify({'error': 'Invalid file format. Please upload a CSV file.'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
