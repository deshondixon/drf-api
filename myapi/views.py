from rest_framework import generics
from .serializers import myapiSerializer
from .models import myapi


class myapiList(generics.ListCreateAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = myapi.objects.all()
    serializer_class = myapiSerializer


# The ThingDetail needs the same things
class myapiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = myapi.objects.all()
    serializer_class = myapiSerializer
