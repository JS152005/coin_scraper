from django.urls import path, include
from rest_framework import routers
from.views import StartScrapingView, ScrapingStatusView

router = routers.DefaultRouter()
router.register(r'taskmanager', StartScrapingView, basename='start_scraping')
router.register(r'taskmanager/(?P<job_id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', ScrapingStatusView, basename='scraping_status')

urlpatterns = [
    path('', include(router.urls)),
]