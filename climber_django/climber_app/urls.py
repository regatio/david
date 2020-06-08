from django.urls import path
from .views import *

app_name = 'climber_app'

urlpatterns = [

    path('climber/list', ClimberView.as_view()),
    path('climber/add', ClimberAdd.as_view()),
    path('climber/<int:pk>', ClimberEdit.as_view()),
    path('group/list', GroupView.as_view()),
    path('group/add', GroupAdd.as_view()),
    path('group/<int:pk>', GroupEdit.as_view()),
    path('mountain/list', MountainView.as_view()),
    path('mountain/add', MountainAdd.as_view()),
    path('mountain/<int:pk>', MountainEdit.as_view()),
    path('climbing/list', ClimbingView.as_view()),
    path('climbing/add', ClimbingAdd.as_view()),
    path('climbing/<int:pk>', ClimbingEdit.as_view()),
    path('club/list', ClubView.as_view()),
    path('club/add', ClubAdd.as_view()),
    path('club/<int:pk>', ClubEdit.as_view()),
    path('owner/add', ClubOwnerAdd.as_view()),
    path('owner/<int:pk>', ClubOwnerEdit.as_view()),
    path('owner/list', ClubOwnerView.as_view()),
]
