from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# Function to search and retrieve matching entries
def search_entries(search_term):
    # Implement your search logic here
    # This function should return the matching entries based on the search term
    # For now, let's assume it returns a list of dummy results
    dummy_results = [
        {'SAP ID': '123', 'Student Name': 'John Doe'},
        {'SAP ID': '456', 'Student Name': 'Jane Smith'}
    ]
    return dummy_results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    results = search_entries(search_term)
    return render_template('results.html', results=results), 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/results.html')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    freezer.freeze()
