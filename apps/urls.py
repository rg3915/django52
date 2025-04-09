from django.contrib import admin
from django.urls import include, path

from apps.core import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('school/', include('apps.school.urls', namespace='school')),
    path('admin/', admin.site.urls),
]
