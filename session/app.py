from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure the app to use a specific session interface (e.g., Flask-Session or Flask-Session-Cookie)
app.config['SESSION_TYPE'] = 'filesystem'  # You can change this to 'filesystem', 'redis', etc.

# Secret key for session management (change this to a strong, secret key in a production app)
app.secret_key = 'your_secret_key'

# Initialize the session extension
Session(app)

@app.route('/')
def index():
    if 'user_data' in session:
        user_data = session['user_data']
    else:
        user_data = None

    return render_template('index.html', user_data=user_data)

@app.route('/set_session', methods=['POST'])
def set_session():
    user_data = request.form['user_data']
    session['user_data'] = user_data
    return 'User data set in session'

@app.route('/clear_session')
def clear_session():
    session.pop('user_data', None)
    return 'Session cleared'

if __name__ == '__main__':
    app.run(debug=True)
