from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, send_file, g
from flask_httpauth import HTTPBasicAuth
from flask_apscheduler import APScheduler
import os

from ratingcal import calculate_rating
from html_process import record_master

#Get .env variable



#Init variables

app = Flask(__name__)
scheduler = APScheduler()
auth = HTTPBasicAuth()

app.secret_key = 'maimai'


users = {
    "admin": "rats",
    "guest": "temp",
}

#Config
scheduler.api_enabled = True


#Init modules
scheduler.init_app(app)
scheduler.start()

#Auth routes
@auth.verify_password
def check_auth(username, password):
    if username in users and users[username] == password:
        return username
    else:
        print("Incorrect username or password.")
        return False

#Webpage routes
@app.route('/')
def home():
    print("Received a request at /")
    return render_template('index.html')

#Serve static files
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

@app.route('/db-export/download')
def db_export_download():
    print("Received a request at /db-export/download")
    path = "/home/admin/Desktop/Projects-Website/flask_app/db/20230423db.sqlite3"
    return send_file(path, as_attachment=True)

@app.route('/mai-camera')
@auth.login_required
def mai_camera():
    print("Received a request at /mai-camera")
    username = auth.username()
    print(f"Username: {username}")

    image_dir = 'static/images/mai-camera'
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return render_template('mai-camera.html', username=username, image_files=image_files)

#@app.route('/mai-camera/upload', methods=['POST'])

@app.route('/test')
def test():
    print("Received a request at /test")
    data = record_master(segaid, password)
    print(data)
    return render_template('index.html')

#Scheduler routes
#@scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
#def job1():
#    print('Job 1 executed')

#use_reloader=False

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
