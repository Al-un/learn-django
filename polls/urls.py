from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet)
router.register(r'choices', views.ChoiceViewSet)

urlpatterns = router.urls