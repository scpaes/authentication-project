from django.contrib import admin
from django.urls import path
from .views import ApiEndpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', ApiEndpoint.as_view()),  # an example resource endpoint
]
