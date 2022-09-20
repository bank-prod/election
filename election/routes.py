from flask import render_template,abort,redirect,request,url_for,flash
from election import app
from election import db
from election.models import Votan,Post,Candidature,Vote

@app.route("/")
def home():
	return render_template('pages/home.html')
@app.route("/vote",methods = ['POST'])
def vote_page():
	votan = Votan.query.filter_by(matricule = request.form['matricule']).first()
	posts = Post.query.all()
	if  votan :
		DejaVote = Vote.query.filter_by(votan_id=votan.id).first()
		if DejaVote :
			flash("A déja voter",'danger')
			return redirect(url_for('home'))
		else :
			flash("Bienvenu ",'primary')
			return render_template('pages/vote_page.html',votan=votan,posts=posts)
	else:
		flash("Matricule Invalide",'danger')
		return redirect(url_for('home'))

@app.route("/valider_vote/<matricule_votan>",methods = ['POST'])
def valider_vote(matricule_votan):
	id_candidature = request.form['candidat']
	candidature = Candidature.query.get(int(id_candidature))
	votan = Votan.query.filter_by(matricule=matricule_votan).first()
	DejaVote = Vote.query.filter_by(votan_id=votan.id).first()
	if DejaVote :
		flash("A déja voter",'danger')
		return redirect(url_for('home'))
	else:
		vote = Vote(votan_id=votan.id,candidature_id=candidature.id)
		db.session.add(vote)
		db.session.commit()
		flash("Félicitation",'primary')
		return render_template('pages/valider_vote.html' , votan=votan, candidature=candidature)
		# return redirect(url_for('home'))
