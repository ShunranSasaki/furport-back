from django.urls import include, path, re_path
from rest_framework import routers
from rest_auth.registration.views import (
    SocialAccountListView,
    SocialAccountDisconnectView,
)
from allauth.socialaccount.views import ConnectionsView

from furport import views


router = routers.DefaultRouter()
router.register(r"events", views.EventViewSet)
router.register(r"general_tags", views.GeneralTagViewSet)
router.register(r"character_tags", views.CharacterTagViewSet)
router.register(r"organization_tags", views.OrganizationTagViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"profiles", views.ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/twitter/", views.TwitterLogin.as_view(), name="twitter_login"),
    path(
        "rest-auth/twitter/connect/",
        views.TwitterConnect.as_view(),
        name="twitter_connect",
    ),
    path(
        "accounts/social/connections/",
        SocialAccountListView.as_view(),
        name="socialaccount_connections",
    ),
    path("socialaccounts/", ConnectionsView.as_view(), name="social_account_list"),
    re_path(
        r"^socialaccounts/(?P<pk>\d+)/disconnect/$",
        SocialAccountDisconnectView.as_view(),
        name="social_account_disconnect",
    ),
]
