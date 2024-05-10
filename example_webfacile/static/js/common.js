const language_selectors = document.querySelectorAll(".webfastoche-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-webfastoche\";SameSite=Strict"
    window.location.reload()
}));
