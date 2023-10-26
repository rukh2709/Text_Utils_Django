from django.http import HttpResponse
from django.shortcuts import render  
import re

def index(request):
    return render(request, 'index.html') 

def contact(request):
    return render(request, 'contact.html') 

def analyze(request):    
    djtext = request.POST.get('text', 'default')
    print("Input text:", djtext)

    removepunc = request.POST.get('removepunc', 'off')    
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')        
  
    if charcount=='on':
        analyzed = len(djtext.replace(" ", ""))
        params = {'purpose': 'number of characters in the text', 'analyzed_text': analyzed}  

    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'with punctuations removed', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'converted to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if newlineremover=='on':
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'with new lines removed', 'analyzed_text': analyzed}   
        djtext = analyzed
    
    if spaceremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed += char
        params = {'purpose': 'with extra spaces removed', 'analyzed_text': analyzed}
                  
    if removepunc!='on' and fullcaps!='on' and newlineremover!='on' and spaceremover!='on' and charcount!='on':
        return HttpResponse("<h1>No switch is On</h1>")
    
    return render(request, 'analyze.html', params) 