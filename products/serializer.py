from rest_framework import serializers

from mysite.products.models import Product


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()


    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance