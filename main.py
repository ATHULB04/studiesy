from flask import *
import studiesy 
import datbase
app=Flask(__name__)

@app.route("/bot",methods=['POST'])
def index():
    user_question=request.json['question']
    subject=request.json['subject']
    time=request.json['time']
    # period=request.json['period']
    r=studiesy.user(user_question,subject)
    datbase.chat(r,time)
    return({"result":r})

if __name__=="__main__":
    app.run(debug=True,port=6000)
