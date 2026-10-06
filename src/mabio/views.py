
from django.shortcuts import render

def indexx(request):
    return render(request, "mabio/presentationbance.html")
    
def index_judi(request):
    return render(request, "mabio/judicael.html")