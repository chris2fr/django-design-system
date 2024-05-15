from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("cfran/dist/favicon/favicon.ico")
        ),
    ),
    # The "django-cfran/" prefix is here because this site is deployed as doc on
    # https://numerique-gouv.github.io/django-cfran/
    path("admin/", admin.site.urls),
    path("django-cfran/", include("example_cfran.urls")),
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
