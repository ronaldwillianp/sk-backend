from rest_framework import viewsets, generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserUpdateSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from .models import User

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class UserChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def put(self, request, pk):
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        obj = get_user_model().objects.get(pk=pk)
        if not obj.check_password(raw_password=old_password):
            return Response({'error': 'password not match'}, status=400)
        else:
            obj.set_password(new_password)
            obj.save()
            return Response({'success': 'Password changed successfully'}, status=200)



# class UserUpdateGroup(generics.RetrieveUpdateAPIView):
#     serializer_class = UserUpdateGroupSerializer
#     queryset = User.objects.all()
#
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)
