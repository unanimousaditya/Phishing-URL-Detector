#importing required libraries

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
from sklearn.ensemble import GradientBoostingClassifier
import warnings
import pickle
import os
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

# Train a new model if the old pickle is incompatible
if not os.path.exists("pickle/model_new.pkl"):
    print("Training new model from phishing.csv...")
    data = pd.read_csv("phishing.csv")
    # Drop both 'Index' and 'class' columns - only keep the 30 features
    X = data.drop(["Index", "class"], axis=1)
    y = data["class"]
    
    print(f"Training with {X.shape[1]} features and {X.shape[0]} samples...")
    
    # Train the model
    gbc = GradientBoostingClassifier(max_depth=4, learning_rate=0.7, random_state=42)
    gbc.fit(X, y)
    
    # Save the new model
    with open("pickle/model_new.pkl", "wb") as file:
        pickle.dump(gbc, file)
    print("✓ New model trained and saved to pickle/model_new.pkl")
else:
    # Load the newly trained model
    with open("pickle/model_new.pkl", "rb") as file:
        gbc = pickle.load(file)
    print("✓ Model loaded from pickle/model_new.pkl")


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('index.html',xx =round(y_pro_non_phishing,2),url=url )
    return render_template("index.html", xx =-1)


if __name__ == "__main__":
    app.run(debug=True)