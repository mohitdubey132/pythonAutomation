import requests
import argparse
api_endpint ="https://api.openai.com/v1/completions"
api_key1="sk-kzRAWgBSrZHsb6uSRB8KT000000000000A4A"  # enter your own openai api key here    i have changed this right now so don`t copy it will not work 
requests_headers ={
    "Content-Type":"application/json",
    "Authorization":"Bearer "+api_key1
}
a=True
while a:
    inputString = input('Enter your query    ')
    requests_data={
        "model":"text-davinci-003",
        "prompt":f"write a python script for{inputString}. Provide only code",#args.prompt
        "prompt":inputString,
        "max_tokens":500,
        "temperature":0.5
    }

    res = requests.post(api_endpint,headers=requests_headers,json=requests_data)

    if res.status_code ==200:
        print(res.json()['choices'][0]['text'])
        option = input('enter Y to continue    ->   ')
        if option != 'y':
           a = False 

    else:
        print(res.status_code)


        
