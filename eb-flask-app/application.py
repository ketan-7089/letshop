from flask import Flask, render_template_string
import os

application = Flask(__name__)

PAGE = """<html><body style='font-family:Arial;text-align:center;margin-top:60px'>
<h1>Hello from AWS Elastic Beanstalk!</h1>
<p>Version: {{ version }}</p><p>Environment: {{ env }}</p>
</body></html>"""

@application.route('/')
def home():
    return render_template_string(PAGE, version='1.0',
                                 env=os.environ.get('APP_ENV', 'not set'))

@application.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    application.run(debug=True)
