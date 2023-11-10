#!/bin/bash

while getopts f:m: option;
do
    # shellcheck disable=SC2220
    case ${option} in
        f) file_path=${OPTARG};;
        m) message=${OPTARG};;
    esac
done

if [ ! "$file_path" ]; then
        echo 'File path(-f) flag cannot be empty' >&2
        exit 1
fi
if [ ! "$message" ]; then
  echo 'Message(-m) flag cannot be empty' >&2
  exit 1
fi

#add the given file path
git add "$file_path"
#commit to git with the given message
git commit -m "$message"
#push the changes to git
git push
