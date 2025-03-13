from django.urls import path
from .views import FacebookVoteView, InstagramVoteView

urlpatterns = [
    path('facebook/', FacebookVoteView.as_view(), name='facebook-vote'),
    path('instagram/', InstagramVoteView.as_view(), name='instagram-vote'),
]