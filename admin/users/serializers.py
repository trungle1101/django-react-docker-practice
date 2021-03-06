from rest_framework import serializers

# from .models import User, Permission, Role
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email' ,'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        """This will overide the default CREATE method"""
        password = validated_data.pop('password', None) # eliminate password from initial data
        instance = self.Meta.model(**validated_data)
        if password is not None: 
            instance.set_password(password) # 
        instance.save()
        return instance


# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         fields = '__all__'


# class PermissionRelatedField(serializers.StringRelatedField):
#     def to_representation(self, value):
#         return PermissionSerializer(value).data
    
#     def to_internal_value(self, data):
#         return data


# class RoleSerializer(serializers.ModelSerializer):
#     permission = PermissionSerializer(many=True)

#     class Meta:
#         model = Role
#         fields = '__all__'
    
#     def create(self, validated_data):
#         permissions = validated_data.pop('permission', None)
#         instance = self.Meta.model(**validated_data)
#         instance.save()

#         instance.permissions.add(**permissions)
#         instance.save()
#         return instance
