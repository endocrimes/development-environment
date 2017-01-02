#!/usr/bin/env bash

CONNECTION_STRING="$1"

ssh -A "$CONNECTION_STRING"
