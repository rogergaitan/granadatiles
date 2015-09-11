from rest_framework import serializers


class BaseCatalogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)


class BaseCatalogOrderSerializer(BaseCatalogSerializer):
    order = serializers.IntegerField()


class BaseContentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(allow_blank=True)


class BaseContentOrderModel(BaseContentSerializer):
    order = serializers.IntegerField()


class BaseGallerieImageSerializer(BaseContentSerializer):
    image = serializers.CharField(allow_blank=True)


class BaseGallerieNavImageSerializer(BaseGallerieImageSerializer):
    target = serializers.BooleanField()
    link = serializers.URLField(allow_blank=True)
