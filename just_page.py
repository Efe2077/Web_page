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
    url_pic = url_for('static', filename='img/riana.png')
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')