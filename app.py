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
            
            rating = request.form.get("rating","")
    
            return render_template('hurricaneSubmit.html',rate = rating)

    return render_template('hurricane.html')

@app.route('/claret')
def claret():
    return render_template('claret.html')

@app.route('/tayandj')
def tayandj():
    return render_template('tayandj.html')