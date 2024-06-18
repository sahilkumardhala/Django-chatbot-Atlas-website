from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import openai

openai.api_key = "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"
model_engine = "gpt-3.5-turbo"
# Create your views here.
def home(request):
    return render(request,'index.html')

def get_response(request,text):
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = [
        {"role":"system","content":"input."},
        {"role":"user","content":f"{text}"},
        ]
    )
    message = response.choices[0]['message']
    print(message)
    return HttpResponse(message['content'])
