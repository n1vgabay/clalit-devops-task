# Clalit DevOps Task

[![Release Version](https://img.shields.io/github/v/release/username/repo.svg)](https://github.com/username/repo/releases/latest)
[![Build Status](https://img.shields.io/travis/username/repo/master.svg)](https://travis-ci.org/username/repo)
[![Coverage Status](https://img.shields.io/coveralls/github/username/repo/master.svg)](https://coveralls.io/github/username/repo)

This project will set up a Flask web application with a single deployment. The main page will display "Welcome Clalit!" and it will use PostgreSQL as the database.

## Prerequisites

Before installing this project, ensure you have the following tools installed:

- [oc CLI](https://docs.openshift.com/container-platform/4.11/cli_reference/openshift_cli/getting-started-cli.html)
- [kubectl CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [helm CLI](https://helm.sh/docs/intro/install/)

## Usage
Use the ```deploy.sh``` to deploy the project.

In order to get the URL endpoint for the deployment, run the command above:
```
oc get route deployment -o json | jq -r '.spec.host'
```

- Insert random data, access to: ```https://<URL>/insert```
- Read the data from the database, access to: ```https://<URL>/read```

Updating deployment index:
First option is updating the configmap itself on-the-go aka ```kubectl edit configmap deployment-configmap```.

Second option is updating changes in the ```charts/deployment/templates/configmap.yaml``` template. After changes, apply helm upgrade using ```helm upgrade --install deployment ./charts/deployment --values ./charts/deployment/values.yaml```.

After updating the configmap, run this command to apply changes ```kubectl rollout restart deployment deployment```.

Enjoy!