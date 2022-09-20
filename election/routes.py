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
		flash("Bienvenu ",'primary')
		return render_template('pages/vote_page.html',votan=votan,posts=posts)
	else:
		flash("Matricule Invalide",'danger')
		return redirect(url_for('home'))

@app.route("/valider_vote/<IdvIdc>",methods = ['POST'])
def valider_vote(IdvIdc):
	idv,idc = IdvIdc.split('-')
	votan = Votan.query.get(int(idv))
	cand = Votan.query.get(int(idc))
	vote = Vote(votant_id=idv,candidat_id=)
