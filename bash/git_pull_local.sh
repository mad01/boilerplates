#!/bin/bash
echo "Pull git repos in currect directory"

GREEN='\033[0;32m'
LIGHTGREEN='\033[1;32m'
NC='\033[0m'
folderArray=()
DIR=$(pwd)

for FILE in $DIR/*; do
    [[ -d $FILE ]] && folderArray+=("$FILE")
    echo $FILE
done

for item in "${folderArray[@]}"
do
    echo " "
    printf  "${GREEN}pull latest of git repo: ${LIGHTGREEN}$item ${NC}"
    pushd $item
    git pull -p
    popd
    echo " "
done
