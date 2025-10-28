# rstrip

trim the spaces at the end of line that can replace the below `sed` command:

```
$ echo -en "Hello World\r\n" | gsed -z -E 's/[[:space:]]*$//' | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64                 |Hello World|
0000000b
$
```

For example,

```
$ echo -ne "Hello World\r\n" | ./rstrip | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64                 |Hello World|
0000000b
$
```

The reason is that sed/bash under various UNIX/Linux/macOS behaves slightly differently; that makes difficult to expect the consistent rstrip behavior from the command.
