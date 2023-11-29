from django.urls import path, include


urlpatterns = [
    path('versions/', include('api.v1.urls')),
]