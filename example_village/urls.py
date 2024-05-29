from django_distill import distill_path

import django_village.views
import example_village.views
from example_village.village_components import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path(
        "", django_village.views.index, name="index", distill_file="django_village/index.html"
    ),
    distill_path(
        "doc-contributing",
        django_village.views.doc_contributing,
        name="doc_contributing",
        distill_file="django_village/doc-contributing/index.html",
    ),
    distill_path(
        "doc-install",
        django_village.views.doc_install,
        name="doc_install",
        distill_file="django_village/doc-install/index.html",
    ),
    distill_path(
        "doc-usage",
        django_village.views.doc_usage,
        name="doc_usage",
        distill_file="django_village/doc-usage/index.html",
    ),
    distill_path(
        "components/",
        django_village.views.components_index,
        name="components_index",
        distill_file="django_village/components/index.html",
    ),
    distill_path(
        "components/header/",
        django_village.views.page_component_header,
        name="page_component_header",
        distill_file="django_village/components/header/index.html",
    ),
    distill_path(
        "components/footer/",
        django_village.views.page_component_footer,
        name="page_component_footer",
        distill_file="django_village/components/footer/index.html",
    ),
    distill_path(
        "components/follow/",
        django_village.views.page_component_follow,
        name="page_component_follow",
        distill_file="django_village/components/follow/index.html",
    ),
    distill_path(
        "components/<slug:tag_name>/",
        django_village.views.page_component,
        name="page_component",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form/",
        django_village.views.doc_form,
        name="doc_form",
        distill_file="django_village/form/index.html",
    ),
    distill_path(
        "form/example/",
        example_village.views.page_form,
        name="page_form",
        distill_file="django_village/form/example/index.html",
    ),
    distill_path(
        "form/example-formset/",
        example_village.views.VillageAuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django_village/form/example-formset/index.html",
    ),
    distill_path(
        "resources/colors",
        django_village.views.resource_colors,
        name="resource_colors",
        distill_file="django_village/resources/colors/index.html",
    ),
    distill_path(
        "resources/icons",
        django_village.views.resource_icons,
        name="resource_icons",
        distill_file="django_village/resources/icons/index.html",
    ),
    distill_path(
        "resources/pictograms",
        django_village.views.resource_pictograms,
        name="resource_pictograms",
        distill_file="django_village/resources/pictograms/index.html",
    ),
    distill_path(
        "search/",
        django_village.views.search,
        name="page_search",
        distill_file="django_village/search/index.html",
    ),
]
