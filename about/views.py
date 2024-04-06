from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about/base.html')

def who(request, who):
    return render(request, 'about/who.html', {'who': who})