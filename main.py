from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<user_list>')
def index(user_list):
    return render_template('base_02.html', title=user_list,)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')