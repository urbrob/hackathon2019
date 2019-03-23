from django.shortcuts import render
from django.http import Http404
from accounts.models import Group
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from oauth2_provider.settings import oauth2_settings
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin
from django.contrib.auth import authenticate, login
import json
from django.urls import reverse
from accounts import models
from accounts import serializers
from accounts.forms import RegistrationForm
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
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
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})


    def post(self, request):
        if request.auth is None:

            data = request.data
            data = data.dict()
            data['is_active'] = True
            data['username'] = data['email']
            serializer = serializers.RegisterSerializer(data=data)
            if serializer.is_valid():
                try:
                    user = serializer.save()

                    """
                    UNSUPPORTED GRANT TYPE - FIX WITH OAUTH2
                    url, headers, body, token_status = self.create_token_response(request)
                    if token_status != 200:
                        raise Exception(json.loads(body).get("error_description", ""))
                    """
                    if data.get('web-api'):
                        login(request, user)
                        return HttpResponseRedirect(reverse('home'))
                    else:
                        return Response({'message': serializer.validated_data}, status=200)
                except Exception as e:
                    # ADD LOGIN TOKEN auth
                    return Response(data={serializer.data()}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
