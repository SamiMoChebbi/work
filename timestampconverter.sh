#!/bin/bash

if (($#)); then
    printf '%(%c)T\n' "$@"
else
    while read -r line; do
        printf '%(%c)T\n' "$line"
    done
fi
