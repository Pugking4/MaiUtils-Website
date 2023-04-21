from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    print("Received a POST request at /calculate")
    # Get the input values from the form
    constant = float(request.form['constant'])
    achievement = request.form['achievement']
    rating = request.form['rating']

    # Process the data here

    # Redirect the user to a new page with a success message
    success_message = "Calculation complete!"
    return redirect(url_for('result', message=success_message))

@app.route('/result')
def result():
    message = request.args.get('message')
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.58.50', port=5000)
