from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from oauth2_provider.settings import oauth2_settings
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin

import json
from accounts import models
from accounts import serializers

from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import gettext_lazy as _
from django.db import transaction


class UserRegister(CsrfExemptMixin, OAuthLibMixin, APIView):
    permission_classes = (permissions.AllowAny,)

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def get(self,request):


    def post(self, request):
        if request.auth is None:
            data = request.data
            data = data.dict()
            serializer = serializers.RegisterSerializer(data=data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        user = serializer.save()

                        url, headers, body, token_status = self.create_token_response(request)
                        if token_status != 200:
                            raise Exception(json.loads(body).get("error_description", ""))

                        return Response(json.loads(body), status=token_status)
                except Exception as e:
                    return Response(data={"error": e.message}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
