 [![dhunter logo](img/logo.png)](https://github.com/MarcinOrlowski/dhunter)
 ---

## Usage example ##

 One example is better than thousands words, so let's assume we got two folders, say 
 `/disk1/pictures` and `/disk2/photos` we want to deduplicate.
 
 Both tools, `dscan` and `dhunt` are part of `dhunter` package. Once you have the
 package [install](install.md), you should have then in your path, available directly
 from your command line or shell.
 
### Scanning ###
 
 First step is to scan these folders. The simplest way is to use `dscan` like this:
 
    dscan /disk1/pictures /disk2/photos

 This will scan specified folders recursively and hash all the files found.

 > ![Tip](img/tip-small.png) If you are scanning non read-only medium, then it is safe to abort the process
 > at any time and restart later. It such case already hashed files will not be hashed
 > again. See [here](#read-only-folders) for closer details.
 
 Once we got folders scanned we need to create project file. Technically speaking, project
 file is a database that will contain information about all the folders we want to 
 deduplicate. Separation of project file createion from scanning lets you i.e. scan the
 whole drive (say `/disk`), but then deduplicate selected folders only (i.e. `/disk1/foo`
 and `/disk1/bar/some/other/foldr`). To create project file pass `--db FILE` argument
 to `dscan`, i.e.
 
     dscan --db my-photos /disk1/pictures /disk2/photos

 If specified no file if selected folders is hashed yet, `dscan` will do that so you can
 safely run the above command even if you never hashed specified folders before. 

 > ![Tip](img/tip-small.png) It a good idea to create your project file on **different
 > disk** that the one you are scanning (assumign you have more than one drive). This
 > makes noticeable difference if you need to scan huge number, like thousands, of files.
 > Also you want to do that if you scan files located on mechanical drive like HDD.
 > If you store project file on the same disk then the scanning process will be
 > slowed down by the updates of project file.
 
#### Filtering ####

 Experience tells that there's no point to hash all the files found, because some, (i.e.
 `.gitignore`) may have the same content intentionally and should not be considered 
 duplicates and not all files are worth scanning (i.e. it's usually safe to ignore 
 `.git` folder and its subfolders). Therefore `dscan` will apply some filters to decide
 if given file or directory should be processed or not.
 
 > ![Tip](img/tip-small.png) If you do not want given folder to be scanned, 
 > simply put empty file named `.dhunterignore` and the whole folder and its subfolders
 > will be ignored.
 
 The following criteria are applied to folders:
 
  * directory is not a symbolic link to other location
  * directory name is not blacklisted. Currently the following names are:
    * .git
    * .svn
    * .cvs
    * vendor

 The following criteria are applied to all files:
  
  * file is not a symbolic link to other file 
  * files of 0 bytes length are always ignored
  * for non-zero length files the following must be true: 
    * file size is not smaller than 2048 (use `--min` to set own value)
    * if `--max` option is given, file size must not be bigger than specified size
  * file name is not blacklisted. Currently the following names are:
    * .dhunter
    * .dhunterignore
    * .env
    * .htaccess
    * .htpasswd
    * .gitignore
 
### Hunting ###

 Duplicate hunting is handled by `dhunt` tool and all you need to hand it is project file
 and searching criteria.
 
#### Hunt by size ####

 Say you want to see top 10 of duplicates that waste most space:
 
    dhunt my-project

 which would produce output like:

     1: size: 2.9 GiB, duplicates: 2, wasted: 5.8 GiB
       1: /disk1/pictures/TWRP/BACKUPS/69aecd3f2/2018-02-03--11-10-10/image-back.dat
       2: /disk2/photos/system_image.emmc.win
       3: /disk1/BACK/USB2/other-name.ddd
       ...
       
     Summary:
       5 files have 7 duplicates, wasting together 17.6 GiB

 listing size of the "base" single file (`2.9 GiB`), number of duplicates and total size occupied by all its
 duplicates (`5.8GiB`), and then list all the files with the same content incl. its location. List is concluded
 by report summary.

#### Hunt by duplicate count ####
 
 To list top 10 of files with highest count of duplicates:
 
    dhunt --sort count my-project

 or in short form:
 
    dhunt --s c my-project

 > ![Tip](img/tip-small.png) See `dhunt --help` for all available options.

### Cache files ###

 If there's at least one file in the folder worth hashing, `dscan` will do that and store 
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
 
 If you add or remove or alter any file in already scanned folder, run `dscan` again
 and it will update dotfile and hash only new or altered files.

 > ![Tip](img/tip-small.png) To remove alal the `.dhunter` files from your disk
 > use any file search utility or, if you have this supported on your platform,
 > use `find` to get that done for you:
 > 
 > `find <PATH> -type f -name .dhunter -exec rm -f "{}" \;`
 

## Read-only folders ##

 `dscan` creates dotfile `.dhunter` in each folder it hash at least one file. This allows
 easy resume of folder scanning if it was aborted for any reason, however if you want to
 scan read-only medium (like DVD ROM) (or do not want `.dhunter` files to be created at
 all), you need to use `--read-only` flag while invoking `dscan`, i.e.:
 
    dscan --db my-photos --read-only /disk1/pictures /disk2/photos

 > ![Tip](img/tip-small.png) when using `--read-only` flag you must specify project file to be created, because
 > without that the whole scanning would produce no re-usable output thus making it completely pointless.
