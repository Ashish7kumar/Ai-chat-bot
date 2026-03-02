from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
llm=HuggingFacePipeline.from_model_id(model_id="Qwen/Qwen2-0.5B-Instruct",
                                      task="text-generation")
model=ChatHuggingFace(llm=llm)
while True:
    user_input=input('you: ')
    if user_input=='exit':
        break;
    else:
        result=model.invoke(user_input) 
        result=result
        print('AI: ',result.content)