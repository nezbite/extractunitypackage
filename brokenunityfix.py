#!/usr/bin/env python
#
# Corrupted UnityPackage Extractor
#
# Extracts files/folders from a .unitypackage file, reading the 'pathname'
# files it contains to rebuild a "readable" file/folder structure.
#
# Usage: brokenunityfix.py
#
# You need an "extracted" folder with the random folders from the unitypackage file. Extract them with WinRar.

import os
import stat
import shutil
import sys
import tarfile

#if len(sys.argv) < 2:
#	print ('No input file specified.')
#	sys.exit()

#name, extension = os.path.splitext(sys.argv[1])

outputDir = ''
#if len(sys.argv) > 2:
#	outputDir = os.path.join(sys.argv[2], name)
#else:
outputDir = './output'
workingDir = './extracted'

# can't proceed if the output dir exists already
# but if the temp working dir exists, we clean it out before extracting
#if os.path.exists(outputDir):
#	print ('Output dir "' + outputDir + '" exists. Aborting.')
#	sys.exit();
#if os.path.exists(workingDir):
#	shutil.rmtree(workingDir)

# extract .unitypackage contents to a temporary space
#tar = tarfile.open(sys.argv[1], 'r:gz')
#tar.extractall(workingDir);
#tar.close()

# build association between the unitypackage's root directory names
# (which each have 1 asset in them) to the actual filename (stored in the 'pathname' file)
mapping = {}
for i in os.listdir(workingDir):
	rootFile = os.path.join(workingDir, i)
	asset = i

	if os.path.isdir(rootFile):
		realPath = ''

		# we need to check if an 'asset' file exists (sometimes it won't be there
		# such as when the 'pathname' file is just specifying a directory)
		hasAsset = False

		for j in os.listdir(rootFile):
			# grab the real path
			if j == 'pathname':
				lines = [line.strip() for line in open(os.path.join(rootFile, j))]
				realPath = lines[0]     # should always be on the first line
			elif j == 'asset':
				hasAsset = True

		# if an 'asset' file exists in this directory, then this directory
		# contains a file that should be moved+renamed. otherwise we can
		# ignore this directory altogether...
		if hasAsset:
			mapping[asset] = realPath

# mapping from unitypackage internal filenames to real filenames is now built
# walk through them all and move the 'asset' files out and rename, building
# the directory structure listed in the real filenames we found as we go

os.makedirs(outputDir)

for asset in mapping:
	path, filename = os.path.split(mapping[asset])

	destDir = os.path.join(outputDir, path)
	destFile = os.path.join(destDir, filename)
	source = os.path.join(workingDir, asset, 'asset');

	if not os.path.exists(destDir):
		os.makedirs(destDir)
	try:
		shutil.move(source, destFile)
	except:
		with open("missingfiles.txt", "a") as myfile:
			myfile.write(destFile + "\n")
	
	# change file permissions for unix because under mac os x 
	# (perhaps also other unix systems) all files are marked as executable
	# for safety reasons os x prevent the access to the extracted files
	try:
		os.chmod(destFile, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
	except:
		print("corrupted")
	
	print (asset + ' => ' + mapping[asset])

# done, cleanup any leftovers...
# shutil.rmtree(workingDir)
