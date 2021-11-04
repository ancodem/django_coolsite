from django.conf.urls import handler404
from django.urls import (
    path, 
    re_path,
)

from .views import (
    index,
    categories,
    archive,
)

urlpatterns = [
    path('', index),
    path('cats/<slug:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
