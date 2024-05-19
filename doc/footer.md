Le pied de page est géré grâce à une balise `include` dans le fichier `base.html`. Si vous n’avez pas besoin de le personnaliser, vous n’avez rien à faire.

Il est alors possible de personnaliser la description ainsi que le bloc-marque via la configuration du site dans l’administration de Django.

- <a class="cfran-link cfran-icon-external-link-line cfran-link--icon-right cfran-link--lg" href="https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pied-de-page" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="cfran-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="cfran-link cfran-icon-external-link-line cfran-link--icon-right cfran-link--lg" href="https://main--ds-gouv.netlify.app/example/component/footer/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="cfran-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

## Personnaliser

Il est possible de l’étendre pour le personnaliser, par exemple pour ajouter le sélecteur de thème :

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "django_cfran/base.html" %}

<!-- [...] -->
{% block footer %}
  {% include "<votre_app>/blocks/footer.html" %}
{% endblock footer %}

```

```
<!-- <votre_app>/templates/<votre_app>/blocks/footer.html -->
{% extends "django_cfran/footer.html" %}
{% block footer_links %}
  {{ block.super }}
  <li class="cfran-footer__bottom-item">
    <button id="footer__bottom-link__parametres-affichage"
            aria-controls="cfran-theme-modal"
            data-cfran-opened="false"
            class="cfran-icon-theme-fill cfran-link--icon-left cfran-footer__bottom-link"
            data-cfran-js-modal-button="true">
      Paramètres d’affichage
    </button>
  </li>
{% endblock footer_links %}
```

## Blocs dépréciés
- Le bloc `brand`, qui ne permet pas toutes les personnalisations nécessaires, va être supprimé à terme. Les personnalisations sont à mettre dans le nouveau bloc `footer_brand`.
- Même chose pour le bloc `footer_content`, à remplacer à terme par le nouveau bloc `footer_description`.
