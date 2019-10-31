from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')       # get the text

    caps = request.POST.get('caps', 'off')
    newLine = request.POST.get('newLine', 'off')
    counter = request.POST.get('counter', 'off')
    spaceRemover = request.POST.get('spaceRemover', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    
    if caps == "on":
        analyzed = text.upper()
        params = {'x' : analyzed, 'purpose' : 'Text Capitalized'}
        text = analyzed
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'x': analyzed}
        text = analyzed

    if newLine == "on":
        analyzed = ""
        for char in text:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose':'New Line Removed', 'x': analyzed}
        text = analyzed
    
    if spaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(text):
            if text[index] == " " and text[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'Extra spaces removed', 'x': analyzed}
        text = analyzed

    if counter == "on":
        count = 0
        for char in text:
            if char != " ":
                count = count+1
        params = {'purpose':'Characters counted', 'x': count}
        text = count

    if(removepunc != "on" and newLine!="on" and spaceRemover!="on" and caps!="on" and counter != "on"):
        return HttpResponse("<h2>Error: Please select any operation and try again.</h2>")
    
    return render(request, 'analyze.html', params)

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')