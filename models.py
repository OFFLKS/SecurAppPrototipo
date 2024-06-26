de flask_sqlalchemy importar SQLAlchemy
de flask_login importar UserMixin

db = SQLAlchemy()

classe Usuario(db.Modelo, UserMixin):
    id = db. Coluna(db.Inteiro, primary_key=Verdadeiro)
    nome_usuario = db. Coluna(db.String(20), unique=True, nullable=Falso)
    e-mail = db. Coluna(db.String(120), unique=True, nullable=Falso)
    senha = db. Coluna(db.String(60), nullable=Falso)
    crimes = db. relacionamento('Crime', backref='autor', preguiçoso=Verdadeiro)

classe Crime (db.Modelo):
    id = db. Coluna(db.Inteiro, primary_key=Verdadeiro)
    descrição = db. Coluna(db.String(200), nullable=Falso)
    latitude = db. Coluna(db.Float, nullable=Falso)
    longitude = db. Coluna(db.Float, nullable=Falso)
    usuario_id = db. Coluna(db.Inteiro, db. ForeignKey('usuario.id'), nullable=False)