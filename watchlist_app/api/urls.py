from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS,
                basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),
    path('list2/', views.WatchListGV.as_view(), name='watch-list2'),

    
    path('', include(router.urls)),


    path('<int:pk>/review/create/',
         views.ReviewCreate.as_view(), name='review-create'),

    path('<int:pk>/reviews/', views.ReviewList.as_view(),
         name='review-list'),  # all the review for a particular movie [streamplatform-detail]
    path('review/<int:pk>/',  views.ReviewDetail.as_view(),
         name="review-detail"),
    path('user-reviews/', views.UserReview.as_view(), name="user-review"),

]
