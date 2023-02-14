from django.urls import path, include
# from rest_framework.authtoken import views as auth_token
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router = SimpleRouter()
router.register(r'user',views.UserViewSet,basename='user')
app_name = 'accounts'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.Register.as_view(),name='register'),
    # path('api-auth-token/',auth_token.obtain_auth_token),
    path('',include(router.urls))
]

# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODEwMTEzMywiaWF0IjoxNjc2MzczMTMzLCJqdGkiOiI2MzFkMDdkODIzOWE0Y2FhYTgwNmI1MGY2YmI5NWE3OCIsInVzZXJfaWQiOjF9.gsbob1FYEgpDXGK7KLyqRJYbuDdaU88abUIPFGeRcHs",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MjM3MTMzLCJpYXQiOjE2NzYzNzMxMzMsImp0aSI6IjVlYzQxYzZiMjNkNDQyMWE4MzEyMmUwYTE0YTQ0ZDFhIiwidXNlcl9pZCI6MX0.m0jNkyYvZSNis_vIM0I_7FjtldBjpIoplvDQvpPMfoo"
# }