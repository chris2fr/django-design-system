from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView
from django_cefran.urls import urlpatterns as cefran_urlpatterns

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("django_cefran/dist/favicon/favicon.ico")
        ),
    ),
    # The "django_cefran/" prefix is here because this site is deployed as doc on
    # https://numerique-gouv.github.io/django_cefran/
    path("admin/", admin.site.urls),
    path("django_cefran/", include("example_cefran.urls")),
]
urlpatterns += cefran_urlpatterns
urlpatterns += [
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
