from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Handle the calculation here
    header_text = "Calculation complete!"
    return render_template('index.html', header=header_text)

if __name__ == '__main__':
    app.run(debug=True)
