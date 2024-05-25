from itertools import islice
from textwrap import dedent

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_safe

from django_cefran.utils import generate_summary_items

from example_cefran.forms import ColorForm, ExampleForm

from example_cefran.cefran_components import (
    ALL_IMPLEMENTED_COMPONENTS,
    IMPLEMENTED_COMPONENTS,
    EXTRA_COMPONENTS,
    NOT_YET_IMPLEMENTED_COMPONENTS,
    WONT_BE_IMPLEMENTED,
)

# Used by the module = getattr(globals()["cefran_tags"], f"cefran_{tag_name}") line
from django_cefran.templatetags import cefran_tags  # noqa

# /!\ In order to test formset
from django.views.generic import CreateView
from django.http import HttpResponse
from example_cefran.forms import (
    CefranAuthorCreateForm,
    CefranBookCreateFormSet,
    CefranBookCreateFormHelper,
)
from example_cefran.models import CefranAuthor
from example_cefran.utils import format_markdown_from_file

from django_cefran import views

def page_form(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ExampleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("/thanks/")
            pass

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExampleForm()

    payload = init_payload(
        "Formulaire basique",
        request=request,
        links=[{"url": reverse("doc_form"), "title": "Formulaires"}],
    )
    payload["form"] = form

    return render(request, "django_cefran/page_form.html", payload)


# /!\ Example view for form and formset
class CefranAuthorCreateView(CreateView):
    model = CefranAuthor
    form_class = CefranAuthorCreateForm
    formset = None
    template_name = "django_cefran/example_form.html"
    # /!\ Your template needs to extends form_base.html. If you use formset,
    # your template needs to include another template which extends formset_base.html

    def get(self, request, *args, **kwargs):
        instance = None  # noqa: F841
        try:
            if self.object:
                instance = self.object  # noqa: F841
        except Exception:
            self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.formset = self.get_formset(request)
        formset = self.formset
        book_formhelper = CefranBookCreateFormHelper()  # noqa: F841

        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def get_formset(self, request, instance=None):
        if request.POST and instance:
            self.formset = CefranBookCreateFormSet(
                request.POST,
                request.FILES,
                instance=instance,
            )
        else:
            self.formset = CefranBookCreateFormSet()
        return self.formset

    def get_context_data(self, **kwargs):
        context = super(CefranAuthorCreateView, self).get_context_data(**kwargs)

        payload = init_payload(
            "Formulaire avec formset",
            request,
            links=[{"url": reverse("doc_form"), "title": "Formulaires"}],
        )

        for key, value in payload.items():
            context[key] = value

        book_formhelper = CefranBookCreateFormHelper()

        instance = None
        try:
            if self.object:
                instance = self.object
        except Exception:
            self.object = None

        # /!\ Pass your form, formset and helper to the context
        if self.request.POST:
            context["form"] = self.form_class(self.request.POST)
            context["formset"] = CefranBookCreateFormSet(
                self.request.POST, self.request.FILES, instance=instance
            )
            context["book_formhelper"] = book_formhelper
        else:
            context["form"] = self.form_class()
            self.formset = self.get_formset(self.request)
            context["formset"] = self.formset
            context["book_formhelper"] = book_formhelper

        context["object_name"] = "book"

        # /!\ Don't forget your cefran button
        context["btn_submit"] = {
            "label": "Soumettre",
            "onclick": "",
            "type": "submit",
        }
        return context

    def post(self, request, *args, **kwargs):
        instance = None
        try:
            if self.object:
                instance = self.object
        except Exception:
            self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = CefranBookCreateFormSet(
            self.request.POST, self.request.FILES, instance=instance
        )

        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):  # type: ignore
        """
        Called if all forms are valid. Creates a CefranAuthor instance along
        with associated books and then redirects to a success page.
        """

        self.object = form.save()
        formset.instance = (
            self.object
        )  # /!\ Before saving formset, link it to the object created with the main form
        formset.save()

        return HttpResponse(b"Success !")

    def form_invalid(self, form, formset):  # type: ignore
        """
        Called if whether a form is invalid. Re-renders the context
        data with the data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

