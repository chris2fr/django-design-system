const language_selectors = document.querySelectorAll(".fastoche-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-fastoche\";SameSite=Strict"
    window.location.reload()
}));
