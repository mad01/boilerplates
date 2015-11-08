#!/bin/bash
GREEN='\033[0;32m'
LIGHTGREEN='\033[1;32m'
NC='\033[0m'
folderArray=()
DIR=$(pwd)

printf "${GREEN}Pull git repos in currect directory ${NC}"

for FILE in $DIR/*; do
    [[ -d $FILE ]] && folderArray+=("$FILE")
    echo $FILE
done

for folder in "${folderArray[@]}"
do
    printf "\n"
    printf "${GREEN}pull latest of git repo: ${LIGHTGREEN} $folder${NC}"
    pushd $folder
    git pull -p
    popd
    printf "\n"
done
