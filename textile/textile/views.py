from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<a href='https://www.youtube.com/watch?v=bO5UG_9ggYA'>Best Himeshre")

# def about(request):
#     return HttpResponse("This is create by me")

def index(request):
    # params={'name':'sonu','sallary':12121,'Role':'Python Developer'}
    return render(request,"index.html")

def removepunc(request):
    djtext = request.POST.get('text', 'default')
    # print(djtext)
    djremove = request.POST.get('removepunc1','off')
    uppercase = request.POST.get('uppercase','off')
    extraspace = request.POST.get('extraspace','off')
    newline_remove = request.POST.get('newline_remove','off')
    count = request.POST.get('count','off')
    if djremove == "on":
        a = ""
        b = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for item in djtext:
            if item not in b:
                a = a + item
        params = {'remo':'Remove Puncuations','analyzed': a}
        # return render(request,'remo.html', params)
        djtext=a
    if uppercase=='on':
        a=''
        for i in djtext:
            a=a+i.upper()
        params = {'remo':'Remove Puncuations','analyzed': a}
        # return render(request,'remo.html', params)
        djtext=a
    if newline_remove =='on':
        a=''
        for i in djtext:
            if i!='\n' and i!='\r':
                a=a+i
        params = {'remo':'Remove Puncuations','analyzed': a}
        # return render(request,'remo.html', params)
        djtext=a
    if extraspace=='on':
        a=''
        for index,item in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                a=a+item
        params = {'remo':'Remove Puncuations','analyzed': a}
        # return render(request,'remo.html', params)
        djtext=a
    if count=='on':
        d=djtext.split(' ')
        a=0
        for i in d:
            for j in i:
                a=a+1
        params = {'remo':'Remove Puncuations','analyzed': a}
        djtext=a
    if count!='on' and extraspace!='on' and newline_remove!='on' and removepunc!='on' and uppercase!='on':
        return HttpResponse("Please select any operation and try again")
    return render(request,'remo.html', params)