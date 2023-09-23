from flask import *
from fpdf import FPDF
app=Flask(__name__)

@app.route("/",methods=['POST'])
def index():
    name=request.json['name']


    f=FPDF()
    f.add_page()

    f.output(f"{name}.pdf")
    return({"result":"done"})

if __name__=="__main__":
    app.run(debug=True,port=6000)
