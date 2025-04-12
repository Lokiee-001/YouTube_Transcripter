from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils.summarizer import get_summary
import os

app = Flask(__name__, template_folder='.')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')

# Dummy user store (use a real database in production)
users = {}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', summary=None)

@app.route('/index.html')
def index_html():
    return redirect(url_for('home'))

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form.get('url', '').strip()
    if not url:
        return render_template('index.html', summary="⚠️ Please enter a YouTube URL", original_url=url)
    summary = get_summary(url)
    return render_template('index.html', summary=summary, original_url=url)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users and users[email] == password:
            session['user'] = email
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users:
            flash('User already exists!', 'warning')
        else:
            users[email] = password
            session['user'] = email  # ✅ Auto-login
            flash('Registered successfully!', 'success')
            return redirect(url_for('home'))  # ✅ Redirect to index.html

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/dashboard')
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
