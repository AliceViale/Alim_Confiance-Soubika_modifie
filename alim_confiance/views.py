from flask import Blueprint, render_template, request, redirect, url_for
from .models import Etablissement
from alim_confiance import db

views = Blueprint('views', __name__)
#vue avec la page d'ajout en page d'accueil pour le moment
@views.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template("ajout_final.html")
#vue de la page d'ajout établissement
##fonction pour remplir la BDD avec le formulaire html
@views.route('/ajout_final', methods=['GET', 'POST'])
def ajoutEtablissement():

    if request.method == "POST":
        etablissement_nom = request.form['nom']
        etablissement_adresse = request.form['adresse']
        etablissement_cp = request.form['code postal']
        etablissement_commune = request.form['adresse']
        etablissement_siret = request.form['siret']
        etablissement_activite = request.form['activite']
        etablissement_agrement = request.form['agrement']
        etablissement_longitude_latitude = request.form['longitude_latitude']
        etablissement_categorie_frais = request.form['categorie_frais']
        
        nv_etablissement = Etablissement(nom =etablissement_nom, 
        adresse = etablissement_adresse,
        cp = etablissement_cp,
        commune = etablissement_commune,
        siret = etablissement_siret,
        agrement = etablissement_agrement,
        activite = etablissement_activite,
        longitude_latitude = etablissement_longitude_latitude,
        categorie_frais = etablissement_categorie_frais
        )

        try:
            db.session.add(nv_etablissement)
            db.session.commit()
            return redirect("/listeE")
        except:
            return "Erreur lors de l'enregistrement"
    else :
        etablissements = Etablissement.query.order_by(Etablissement.id)
        return render_template("ajout_final.html")

