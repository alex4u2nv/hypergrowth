#!/bin/sh
if [ ! $1 ]; then
	echo "Missing version number"
	grep current < .bumpversion.cfg
	exit 1
fi
#if ! bump2version --new-version "$1"  minor --verbose; then
#  exit 1
#fi
if ! (cd framework/hypergrowth; tox); then
  exit 1
fi
if ! twine check framework/hypergrowth/.tox/dist/*; then
  exit 1
fi
if ! twine upload framework/hypergrowth/.tox/dist/* -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}"; then
  exit 1
fi
git push origin main
git push origin --tags