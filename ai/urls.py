from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
path("",views.index,name="index"),
path("/news_of_ai=<int:id>",views.page,name="ai"),
path("",views.index1,name="page")

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

