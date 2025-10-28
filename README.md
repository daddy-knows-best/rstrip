[![Python package](https://github.com/daddy-knows-best/rstrip/actions/workflows/python-package.yml/badge.svg)](https://github.com/daddy-knows-best/rstrip/actions/workflows/python-package.yml)
![](https://github.com/daddy-knows-best/rstrip/blob/main/pybadge.svg)<img src="./pybadge.svg">

# rstrip

trim the trailing spaces at the end of line that can replace the below `sed` command:

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

The reason is that sed under various shell such as bash/zsh and UNIX/Linux/macOS behaves slightly differently; that makes difficult to expect the consistent rstrip behavior from the command, not to mention to remember those options and extended regular expression patterns.

I decided to write a simple `rstrip` command that I can use in command line.

```
$ ./rstrip --help

Usage: echo -en "Hello World\r\n" | rstrip

Arguments:
    <filename>  The name of the file to process, or None

Options:
    -h, --help  Show this help message and exit.

$
```

# History

10/27/25 v0.1.0
