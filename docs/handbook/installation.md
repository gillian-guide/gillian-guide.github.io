# Installation

## Introduction 
It is assumed that you have a partition layout already setup.
It is also assumed that you are using a UEFI system.
Kreato Linux doesn't have a live ISO image. It is assumed that you would start the installation from another Linux installation. 
If you do not have a working Linux install, we recommend [Arch Linux LiveISO](https://archlinux.org/download/) for installation.

## Get rootfs tarball
First step should be to get the rootfs tarball. Kreato Linux installs through a rootfs (Like Gentoo). You can get the latest nightly through [Github Actions](https://github.com/kreatolinux/src/actions/workflows/build-rootfs.yml?query=is%3Asuccess).

### Choosing the right tarball
Kreato Linux is a modular distribution. There are four build types currently available.

* nocc-rootfs
* builder-rootfs
* builder-gnu-rootfs
* and server-rootfs.

nocc-rootfs is completely built by GitHub Actions and as the name implies, doesnt have any compilers by default. You can use binaries to install any compilers, or dont build at all and use the system with just binaries.

builder-rootfs is also built by GitHub actions and comes with gcc.

builder-gnu-rootfs is just builder-rootfs with GNU coreutils, this is for building problematic packages with Busybox such as systemd.

You dont need to touch server-rootfs, it is meant for Kreato Linux binary repository server and it comes with an web server for that purpose.

### Extracting
Mount the partition you are gonna install it to `/mnt`.
Once downloaded, extract the zip file and you will get a tarball.
Extract the tarball using the command here;
`tar --same-owner -xvf kreato-linux-*.tar.gz -C /mnt`
Once extracted, we can move on to chrooting.

## Chrooting
Before chrooting, mount your EFI partition to `/boot`.
Run these commands to chroot.

```
mount -o bind /dev /mnt/dev
mount -t proc none /mnt/proc
mount -o bind /sys /mnt/sys
mount -o bind /tmp /mnt/tmp
chroot /mnt /bin/bash
. /etc/profile
```

And you should be in! 

## Installing base system packages

### Binary vs. Source
Kreato Linux offers 2 choices for installation.
* Source based (compiling software),
* And binary based (installing from binary repository).

Both choices have their own advantages.

#### Advantages and disadvantages of building packages
* Updates come faster.
* Has more customizability and optimization options.
* Building is slower than downloading a binary tarball.

#### Advantages and disadvantages of binary packages
* Updates are available with a lag.
* Has less customizability.
* Doesn't require building packages, making it more suitable to older/less powerful systems.
* Is not currently stable, packages may not even exist on the mirror.

This installation guide will assume that you are gonna install binary packages (`kpkg install packagename`). If you want to build packages, please change `kpkg install` to `kpkg build` so it builds the packages instead of installing the binary.

Now we can continue with installing base system packages.

### Installing the init system
Kreato Linux includes multiple init systems. OpenRC, busybox init and jumpstart exist as a option. Jumpstart is the default and recommended option. 

* If you want busybox init, you can install `base-runit`: `kpkg install base-runit`
* If you want OpenRC: you can install `openrc`: `kpkg install openrc`
* If you want Jumpstart, it is installed by default

### Installing networking tools
`dhcpcd` is recommended. run `kpkg install dhcpcd` to install `dhcpcd`.
you should install `wpa_supplicant` aswell if you need Wi-Fi connectivity. run `kpkg install wpa_supplicant` to install it.

<!---
### Building the kernel
You can either build your own kernel or use Kreato Linux's kernel, that uses Arch Linux's kernel configuration.
It is recommended to build your own kernel, since it will be much more minimal and will compile faster.
You can run `kpkg install linux-arch` to install the prebuilt kernel.
As for building your own kernel, you can check out [This video](https://www.youtube.com/watch?v=NVWVHiLx1sU).
-->

### Installing the bootloader
Kreato Linux offers multiple bootloaders.
You can use Limine or Grub.

This guide will show Limine since it is the most tested option.
You can install Limine by running `kpkg install limine`.
Configuration is already explained greatly on [Arch Wiki](https://wiki.archlinux.org/title/Limine), so i wont repeat it here.

## Change the root password
You should change the root password by running this command;
`passwd root`
If you want to do so, you can also add additional users with `useradd`.

Now you should be able to boot Kreato Linux by itself.

## Setting up the locale
You can set up the locale by running these commands. Change `LOCALE=en_US` with your language (Example; `LOCALE=de_DE` for German)

```
LOCALE=en_US
mkdir -p /usr/lib/locale
localedef -i $LOCALE -c -f UTF-8 $LOCALE
echo "export LANG=$LOCALE" >> /etc/profile
```

## Installing a Window Manager
Kreato Linux only offers `sway` for now and will only support Wayland for now.
You can install sway by running `kpkg install sway`.
More Wayland window managers are coming soon.
You can also install foot, a terminal by running `kpkg install foot`

# What's Next
You can tinker with your setup, install additional software, package something, etc.

If you want to contribute to Kreato Linux, you can look at the [Contribution Guide](./contributing/index.md).
