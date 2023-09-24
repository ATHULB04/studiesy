import firebase_admin
from firebase_admin import credentials,firestore
import json
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred) 
db=firestore.client()



def importing(subject,date,period):
    print(subject,date,period)
    list=db.collection("Notes").document(subject).collection(date).document(period).get()
    if list.exists:  
        list=db.collection("Notes").document(subject).collection(date).document(period).get()
        data=list.to_dict()
        return (data.get('summary', '').strip())
    else:
        return ("there was no period today")







#to generate summary
# list=db.collection("Notes").document("Chemistry").collection("23-09-2023").document("1").get()
# data=list.to_dict()
# print(data)
# if 'summary' in data:
#       print(data["summary"])
    
# else:
#     def prompt():
#         llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.1)

#         prompt = PromptTemplate(
#             input_variables=["summ"],
#             template="write a detailed summary of {summ} and explain it in a very understandable way.",
#         )
#         chain = LLMChain(llm=llm, prompt=prompt)
#         return chain

#     def question1(inputs):
#         chain = prompt()
#         return chain.run(inputs)
#     data1=question1(data['transcribe'])
#     db.collection("Notes").document("Chemistry").collection("23-09-2023").document("1").update({"summary":data1})
#     print("done")
