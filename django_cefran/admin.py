from django.contrib import admin
from django_cefran.models import CefranConfig, CefranSocialMedia

from django.utils.translation import gettext_lazy as _


class CefranSocialMediaInline(admin.TabularInline):
    model = CefranSocialMedia
    readonly_fields = ("id",)
    extra = 1


@admin.register(CefranConfig)
class CefranConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("", {"fields": ("language",)}),
        (
            "Site",
            {
                "fields": (
                    ("site_title", "beta_tag"),
                    "site_tagline",
                    "notice",
                    "mourning",
                )
            },
        ),
        (
            "En-tête",
            {
                "fields": (
                    "header_brand",
                    "header_brand_html",
                ),
            },
        ),
        (
            "Pied de page",
            {
                "fields": (
                    "footer_brand",
                    "footer_brand_html",
                    "footer_description",
                    "accessibility_status",
                ),
            },
        ),
        (
            "Logo opérateur",
            {
                "fields": (
                    "operator_logo_file",
                    "operator_logo_alt",
                    "operator_logo_width",
                ),
            },
        ),
        (
            _("Newsletter"),
            {
                "fields": (
                    "newsletter_description",
                    "newsletter_url",
                )
            },
        ),
    )
    inlines = [CefranSocialMediaInline]
