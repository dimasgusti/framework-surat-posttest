from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'pages/about.html')