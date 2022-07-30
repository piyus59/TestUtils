from email.policy import default
import re
from string import punctuation
import django
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1><a href='https://www.youtube.com/'>YouTube</h1>")

# def about(request):
#     return HttpResponse("Haa bhai")

# def contact(request):
#     return HttpResponse("Aoo")


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''Home <a href="removepunc">Next</a>''')

def analyaze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyazed = ""
        for char in djtext:
            if char not in punctuations:
                analyazed = analyazed + char
        
        params = {'purpose' : 'Removed Punctuations', 'analyazed_text' : analyazed}
        djtext = analyazed
        # return render(request, 'analyaze.html', params)

    if(capfirst == 'on'):
        analyazed=""
        for char in djtext:
            analyazed = analyazed + char.upper()

        params = {'purpose' : 'Changed to Uppercase', 'analyazed_text' : analyazed}
        djtext = analyazed
        # return render(request, 'analyaze.html', params)

    if(spaceremover == 'on'):
        analyazed=""
        # for char in djtext:
        #     if char != "  ":
        #         analyazed = analyazed + char
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyazed = str(analyazed) + char

        params = {'purpose' : 'Remove the double space', 'analyazed_text' : analyazed}
        djtext = analyazed

    if(newlineremover == 'on'):
        analyazed=""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyazed = analyazed + char
        params = {'purpose' : 'Remove the new Line', 'analyazed_text' : analyazed}
        # return render(request, 'analyaze.html', params)

    
        # return render(request, 'analyaze.html', params)
    
    # if(charcount == 'on'):
    #     count = 0
    #     analyazed= ""
    #     for char in djtext:
    #         if char == djtext:
    #             analyazed = analyazed + char.count(analyazed)

    #     params = {'purpose' : 'Count the character', 'analyazed_text' : analyazed}
    #     djtext = analyazed

    if(removepunc != 'on' and capfirst != 'on' and newlineremover != 'on' and spaceremover != 'on'):
        return HttpResponse("Please select any operations and try again!!") 
        
    
    return render(request, 'analyaze.html', params)

# def capfirst(request):
#     return HttpResponse("UPPERCASE")

# def newlineremover(request):
#     return HttpResponse("new line remove")

# def spaceremover(request):
#     return HttpResponse("remove spaces")

# def charcount(request):
#     return HttpResponse("count the characters")