import os
import datbase
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')
response_cache = {}

def user(user_question,subject,date,period):
    summary=datbase.importing(subject,date,period)
    print(summary)
    def promptmaker(summary, question):
        print(summary)
        instructions = """You are a chatbot who helps students learn.
        The summary of the topic that teacher taught that day is '{summary}'.
        You should help them answer all their questions with data mentioned in the '{summary}'.
        And  only answer the questions related to topics mentioned in  '{summary}'.
        If students ask anything outside the topic, you should say 'Sorry, I only know what the teacher taught'.
        Don't ever mislead students with wrong answers or anything other than the {summary}.
        ask a creative question at the end of the answer to make students think more about the topic.
        Make sure you give an answer to the question in a way that students can understand easily.
        Don't give too long answers and go too deep into the answer.
        Don't forget to give a 'do you know' type question that invokes curiosity in students.
        Expected output example:
                        Photosynthesis is a process by which plants make their own food using sunlight, carbon dioxide and water. This process is an endothermic reaction and takes place in the chloroplasts of green plants. In this process, light energy is absorbed by chlorophyll and converted into chemical energy. This chemical energy is used to make glucose from carbon dioxide and water. Oxygen is also released as a by-product.
                        By the way, do you know about when it will take place?
    """

        data = str(summary)  # Convert summary to a string
        question = str(question)  # Convert question to a string
        
        # Check if the student asked about the topic taught that day
        if "topic" in question.lower() and "teacher" in question.lower() and "teach" in question.lower():
            # Provide information about the topic instead of the default response
            
            prompt = instructions + data + "what is the summary about ?"
        elif question.lower() == "what did teacher teach on that day?" or question.lower() == "what did teacher teach today?" or question.lower() == "what did teacher say?":
            prompt = instructions + data + "what is the summary about ?"

        else:
            # Use the default prompt for other questions
            prompt = instructions + data + question

        return askgpt(prompt)

    def askgpt(prompt):
        
        chat_model = ChatOpenAI(temperature=0.1, model='gpt-3.5-turbo', openai_api_key=os.environ.get("OPENAI_API_KEY"), max_tokens=250, stop=["\n"])
        
        if prompt in response_cache:
            return response_cache[prompt]

        output = chat_model([HumanMessage(content=prompt)])
        response = output.content
        response_cache[prompt] = response
        return response
    response1 = promptmaker(summary, user_question)
    return response1




