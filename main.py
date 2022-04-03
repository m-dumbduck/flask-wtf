from flask import Flask, render_template
from werkzeug.utils import redirect

from forms.emergency_access import EmergencyAccessForm

PROF_LIST = [
    'инженер-исследователь',
    'пилот',
    'строитель',
    'экзобиолог',
    'врач',
    'инженер по терраформированию',
    'климатолог',
    'специалист по радиационной защите',
    'астрогеолог',
    'гляциолог',
    'инженер жизнеобеспечения',
    'метеоролог',
    'оператор марсохода',
    'киберинженер',
    'штурман',
    'пилот дронов'
]
AUTO_ANSWER = {
    'title': '',
    'surname': 'Watny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': 'True'
}
ASTRONAUTS = [
    'Ридли Скотт',
    'Энди Уир',
    'Марк Уотни',
    'Венката Капур',
    'Тедди Сандерс',
    'Шон Бин'
]

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/list_prof/<list_type>')
def prof_list(list_type):
    print(list_type)
    return render_template('prof_list.html', list_type=list_type, prof_list=PROF_LIST)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('answer.html', data=AUTO_ANSWER)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = EmergencyAccessForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('emergency_access.html', form=form)


@app.route('/success')
def success():
    return 'Форма успешно отправлена'


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', astronauts=ASTRONAUTS)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
