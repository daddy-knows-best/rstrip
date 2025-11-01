[![Python package](https://github.com/daddy-knows-best/rstrip/actions/workflows/python-package.yml/badge.svg)](https://github.com/daddy-knows-best/rstrip/actions/workflows/python-package.yml)
[![Release Python Package](https://github.com/daddy-knows-best/rstrip/actions/workflows/release.yml/badge.svg)](https://github.com/daddy-knows-best/rstrip/actions/workflows/release.yml)
![](https://github.com/daddy-knows-best/rstrip/blob/main/pybadge.svg)

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
$ echo -ne "Hello World\r\n" | rstrip | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64                 |Hello World|
0000000b
$
$ cat hello_world.txt | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64 0d 0a           |Hello World..|
0000000d
$ rstrip hello_world.txt | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64                 |Hello World|
0000000b
$
```

The reason is that sed under various shell such as bash/zsh and UNIX/Linux/macOS behaves slightly differently; that makes difficult to expect the consistent rstrip behavior from the command, not to mention to remember those options and extended regular expression patterns.

I decided to write a simple `rstrip` command that I can use in command line.

```
$ rstrip --help

Usage: echo -en "Hello World\r\n" | rstrip

Arguments:
    <filename>  The name of the file to process, or None

Options:
    -h, --help  Show this help message and exit.

$
```

# Installation and How to use

```
$ uv init test_rstrip
Initialized project `test-rstrip` at `/Users/seungyeop/tests/test_rstrip`
$ cd test_rstrip
$ uv venv
Using CPython 3.14.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
$ source .venv/bin/activate
(test_rstrip) $ whereis rstrip
rstrip:
(test_rstrip) $ uv pip install -i https://test.pypi.org/simple/ rstrip
Resolved 1 package in 77ms
Installed 1 package in 5ms
 + rstrip==0.7.0
(test_rstrip) $ whereis rstrip
rstrip: /Users/seungyeop/tests/test_rstrip/.venv/bin/rstrip
(test_rstrip) $ echo -ne "Hello World\r\n" | rstrip | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64                 |Hello World|
0000000b
(test_rstrip) $
```

# History

11/01/25 v0.7.0
11/01/25 v0.6.2\
10/31/25 v0.5.0\
10/29/25~10/30/25 various pre-releases 0.2.0, 0.3.0, 0.4.0\
10/28/25 v0.1.1\
10/27/25 v0.1.0
