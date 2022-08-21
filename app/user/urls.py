from django.urls import path

from user.views import UserViewSet, CreateUserView, CreateTokenView, ManageUserView

app_name = 'user'

urlpatterns = [
    # url(r'^inform/$', UserViewSet.as_view({'get': 'list'}), name='information')
    path('', UserViewSet.list, name='list'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('manage/', ManageUserView.as_view(), name='manage')
    # path('read/<id>/')
]

