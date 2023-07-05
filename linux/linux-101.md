# Linux 101

## Key Concepts

### What is Linux?

Linux is a family of open-source operating systems based on the Linux kernel, an operating system kernel based on the Unix kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

### What is a Linux distribution?

A Linux distribution (often abbreviated as distro) is an operating system made from a software collection that is based upon the Linux kernel and, often, a package management system. Linux users usually obtain their operating system by downloading one of the Linux distributions, which are available for a wide variety of systems ranging from embedded devices (for example, OpenWrt) and personal computers (for example, Linux Mint) to powerful supercomputers (for example, Rocks Cluster Distribution).

A typical Linux distribution comprises a Linux kernel, GNU tools and libraries, additional software, documentation, a window system (the most common being the X Window System), a window manager, and a desktop environment. Most of the included software is free and open-source software made available both as compiled binaries and in source code form, allowing modifications to the original software. Usually, Linux distributions optionally include some proprietary software that may not be available in source code form, such as binary blobs required for some device drivers.

### What is a package manager?

A package manager or package-management system is a collection of software tools that automates the process of installing, upgrading, configuring, and removing computer programs for a computer's operating system in a consistent manner.

### What is a shell?

A shell is a computer program which exposes an operating system's services to a human user or other program. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation. It is named a shell because it is the outermost layer around the operating system kernel.

## What is file system?

A file system is a method and data structure that an operating system uses to organize and keep track of files. The file system is responsible for managing files and directories, and it defines the syntax that you use to access and manipulate them.

File systems can vary between operating systems. Common file systems include FAT, NTFS, ext4, and HFS+. Linux supports a wide variety of file systems, including many that are not native to Linux. For example, Linux can read and write to FAT and NTFS file systems, but Windows cannot read and write to ext4 file systems.

Ubuntu uses the ext4 file system by default which cannot be read by Windows. If you want to share files between Ubuntu and Windows, you should use a separate partition (on your hard drive or in a portable drive) formatted as FAT or exFAT that can be read and written to by both operating systems.

## Linux Directory Structure

The Linux file system hierarchy is the directory structure used in Linux or other Unix-like operating systems. It resembles a tree with the root directory (/) at the top and all other directories as subdirectories of root.

Here are some examples of directory paths in Linux:

```bash
/

/home/username

/home/username/Downloads

/usr

/usr/bin

/usr/local/lib

/var/log

```

### Linux File System Hierarchy

- `/` - The root directory. Everything on the system is located under this directory.

- `/bin` - Contains essential command binaries.

- `/boot` - Contains files required for booting the system.

- `/dev` - Contains device files.

- `/etc` - Contains system-wide configuration files.

- `/home` - Contains home directories for users.

- `/lib` - Contains libraries needed by the essential binaries in the `/bin` and `/sbin` directories.

- `/media` - Mount point for removable media.

- `/mnt` - Mount point for mounting a file system temporarily.

- `/opt` - Contains add-on applications from third parties.

- `/proc` - Contains virtual files that store information about the system.

- `/root` - Home directory for the root user.

- `/run` - Contains system information data describing the system since it was booted.

- `/sbin` - Contains essential system binaries.

- `/srv` - Contains data for services provided by the system.

- `/sys` - Contains information about devices, drivers, and some kernel features.

- `/tmp` - Contains temporary files.

- `/usr` - Contains binaries, libraries, documentation, and source-code for second level programs.

- `/var` - Contains variable data files.

### Linux File System Permissions

Linux file system permissions are used to control who is able to read, write and execute a certain file. These permissions can be granted to the owner of the file, the group associated with the file, and all other users.

There are three types of permissions:

- Read (r) - The ability to read a file. For directories, this means the ability to list the contents of the directory.

- Write (w) - The ability to write to a file. For directories, this means the ability to create and delete files in the directory.

- Execute (x) - The ability to execute a file. For directories, this means the ability to access files and subdirectories in the directory.

To see permissions for a file, run:

```bash
ls -l <filename or path>
```

It should show something like this (may be different depending on the file and its permissions):

```bash
-rw-r--r-- 1 user user 0 Jan 1 00:00 <filename or path>
```

The first character indicates the type of file. A dash (-) indicates a regular file. A d indicates a directory.

The next three characters indicate the permissions for the owner of the file. In this case, the owner has read and write permissions, but not execute permissions.

The next three characters indicate the permissions for the group associated with the file. In this case, the group has read permissions, but not write or execute permissions.

The last three characters indicate the permissions for all other users. In this case, all other users have read permissions, but not write or execute permissions.

## References

- [Linux | Wikipedia][1]
- [Shell (computing) | Wikipedia][2]
- [What is Linux? | Linux.com][3]
- [Introduction to Linux | The Linux Foundation][4]

[1]: https://en.wikipedia.org/wiki/Linux
[2]: https://en.wikipedia.org/wiki/Shell_(computing)
[3]: https://www.linux.com/what-is-linux/
[4]: https://training.linuxfoundation.org/training/introduction-to-linux
