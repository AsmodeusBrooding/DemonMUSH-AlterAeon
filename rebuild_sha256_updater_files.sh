#!/bin/bash

if [ ! -d .git ]; then
	echo "Please run this from the root .git tree for the demonmush release code."
	exit
fi
if [ ! -d DemonMUSH ]; then
	echo "Can't find 'DemonMUSH' directory."
	echo "Please run this from the root .git tree for the demonmush release code."
	exit
fi

# Note that gnu sort is BROKEN when it comes to consistent sort order on different machines.
# This is a shitty hack to force gnu sort to sort the same way every time.
export LC_ALL=C

cd DemonMUSH

echo "Computing checksums into temp file 'master.lst'."
echo "This may take several minutes."

# note that this updater can update the old updater, and fails gracefully if it
# can't update itself.  (ok, mostly gracefully)
find . -type f | grep -v -i \
 -e "worlds.Demonclient.MCL" \
 -e "swp$" \
 -e "worlds.plugins.state" \
 -e "update_.*lst" \
 -e "db_backups" \
 -e "Demonclient.db" \
 -e "mushclient_prefs.sqlite" \
 -e "crap$"\
 | sort -f | cut -b 3- | while read LINE ; do
	SHA=`cat "$LINE" | sha256sum | cut -b -20`
	SIZE=`ls -l "$LINE" | awk '{ print $5 }'`
	printf "%s %10d %s\n" $SHA $SIZE "$LINE"
done > ../master.lst

grep -v " update.exe$" ../master.lst > update_everything.lst

# this is a 'fake' manifest which is only downloaded by the old downloader
# before people start using the new downloader.  It prevents them from
# having to download all ten thousand files to fill out the manifest.
cp update_everything.lst update_manifest.lst
# warning we'll need to use this instead when doing the install/zip files
#cp ../master.lst update_manifest.lst

gzip -nc update_everything.lst > update_everything.lst.gz

echo "Output written to file 'update_everything.lst'."
echo "Run 'git diff' to see changes."

rm crap
cd ..

# this file can be used by the installer build scripts
mv master.lst innosetup

