from django_distill import distill_path

import django_fastoche.views
import example_fastoche.views
from example_fastoche.fastoche_components import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path(
        "", django_fastoche.views.index, name="index", distill_file="django_fastoche/index.html"
    ),
    distill_path(
        "doc-contributing",
        django_fastoche.views.doc_contributing,
        name="doc_contributing",
        distill_file="django_fastoche/doc-contributing/index.html",
    ),
    distill_path(
        "doc-install",
        django_fastoche.views.doc_install,
        name="doc_install",
        distill_file="django_fastoche/doc-install/index.html",
    ),
    distill_path(
        "doc-usage",
        django_fastoche.views.doc_usage,
        name="doc_usage",
        distill_file="django_fastoche/doc-usage/index.html",
    ),
    distill_path(
        "components/",
        django_fastoche.views.components_index,
        name="components_index",
        distill_file="django_fastoche/components/index.html",
    ),
    distill_path(
        "components/header/",
        django_fastoche.views.page_component_header,
        name="page_component_header",
        distill_file="django_fastoche/components/header/index.html",
    ),
    distill_path(
        "components/footer/",
        django_fastoche.views.page_component_footer,
        name="page_component_footer",
        distill_file="django_fastoche/components/footer/index.html",
    ),
    distill_path(
        "components/follow/",
        django_fastoche.views.page_component_follow,
        name="page_component_follow",
        distill_file="django_fastoche/components/follow/index.html",
    ),
    distill_path(
        "components/<slug:tag_name>/",
        django_fastoche.views.page_component,
        name="page_component",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form/",
        django_fastoche.views.doc_form,
        name="doc_form",
        distill_file="django_fastoche/form/index.html",
    ),
    distill_path(
        "form/example/",
        example_fastoche.views.page_form,
        name="page_form",
        distill_file="django_fastoche/form/example/index.html",
    ),
    distill_path(
        "form/example-formset/",
        example_fastoche.views.FastocheAuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django_fastoche/form/example-formset/index.html",
    ),
    distill_path(
        "resources/colors",
        django_fastoche.views.resource_colors,
        name="resource_colors",
        distill_file="django_fastoche/resources/colors/index.html",
    ),
    distill_path(
        "resources/icons",
        django_fastoche.views.resource_icons,
        name="resource_icons",
        distill_file="django_fastoche/resources/icons/index.html",
    ),
    distill_path(
        "resources/pictograms",
        django_fastoche.views.resource_pictograms,
        name="resource_pictograms",
        distill_file="django_fastoche/resources/pictograms/index.html",
    ),
    distill_path(
        "search/",
        django_fastoche.views.search,
        name="page_search",
        distill_file="django_fastoche/search/index.html",
    ),
]
