#!/usr/bin/env bash

pip3 install -r requirements.txt
chmod a+x mvnp
cp mvnp /usr/local/bin
mvnp --help
