import pkgutil
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open('modelstnew.pkl','rb'))
@app.route('/')
def index():
    return render_template('indexnew1.html')
    # return "SUCCESS"

@app.route('/predict1')
def student():

    var_cgpa= float(request.form.get('cgpa'))
    var_iq= int(request.form.get('iq'))
    var_ps= int(request.form.get('ps'))

    # print(f"{var_cgpa},{var_iq},{var_ps}")

    result = model.predict([[var_cgpa,var_iq,var_ps]])
    print(result[0])

    if result[0] == 1:
        final_result = "Student Placed"
    else:
        final_result= "Not Placed"

    return render_template('indexnew1.html',prediction= final_result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port=8080)