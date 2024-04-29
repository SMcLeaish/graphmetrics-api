#!/bin/bash

curl -X POST 'http://127.0.0.1:8000/create-graph/' \
     -H 'Content-Type: application/json' \
     --data @karate.json > result.json
