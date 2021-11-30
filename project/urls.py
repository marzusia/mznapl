from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mznapl.urls')),
]


handler404 = 'mznapl.views.handler404'
handler500 = 'mznapl.views.handler500'
