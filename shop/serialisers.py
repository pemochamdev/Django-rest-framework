from rest_framework.serializers import ModelSerializer

from shop import models

class CategorySerializer(ModelSerializer):


    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description', 'date_created']



class ProductSerializer(ModelSerializer):


    class Meta:
        model = models.Product
        fields = ['id', 'name', 'category', 'date_created']



class ArticleSerializer(ModelSerializer):


    class Meta:
        model = models.Article
        fields = ['id', 'date_created', 'name', 'price', 'product']