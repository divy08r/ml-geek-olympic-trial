from flask import Flask, render_template, request, url_for, redirect
import pickle
import Health_predict as hp
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import OneHotEncoder

encoded_cols = hp.encoded_cols
encoder = hp.encoder
numeric_cols = hp.numeric_cols
categorical_cols = hp.categorical_cols
minscaler = hp.minscaler

app = Flask(__name__)

model2=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("index.html")
    # return 'Hello, World!'


@app.route('/model', methods=['GET'])
def bye_World():
    return render_template("model.html")

@app.route('/model', methods=['POST'])
def predict():
    if request.method == 'POST':
        int_features=[x for x in request.form.values()]
        finalarray=[np.array(int_features)]
        def input(finalarray):
            final = {
                "gender" : finalarray[0][0].lower(),
                "age"  : (float)(finalarray[0][1]),
                "heart_rate" : (float)(finalarray[0][2]),
                "temperature" : (float)(finalarray[0][3]),
                "SpO2_saturation" : (float)(finalarray[0][4]),
                "bpm" :(float)(finalarray[0][5])
            } 
            new_input_df = pd.DataFrame([final])
            new_input_df[encoded_cols] = encoder.transform(new_input_df[categorical_cols])
            new_input_df[numeric_cols] = minscaler.transform(new_input_df[numeric_cols])
            x_input = new_input_df[numeric_cols + encoded_cols]
            return x_input
        x_input = input(finalarray)
        prediction=model2.predict(x_input)
        output= prediction[0]

        if output == 1:
            return render_template('model.html',pred='Athelete is all right🥳🥳')
        else:
            return render_template('model.html',pred='Athelete requires medical emergency🏥🏥')
    else:
        return render_template('model.html')


@app.route('/analysis')
def new_world():
    return render_template("analysis.html")



if __name__ == "__main__" :
    app.run(debug=True)
