from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'library/index.html')


def about(request):
    return render(request,'library/about.html')
