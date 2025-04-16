from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        # Handle form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(name, email, message)  # You can replace this with DB/email logic
    return render(request, 'contact.html')
