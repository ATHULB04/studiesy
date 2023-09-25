from flask import *
import studiesy 
import datbase
app=Flask(__name__)

@app.route("/bot",methods=['POST'])
def index():
    user_question=request.json['question']
    subject=request.json['subject']
    # date=request.json['date']
    # period=request.json['period']
    r=studiesy.user(user_question,subject)
    print(r)
    return({"result":r})

@app.route("/summary",methods=['POST'])
def index1():
    yes=request.json['yes']
    subject=request.json['subject']
    # date=request.json['date']
    # period=request.json['period']
    r=datbase.to_summ(yes,subject)
    print(r)
    return({"result":r})

if __name__=="__main__":
    app.run(debug=True,port=6000)
