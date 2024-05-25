from django_distill import distill_path

import django_cefran.views
import example_cefran.views
from example_cefran.cefran_components import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path(
        "", django_cefran.views.index, name="index", distill_file="django_cefran/index.html"
    ),
    distill_path(
        "doc-contributing",
        django_cefran.views.doc_contributing,
        name="doc_contributing",
        distill_file="django_cefran/doc-contributing/index.html",
    ),
    distill_path(
        "doc-install",
        django_cefran.views.doc_install,
        name="doc_install",
        distill_file="django_cefran/doc-install/index.html",
    ),
    distill_path(
        "doc-usage",
        django_cefran.views.doc_usage,
        name="doc_usage",
        distill_file="django_cefran/doc-usage/index.html",
    ),
    distill_path(
        "components/",
        django_cefran.views.components_index,
        name="components_index",
        distill_file="django_cefran/components/index.html",
    ),
    distill_path(
        "components/header/",
        django_cefran.views.page_component_header,
        name="page_component_header",
        distill_file="django_cefran/components/header/index.html",
    ),
    distill_path(
        "components/footer/",
        django_cefran.views.page_component_footer,
        name="page_component_footer",
        distill_file="django_cefran/components/footer/index.html",
    ),
    distill_path(
        "components/follow/",
        django_cefran.views.page_component_follow,
        name="page_component_follow",
        distill_file="django_cefran/components/follow/index.html",
    ),
    distill_path(
        "components/<slug:tag_name>/",
        django_cefran.views.page_component,
        name="page_component",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form/",
        django_cefran.views.doc_form,
        name="doc_form",
        distill_file="django_cefran/form/index.html",
    ),
    distill_path(
        "form/example/",
        example_cefran.views.page_form,
        name="page_form",
        distill_file="django_cefran/form/example/index.html",
    ),
    distill_path(
        "form/example-formset/",
        example_cefran.views.CefranAuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django_cefran/form/example-formset/index.html",
    ),
    distill_path(
        "resources/colors",
        django_cefran.views.resource_colors,
        name="resource_colors",
        distill_file="django_cefran/resources/colors/index.html",
    ),
    distill_path(
        "resources/icons",
        django_cefran.views.resource_icons,
        name="resource_icons",
        distill_file="django_cefran/resources/icons/index.html",
    ),
    distill_path(
        "resources/pictograms",
        django_cefran.views.resource_pictograms,
        name="resource_pictograms",
        distill_file="django_cefran/resources/pictograms/index.html",
    ),
    distill_path(
        "search/",
        django_cefran.views.search,
        name="page_search",
        distill_file="django_cefran/search/index.html",
    ),
]
