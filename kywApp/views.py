from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def study(request):
    return render(request, 'study.html')

def introduce(request):
    return render(request, 'introduce.html')
# Create your views here.
