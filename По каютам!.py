from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html', title="Марс")


@app.route('/distribution')
def distribution():
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                  'Чубака', 'Рядовой Боб', 'Уборщик Макарчик']

    return render_template('cabins_for_astronauts.html',
                           list_of_astronauts=astronauts, loop=0)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')