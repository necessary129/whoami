#!/bin/bash

set -eu
url=$(cat identities/url)

curl -X POST "https://web.archive.org/save/$url" --data-urlencode "url=$url" --data-urlencode "capture_all=off"