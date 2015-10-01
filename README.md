Frontend
========

The frontend is hosted using [GitHub Pages](https://pages.github.com/).

The app is written using [AngularJS](https://angularjs.org/) and [Foundation](http://foundation.zurb.com/). All dependencies are already included.

The data is queried from the [Code for Birmingham Brigade Site](https://brigades.opendatanetwork.com/catalog?Brigade_Group=Code%20for%20Birmingham) on the [Brigade Open Data Sharing Platform](https://brigades.opendatanetwork.com/) through the [Socrata API](http://dev.socrata.com/). The four datasets of interest start with "Open Disclosure Alabama" and are updated once a day:

- [Parties](https://brigades.opendatanetwork.com/dataset/Open-Disclosure-Alabama-Parties/kjgr-g56d)
- [Districts](https://brigades.opendatanetwork.com/dataset/Open-Disclosure-Alabama-Districts/p8kt-epji)
- [Transactions](https://brigades.opendatanetwork.com/dataset/Open-Disclosure-Alabama-Transactions/vcap-yyfq)
- [Transactees](https://brigades.opendatanetwork.com/dataset/Open-Disclosure-Alabama-Transactees/9xmj-xdkh)


## Getting Started
To serve the application locally for development, run script/server and navigate to localhost:8000 in Chrome or 0.0.0.0:8000 in Firefox.
