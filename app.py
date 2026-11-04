from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from dbDef import LockRatings,AnimeRatings,BikeRatings,ResidentRatings

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/locks',methods=['GET','POST'])
def locks():

    if request.method == "POST":

        rating_american = request.form.get("rating_american","")
        rating_link = request.form.get("rating_link","")
        rating_master_lock = request.form.get("rating_Master_lock","")
        rating_smart = request.form.get("rating_Smart","")

        try:
            newRating = LockRatings(
                american = rating_american,
                link = rating_link,
                master_lock = rating_master_lock,
                smart = rating_smart
            )
            
            db.session.add(newRating)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(e)
            return render_template('locks.html')



        return render_template('locksSubmit.html',rating_american = rating_american, rating_link = rating_link, rating_master_lock = rating_master_lock, rating_smart = rating_smart)

    return render_template('locks.html')


@app.route('/hurricane',methods=['GET','POST'])
def hurricane():
    if request.method == "POST":
            
            rating_dbz = request.form.get("rating_dbz","")
            rating_naruto = request.form.get("rating_naruto","")
            rating_onepiece = request.form.get("rating_onepiece","")
            rating_inuyasha = request.form.get("rating_inuyasha","")

            try:
                newRating = AnimeRatings(
                dbz = rating_dbz,
                naruto = rating_naruto,
                onepiece = rating_naruto,
                inuyasha = rating_inuyasha
                )
                
                db.session.add(newRating)
                db.session.commit()
            
            except Exception as e:
                    db.session.rollback()
                    print(e)
                    return render_template('hurricane.html')

    
            return render_template('hurricaneSubmit.html',rating_dbz = rating_dbz,rating_naruto = rating_naruto,rating_onepiece = rating_onepiece,rating_inuyasha = rating_inuyasha)

    return render_template('hurricane.html')

@app.route('/claret',methods=['GET','POST'])
def claret():
    if request.method == "POST":

        rating_Panigale = request.form.get("DUCATI-Panigale")
        rating_Diavel = request.form.get("DucactiDiavel")
        rating_scout_bobber = request.form.get("indian-scout-bobber")
        rating_Ninja = request.form.get("Kawasaki-Ninja-H2R")
        rating_Indian = request.form.get("Keino+Cycles+Indian")

        try:
            newRating = BikeRatings(
            Panigale = rating_Panigale,
            Diavel = rating_Diavel,
            scout_bobber = rating_scout_bobber,
            Ninja = rating_Ninja,
            Indian = rating_Indian
            )
            
            db.session.add(newRating)
            db.session.commit()
        
        except Exception as e:
                db.session.rollback()
                print(e)
                return render_template('claret.html')



        return render_template('claretSubmit.html',Panigale = rating_Panigale, Diavel = rating_Diavel, scout_bobber = rating_scout_bobber, Ninja = rating_Ninja, Indian = rating_Indian)
    
    return render_template('claret.html')

@app.route('/tayandj',methods=['GET','POST'])
def tayandj():
    if request.method == "POST":
    
            rating_Chris = request.form.get("Chris")
            rating_Claire = request.form.get("Claire")
            rating_Jill = request.form.get("Jill")
            rating_Leon = request.form.get("Leon")

            try:
                newRating = ResidentRatings(
                Chris = rating_Chris,
                Claire = rating_Claire,
                Jill = rating_Jill,
                Leon = rating_Leon
                )
                
                db.session.add(newRating)
                db.session.commit()
            
            except Exception as e:
                    db.session.rollback()
                    print(e)
                    return render_template('tayandj.html')


    
            return render_template('tayandjSubmit.html',Chris = rating_Chris, Claire = rating_Claire, Jill = rating_Jill, Leon = rating_Leon)
    
    return render_template('tayandj.html')

@app.route("/credit")
def credit():
     return render_template("credit.html")