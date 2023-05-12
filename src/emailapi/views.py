from rest_framework import generics

from emailapi.models import Email
from emailapi.serializers import EmailSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

#  The EmailList view will return a list of all email 
#  objects in the database and allow users to create 
#  new email objects
class EmailList(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

# EmailDetail view will retrieve, update, or 
# delete a specific email object based on its ID.
class EmailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
