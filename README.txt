INFOTOOLS

What is/are infotools you ask???

This app is a collection of custom commands that let you see file system info about some important file system objects in Splunk.

In version 1.0 there are 3 custom commands:

| lookupinfo

| bundleinfo

| userinfo

Each of these commands is a generating command (must be first command in the pipeline) and return results about the file objects.

What is the use case for infotools?

Glad you asked...

In Splunk Cloud and with many on-premise deployments most users do not have access to the file system.
It can be very useful to be able to see details about some specific Splunk files to help with troubleshooting.

For example:

One of the most common problems in many environments is large lookups file affecting bundle replication
the restapi commands for lookups do not return information about the file size if the lookup is not defined in transforms.conf, so you need access to the file system to see this information

In a search head cluster, large lookups that are frequently updated can impact performance since the entire file is replicated to all members
since lookupinfo provides the modtime, you can see if a lookup has been recently updated


lookupinfo
==========
For support, please email sjohnson@splunk.com

Version 1.0.0

usage:

| lookupinfo

lookupinfo is a custom search command that will return information about the files contained in lookups directory for all apps on the search head where it is run
lookupinfo is a generating command and must be the first command in the pipeline
lookupinfo has no arguments
lookupinfo requires python3 to run
lookupinfo returns the following results:

app - the name of the app folder
name - the name of a file in the lookup folder
size - the size in bytes of the file
mtime - the modtime of the file in epoch format

lookupinfo returns ALL files found in the lookups folder, mostly this will be .csv files but also other files such as .gz, .kmz and the occasional README


bundleinfo
==========
For support, please email sjohnson@splunk.com

Version 1.0.0

usage:

| lookupinfo

bundleinfo is a custom search command that will return information about all the files contained in the most current search bundle (.bundle) on the search head where it is run
bundleinfo is a generating command and must be the first command in the pipeline
bundleinfo has no arguments
bundleinfo requires python3 to run
bundleinfo returns the following results:

bundlename - the full path and name of the bundle file
file - the name of a file in the bundle
size - the size in bytes of the file
mtime - the modtime of the file in epoch format
 
 
userinfo
==========
For support, please email sjohnson@splunk.com

Version 1.0.0

usage:

| userinfo

userinfo is a custom search command that will return information about all the user folders and files on the search head where it is run
userinfo is a generating command and must be the first command in the pipeline
userinfo has no arguments
userinfo requires python3 to run
userinfo returns the following results:

user - the user name (foldername) from the etc/users directory
app - the name of the app folder
fileobject - the path and name of a file(s) below the app
size - the size in bytes of the file
mtime - the modtime of the file in epoch format

btoolinfo
==========
For support, please email sjohnson@splunk.com

Version 1.0.0

usage:

| btoolinfo confname=".conf file name"

btoolinfo will run a btool command with the --debug option for conf files on the search head where it is run
btoolinfo is a generating command and must be the first command in the pipeline
btoolinfo has an arguement confname= that should be the name of a valid .conf file - invalid names will return no results
userinfo requires python3 to run
userinfo returns the following results:

confpath - the full path the .conf file for the property
stanza - the name of the stanza with square brackets included
property - the name of the property
value - the value of the property
