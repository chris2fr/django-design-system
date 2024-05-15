const language_selectors = document.querySelectorAll(".cfran-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-cfran\";SameSite=Strict"
    window.location.reload()
}));
