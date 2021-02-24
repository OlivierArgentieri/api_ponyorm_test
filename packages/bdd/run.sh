#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
BASEDIR="${BASEDIR//\\//}"  # backslash to forward slash
echo $BASEDIR"/src/bdd.py"
rez-env bdd -- bdd

$SHELL