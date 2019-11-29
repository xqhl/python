#!/usr/bin/env bash


array=($(cat files.txt))
echo "array's all element: ${array[*]}"

echo "delete index: 3"
unset array[3]
echo "array's all element: ${array[*]}"

echo "delete all element"
unset array
echo "array's all element: ${array[*]}"

