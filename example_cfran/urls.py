from django_distill import distill_path

from example_cfran import views
from example_cfran.cfran_components import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path(
        "", views.index, name="index", distill_file="django-cfran/index.html"
    ),
    distill_path(
        "doc-contributing",
        views.doc_contributing,
        name="doc_contributing",
        distill_file="django-cfran/doc-contributing/index.html",
    ),
    distill_path(
        "doc-install",
        views.doc_install,
        name="doc_install",
        distill_file="django-cfran/doc-install/index.html",
    ),
    distill_path(
        "doc-usage",
        views.doc_usage,
        name="doc_usage",
        distill_file="django-cfran/doc-usage/index.html",
    ),
    distill_path(
        "components/",
        views.components_index,
        name="components_index",
        distill_file="django-cfran/components/index.html",
    ),
    distill_path(
        "components/header/",
        views.page_component_header,
        name="page_component_header",
        distill_file="django-cfran/components/header/index.html",
    ),
    distill_path(
        "components/footer/",
        views.page_component_footer,
        name="page_component_footer",
        distill_file="django-cfran/components/footer/index.html",
    ),
    distill_path(
        "components/follow/",
        views.page_component_follow,
        name="page_component_follow",
        distill_file="django-cfran/components/follow/index.html",
    ),
    distill_path(
        "components/<slug:tag_name>/",
        views.page_component,
        name="page_component",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form/",
        views.doc_form,
        name="doc_form",
        distill_file="django-cfran/form/index.html",
    ),
    distill_path(
        "form/example/",
        views.page_form,
        name="page_form",
        distill_file="django-cfran/form/example/index.html",
    ),
    distill_path(
        "form/example-formset/",
        views.CfranAuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django-cfran/form/example-formset/index.html",
    ),
    distill_path(
        "resources/colors",
        views.resource_colors,
        name="resource_colors",
        distill_file="django-cfran/resources/colors/index.html",
    ),
    distill_path(
        "resources/icons",
        views.resource_icons,
        name="resource_icons",
        distill_file="django-cfran/resources/icons/index.html",
    ),
    distill_path(
        "resources/pictograms",
        views.resource_pictograms,
        name="resource_pictograms",
        distill_file="django-cfran/resources/pictograms/index.html",
    ),
    distill_path(
        "search/",
        views.search,
        name="page_search",
        distill_file="django-cfran/search/index.html",
    ),
]
