from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),#for login and logout in browasble api
    path('api/v1/', include('api.urls')),
    path("api/v1/auth/", include("dj_rest_auth.urls")), 
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls'))
]
