from django.shortcuts import render

# Create your views here.
from .models import Contact
def index(request):
    return render(request, 'mycapp/index.html')

def help(request):
    return render(request, 'mycapp/help.html')

def contacts(request):
    contact_list = Contact.objects.order_by('first_name')
    contact_dict = {'contacts':contact_list}
    return render(request, 'mycapp/contacts.html', context=contact_dict)