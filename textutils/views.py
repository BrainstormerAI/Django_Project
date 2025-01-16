#I have created this file - Anubhav
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'Contact.html')
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    removespace=request.POST.get('removespace', 'off')
    charcount=request.POST.get('charcount', 'off')
    #removepunc=request.GET.get('removepunc', 'off')

    if removepunc == "on":
        #analyzed=djtext
        punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        #Analyze the text
        djtext=analyzed
        #return render(request, 'analyze.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if (removespace == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if (charcount == "on"):
        charactercount = 0
        for char in djtext:
            if char != ' ':  # not counting the space as a character
                charactercount += 1
        params = {'purpose': 'Count Number of Characters', 'analyzed_text': charactercount}


    if(removepunc !="on" and fullcaps!="on" and newlineremover!="on" and removespace!="on" and charcount!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def removespace(request):
#     return HttpResponse("Removed the unnecessary spaces")
# def newlineremove(request):
#     return HttpResponse("remove the new line")
# def countchar(request):
#     return HttpResponse("count number of character")

