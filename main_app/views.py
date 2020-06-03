from django.shortcuts import render
from .models import Bill
# Add the following import
from django.http import HttpResponse

# Define the home view
def index(request):
  return render(request, 'index.html')

def bills_index(request):
  bills = Bill.objects.all()
  return render(request, 'bills/index.html', { 'bills': bills })