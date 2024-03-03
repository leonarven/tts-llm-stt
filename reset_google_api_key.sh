#!/bin/bash

set -e;

APIKEY="$(~/google-cloud-sdk/bin/gcloud auth print-access-token)"

ENV_FILE=".env"

LINE="$(grep GOOGLE_API_KEY $ENV_FILE)"

sed -i "s%$LINE%GOOGLE_API_KEY=\"$APIKEY\"%" $ENV_FILE
