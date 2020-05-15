#!/bin/sh

set -e

readonly config_file=/app/configs/${ENVIRONMENT}.env

export $(cat "$config_file")

exec nubosas-aiotemplate
