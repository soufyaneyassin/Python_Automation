#!/usr/bin/env bash

LOG_FILE=${HOME}/test_paramiko.log # we chose the absolute path because the script is moving between folder ;) 

echo "$(date +"%Y-%m-%d %H:%M:%S" ) Testing Paramiko from python.." > $LOG_FILE
echo "Current Folder you're at right now is $(pwd) " >> $LOG_FILE

if [[ $(pwd) == $HOME ]]; then
    cd ${HOME}/Downloads
    echo "Changed Dir to $(pwd)" >> $LOG_FILE
else
    cd $HOME
    echo "you're now switched back to the home dir $(pwd)" >> $LOG_FILE
fi
