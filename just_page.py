from flask import Flask, url_for


app = Flask(__name__)


lines = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
         'И начнем с Марса!', 'И начнем с Марса!', 'Присоединяйся!'
         ]


@app.route('/')
def page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    countdown_list = lines
    return '</br>'.join(countdown_list)


@app.route('/image_sample')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/riana.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <h1>Вот она какая, красная планета</h1>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion2():
    pr_list = lines
    url_pic = url_for('static', filename='img/mars.gif')
    url_style = url_for('static', filename='css/style.css')
    return """<!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{}" />
                <title>Колонизация</title>
              </head>
              <body>
                <h1>Жди нас, Марс</h1>
                <img src="{}" 
                alt="здесь должна была быть картинка, но не нашлась">
                </div>
                <div class="alert-primary" role="alert">
                    <br><h2>{}</h2>
                </div>
                <div class="alert-success" role="alert">
                    <br><h2>{}</h2>
                </div>
                <div class="alert-primary" role="alert">
                    <br><h2>{}</h2>
                </div>
                <div class="alert-success" role="alert">
                    <br><h2>{}</h2>
                </div>
                <div class="alert-warning" role="alert">
                    <br><h2>{}</h2>
                </div>
                <div class="alert-info" role="alert">
                    <br><h2>{}</h2> 
                </div>
                <div class="alert-danger" role="alert">
                    <br><h2>{}</h2>
                </div>
              </body>
            </html>
            """.format(url_style, url_pic,  *pr_list)


@app.route('/choice/<planet_name>')
def print_inp(planet_name):
    return """<!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
              </head>
              <body>
                </div>
                    <h2>Мое предположение: {}</h2>
                </div>
                    <h3>Эта планета близка к Земле;</h3>
                <div/>
                <div class="alert-success" role="alert">
                    <br><h3>На ней много необходимых ресурсов;</h3>
                </div>
                <div class="alert-secondary" role="alert">
                    <br><h3>На ней есть вода и атмосфера;</h3>
                </div>
                <div class="alert-warning" role="alert">
                    <br><h3>На ней есть небольшое магнитное поле;</h3>
                </div>
                <div class="alert-danger" role="alert">
                    <br><h3>Наконец, она просто красива!</h3>
                </div>
              </body>
            </html>
            """.format(planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    </div>
                        <h2>Результаты отбора</h2>
                    </div>
                        <h3>Претенденты на участие в миссии {}:</h3>
                    <div/>
                    <div class="alert-success" role="alert">
                        <br><h3>Поздравляем! Ваш рейтинг после {} этапа отбора</h3>
                    </div>
                        <br><h3>составляет {}!</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                        <br><h3>Желаем удачи!</h3>
                    </div>
                  </body>
                </html>
                """.format(nickname, level, rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')