#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

echo $BASEDIR"/alchemy/alchemy.py"
rez-env bdd -- $BASEDIR"/alchemy/alchemy.py"

$SHELL