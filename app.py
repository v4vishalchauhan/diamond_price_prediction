
from flask import Flask,request,render_template,jsonify
import numpy as np
# from extractive_summarizer import text_summarizer
from KNN import KNN_regression

app=Flask(__name__)
knn=KNN_regression()


@app.route("/")
def my_form2():
    return render_template("index2.html")

@app.route('/',methods=["POST"])
def my_form_post2():
    # try:
        carat=request.form['carat']
        cut=request.form['options']
        
        cut_dict={"Ideal":1,
                    "Premium":2,
                    "Very_Good":3,
                    "Good":4,
                    "Fair":5}

        cut=cut_dict[cut]

        color=request.form['options2']
        color_dict= {"G":1,
                    "E":2,
                    "F":3,
                    "H":4,
                    "D":5,
                    "I":6,
                    "J":7}
        color=color_dict[color]
        
        clarity=request.form['options3']
        clarity_dict={ "SI1":1,
                        "SI2":2,
                        "VS1":3,
                        "VS2":4,
                        "VVS1":5,
                        "VVS2":6,
                        "IF":7,
                        "I1":8}
        clarity=clarity_dict[clarity]
        depth=request.form['depth']
        table=request.form['table']
        x=request.form['x']
        y=request.form['y']
        z=request.form['z']
        test_array=np.array([carat,cut,color,clarity,depth,table,x,y,z])
        price=knn.predict(test_array)
        return render_template("index2.html",price=price)
    # except:
    #     return render_template("error.html")

if __name__=="__main__":
    app.run(debug=True,port=8080)



