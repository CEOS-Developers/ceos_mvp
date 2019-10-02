from django.urls import path
from .views import SiteListView, SiteCreateView, SiteVoteView

urlpatterns = [
    path('sites/', SiteListView.as_view(), name='site-list'),
    path('sites/create/', SiteCreateView.as_view(), name='site-create'),
    path('sites/<int:pk>/vote/', SiteVoteView.as_view(), name='site-vote')
]