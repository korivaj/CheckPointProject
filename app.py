from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/profile',methods=['GET','POST'])
def profile():

    if request.method == "POST":

        name = request.form.get("name", '').strip()
        email = request.form.get("email",'').strip()
        quant = request.form.get("quant" , "1").strip()
        comments = request.form.get("comments","").strip()
        relation = request.form.get("rel","").strip()
        accomodations = request.form.get("accomodations") == "yes"

        if not name or not email or not quant or not relation:
            error = "Please fill out all the required fields"
            return render_template("profileForm.html",error=error)

        return render_template('profileSuccess.html',name=name,email=email,quant=quant,comments=comments,rel=relation,accomodations=accomodations)

    return render_template('profileForm.html')



# @app.route('/feedbackForm',methods=['GET','POST'])
# def feedback():
#     if request.method == "POST":

#         rating = request.form.get("rating",'').strip()
#         feedback = request.form.get("feedback",'').strip()

#         if not rating:
#             error = "Please enter a rating"
#             return render_template("feedbackForm.html",error=error)

#         return render_template("feedbackSuccess.html",rating = rating,feedback = feedback)

#     return render_template("feedbackForm.html")

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
