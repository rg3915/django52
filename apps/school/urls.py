from django.urls import path

from apps.school import views as v

app_name = 'school'


urlpatterns = [
    path('', v.StudentListView.as_view(), name='student_list'),
    path('create', v.StudentCreateView.as_view(), name='student_create'),
]
