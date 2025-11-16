#!/bin/bash
youngest_age=-1
oldest_age=-1
yongest_data=""
oldest_data=""

for i in $(ls $1)
do
  for file in $(cat $1$i)
  do
   age=$(echo $file | grep -o "[0-9]*" | head -2 |tail -1)

   if [ $youngest_age -eq -1 ]
   then
     yongest_age="$age"
     oldest_age="$age"
     youngest_data="$file"
     oldest_data="$file"
    else
      if [ $age -lt $youngest_age ]
       yongest_age="$age"
       youngest_data="$file"
      fi

      if [ $age -lt $oldest_age ]
      then
         oldest_age="$age"
         oldest_data="$file"
      fi
    fi
  done
done

echo "$youngest_data"
echo "$oldest_data"
