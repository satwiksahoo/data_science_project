import os
from src.datascience.pipeline.prediction import Predictionpipeline
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("artifacts/model_trainer/model.joblib")


@app.route('/' , methods = ['GET'])

def homepage():

    return render_template('index.html')



@app.route("/train", methods=["GET"])

def training():
    os.system("python main.py")
    return 'training successful'



@app.route("/predict", methods=['POST' , "GET"])
def index():
    if request.method == "POST":
        try:
            # Get all input values from form
            data = [
                float(request.form["fixed_acidity"]),
                float(request.form["volatile_acidity"]),
                float(request.form["citric_acid"]),
                float(request.form["residual_sugar"]),
                float(request.form["chlorides"]),
                float(request.form["free_sulfur_dioxide"]),
                float(request.form["total_sulfur_dioxide"]),
                float(request.form["density"]),
                float(request.form["pH"]),
                float(request.form["sulphates"]),
                float(request.form["alcohol"])
            ]

            # prediction = model.predict([np.array(data)])
            # quality = round(prediction[0], 2)

            data = np.array(data).reshape(1,11)

            obj = Predictionpipeline()
            predict = obj.predict(data)

            return render_template("results.html", prediction=f"Predicted Wine Quality: {predict}")
        
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {str(e)}")

    return render_template("index.html", prediction="")


if __name__ == "__main__":
    app.run(host='0.0.0.0' ,  port = 8080)




