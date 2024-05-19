Le bandeau de Lettre d’information et Réseaux Sociaux est géré grâce à une balise `include` à insérer dans le bloc `follow_newsletter_social_media` dans le fichier `base.html`.

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "django_cfran/base.html" %}

<!-- [...] -->
{% block follow_newsletter_social_media %}
  {% include "django_cfran/follow.html" %}
{% endblock follow_newsletter_social_media %}

```

Il est alors possible de personnaliser la description de la lettre d’information, l’URL d’inscription ainsi que les réseaux sociaux via la configuration du site dans l’administration de Django.
`
- `<a class="cfran-link cfran-icon-external-link-line cfran-link--icon-right cfran-link--lg" href="https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pied-de-page" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="cfran-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>`
- `<a class="cfran-link cfran-icon-external-link-line cfran-link--icon-right cfran-link--lg" href="https://main--ds-gouv.netlify.app/example/component/footer/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="cfran-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

## Classes pour les boutons des réseaux sociaux

- `cfran-btn--dailymotion`
- `cfran-btn--facebook`
- `cfran-btn--github`
- `cfran-btn--instagram`
- `cfran-btn--linkedin`
- `cfran-btn--mastodon`
- `cfran-btn--snapchat`
- `cfran-btn--telegram`
- `cfran-btn--threads`
- `cfran-btn--tiktok`
- `cfran-btn--twitch`
- `cfran-btn--twitter`
- `cfran-btn--twitter-x`
- `cfran-btn--vimeo`
- `cfran-btn--youtube`

## Personnaliser
Il est possible de le remplacer par votre propre bloc pour étendre ses capacités (par exemple pour n’afficher qu’un des deux blocs ou pour inclure le champ d’adhésion directement dans le bandeau.)

```{.django}
<!-- <votre_app>/templates/<votre_app>/base.html -->
{% extends "django_cfran/base.html" %}

<!-- [...] -->
{% block follow_newsletter_social_media %}
  {% include "<votre_app>/blocks/follow.html" %}
{% endblock follow_newsletter_social_media %}

```

```{.django}
<!-- <votre_app>/templates/<votre_app>/blocks/follow.html -->
{% extends "django_cfran/follow.html" %}
{% block follow_newsletter %}
  <div class="cfran-col-12">
      <div class="cfran-follow__newsletter">
          <div>
              <h2 class="cfran-h5">Abonnez-vous à notre lettre d’information</h2>
              <p class="cfran-text--sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas varius tortor nibh, sit amet tempor nibh finibus et.</p>
          </div>
          <div>
              <form action="">
                  <div class="cfran-input-group">
                      <label class="cfran-label" for="newsletter-email">
                          Votre adresse électronique (ex. : nom@domaine.fr)
                      </label>
                      <div class="cfran-input-wrap cfran-input-wrap--addon">
                          <input class="cfran-input" title="Votre adresse électronique (ex. : nom@domaine.fr)" autocomplete="email" attributes="[object Object]" aria-describedby="newsletter-email-hint-text newsletter-email-messages" placeholder="Votre adresse électronique (ex. : nom@domaine.fr)" id="newsletter-email" type="email">
                          <button class="cfran-btn" id="newsletter-button" title="S’abonner à notre lettre d’information" type="submit">
                              S’abonner
                          </button>
                      </div>
                      <div class="cfran-messages-group" id="newsletter-email-messages" aria-live="assertive">
                      </div>
                  </div>
                  <p id="newsletter-email-hint-text" class="cfran-hint-text">En renseignant votre adresse électronique, vous acceptez de recevoir nos actualités par courriel. Vous pouvez vous désinscrire à tout moment à l’aide des liens de désinscription ou en nous contactant.</p>
              </form>
          </div>
      </div>
  </div>
{% endblock follow_newsletter %}

{% block follow_social %}
{% endblock follow_social %}
```
