from rest_framework import serializers

from new_app.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['name', 'game_count', 'score']