#!/bin/bash

set -e

docker-compose up -d || docker compose up -d
sleep 5

echo  "copy pwn file and libc "

imageid=$(docker ps -n 1 -q)
mkdir ./challenge/glibc -p
cd ./challenge
docker cp ${imageid}:/home/ctf/pwn .
docker cp ${imageid}:/home/ctf/glibc .
echo "copy success!"
