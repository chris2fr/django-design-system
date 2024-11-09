from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView
from django_design_system.urls import urlpatterns as design_system_urlpatterns

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("django_design_system/dist/favicon/favicon.ico")
        ),
    ),
    # The "django_design_system/" prefix is here because this site is deployed as doc on
    # https://numerique-gouv.github.io/django_design_system/
    path("admin/", admin.site.urls),
    path("django_design_system/", include("example_design_system.urls")),
]
urlpatterns += design_system_urlpatterns
urlpatterns += [
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
