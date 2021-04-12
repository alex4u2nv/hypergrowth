#!/usr/bin/env sh
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html
if ! tox &> /dev/null; then
  echo "Please install tox: https://tox.readthedocs.io/en/latest/install.html"
fi
if ! jq &> /dev/null; then
  echo "Please install jq: https://stedolan.github.io/jq/download/"
fi
if ! sam &> /dev/null; then
  echo "Please install sam: https://aws.amazon.com/serverless/sam/"
fi

if ! docker &> /dev/null; then
  echo "Please install Docker: https://docs.docker.com/get-docker/"
fi
tox
sam build
sam local invoke -e events/event.json