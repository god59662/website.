from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.after_request
def add_security_headers(response):
    for header, value in app.config['SECURITY_HEADERS'].items():
        response.headers[header] = value
    return response

@app.route('/')
def home():
    projects = [
        {
            'title': 'Discord Server Developing',
            'description': 'Architecting premium community spaces with advanced permissions and engagement systems.',
            'tech': ['Community Design', 'Security', 'Management']
        },
        {
            'title': 'Discord Custom Bot Builder',
            'description': 'Creating intelligent, automated solutions to streamline server interactions and features.',
            'tech': ['Python', 'discord.py', 'API Integration']
        },
        {
            'title': 'Website Builder',
            'description': 'Building responsive, high-performance web experiences with modern aesthetics.',
            'tech': ['HTML/CSS', 'JavaScript', 'Flask']
        },
    ]
    return render_template('index.html', title="penguin-dev.com", projects=projects)

if __name__ == '__main__':
    from waitress import serve
    # Run secure production WSGI server, strictly bound to localhost
    serve(app, host='127.0.0.1', port=5000)
