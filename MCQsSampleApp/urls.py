from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mcqs_list),
    path('question_details/', views.question_details,name='question_details'),
    path(r'^question_list/(?P<qestion_id>\w+)', views.question_list,name='question_list'),
]
