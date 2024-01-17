#!/bin/bash

set -e

if [ ! -z $FLAG ]
then
    if [ "$(cat /home/ctf/flag)" != "$FLAG" ]
    then
        echo $FLAG > /home/ctf/flag
        chmod 644 /home/ctf/flag
    fi
fi

unset FLAG

cd /home/ctf

exec timeout 300 $(which chroot) --userspec=1000:1000 /home/ctf ./pwn
