#!/bin/sh

set -e

# Wait for mongo express to be ready
/app/wait_for_mongo_express.sh

nginx -g "daemon off;"