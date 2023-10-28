from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/apple-app-site-association')
def apple_association():
    return send_from_directory('.', 'apple-app-site-association', mimetype='application/json')

if __name__ == '__main__':
    app.run()