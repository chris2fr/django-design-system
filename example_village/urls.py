from django_distill import distill_path

import django_design_system.views
import example_design_system.views
from example_design_system.design_system_components import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path(
        "", django_design_system.views.index, name="index", distill_file="django_design_system/index.html"
    ),
    distill_path(
        "doc-contributing",
        django_design_system.views.doc_contributing,
        name="doc_contributing",
        distill_file="django_design_system/doc-contributing/index.html",
    ),
    distill_path(
        "doc-install",
        django_design_system.views.doc_install,
        name="doc_install",
        distill_file="django_design_system/doc-install/index.html",
    ),
    distill_path(
        "doc-usage",
        django_design_system.views.doc_usage,
        name="doc_usage",
        distill_file="django_design_system/doc-usage/index.html",
    ),
    distill_path(
        "components/",
        django_design_system.views.components_index,
        name="components_index",
        distill_file="django_design_system/components/index.html",
    ),
    distill_path(
        "components/header/",
        django_design_system.views.page_component_header,
        name="page_component_header",
        distill_file="django_design_system/components/header/index.html",
    ),
    distill_path(
        "components/footer/",
        django_design_system.views.page_component_footer,
        name="page_component_footer",
        distill_file="django_design_system/components/footer/index.html",
    ),
    distill_path(
        "components/follow/",
        django_design_system.views.page_component_follow,
        name="page_component_follow",
        distill_file="django_design_system/components/follow/index.html",
    ),
    distill_path(
        "components/<slug:tag_name>/",
        django_design_system.views.page_component,
        name="page_component",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form/",
        django_design_system.views.doc_form,
        name="doc_form",
        distill_file="django_design_system/form/index.html",
    ),
    distill_path(
        "form/example/",
        example_design_system.views.page_form,
        name="page_form",
        distill_file="django_design_system/form/example/index.html",
    ),
    distill_path(
        "form/example-formset/",
        example_design_system.views.DesignSystemAuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django_design_system/form/example-formset/index.html",
    ),
    distill_path(
        "resources/colors",
        django_design_system.views.resource_colors,
        name="resource_colors",
        distill_file="django_design_system/resources/colors/index.html",
    ),
    distill_path(
        "resources/icons",
        django_design_system.views.resource_icons,
        name="resource_icons",
        distill_file="django_design_system/resources/icons/index.html",
    ),
    distill_path(
        "resources/pictograms",
        django_design_system.views.resource_pictograms,
        name="resource_pictograms",
        distill_file="django_design_system/resources/pictograms/index.html",
    ),
    distill_path(
        "search/",
        django_design_system.views.search,
        name="page_search",
        distill_file="django_design_system/search/index.html",
    ),
]
