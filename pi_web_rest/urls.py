from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from pi_web_rest import views

urlpatterns = [
    path('current_values/<str:str_taglist>/', views.CurrentValues.as_view()),
    path('recorded_values/<str:begin>/<str:end>/<str:str_taglist>/', views.RecordedValues.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)