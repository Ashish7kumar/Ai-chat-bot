from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
     api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)
context=[SystemMessage(content='you are a helfull agent named sura')]
while True:
    user_input=input('you: ')
    context.append(HumanMessage(content=user_input))
    if user_input=='exit':
        print(str(context))
        break;
    else:
        result=model.invoke(context) 
        result=result
        response = result.content
        context.append(AIMessage(content=response))
        print("AI:", response)