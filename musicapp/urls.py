from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongsViewset, ArtisteViewset, LyricViewset

router = DefaultRouter()
router.register('song', SongsViewset)
router.register('artiste', ArtisteViewset)
router.register('lyric', LyricViewset)

urlpatterns = [
  path('', include(router.urls)),
]