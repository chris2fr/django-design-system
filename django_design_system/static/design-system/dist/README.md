# design-system

## Utilisation
Afin d’utiliser le composant `design-system`, il est nécessaire d’ajouter les fichiers de styles et de scripts présents dans le dossier dist dans l'ordre suivant :\n
```html
<html>
  <head>
    <link href="design-system/css/design-system/design-system.min.css" rel="stylesheet">
  </head>
  <body>
    <script type="module" href="js/design-system/design-system.module.min.js" ></script>
    <script type="text/javascript" nomodule href="js/design-system/design-system.nomodule.min.js" ></script>
  </body>
</html>
```