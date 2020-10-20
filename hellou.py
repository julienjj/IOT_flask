from flask import request
from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

t1=None


@app.route('/', methods=['GET','POST'])


def hello():
    if request.method == 'POST':
        if request.form.get("liga") == "Liga":
            f=open('C:/teste.csv','a+')
            f.write("LIGOU \n")
            f.close()
            return render_template('controle1.html')
        elif  request.form.get("desliga") == "Desliga":
            f=open('C:/teste.csv','a+')
            f.write("DESLIGOU \n")
            f.close()
            return render_template('controle1.html')
        if request.form.get("liga1") == "Liga1":
            f=open('C:/teste.csv','a+')
            f.write("LIGOU1 \n")
            f.close()
            return render_template('controle1.html')
        elif  request.form.get("desliga1") == "Desliga1":
            f=open('C:/teste.csv','a+')
            f.write("DESLIGOU1 \n")
            f.close()
            return render_template('controle1.html')

        
    elif request.method == 'GET': 
        return render_template('controle1.html')
        
if __name__ == '__main__':
    app.run()

