/*! CFRAN v11.2.2 | SPDX-License-Identifier: MIT | License-Filename: LICENSE.md | restricted use (see terms and conditions) */

(function () {
  'use strict';

  var config = {
    prefix: 'cfran',
    namespace: 'cfran',
    version: '11.2.2'
  };

  var api = window[config.namespace];

  var ButtonSelector = {
    EQUISIZED_BUTTON: ((api.internals.ns.selector('btns-group--equisized')) + " " + (api.internals.ns.selector('btn'))),
    EQUISIZED_GROUP: api.internals.ns.selector('btns-group--equisized')
  };

  api.button = {
    ButtonSelector: ButtonSelector
  };

  api.internals.register(api.button.ButtonSelector.EQUISIZED_BUTTON, api.core.Equisized);
  api.internals.register(api.button.ButtonSelector.EQUISIZED_GROUP, api.core.EquisizedsGroup);

})();
//# sourceMappingURL=button.nomodule.js.map
