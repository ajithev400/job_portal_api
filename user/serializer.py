from rest_framework import serializers
from account.models import Account
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','email','first_name','last_name','mobile','password')
        extra_kwargs={'email':{'required':True},'password': {'write_only': True},}
        

    def validate(self,data):
        user = Account(**data)
        password = data.get('password')
        try:
            validate_password(password,user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password':serializer_errors['non_field_errors']}
            )
        return data
    
    def create(self,validated_data):
        first_name =validated_data['first_name']
        last_name = validated_data['last_name']
        user=Account.objects.create_user(
            email= validated_data['email'],
            first_name = first_name,
            last_name= last_name,
            mobile = validated_data['mobile'],
            password = validated_data['password'], 
        )
        return user

# class UserSerializer1(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = (
#             'first_name',
#             'last_name',
#             'mobile',
#             'email',
#         )