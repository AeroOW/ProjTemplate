from django.urls import path
from esports import views as esports_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', esports_views.index.as_view(), name='home'),
    path('api/esports/', esports_views.esport_list),
    path('api/esports/<int:pk>/', esports_views.esport_detail),
    path('api/esports/published/', esports_views.esport_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
