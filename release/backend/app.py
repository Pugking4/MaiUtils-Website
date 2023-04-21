from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the input values from the form
    constant = float(request.form['constant'])
    achievement = request.form['achievement']
    rating = request.form['rating']

    # Process the data here

    header_text = "Calculation complete!"
    return header_text

if __name__ == '__main__':
    app.run(debug=True)
