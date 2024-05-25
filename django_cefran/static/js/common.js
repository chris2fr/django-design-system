const language_selectors = document.querySelectorAll(".cefran-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-cefran\";SameSite=Strict"
    window.location.reload()
}));
