#Views File by Create.....Akash
from django .http import HttpResponse
from django .shortcuts import render


def func(request):
    dic={"name":"Akash","number":"0123456789"}
    return render(request,"learnhtml.html",dic)  

def about(request):
    return HttpResponse('''<h1>This is About...</h1>
                            <a href="https://www.google.com/">Google</a><br><br>
                            <a href="/removepunc">removepunc</a>&nbsp&nbsp
                            <a href="/capitalizefirst">capitalizefirst</a>&nbsp&nbsp
                            <a href="/newlineremove">newlineremove</a>&nbsp&nbsp
                            <a href="/spaceremove">spaceremove</a>&nbsp&nbsp
                            <a href="/charcount">charcount</a>&nbsp&nbsp
                            ''')

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse('''<h1>This is Removepunc</h1><input type=button value="Back" onClick="javascript:history.go(-1);">''')


def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcapitalize = request.POST.get('fullcapitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    print(djtext)
    print(removepunc)
    if removepunc=="on":
        punctuations='''!()-[]{};:"'\,<>./@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i    
        params={'purpose':'REMOVED PUNCTUATIONS','Analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if fullcapitalize=="on":
        analyzed=""
        for i in djtext:
                analyzed=analyzed+i.upper()    
        params={'purpose':'FULL CAPITALIZE','Analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if newlineremove=="on":
        analyzed=""
        for i in djtext:
            if i != "\n" and i !="\r":
                analyzed=analyzed+i    
        params={'purpose':'NEW LINE REMOVE','Analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if spaceremove=="on":
        analyzed=""
        for index,i in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == "  "):
                analyzed=analyzed+i    
        params={'purpose':'SPACE REMOVE','Analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if charcount=="on":
        analyzed=len(djtext) 
        params={'purpose':'SPACE REMOVE','Analyzed_text':analyzed}
        djtext=len(djtext)
        #return render(request,'analyze.html',params)

    if(removepunc!="on" and fullcapitalize!="on" and newlineremove!="on" and spaceremove!="on" and charcount!="on"):
        return HttpResponse("ERROR...(Please Select Any Operation)")
    
    return render(request,'analyze.html',params)


    #else:
    #   return HttpResponse("ERROR...")

def capitalizefirst(request):
    return HttpResponse('''<h1>This is capitalizefirst</h1><a href="about/">Back</a>''')

def newlineremove(request):
    return HttpResponse('''<h1>This is newlineremove</h1><a href="about/">Back</a>''')
    
def spaceremove(request):
    return HttpResponse('''<h1>This is spaceremove</h1><a href="about/">Back</a>''')

def charcount(request):
    return HttpResponse('''<h1>This is charcount</h1><a href="about/">Back</a>''')

