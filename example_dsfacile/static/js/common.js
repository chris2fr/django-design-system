const language_selectors = document.querySelectorAll(".dsfacile-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-dsfacile\";SameSite=Strict"
    window.location.reload()
}));
