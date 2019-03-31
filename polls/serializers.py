from rest_framework import serializers

from .models import Poll, Choice

class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = ('topic', 'public', 'closed')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('text', 'poll')