from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("products/", include("products.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))

]