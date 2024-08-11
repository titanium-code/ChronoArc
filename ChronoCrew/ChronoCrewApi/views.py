from rest_framework import generics
from .models import Members
from .serializers import MembersSerializer


class MembersListCreate(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class MembersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
