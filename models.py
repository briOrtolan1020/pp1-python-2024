from app import db

class Marca(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(30), nullable=False)

    def __srt___(self):
        return self.nombre
    

class Tipo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(30), nullable=False)

    def __srt___(self):
        return self.nombre