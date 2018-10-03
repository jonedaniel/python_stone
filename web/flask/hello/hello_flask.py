from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect(url_for('index'))

@app.route("/main")
def index():
    return 'index'



@app.route("/sum/<int:a>/<int:b>")
def twoNumSum(a, b):
    return "%d" % (a + b)


def valid_login(param, param1):
    return True


def log_the_user_in(param):
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    searchword = request.args.get('key', '')
    print(searchword)
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
