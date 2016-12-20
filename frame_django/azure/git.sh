#!/bin/bash
# linux下执行./git.sh同步到github
now=$(date '+%Y-%m-%d %H:%M:%S')
# echo $(date '+%Y-%m-%d %H:%M:%S')
git status|grep "nothing to commit"
# echo $?
if [ $? == 0 ]
then git pull origin master
elif [ $? == 1 ]
then git add --all && git commit -m "$now" && git pull origin master && git push origin master
fi
