import os
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
import datbase

os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')


def scheckpromptmaker(question,summary):#for double checking g=for summary
    instructions = f"""You are teachers assistant. Your duty is to classify students doubt's into the following categories:
    1.{question} regarding the data from summary :{summary} or about a summary of {summary}
    0.question not regarding the data from summary :{summary}

    Only return the number of the category in which the statement falls.

    return the number of the category in which the statement falls.
    excepted output is 1 or 0 only.no other alphabets or characters are allowed.
    """

    question = f'''return in the above-mentioned categories which type '{summary}' falls into.only return integer value.'''  
    
    sprompt = instructions + question

    return scheckaskgpt(sprompt)

def scheckaskgpt(sprompt):
    
    chat_model = ChatOpenAI(temperature=0.0, model='gpt-4', openai_api_key=os.environ.get("OPENAI_API_KEY"), max_tokens=250, stop=["\n"])
    
    output = chat_model([HumanMessage(content=sprompt)])
    response2 = output.content
    # print(response2)
    return response2


def promptmaker(summary, question):
    instructions = f"""You are teachers assistant. Your duty is to answer students doubts only based on the data from the summary:{summary}.
                    answer the question only based on {summary}."""
    question=f"answer the {question} using summary {summary}. "  # Convert question to a string
    prompt = instructions + question
    return askgpt(prompt)

def askgpt(prompt):
    
    chat_model = ChatOpenAI(temperature=0.0, model='gpt-4', openai_api_key=os.environ.get("OPENAI_API_KEY"), max_tokens=250, stop=["\n"])
    output = chat_model([HumanMessage(content=prompt)])
    response = output.content
    print(response)
    return response

    # response = promptmaker(summary, user_question)
    # print(response)

    # return response
def final(user_question,subject):
    summary=datbase.importing(subject)
    print(summary)
    ch=scheckpromptmaker(user_question,summary)
    print(ch)
    if ch=='1':
        response = promptmaker(summary, user_question)
        return response
    else:
        return "I am not able to answer this question as teacher did not teach this in the class."
    
# print(final("what is apple", "python"))

