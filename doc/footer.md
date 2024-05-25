Le pied de page est géré grâce à une balise `include` dans le fichier `base.html`. Si vous n’avez pas besoin de le personnaliser, vous n’avez rien à faire.

Il est alors possible de personnaliser la description ainsi que le bloc-marque via la configuration du site dans l’administration de Django.

- <a class="cefran-link cefran-icon-external-link-line cefran-link--icon-right cefran-link--lg" href="https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pied-de-page" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="cefran-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="cefran-link cefran-icon-external-link-line cefran-link--icon-right cefran-link--lg" href="https://main--ds-gouv.netlify.app/example/component/footer/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="cefran-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

## Personnaliser

Il est possible de l’étendre pour le personnaliser, par exemple pour ajouter le sélecteur de thème :

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "django_cefran/base.html" %}

<!-- [...] -->
{% block footer %}
  {% include "<votre_app>/blocks/footer.html" %}
{% endblock footer %}

```

```
<!-- <votre_app>/templates/<votre_app>/blocks/footer.html -->
{% extends "django_cefran/footer.html" %}
{% block footer_links %}
  {{ block.super }}
  <li class="cefran-footer__bottom-item">
    <button id="footer__bottom-link__parametres-affichage"
            aria-controls="cefran-theme-modal"
            data-cefran-opened="false"
            class="cefran-icon-theme-fill cefran-link--icon-left cefran-footer__bottom-link"
            data-cefran-js-modal-button="true">
      Paramètres d’affichage
    </button>
  </li>
{% endblock footer_links %}
```

## Blocs dépréciés
- Le bloc `brand`, qui ne permet pas toutes les personnalisations nécessaires, va être supprimé à terme. Les personnalisations sont à mettre dans le nouveau bloc `footer_brand`.
- Même chose pour le bloc `footer_content`, à remplacer à terme par le nouveau bloc `footer_description`.
