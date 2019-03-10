Preface
=======
 To use `dhunter` you need to scan folders of your interest first. You can scan all at once,
 or scan them "in portions" - it does not make much difference as during the whole scanning
 and hashing process all the information about each directory is stored separately. When you
 try to scan folders again, `dhunter` will first try to reuse cached data (updating them if
 changed) which should speed the whole process up a lot.

Usage example
=============
 Let's assume we got two folders, `/disk1/pictures` and `/disk2/photos` and we would like
 scan and then deduplicate.
 
 First step is to scan these folders. The simplest way is to use `dscan` like this:
 
    dscan /disk1/pictures /disk2/photos

 This will scan specified folders recursively hash all the files found.
 
 While the above will work just fine, it's far better to create project file during scanning.
 Project file is simply a database that holds all the information about scanned folders and
 using project file speeds deduplication dramatically. While it is technically correct to just
 scann the folders, it's far better (and faster) to scan **AND** create database at the 
 same time:
 
    dscan -db database /disk1/pictures /disk2/photos

 Once `dscan` is done, you will have `database` file that can be consumed by `dhunt` tool 
 and used to find files matching your criterias. Let's list first 10 files what are the
 biggest (in size) storage consuming duplicates:
 
    dhunt --limit 10 --sort size --reverse
 
 or in short notation:
 
    dhint -l 10 -s s -r
 
 
Cache files
===========
 If there's at least one file in the folder worth hashing, Deduper will do that and store 
 the result hash in cache file named `.dhunter`. Next time the same folder is scanned, it
 will look for cache file, load it if exists and then check if file changed since last
 hashing and either reuse already computed hash, or hash the file again. To detect if file
 changed or not, file creation time, modify time, inode number and filename is taken into
 consideration.
 
 It's safe to remove `.dhunter` files if needed, yet all the files will need to be rehashed
 if these folders are scanned again.
 
 If you move folder to different location, move corresponding `.dhunter` file as well.
 On next run, dhunter will try to reuse cached data and only hash files that are new or
 changed since list scan.
 
Control files
============

 dhunter looks for `.dhunter_ignore` file in each folder. If file exists then the whole
