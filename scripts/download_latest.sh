#!/bin/bash

# clean the dist directory
cd django_design_system/static/design-system/
rm dist/* -rf

# Get the latest release
latest_release="$(
curl -s https://api.github.com/repos/GouvernementFR/design-system/releases/latest \
| grep browser_download_url \
| sed -re 's/.*: "([^"]+)".*/\1/' \
)"

curl -Lo latest_release.zip $latest_release

# Unzip dist folder and clean
unzip latest_release.zip "dist/*"
rm latest_release.zip
