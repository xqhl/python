#!/usr/bin/env bash


files=($(cat files.txt))
array=("Python" "Shell" "PHP" "Java" "C++" "Go" "C#")

arraylink=(${files[*]} ${array[*]})
echo "arratlink's all element: ${arraylink[*]}"
