from rest_framework import serializers
from .models import ROLE_CHOICES, CustomUser, Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=ROLE_CHOICES, source="type")

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "password", "user_type"]

    def create(self, validated_data):
        user_type = validated_data.pop("type")
        user = CustomUser.objects.create_user(**validated_data, user_type=user_type)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user.id", read_only=True)

    class Meta:
        model = Profile
        fields = ["user_id", "dob"]
