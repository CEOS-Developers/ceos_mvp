from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .views import SiteListView, SiteCreateView, SiteVoteView

urlpatterns = [
    path('docs/', get_swagger_view(title='API Document')),
    path('sites/', SiteListView.as_view(), name='site-list'),
    path('sites/create/', SiteCreateView.as_view(), name='site-create'),
    path('sites/<int:pk>/vote/', SiteVoteView.as_view(), name='site-vote')
]