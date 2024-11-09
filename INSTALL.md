# Installation de Django-Design-System

## Installation basique

- Installez le paquet

```{ .bash }
pip install django-design-system
```
### Pour Django 5.0+

- Ajoutez `widget_tweaks` et `design_system` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "design_system",
    <votre_app>
]
```

### Pour Django 4.2 et avant

- Ajoutez `widget_tweaks`, `design_system` et `django.forms` à `INSTALLED_APPS` dans le `settings.py` avant la ou les app avec laquelle vous voulez l’utiliser :

```{ .python }
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "design_system",
    "django.forms",
    <votre_app>
]
```

**Attention** : si `django.forms` apparait déjà dans `INSTALLED_APPS`, il doit être placé *après* `design_system`. Sinon les `FormSet`s ne seront pas correctement rendus.

- Ajouter le `FORM_RENDERER` in `settings.py` pour faire fonctionner les formulaires :

```{ .python }
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
```

### Pour toutes les versions

- Inclure les tags dans votre fichier `base.html` (voir par exemple sur [base.html](https://github.com/numerique-gouv/django-design-system/blob/main/example_design_system/templates/example_design_system/base.html))

- Lancer le serveur (`python manage.py runserver`) et aller sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
