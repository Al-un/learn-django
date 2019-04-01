from rest_framework import viewsets
from rest_framework.response import Response

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer

class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint for polls
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def list(self, request):
        '''
        Limit polls list to public polls only
        '''
        queryset = Poll.objects.filter(public=True)
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for choices
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
