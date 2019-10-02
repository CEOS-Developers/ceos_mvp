from rest_framework import serializers
from core.models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = [
            'id',
            'title',
            'url',
            'vote_count'
        ]
