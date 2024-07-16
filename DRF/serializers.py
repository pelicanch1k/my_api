from rest_framework import serializers

from .models import Json, Metadata, Microdata

class JsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Json
        fields = ('title',)

class MetadataSerializer(serializers.ModelSerializer):
    keywords = serializers.JSONField()

    class Meta:
        model = Metadata
        fields = ('description', 'keywords', 'canonical', 'language')

class ContactSerializer(serializers.Serializer):
    telephone = serializers.CharField()
    email = serializers.EmailField()

class MicrodataSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Microdata
        fields = ('schemaType', 'name', 'url', 'logo', 'contact')

class WebsiteSerializer(serializers.Serializer):
    json = JsonSerializer()
    metadata = MetadataSerializer()
    microdata = MicrodataSerializer()

    def to_representation(self, instance):
        json_data = self.fields['json'].to_representation(instance)
        metadata_data = self.fields['metadata'].to_representation(instance)
        microdata_data = self.fields['microdata'].to_representation(instance)
        return {
            'json': json_data,
            'metadata': metadata_data,
            'microdata': microdata_data
        }