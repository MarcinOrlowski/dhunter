 [![dhunter logo](img/logo.png)](https://github.com/MarcinOrlowski/dhunter)
 ---

## Changelog ##

dev
---
 * Now uses full absolute path for each item strored in project db file
 * dhunter: automatically removes dead entries from used DB if they hit the filter
 * dhunter: added `--clean-db` option to remove dead entries from project DB
 * dhunter: now yields proper warning when source dir is a symlink
 * dscan: now supports `--force` to overwrite existing database file
 * dscan: added `--relative-paths` option

v1.2.0 (2019-03-11)
-------------------
 * Added project logo
 * `dhunt` now supports size `--min` and `--max` arguments.
 * Updated documentation and usage examples 

v1.1.0 (2019-03-10)
-------------------
 * By default files smaller than 2048 bytes are ignored (use `--min` to override).
 * Updated usage documentation to cover filtering, scanning and read-only media

v1.0.0 (2019-03-09)
-------------------
 * Initial release
