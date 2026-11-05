from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from dbDef import LockRatings,AnimeRatings,BikeRatings,ResidentRatings

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/admin")
def admin():
     return render_template("admin.html")


@app.route('/locks',methods=['GET','POST'])
def locks():

    if request.method == "POST":

        rating_american = request.form.get("rating_american","")
        rating_link = request.form.get("rating_link","")
        rating_master_lock = request.form.get("rating_Master_lock","")
        rating_smart = request.form.get("rating_Smart","")
        rater_name = request.form.get("name")

        try:
            newRating = LockRatings(
                american = rating_american, # type: ignore
                link = rating_link, # type: ignore
                master_lock = rating_master_lock, # type: ignore
                smart = rating_smart, # type: ignore
                name = rater_name, # type: ignore
                
                created_at = datetime.now() # type: ignore
            )
            
            db.session.add(newRating)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print('\033[31m' + str(e) + '\033[0m')
            return render_template('/locks/locks.html')



        return render_template('/locks/locksSubmit.html',rating_american = rating_american, rating_link = rating_link, rating_master_lock = rating_master_lock, rating_smart = rating_smart, name = rater_name)

    return render_template('/locks/locks.html')

@app.route("/admin/locksResults")
def locksResults():
     locksResults = LockRatings.query.all()
     return render_template("/locks/locksResults.html", locksResults = locksResults)


@app.route('/hurricane',methods=['GET','POST'])
def hurricane():
    if request.method == "POST":
            
            rating_dbz = request.form.get("rating_dbz","")
            rating_naruto = request.form.get("rating_naruto","")
            rating_onepiece = request.form.get("rating_onepiece","")
            rating_inuyasha = request.form.get("rating_inuyasha","")
            rater_name = request.form.get("name")

            try:
                newRating = AnimeRatings(
                dbz = rating_dbz, # type: ignore
                naruto = rating_naruto, # type: ignore
                onepiece = rating_naruto, # type: ignore
                inuyasha = rating_inuyasha, # type: ignore
                name = rater_name, # type: ignore

                created_at = datetime.now() # type: ignore
                )
                
                db.session.add(newRating)
                db.session.commit()
            
            except Exception as e:
                    db.session.rollback()
                    print('\033[31m' + str(e) + '\033[0m')
                    return render_template('/hurricane/hurricane.html')

    
            return render_template('/hurricane/hurricaneSubmit.html',rating_dbz = rating_dbz,rating_naruto = rating_naruto,rating_onepiece = rating_onepiece,rating_inuyasha = rating_inuyasha, name = rater_name)

    return render_template('/hurricane/hurricane.html')

@app.route("/admin/hurricaneResults")
def hurricaneResults():
     hurricaneResults = AnimeRatings.query.all()
     return render_template("/hurricane/hurricaneResults.html", hurricaneResults = hurricaneResults)


@app.route('/claret',methods=['GET','POST'])
def claret():
    if request.method == "POST":

        rating_Panigale = request.form.get("DUCATI-Panigale")
        rating_Diavel = request.form.get("DucactiDiavel")
        rating_scout_bobber = request.form.get("indian-scout-bobber")
        rating_Ninja = request.form.get("Kawasaki-Ninja-H2R")
        rating_Indian = request.form.get("Keino+Cycles+Indian")
        rater_name = request.form.get("name")

        try:
            newRating = BikeRatings(
            Panigale = rating_Panigale, # type: ignore
            Diavel = rating_Diavel, # type: ignore
            scout_bobber = rating_scout_bobber, # type: ignore
            Ninja = rating_Ninja, # type: ignore
            Indian = rating_Indian, # type: ignore
            name = rater_name, # type: ignore

            created_at = datetime.now() # type: ignore
            )
            
            db.session.add(newRating)
            db.session.commit()
        
        except Exception as e:
                db.session.rollback()
                print('\033[31m' + str(e) + '\033[0m')
                return render_template('/claret/claret.html')



        return render_template('/claret/claretSubmit.html',Panigale = rating_Panigale, Diavel = rating_Diavel, scout_bobber = rating_scout_bobber, Ninja = rating_Ninja, Indian = rating_Indian, name = rater_name)
    
    return render_template('/claret/claret.html')

@app.route("/admin/claret")
def claretResults():
     bikeratings = BikeRatings.query.all()
     return render_template("/claret/claretRating.html", bikeratings = bikeratings)


@app.route('/tayandj',methods=['GET','POST'])
def tayandj():
    if request.method == "POST":
    
            rating_Chris = request.form.get("Chris")
            rating_Claire = request.form.get("Claire")
            rating_Jill = request.form.get("Jill")
            rating_Leon = request.form.get("Leon")
            rater_name = request.form.get("name")

            try:
                newRating = ResidentRatings(
                Chris = rating_Chris, # type: ignore
                Claire = rating_Claire, # type: ignore
                Jill = rating_Jill, # type: ignore
                Leon = rating_Leon, # type: ignore
                name = rater_name, # type: ignore

                created_at = datetime.now() # type: ignore
                )
                
                db.session.add(newRating)
                db.session.commit()
            
            except Exception as e:
                    db.session.rollback()
                    print('\033[31m' + str(e) + '\033[0m')
                    return render_template('/tayandj/tayandj.html')


    
            return render_template('/tayandj/tayandjSubmit.html',Chris = rating_Chris, Claire = rating_Claire, Jill = rating_Jill, Leon = rating_Leon, name = rater_name)
    
    return render_template('/tayandj/tayandj.html')

@app.route("/admin/tayandjResults")
def tayandjResults():
     residentRatings = ResidentRatings.query.all()
     return render_template("/tayandj/tayandjResults.html", residentRatings = residentRatings)


@app.route("/credit")
def credit():
     return render_template("credit.html")