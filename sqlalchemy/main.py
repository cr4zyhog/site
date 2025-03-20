from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JSJhshkas78734HAG-dashjHYSDA23G6s7sSSD6fO'


@app.route('/')
def base_html():
    return render_template('base.html')


def main():
    app.run(port=15908, host='127.0.0.1')
    # for i in range(10):
    #     db_sess = db_session.create_session()
    #     user = User()
    #     user.name = f"Пользователь {i}"
    #     user.about = f"биография пользователя {i}"
    #     user.email = f"email{i}@email.ru"
    #     db_sess.add(user)
    #     db_sess.commit()


if __name__ == '__main__':
    main()
