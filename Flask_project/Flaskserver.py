from flask import Flask,jsonify,request
import joblib
from pathlib import Path
app=Flask(__name__)

#model_path="marks_predictor.joblib"
model_path = Path(__file__).resolve().parent / "marks_predictor.joblib"
model=joblib.load(model_path)

@app.route("/")
def home():
    return "welcome home"

#routes


# prediction part

@app.route("/predict",methods=["POST"])
def predict():
    data=request.get_json()
    
    attendance=data["attendance"]
    studyhours=data["studyhours"]
    assignmentscore=data["assignmentscore"]
    internalmarks=data["internalmarks"]
    previousgpa=data["previousgpa"]
    
    input_data=[[
        attendance,
        studyhours,
        assignmentscore,
        internalmarks,
        previousgpa
    ]]
    
    prediction=float(model.predict(input_data)[0])
    return jsonify({
        "prediction":prediction
    })
    
app.run(debug=True)
    

