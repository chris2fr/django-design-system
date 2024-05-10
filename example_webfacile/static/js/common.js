const language_selectors = document.querySelectorAll(".webfacile-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-webfacile\";SameSite=Strict"
    window.location.reload()
}));
