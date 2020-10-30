from django.urls import path
from .views import Get_Summary, Get_Summary_Text, Get_Summary_No_User, Get_Summary_Text_No_User

app_name='Summary'
urlpatterns = [
    path('Get/Summary/<id>/', Get_Summary, name='Get Summary'),
    path('Get/Summary/Text/<id>/', Get_Summary_Text, name='Get Summary Text'),
    path('Get/Summary/User/<id>/',  Get_Summary_No_User, name='Get Summary No User'),
    path('Get/Summary/Text/User/<id>/', Get_Summary_Text_No_User, name='Get Summary Text No User'),
    ]