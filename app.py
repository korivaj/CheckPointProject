from flask import Flask,render_template,request

app = Flask(__name__)

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

        return render_template('locksSubmit.html',rating_american = rating_american, rating_link = rating_link, rating_master_lock = rating_master_lock, rating_smart = rating_smart)

    return render_template('locks.html')


@app.route('/hurricane',methods=['GET','POST'])
def hurricane():
    if request.method == "POST":
            
            rating_dbz = request.form.get("rating_dbz","")
            rating_naruto = request.form.get("rating_naruto","")
            rating_onepiece = request.form.get("rating_onepiece","")
            rating_inuyasha = request.form.get("rating_inuyasha","")
    
            return render_template('hurricaneSubmit.html',rating_dbz = rating_dbz,rating_naruto = rating_naruto,rating_onepiece = rating_onepiece,rating_inuyasha = rating_inuyasha)

    return render_template('hurricane.html')

@app.route('/claret',methods=['GET','POST'])
def claret():
    if request.method == "POST":

        Panigale = request.form.get("DUCATI-Panigale")
        Diavel = request.form.get("DucactiDiavel")
        scout_bobber = request.form.get("indian-scout-bobber")
        Ninja = request.form.get("Kawasaki-Ninja-H2R")
        Indian = request.form.get("Keino+Cycles+Indian")

        return render_template('claretSubmit.html',Panigale = Panigale, Diavel = Diavel, scout_bobber = scout_bobber, Ninja = Ninja, Indian = Indian)
    
    return render_template('claret.html')

@app.route('/tayandj',methods=['GET','POST'])
def tayandj():
    if request.method == "POST":
    
            Chris = request.form.get("Chris")
            Claire = request.form.get("Claire")
            Jill = request.form.get("Jill")
            Leon = request.form.get("Leon")
    
            return render_template('tayandjSubmit.html',Chris = Chris,Claire = Claire,Jill = Jill,Leon = Leon)
    
    return render_template('tayandj.html')
