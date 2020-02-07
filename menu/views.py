from django.shortcuts import render, redirect

# Create your views here.
def menu(request):
    return render(request, "menu.html")

def submission(request):
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comments']=request.POST['comments']
    return render(request, "submittedInfo.html")