#!/bin/bash

while true; do
	HEAD=`git ls-remote -q | grep -e "HEAD$" | awk '{ print $1 }'`
	#echo "Server: $HEAD"
	CURR=`git show-ref | grep -e "HEAD$" | awk '{ print $1 }'`
	#echo "Local:  $CURR"
		
	if [ $HEAD != $CURR ]; then
		# restore the old versions first, so git pull will be clean
		git checkout -- DemonMUSH/update_everything.lst
		git checkout -- DemonMUSH/update_everything.lst.gz
		git checkout -- DemonMUSH/update_manifest.lst
		git checkout -- innosetup/master.lst

		# now it should be safe to pull
		git pull

		# finally, rebuild the manifests for release

		# this is for the new stable/beta/lite updaters
		./rebuild_sha256_updater_files.sh
	fi
	
	sleep 60
done

