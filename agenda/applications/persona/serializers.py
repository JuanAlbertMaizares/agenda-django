from email.policy import default
from .models import Person, Reunion, Hobby
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ('__all__')
        
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField() 
    activo = serializers.BooleanField(default=False)
    
class PersonSerializer2(serializers.ModelSerializer):
    modelo_activo = serializers.BooleanField(default=False)
    class Meta:
        model = Person
        fields = ('__all__')
class ReunionSerializer(serializers.ModelSerializer):
    persona = PersonSerializer()
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
class HobbySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hobby
        fields = ('__all__')
class PersonSerializer3(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True)
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
        )