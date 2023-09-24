from flask import *
import studiesy
app=Flask(__name__)

@app.route("/",methods=['POST'])
def index():
    user_question=request.json['question']
    subject=request.json['subject']
    date=request.json['date']
    period=request.json['period']
    r=studiesy.user(user_question,subject,date,period)
    return({"result":r})

if __name__=="__main__":
    app.run(debug=True,port=6000)
