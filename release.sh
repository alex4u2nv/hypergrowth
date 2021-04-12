#!/bin/sh
if [ ! $1 ]; then
	echo "Missing version number"
	grep current < .bumpversion.cfg
	exit 1
fi
bump2version --new-version "$1"  minor --verbose
tox
twine check .tox/dist/*
twine upload .tox/dist/* -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}"
git push origin main
git push origin --tags