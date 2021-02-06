from flask import Flask, request, jsonify, render_template, url_for
import joblib

new_cl = joblib.load("joblib-model.pkl")
# new_cl.predict(["UV lamps should not be used to sterilize hands or other areas of skin as UV radiation can cause skin irritation."])


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify',methods = ['POST'])
def classify():
    if request.method == 'POST':
        stmt = request.form['statement']
        Judgement = new_cl.predict([str(stmt)])

        return render_template('index.html', judgement_text=Judgement[0])



if __name__ == '__main__':
    app.run(debug=True)