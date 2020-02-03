from rest_framework import serializers
from apis.models import Article

# Serializers define the API representation.
class ArticleSerializer(serializers.Serializer):
    headline = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        model = Article
        fields = ['headline', 'content']