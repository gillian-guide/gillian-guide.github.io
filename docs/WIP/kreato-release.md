# kreato-release file
`kreato-release` is a release file on `/etc`. It is like `os-release` in functionality.
It allows any software to see how the Kreato Linux system is configured.

# Example

```sh
KVERSION="rolling"
CODENAME="illusion"
BUILD_TYPE="custom"
COREUTILS="gnu"
LIBC="glibc"
CC="none"
TLS="openssl"
INIT="jumpstart"
```

The file will be sourced by kpkg at build-time so package scripts can use these variables.
Kreastrap will generate this file at the time the rootfs is built.