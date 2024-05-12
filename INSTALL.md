# Installation de Django-FASTOCHE

## Installation basique

- Installez le paquet

```{ .bash }
pip install django-fastoche
```
### Pour Django 5.0+

- Ajoutez `widget_tweaks` et `fastoche` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "fastoche",
    <votre_app>
]
```

### Pour Django 4.2 et avant

- Ajoutez `widget_tweaks`, `fastoche` et `django.forms` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "fastoche",
    "django.forms",
    <votre_app>
]
```

**Attention** : si `django.forms` apparait déjà dans `INSTALLED_APPS`, il doit être placé *après* `fastoche`. Sinon les `FormSet`s ne seront pas correctement rendus.

- Ajouter le `FORM_RENDERER` in `settings.py` pour faire fonctionner les formulaires :

```{ .python }
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
```

### Pour toutes les versions

- Inclure les tags dans votre fichier `base.html` (voir par exemple sur [base.html](https://github.com/numerique-gouv/django-fastoche/blob/main/example_fastoche/templates/example_fastoche/base.html))

- Lancer le serveur (`python manage.py runserver`) et aller sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
