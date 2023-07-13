# JumpStart internal documentation

## Communication
Communication happens through UNIX sockets. `/run/jumpstart.lock` is the default socket path.

## Interacting with services

The client sends these information onto the socket.

```json
{
    "client": {
        "name": "Jumpstart CLI",
        "version": "0.0.1-alpha"
    },
    
    "service": {
        "name": "test.service",
        "action": "enable",
        "now": "false"
    }    
}
```


Change the action to whatever you want.

If it is supported within Jumpstart, you should see an reply. Unsupported operations are ignored.

## Checking the status of services
Service status is sent through `/run/serviceHandler/serviceName.service/status`.

## serviceHandler
serviceHandler is the service handler of JumpStart. It manages services.

## Services
Services are parsed using std/parsecfg, which is like ini.

Services are stored in `/etc/jumpstart/services` by default and have the `.service` extension.

```ini
[Info]
Desc="This is a test service."
Type="service" # Specify type, 'service' is for services, 'mount' is for mounting

[Service]
execPre="echo 'This will be ran before Exec'"
exec="echo 'this is a test'"
execPost="echo 'This will be ran after the initial command'"
```

Enabled services are stored in `/etc/jumpstart/services/enabled`.

## Mounts
Mounts are also parsed using std/parsecfg, which is like ini.
They are stored in `/etc/jumpstart/mounts` and have the `.mount` extension.

```ini
[Info]
Desc="This is an test mount."
Type="mount"

[Mount]
From="/dev/nvme0n1p1"
To="/mnt"
Type="ext4"
Timeout="5s"
lazyUmount="true"
Chmod="755"
extraArgs="--bind"
```


## Jumpstart configuration
Jumpstart has a config file in `/etc/jumpstart/main.conf`. It has an ini-like format.

```ini
[Startup]
emergencyShell="yes"
debugLogs="yes"

[System]
hostname="klinux"
```


## Using another service manager
Jumpstart is designed to be modular, and allows using other service managers.

Using other service managers means Jumpstart will just be an middleman between the service manager (eg. runit ) and the user.

This way no backwards compatibility is lost, and user choice is retained.

This is coming soon.

# Jumpstart FAQ

## Why?
Because i need a simple and stable init system/service manager for Kreato Linux.

## How is this better than other init system/service managers like systemd, runit, openrc etc.
It isnt and it doesnt try to be. Jumpstart is meant for use with Kreato Linux and is designed for that purpose.

