from flask import Flask,render_template,request

#model
import pickle
with open('model_pkl' , 'rb') as f:
    model = pickle.load(f)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intro.html')



@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':

        f1 =  float(request.form.get('fname1'))
        f2 =  float(request.form.get('fname2'))
        f3 =  float(request.form.get('fname3'))
        f4 =  float(request.form.get('fname4'))
        f5 =  float(request.form.get('fname5'))
        f6 =  float(request.form.get('fname6'))
        f7 =  float(request.form.get('fname7'))
        f8 =  float(request.form.get('fname8'))
        f9 =  float(request.form.get('fname9'))
        f10 = float(request.form.get('fname10'))
        f11 = float(request.form.get('fname11'))
        f12 = float(request.form.get('fname12'))
        f13 = float(request.form.get('fname13'))

        result=model.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]])
    
    res=''
    if int(result[0])==0:
        res='High Adaptability'
    elif int(result[0])==1:
        res= 'Low Adaptability'
    else:
        res = 'Moderate Adaptability'''
    
    return render_template('result.html',result=res)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
    