#!/usr/bin/env bash

pip3 install -r requirements.txt
cp mvnp.py mvnp
chmod a+x mvnp
mv mvnp /usr/local/bin
mvnp --help
