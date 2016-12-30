###备份数据库
shell> MYSQLDUMP -h host -u root -p db_name > dbname_backup.sql

如果不希望后来手工创建staffer,可以
shell> mysqldump -uroot -proot --databases db_name>dbname_backup.sql

如果只想卸出建表指令：
shell> MYSQLADMIN -u root -p -d db_name > dbname_backup.sql

如果只想卸出插入数据的sql命令，而不需要建表命令：
shell> MYSQLADMIN -u root -p -t db_name > dbname_backup.sql

如果只想要数据，而不要sql命令：
shell> MYSQLADMIN -T./filename 表名
【指定-T参数，卸出纯文本文件。./表示当前目录，即与mysqldump同一目录。如果不指定表，则将卸出整个数据库的数据。每个表会生成两个文件，一个为.sql文件，包含建表执行。另一个为.txt文件，只包含数据，且没有sql指令。】

###恢复数据库
shell> MYSQLADMIN -h myhost -u root -p CREATE dbname
shell> MYSQLDUMP -h host -u root -p dbname < dbname_backup.sql

###从文本向数据库导入数据
1）mysqlimport，这个工具的作用是将文件导入到和去掉文件扩展名名字相同的表里。
常用选项及功能如下
-d or --delete........新数据导入数据表中之前删除数据表中的所有信息
-f or --force.........不管是否遇到错误，强制继续插入数据
-i or --ignore........跳过或者忽略那些有相同唯一关键字的行，导入文件中的数据将被忽略。
-l or -lock-tables....数据被插入之前锁住表，这样就防止了你在更新数据库时，用户的查询和更新受到影响。
-r or -replace........这个选项与－i选项的作用相反；此选项将替代表中有相同唯一关键字的记录。
-v....................显示版本（version）。
-p....................提示输入密码（password）等。
--fields-enclosed- by= char，指定文本文件中数据的记录是以什么括起的，很多情况下数据以双引号括起。 默认的情况下数据是没有被字符括起的。
--fields-terminated- by=char，指定各个数据的值之间的分隔符，在句号分隔的文件中，分隔符是句号。您可以用此选项指定数据之间的分隔符。默认的分隔符是跳格符（Tab）
--lines-terminated- by=str，此选项指定文本文件中行与行之间数据的分隔字符串或者字符。默认的情况下mysqlimport以newline为行分隔符。您可以选择用一个字符串来替代一个单个的字符：一个新行或者一个回车。

2）Load Data INFILE file_name into tb_name(column1,column2,...);
这个命令在mysql>提示符下使用，优点是可以指定列导入。

###SQL脚本，将查询存储在一个文件中并告诉mysql从文件中读取查询而不是等待键盘输入。可利用外壳程序键入重定向实用程序来完成这项工作。例如，如果在文件my_file.sql 中存放有查
询，可如下执行这些查询：
例如，如果您想将建表语句提前写在sql.txt中:
mysql > mysql -h myhost -u root -p database < sql.txt

1、书写脚本的时候，多用空格、Tab键，不要让代码拥挤，杂糅在一起。
2、统一关键字大小写，不要一部分大写、一部分小写。
3、书写出来的脚本至少要结构清晰，一目了然。


source fileName.txt;建立数据库
通过source命令导入多个文件，可以新建一个sou.sql文件，里面存放下面的命令
例如：
source d:/a1.sql;
source d:/a2.sql;
当你运行source命令，就可以在一个source命令里面导入多个sql文件了。


1．  内联结：将两个表中存在联结关系的字段符合联结关系的那些记录形成记录集的联结。
2．  外联结：分为外左联结和外右联结。
默认的JOIN都是INNER JOIN