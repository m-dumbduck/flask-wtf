from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if any([spec in prof.lower() for spec in ['инженер', 'строитель']]):
        training_title, img = 'Инженерные тренажеры', '/static/img/engineer_scheme.png'
    else:
        training_title, img = 'Научные симуляторы', '/static/img/science_simulators.png'
    return render_template('training.html', training_title=training_title, scheme=img)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
