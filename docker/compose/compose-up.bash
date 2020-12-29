#!/bin/bash

cd $( dirname $0 )

[ -e ~/.bash_profile ] && source ~/.bash_profile

docker-compose -p fincon-dev up