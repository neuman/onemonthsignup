from django.conf.urls import patterns, include, url
import core.views

urlpatterns = patterns('',
    url(r'^$', core.views.SignupView.as_view(), name="signup"),

)


