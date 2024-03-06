from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hey I am Django server</h1>"
     #                   "<p>Hello Django!</p>"
      #                  "<hr>")

    peoples=[
        {"name":"Vicky Kaushal",'age':24},
        {"name":"Julian",'age':13},
        {"name":"Daniel",'age':20},
        {"name":"Sarah",'age':17},
        {"name":"Sarah",'age':63}
    ]

    text="""
    In Python, triple double quotes (""" """) are used to create multiline string literals. This syntax allows you to define strings that span multiple lines without using escape characters. Triple double quotes are often used for docstrings, which are special comments used to document functions, classes, and modules."""

    vegetables=['pumpkin','tomatoes','potatoes','chicken']


    return render(request,'index.html',context={'page':'django 2024','peoples':peoples,'text':text,'vegetables':vegetables})

def about(request):
    context = {'page': 'About'}
    return render(request,'about.html',context)

def contact(request):
    context={'page':'Contact'}
    return render(request,'contact.html',context)
def success_page(request):
    print('*'*10)
    return HttpResponse("Hey I am a success page")
