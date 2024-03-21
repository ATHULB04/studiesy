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
    r=studiesy.final(user_question,subject)
    print(r)
    datbase.chat(r,time,subject)
    return({"result":r})

if __name__=="__main__":
    app.run(debug=True,port=6000)
