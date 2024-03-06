from subprocess import run
from flask import Flask, request

UPDATE_TOKEN = 'your_token'

app = Flask(__name__)

@app.route('/update')
def update():
    repo = request.args.get('repo')
    token = request.args.get('token')
    if token != UPDATE_TOKEN:
        return '403 Invalid token', 403
    if not repo:
        return 'Repo not specified', 400
    print(f'Updating {repo}')
    run(['git', 'pull'], cwd=repo)
    print(f'Updated {repo}')
    return 'Updated'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
