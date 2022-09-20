from election import db

class Votan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(50) , unique=True)
    nom = db.Column(db.String(25),  nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    vote = db.relationship('Vote', backref='votan', lazy=True)
    candidat = db.relationship('Candidature', backref='votan', lazy=True)

class Post(db.Model): # One
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50) , unique=True)
    candidatures = db.relationship('Candidature', backref='post', lazy=True)

class Candidature(db.Model): # Many
    id = db.Column(db.Integer, primary_key=True)
    votan_id = db.Column(db.Integer, db.ForeignKey('votan.id'),  nullable=False,unique = True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),  nullable=False)
    votes = db.relationship('Vote', backref='candidature', lazy=True)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    votan_id = db.Column(db.Integer, db.ForeignKey('votan.id'),  nullable=False, unique=True)
    candidature_id = db.Column(db.Integer, db.ForeignKey('candidature.id'),  nullable=False)




# class Votan(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     matricule = db.Column(db.String(50) , unique=True)
#     nom = db.Column(db.String(25),  nullable=False)
#     prenom = db.Column(db.String(100), nullable=False)
#     vote= db.relationship('Vote', backref='votant', lazy=True)

# class Post(db.Model): # One
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(50) , unique=True)
#     candidats = db.relationship('Candidat', backref='post', lazy=True)

# class Candidat(db.Model): # Many
#     id = db.Column(db.Integer, primary_key=True)
#     votan_id = db.Column(db.Integer, db.ForeignKey('votan.id'),  nullable=False,unique = True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'),  nullable=False)
#     votes = db.relationship('Vote', backref='votant', lazy=True)

# class Vote(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     votan_id = db.Column(db.Integer, db.ForeignKey('votan.id'),  nullable=False)
#     candidat_id = db.Column(db.Integer, db.ForeignKey('candidat.id'),  nullable=False)

