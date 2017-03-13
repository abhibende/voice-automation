#!/bin/bash
SSH_ARGS='-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q -tt'
val=0
cmd=`echo $1 |  tr '[A-Z]' '[a-z]'`
branch() {
docr=`echo $cmd | awk '{print $NF}'`
case $docr in
*labs*) doc="labs";;
*staging*|*stadium*) doc="staging";;
*md*) doc="mdrn";;
*) echo "Error in reading port";exit 1;;
esac
if [[ $cmd =~ .*branch.* ]]
        then
        branch=`echo $cmd | grep -o "branch.*" | awk '{print $(NF-1)}'`
        else
        branch="null"
        fi
}
case $cmd in
*update*|*object*) val="1";;
hostname|"host name") echo `hostname` ;exit 0 ;;
*) val="0";;
esac

case $cmd in

*website*) mod=1;;
*labs*|*laps*|*lamp*)mod=2;branch "$cmd";;
*vendor*|*35*)mod=3;;
*) mod=0;;
esac

result=`echo "$mod * $val" | bc`

case $result in

1) cd svn && svn up ;;
2) sudo ssh $SSH_ARGS web_backup@192.168.12.31 "echo -e \"$branch\n$doc\" > branch;curl -s http://172.29.0.123/download/abhinav/testlabs | sudo bash -s" ;;
3) sudo ssh $SSH_ARGS web_backup@192.168.17.101 "curl -s http://172.29.0.123/download/abhinav/vendor | sudo bash -s" && sudo ssh $SSH_ARGS web_backup@192.168.17.102 "curl -s http://172.29.0.123/download/abhinav/vendor | sudo bash -s" ;;
*) echo "yet to configure" ;;

esac
