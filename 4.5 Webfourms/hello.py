from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app=Flask (__name__)
app.config['SECRET KEY']="admin"
bootstrap = Bootstrap(app)

class NameForm(Form):
 name = StringField('What is your name?', validators=[Required()])
 submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])

def index():
 form = NameForm()
 if form.validate_on_submit():
  session['name'] = form.name.data
 return redirect(url_for('index'))
 return render_template('index.html', form=form, name=session.get('name'))