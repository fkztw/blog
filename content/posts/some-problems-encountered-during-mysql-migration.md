Title: Some Problems Encountered During MySQL Migration  
Date: 2014-08-31 23:19  
Author: fkz  
Category: Note  
Tags: MySQL, Database, sysadmin  
Slug: some-problems-encountered-during-mysql-migration  
Modified: 2015-10-26 14:48  
  
  
### Some encountered errors  
  
1. `ERROR 1215 (HY000): Cannot add foreign key constraint`  
    + in mysql shell: `SET GLOBAL FOREIGN_KEY_CHECKS = 0;`  
        + in mysql => not worked  
        + add into backup.sql => not worked  
        + finally deleted the foreign key constraint line in `backup.sql`  
2. `ERROR 1367 (22007): Illegal double`  
    + `$ replace 1.79769313486232e+308 \'1.79769313486232e+308\' -- backup.sql` can solve the problem (bug).  
  
---  
  
### Backup  
  
+ On local server  
    + `mysqldump -f --all-databases --password='xxx' > /tmp/bakcup.sql`  
  
Use `scp` or other command to transfter the `backup.sql` to destination server  
  
---  
  
### Restore  
  
+ On destination server  
    + `mysql -u user -p < /tmp/backup.sql`  
  
#### Use the Force  
  
`mysql --force -u user -p < /tmp/backup.sql`  
  
---  
  
### References  
  
+ Backup / Restore  
    + <https://snipt.net/danfreak/backup-and-restore-all-mysql-databases-with-2-simple-commands/>  
+ ERROR 1215 (HY000): Cannot add foreign key constraint  
    + <http://forums.mysql.com/read.php?35,581311,581311#msg-581311>  
    + <http://stackoverflow.com/questions/16608042/error-1215-hy000-cannot-add-foreign-key-constraint>  
    + <http://stackoverflow.com/questions/18930084/mysql-error-1215-hy000-cannot-add-foreign-key-constraint>  
    + <http://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html#sysvar_foreign_key_checks>  
+ ERROR 1367 (22007): Illegal double  
    + <http://dba.stackexchange.com/questions/7885/error-on-import-of-mysqldump-file-illegal-double-value-found-during-parsing>  
    + <http://bugs.mysql.com/bug.php?id=44995>  
