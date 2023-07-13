# How to build an rootfs
This tutorial will teach you how to build an rootfs.

# Dependencies
* Docker/podman and docker/podman-compose
* Nim with Nimble
* Make (preferably GNU make, others are untested)
* Git

# Steps

## Downloading the source tree
You can clone the source code with `git clone https://github.com/kreatolinux/src`.
If you want, you can also use an stable release off GitHub Releases.

## Use kreastrap
To run kreastrap, you just do `docker compose up builder`. Change `docker compose` with `podman-compose` if you are using podman-compose.

Once finished, your rootfs will be available at `./out`. It builds builder-rootfs by default [(See what build types are)](../installation.md#choosing-the-right-tarball)
