#!/bin/bash

# pre-install
oc create route edge --service=deployment --insecure-policy=Redirect

# install postgresql
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm upgrade --install postgresql bitnami/postgresql --version 15.2.7 --values ./charts/postgresql/override-values.yaml

# install deployment
helm upgrade --install deployment ./charts/deployment --values ./charts/deployment/values.yaml

# post-install
echo "Access deployment URL: $(oc get route deployment -o jso
n | jq -r '.spec.host')"