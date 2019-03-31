from rest_framework import viewsets

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer

class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint for polls
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for choices
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
