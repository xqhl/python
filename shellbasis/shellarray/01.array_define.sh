#!/usr/bin/env bash
#
# filepath: cloud1908/shellbasis/shellarray/01.array_define.sh
# usage: define array
# create_date: 2019/11/25
# @modify_time: @time


# array define
array01=("helloworld" "hellokitty" 13 3.14 true)
file01=($(cat files.txt))

# array rever
echo ${array01[@]} # ${array01[*]}
echo ${file01[*]}


# index -> define
array02=([0]="helloworld" [2]="56")
echo "array02's element: ${array02[*]}"
echo "array02[0] = ${array02[0]}"
echo "array02[1] = ${array02[1]}"
echo "array02[2] = ${array02[2]}"

array03[0]="12"
array03[2]="34"
array03[3]="56"
array03[4]="78"
echo "array03's element: ${array03[*]}"
echo "array03[0]=${array03[0]}"
echo "array03[1]=${array03[1]}"
echo "array03[2]=${array03[2]}"
echo "array03[3]=${array03[3]}"
echo "array03[4]=${array03[4]}"

# declare -s arrayName=(elements)
declare -s array04
array04[0]="hello"












