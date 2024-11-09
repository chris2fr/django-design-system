const language_selectors = document.querySelectorAll(".design-system-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-design-system\";SameSite=Strict"
    window.location.reload()
}));
