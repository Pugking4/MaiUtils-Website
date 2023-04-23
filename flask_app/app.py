from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from ratingcal import calculate_rating

app = Flask(__name__)
app.secret_key = 'maimai'

@app.route('/')
def home():
    print("Received a request at /")
    return render_template('index.html')

# Serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/index')
def index():
    print("Received a request at /index")
    return render_template('index.html')

@app.route('/rating-calculator')
def ratingcal():
    print("Received a request at /ratingcal")
    return render_template('ratingcal.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    print("Received a POST request at /calculate")
    # Get the input values from the form

    if request.form['constant']:
        constant = float(request.form['constant'])
    else:
        constant = 0

    if request.form['achievement']:
        achievement = float(request.form['achievement'])
    else:
        achievement = 0

    if request.form['rating']:
        rating = request.form['rating']
    else:
        rating = 0
    
    print(f"Constant: {constant}")
    print(f"Achievement: {achievement}")
    print(f"Rating: {rating}")

    # Process the data here
    s_rating, splus_rating, ss_rating, ssplus_rating, sss_rating, sssplus_rating, custom_rating = calculate_rating(constant=constant, achievement=achievement, rating=rating)

    # Store the result in session variables
    session['constant'] = constant
    session['achievement'] = achievement
    session['rating'] = rating
    session['s_rating'] = s_rating
    session['splus_rating'] = splus_rating
    session['ss_rating'] = ss_rating
    session['ssplus_rating'] = ssplus_rating
    session['sss_rating'] = sss_rating
    session['sssplus_rating'] = sssplus_rating
    session['custom_rating'] = custom_rating

    # Return the result through POST method
    return render_template('ratingcal.html', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating)

@app.route('/result')
def result():
    print("Received a request at /result")
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
    #Make it insert data rather than use template or use templates exclusively

    return render_template('ratingcal.html', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating, header_text=header_text)

@app.route('/privacy-policy')
def privacy_policy():
    print("Received a request at /privacy-policy")
    return render_template('privacy-policy.html')

@app.route('/db-export')
def db_export():
    print("Received a request at /db-export")
    return render_template('db-export.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
