import os
from flask import Flask

import openai

openai.api_key = os.environ.get('API_KEY')

app = Flask('__name__')


@app.route('/')
def get_completion(prompt, model="gpt-3.5-turbo"):
    prompt = {'prompt': 'hello'}
    messages = [{"role": "user", "content": prompt}]
    response = openai.Completion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
@app.route('/chat')
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = openai.Completion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]



if __name__ == '__main__':
    messages =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}  ]
    app.run(messages)