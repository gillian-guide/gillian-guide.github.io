# Source tree Internals
Welcome! In this page you will find information as how kpkg works.

# What is kpkg?
kpkg is the rewrite of the package manager called [nyaa2](https://github.com/kreatolinux/nyaa2) in Nim. It was originally called nyaa3. This has been done for many reasons, which i won't repeat here. Nyaa2 has more features in some areas, but is now **unsupported** and shouldn't be used.

# Layout of the source tree
The layout of the project is really simple to understand.

* `Makefile` allows you to install dependencies and build the project.
* `docker-compose.yml` is there for testing.
* `man` directory has the pandoc-generated manpages, which have their source files in `src/man`.
* `nix` directory contains nix build support. Please keep in mind that NixOS is a completely seperate project, we just have it as a build tool option.

# The src directory
`src` directory has many projects, including (currently) purr for testing, kreastrap for building packages and rootfs automatically, kpkg for package management, chkupd for version checking and mari for the binary repository.

## kreastrap
`src/kreastrap` has the source code of kreastrap. Kreastrap v3 is the newest rewite the Kreato Linux build tool. It is rewritten in Nim, so it can utilize kpkg's internal functions and have better error handling than nyaastrap v2. It allows you to build packages, and an rootfs. More features may come soon.

You can learn how to build an rootfs [through here](./how-to-rootfs.md).

## purr
`src/purr` has the source code of purr. Purr is an test utility, checking if things are still working the way they should.

Please note that both of these projects should be ran on an Docker container, which is why `docker-compose.yml` exists. **DO NOT** run these tests in your host machine, as it will probably break your host system and/or not work at all.

## chkupd
`src/chkupd` has the source code for chkupd v3, a Nim rewrite of chkupd v2. It allows to maintain repositories easier by checking versions off Repology API and updating accordingly.

## mari
`src/mari` has the source code for mari, a extremely simple HTTP server that uses the awesome httpbeast library. It is only for Kreato Linux binary repository.

## kpkg
The biggest project in the source tree which includes an easy-to-use library to use for other projects. It resides mostly in `src/kpkg` and is neatly seperated onto seperate files.
`src/kpkg/modules` includes more internal functions such as the downloader, the config system, etc.
