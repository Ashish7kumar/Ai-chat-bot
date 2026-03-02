from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
llm=HuggingFacePipeline.from_model_id(model_id="Qwen/Qwen2-0.5B-Instruct",
                                      task="text-generation"
                                      ,
                                       pipeline_kwargs=dict(
        max_new_tokens=150,
        return_full_text=False   
    )
                     )
model=ChatHuggingFace(llm=llm)
context=[]
while True:
    user_input=input('you: ')
    context.append(user_input)
    if user_input=='exit':
        break;
    else:
        result=model.invoke(context) 
        result=result
        response = result.content
        context.append(response)
        print("AI:", response)