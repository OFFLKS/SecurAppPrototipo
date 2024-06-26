from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import folium
from models import Usuario, Crime, db
from forms import FormularioRegistro, FormularioLogin, FormularioReporte

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
@app.route('/home')
def home():
    crimes = Crime.query.all()
    crime_map = folium.Map(location=[-15.7942, -47.8822], zoom_start=12)
    for crime in crimes:
        folium.Marker(
            location=[crime.latitude, crime.longitude],
            popup=crime.descricao,
            icon=folium.Icon(color='red')
        ).add_to(crime_map)
    crime_map.save('templates/crime_map.html')
    return render_template('home.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = FormularioRegistro()
    if form.validate_on_submit():
        usuario = Usuario(nome_usuario=form.nome_usuario.data, email=form.email.data, senha=form.senha.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.senha == form.senha.data:
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Falha no login. Verifique seu email e senha', 'danger')
    return render_template('login.html', form=form)

@app.route('/reportar', methods=['GET', 'POST'])
@login_required
def reportar():
    form = FormularioReporte()
    if form.validate_on_submit():
        crime = Crime(descricao=form.descricao.data, latitude=form.latitude.data, longitude=form.longitude.data, usuario_id=current_user.id)
        db.session.add(crime)
        db.session.commit()
        flash('Crime reportado com sucesso!', 'success')
        return redirect(url_for('home'))
    return render_template('report.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
