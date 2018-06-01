from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


#serializer for user profile object
#model serializers are designed to be used with models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #write only implies you will never be able to read it through the serializer
        extra_kwargs = {'password': {'write_only': True}}

    #start with our create model
    def create(self, validated_data):
        """create and return a new user."""

        #when creating (posting) the user will make sure name and email are validated
        #and then have their password hashsed
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        #write to database and save
        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        #id: primary key
        #user_profile: id from the user profile
        #status_text: actual text of the status
        #created_on: date the post was created on

        #user profiles should be read only, you only want the currently logged in user
        #to create their own statuses

        extra_kwargs = {'user_profile': {'read_only': True}}
