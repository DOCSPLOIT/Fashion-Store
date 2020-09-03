from rest_framework import serializers

from .models import Fashions
from django.forms.models import model_to_dict


class FashionSerializer(serializers.ModelSerializer):

    fields_to_be_removed = model_to_dict(Fashions, fields=[
        field.name for field in Fashions._meta.fields])

    class Meta:
        model = Fashions
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for field in self.fields_to_be_removed:
            try:
                if rep[field] is None:  # checks if value is 'None', this is different from "emptiness"
                    rep.pop(field)
            except KeyError:
                pass
        return rep
