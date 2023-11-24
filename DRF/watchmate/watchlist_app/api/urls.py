from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import(ReviewList, ReviewDetail, ReviewCreate,
WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV)


urlpatterns = [
    # Function Urls
    # path('Flist/', movie_list, name='watch-list-function'),
    # path('<int:pk>', movie_details, name='watch-detail-function'),

    # Class Urls------------------------------
    path('list/', WatchListAV.as_view(), name='watch-list-class'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail-class'),

    path('stream/', StreamPlatformAV.as_view(), name='stream-list-class'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),
         name='stream-detail-class'),

    # Generic Urls------------------------------
    path('review/', ReviewList.as_view(), name='review-list-generic'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail-generic'),


    # Custom Urls------------------------------
    path('stream/review/<int:pk>', ReviewDetail.as_view()),
    path('stream/<int:pk>/review', ReviewList.as_view()),
    path('stream/<int:pk>/review-create',
         ReviewCreate.as_view(), name='review-create-specific'),
]
