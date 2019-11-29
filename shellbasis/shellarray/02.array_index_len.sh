#!/usr/bin/env bash
# ...


array=($(cat ./files.txt))

echo "array's len: ${#array[*]}"
echo "array's index: ${!array[*]}"
