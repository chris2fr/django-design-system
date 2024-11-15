/*! DESIGN-SYSTEM v0.0.3 | SPDX-License-Identifier: MIT | License-Filename: LICENSE.md | restricted use (see terms and conditions) */

(function () {
  'use strict';

  var config = {
    prefix: 'design-system',
    namespace: 'design-system',
    version: '0.0.3'
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
