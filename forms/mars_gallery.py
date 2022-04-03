from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import SubmitField, FileField


class MarsGalleryUpload(FlaskForm):
    file = FileField('Добавить картинку', validators=[FileRequired()])
    submit = SubmitField('Отправить')
