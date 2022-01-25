from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


model = pickle.load(open("model.pkl","rb"))



@app.route('/',methods=['GET'])
def index():
    return render_template("index2.html")

@app.route("/account_data", methods=["POST"])
def get_data():
    Age = request.form["Age"]
    Gender = request.form["Gender"]
    BMI = request.form["Body_Mass_Index"]
    childrens = request.form["no_of_children"]
    smoker = request.form["Smoker_or_not"]
    region = request.form["Enter_your_Region"]
    charges = request.form["Charges"]
    
    output = model.predict([[Age,Gender,BMI,childrens,smoker,region,charges]])
    
    if output == 1:
        return "Will claim for insurance"
    else:
        return "Will not claim for insurance"
            
        

if __name__ == '__main__':
    app.run(debug=True)
