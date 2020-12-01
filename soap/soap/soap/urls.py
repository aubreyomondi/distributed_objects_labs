from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^soap_service/', 'soap_students_app.views.my_soap_application'),
]
