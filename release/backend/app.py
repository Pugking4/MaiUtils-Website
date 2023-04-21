from flask import Flask, render_template, request, redirect, url_for
from ratingcal import calculate_rating

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


    print(f"Constant: {constant}")
    print(f"Achievement: {achievement}")
    print(f"Rating: {rating}")

    

    # Process the data here
    s_rating, splus_rating, ss_rating, ssplus_rating, sss_rating, sssplus_rating, custom_rating = calculate_rating(constant=constant, achievement=achievement, rating=rating)


    # Redirect the user to a new page with a success message
    return redirect(url_for('result', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating))

@app.route('/result')
def result():
    constant = float(request.args.get('constant'))
    achievement = request.args.get('achievement')
    rating = request.args.get('rating')
    
    s_rating = request.args.get('s_rating')
    splus_rating = request.args.get('splus_rating')
    ss_rating = request.args.get('ss_rating')
    ssplus_rating = request.args.get('ssplus_rating')
    sss_rating = request.args.get('sss_rating')
    sssplus_rating = request.args.get('sssplus_rating')
    custom_rating = request.args.get('custom_rating')

    header_text = "Calculation complete!"
    return render_template('result.html', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating, header_text=header_text)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.58.50', port=5000)
