from rest_framework import serializers
from .models import Post
from django.contrib.auth import authenticate

class PostModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ("author", "title", "text")


class AuthTokenSerializer(serializers.Serializer):
	username = serializers.CharField(label="Username")
	password = serializers.CharField(
		label="Password",
		style={'input_type': 'password'},
		trim_whitespace=False
	)

	def validate(self, attrs):
		username = attrs.get('username')
		password = attrs.get('password')

		if username and password:
			print("----------Teste--------------")
			print(password)
			print(username)
			print("----------Teste--------------")

			user = authenticate(request=self.context.get('request'),
			username=username, password=password)

			print("----------Teste--------------")
			print(user)
			print("----------Teste--------------")

			# The authenticate call simply returns None for is_active=False
			# users. (Assuming the default ModelBackend authentication
			# backend.)
			if not user:
				msg = 'Unable to log in with provided credentials.'
				raise serializers.ValidationError(msg, code='authorization')
		else:
			msg = 'Must include "username" and "password".'
			raise serializers.ValidationError(msg, code='authorization')

		attrs['user'] = user
		return attrs