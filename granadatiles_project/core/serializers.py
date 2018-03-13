from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class BaseCatalogSerializer(BaseSerializer):
    name = serializers.CharField(max_length=150)


class BaseCatalogOrderSerializer(BaseCatalogSerializer):
    order = serializers.IntegerField()


class BaseContentSerializer(BaseSerializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(allow_blank=True)


class BaseContentOrderModel(BaseContentSerializer):
    order = serializers.IntegerField()


class BaseGalleryImageSerializer(BaseContentSerializer):
    image = serializers.CharField(allow_blank=True)


class BaseGalleryNavImageSerializer(BaseGalleryImageSerializer):
    target = serializers.BooleanField()
    link = serializers.URLField(allow_blank=True)
