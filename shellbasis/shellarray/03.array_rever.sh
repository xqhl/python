#!/usr/bin/env bash


array=($(cat files.txt))

# 遍历数组
for lines in ${array[*]};do
  echo ${lines}
done

echo "*******************************************"

for index in ${!array[*]};do
  echo "index ${index}: ${array[${index}]}"
done
