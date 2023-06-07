#!/bin/sh

# Wait for MySQL to be ready
until nc -z -v -w120 micro-mexpress 8081
do
  echo 'Waiting for Mongo Express...'
  sleep 5
done

echo "Mongo Express is ready then run nginx!"
