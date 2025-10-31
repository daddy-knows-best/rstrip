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
macbookair:tests seungyeop$ uv init test_rstrip
Initialized project `test-rstrip` at `/Users/seungyeop/tests/test_rstrip`
macbookair:tests seungyeop$ cd test_rstrip
macbookair:test_rstrip seungyeop$ wget rstrip-0.5.0-py3-none-any.whl
--2025-10-31 10:28:59--  http://rstrip-0.5.0-py3-none-any.whl/
Resolving rstrip-0.5.0-py3-none-any.whl (rstrip-0.5.0-py3-none-any.whl)... failed: nodename nor servname provided, or not known.
wget: unable to resolve host address ‘rstrip-0.5.0-py3-none-any.whl’
macbookair:test_rstrip seungyeop$ wget https://github.com/daddy-knows-best/rstrip/releases/download/v0.5.0/rstrip-0.5.0-py3-none-any.whl
--2025-10-31 10:30:06--  https://github.com/daddy-knows-best/rstrip/releases/download/v0.5.0/rstrip-0.5.0-py3-none-any.whl
Resolving github.com (github.com)... 140.82.114.3
Connecting to github.com (github.com)|140.82.114.3|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://release-assets.githubusercontent.com/github-production-release-asset/1084615457/f2547e42-2136-49e2-844c-620182a35e3b?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-10-31T16%3A19%3A48Z&rscd=attachment%3B+filename%3Drstrip-0.5.0-py3-none-any.whl&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-10-31T15%3A19%3A05Z&ske=2025-10-31T16%3A19%3A48Z&sks=b&skv=2018-11-09&sig=fMKewEx%2BcF1r1Gno24oEe1wMZ9HZtx%2BNsukf0ecd4%2Fo%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2MTkyNDkwNiwibmJmIjoxNzYxOTI0NjA2LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.FU2p7kAlwzFyjC3b3VwSSL8FcBSxbpu9pv-28Y0pv1Y&response-content-disposition=attachment%3B%20filename%3Drstrip-0.5.0-py3-none-any.whl&response-content-type=application%2Foctet-stream [following]
--2025-10-31 10:30:06--  https://release-assets.githubusercontent.com/github-production-release-asset/1084615457/f2547e42-2136-49e2-844c-620182a35e3b?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-10-31T16%3A19%3A48Z&rscd=attachment%3B+filename%3Drstrip-0.5.0-py3-none-any.whl&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-10-31T15%3A19%3A05Z&ske=2025-10-31T16%3A19%3A48Z&sks=b&skv=2018-11-09&sig=fMKewEx%2BcF1r1Gno24oEe1wMZ9HZtx%2BNsukf0ecd4%2Fo%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2MTkyNDkwNiwibmJmIjoxNzYxOTI0NjA2LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.FU2p7kAlwzFyjC3b3VwSSL8FcBSxbpu9pv-28Y0pv1Y&response-content-disposition=attachment%3B%20filename%3Drstrip-0.5.0-py3-none-any.whl&response-content-type=application%2Foctet-stream
Resolving release-assets.githubusercontent.com (release-assets.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.109.133, ...
Connecting to release-assets.githubusercontent.com (release-assets.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3365 (3.3K) [application/octet-stream]
Saving to: ‘rstrip-0.5.0-py3-none-any.whl’

rstrip-0.5.0-py3-none-any.whl                      100%[==============================================================================================================>]   3.29K  --.-KB/s    in 0s

2025-10-31 10:30:06 (9.75 MB/s) - ‘rstrip-0.5.0-py3-none-any.whl’ saved [3365/3365]

macbookair:test_rstrip seungyeop$ ls
main.py				pyproject.toml			README.md			rstrip-0.5.0-py3-none-any.whl
macbookair:test_rstrip seungyeop$ uv venv
Using CPython 3.14.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
macbookair:test_rstrip seungyeop$ source .venv/bin/activate
(test_rstrip) macbookair:test_rstrip seungyeop$ whereis rstrip
rstrip:
(test_rstrip) macbookair:test_rstrip seungyeop$ uv pip install ./rstrip-0.5.0-py3-none-any.whl
Resolved 1 package in 7ms
Prepared 1 package in 3ms
Installed 1 package in 3ms
 + rstrip==0.5.0 (from file:///Users/seungyeop/tests/test_rstrip/rstrip-0.5.0-py3-none-any.whl)
(test_rstrip) macbookair:test_rstrip seungyeop$ whereis rstrip
rstrip: /Users/seungyeop/tests/test_rstrip/.venv/bin/rstrip
(test_rstrip) macbookair:test_rstrip seungyeop$ echo -ne "Hello World\r\n" | rstrip | hexdump -C
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64                 |Hello World|
0000000b
(test_rstrip) macbookair:test_rstrip seungyeop$
```

# History

10/31/25 v0.5.0\
10/29/25~10/30/25 various pre-releases 0.2.0, 0.3.0, 0.4.0\
10/28/25 v0.1.1\
10/27/25 v0.1.0
