from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


@permission_classes([AllowAny])
class CreateUserView(CreateAPIView):

    model = get_user_model()
    serializer_class = UserSerializer
