
from django.urls import path
from .views import *


urlpatterns = [
    path('', HomezView.as_view(), name="home"),
    path('knowledge/', Knowledge.as_view(), name="knowledge"),
    path('research/', Research.as_view(), name="research"),   
    path('publications/', Publications.as_view(), name="publications"),
    path('events/', Events.as_view(), name="events"),   
]
