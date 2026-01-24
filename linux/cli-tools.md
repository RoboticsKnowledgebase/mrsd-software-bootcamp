# Command-line Tools

## Why Learn the Command Line?

The terminal or the command line is a powerful tool that can be used to perform a wide variety of tasks. It can be used to navigate through files and folders, run programs, and automate tasks. In robotics, the ability to use the command line effectively can come in very handy when logging into a robot remotely or debugging a robot that is not responding. Since complex robots often have full fledged operating systems running on them, the ability to work directly with the command line can be very useful.

## Key Concepts

### What is the command line?

The command line is a text interface for your computer. It's a program that takes in commands, which it passes on to the computer's operating system to run. From the command line, you can navigate through files and folders on your computer through a text-based interface and run programs without a graphical user interface (GUI).

### What is a shell?

A shell is a program whose primary purpose is to read commands and run other programs.

Some of the most popular shells are:

- Bourne Shell (Sh)
- Bourne Again Shell (Bash)
- Zsh
- Fish

Shell scripts are files that contain shell commands. They are used to automate tasks and can be run from the command line. Typically, shell scripts have the `.sh` extension. The first line of a shell script is called the shebang and it tells the shell which program to use to run the script. For example, the shebang `#!/bin/bash` tells the shell to use the Bash shell to run the script.

Example of a shell script

```bash
#!/bin/bash

echo "Hello, world!"
```

### What is a terminal emulator?

A terminal emulator is a program that opens a window and lets you interact with the shell. There are several different terminal programs that vary across operating systems and desktop environments. Some of the most popular terminal emulators are:

- GNOME Terminal
- iTerm2
- xterm
- Konsole

## Basic Commands

### `ls`

`ls` lists the contents of a directory.

```bash
ls
```

### `cd`

`cd` changes the current working directory.

```bash

# Change to the home directory

cd

# Change to the root directory

cd /

# Change to the parent directory

cd ..

# Change to the previous directory

cd -

# Change to the directory named "foo"

cd foo

# Change to the directory named "foo" in the current directory

cd ./foo

# Change to the directory named "foo" in the parent directory

cd ../foo

# Change to the directory named "foo" in the root directory

cd /foo
```

### `pwd`

`pwd` prints the current working directory.

```bash

# Print the current working directory

pwd
```

### `mkdir`

`mkdir` creates a new directory.

```bash

# Create a new directory named "foo"

mkdir foo
```

### `touch`

`touch` creates a new file.

```bash

# Create a new file named "foo"

touch foo
```

### `cp`

`cp` copies a file or directory.

```bash

# Copy the file "foo" to the file "bar"

cp foo bar

# Copy the file "foo" to the directory "bar"

cp foo bar/

# Copy the directory "foo" to the directory "bar"

cp -r foo bar
```

### `mv`

`mv` moves a file or directory.

```bash

# Move the file "foo" to the file "bar"

mv foo bar

# Move the file "foo" to the directory "bar"

mv foo bar/

# Move the directory "foo" to the directory "bar"

mv foo bar
```

### `rm`

`rm` removes a file or directory.

```bash

# Remove the file "foo"

rm foo

# Remove the directory "foo"

rm -r foo
```

### `cat`

`cat` prints the contents of a file to the terminal.

```bash

# Print the contents of the file "foo"

cat foo
```

### `less`

`less` prints the contents of a file to the terminal one page at a time.

```bash

# Print the contents of the file "foo"

less foo
```

### `head`

`head` prints the first 10 lines of a file to the terminal.

```bash

# Print the first 10 lines of the file "foo"

head foo
```

### `tail`

`tail` prints the last 10 lines of a file to the terminal.

```bash

# Print the last 10 lines of the file "foo"

tail foo
```

### `grep`

`grep` searches for a pattern in a file.

```bash

# Search for the pattern "foo" in the file "bar"

grep foo bar
```

### `find`

`find` searches for files in a directory hierarchy.

```bash

# Search for files named "foo" in the current directory

find . -name foo

# Search for files named "foo" in the current directory and its subdirectories

find . -name foo -print

# Search for files named "foo" in the current directory and its subdirectories and delete them

find . -name foo -delete
```

### `locate`

`locate` searches for files in a database.

```bash

# Search for files named "foo" in the database

locate foo
```

### `which`

`which` searches for a program in the directories specified by the `PATH` environment variable.

```bash

# Search for the program "foo" in the directories specified by the `PATH` environment variable

which foo
```

### `man`

`man` displays the manual page for a program.

```bash

man foo
```

### `alias`

`alias` creates an alias for a command.

```bash

# Create an alias for the command "ls" named "l"

alias l="ls"
```

### `echo`

`echo` prints a string to the terminal.

```bash

# Print the string "foo" to the terminal

echo foo
```

### `export`

`export` sets an environment variable.

```bash

# Set the environment variable "FOO" to the value "bar"

export FOO=bar
```

### `source`

`source` executes a file in the current shell.

```bash

# Execute the file "foo" in the current shell

source foo
```

### `chmod`

`chmod` changes the permissions of a file or directory.

```bash

# Give the user read, write and execute permissions, the group read and execute permissions and the others read and execute permissions to the file "foo"

chmod 755 foo
```

### `chown`

`chown` changes the owner and group of a file or directory.

```bash

# Change the owner of the file "foo" to the user "bar" and the group "baz"

chown bar:baz foo
```

### `sudo`

`sudo` executes a command as another user, usually the superuser.

```bash

# Execute the command "foo" as the superuser

sudo foo
```

### `su`

`su` switches to another user.

```bash

# Switch to the user "foo"

su foo
```

### `passwd`

`passwd` changes the password of a user.

```bash

passwd
```

### `exit`

`exit` exits the current shell.

```bash

exit
```

### `clear`

`clear` clears the terminal screen.

```bash

clear
```

### `history`

`history` prints the command history.

```bash

history
```

### `date`

`date` prints the current date and time.

```bash

date
```

### `uptime`

`uptime` prints the system uptime.

```bash

uptime
```

### `uname`

`uname` prints system information.

```bash

uname
```

### `df`

`df` prints disk usage information.

```bash

df
```

### `du`

`du` prints disk usage information for a file or directory.

```bash

# Print disk usage information for the file "foo"

du foo

# Print disk usage information for the directory "foo"

du foo
```

### `free`

`free` prints memory usage information.

```bash

free
```

### `ps`

`ps` prints information about running processes.

```bash

ps
```

### `kill`

`kill` sends a signal to a process.

```bash

# Send the SIGTERM signal to the process with the PID 1234

kill -s SIGTERM 1234
```

### `top`

`top` prints information about running processes and system resource usage.

```bash

top
```

### `bg`

`bg` resumes a suspended process in the background.

```bash

# Resume the suspended process with the PID 1234 in the background

bg 1234
```

### `fg`

`fg` resumes a suspended process in the foreground.

```bash

# Resume the suspended process with the PID 1234 in the foreground

fg 1234
```

### `jobs`

`jobs` lists the jobs running in the background.

```bash

jobs
```

### `nohup`

`nohup` runs a command that ignores the `HUP` signal.

```bash

# Run the command "foo" that ignores the `HUP` signal

nohup foo
```

### `killall`

`killall` sends a signal to all processes with a given name.

```bash

# Send the SIGTERM signal to all processes with the name "foo"

killall -s SIGTERM foo
```

### `ifconfig`

`ifconfig` prints network interface information.

```bash

ifconfig
```

### `ping`

`ping` pings a host.

```bash

ping foo.com
```

### `traceroute`

`traceroute` traces the route taken by packets across an IP network.

```bash

traceroute foo.com
```

### `wget`

`wget` downloads files from the internet.

```bash

# Download the file "foo" from the URL "http://example.com/foo"

wget http://example.com/foo
```

### `curl`

`curl` transfers data from or to a server.

```bash

# Transfer data from the URL "http://example.com/foo" to the file "foo"

curl http://example.com/foo -o foo
```

### `ssh`

`ssh` connects to a remote server.

```bash

# Connect to the remote server "foo.com" as the user "bar"

ssh bar@foo.com

# Connect to the remote server "foo.com" as the user "bar" and execute the command "baz"

ssh bar@foo.com "baz"

# Connect to the remote server "foo.com" as the user "bar" and execute the command "baz" in the background

ssh -f bar@foo.com "baz"
```

### `scp`

`scp` copies files between hosts on a network.

```bash

# Copy the file "foo" from the remote server "bar.com" to the current directory

scp bar.com:foo .

# Copy the file "foo" from the current directory to the remote server "bar.com"

scp foo bar.com:

# Copy the directory "foo" from the remote server "bar.com" to the current directory

scp -r bar.com:foo .

# Copy the directory "foo" from the current directory to the remote server "bar.com"

scp -r foo bar.com:
```

### `rsync`

`rsync` copies files between hosts on a network.

```bash

# Copy the file "foo" from the remote server "bar.com" to the current directory

rsync bar.com:foo .

# Copy the file "foo" from the current directory to the remote server "bar.com"

rsync foo bar.com:

# Copy the directory "foo" from the remote server "bar.com" to the current directory

rsync -r bar.com:foo .

# Copy the directory "foo" from the current directory to the remote server "bar.com"

rsync -r foo bar.com:
```

### `tar`

`tar` creates or extracts an archive.

```bash

# Create an archive named "foo.tar" from the file "foo"

tar -cf foo.tar foo

# Extract the archive named "foo.tar" to the current directory

tar -xf foo.tar
```

### `gzip`

`gzip` compresses or decompresses a file.

```bash

# Compress the file "foo"

gzip foo

# Decompress the file "foo.gz"

gzip -d foo.gz
```

### `gunzip`

`gunzip` decompresses a file.

```bash

# Decompress the file "foo.gz"

gunzip foo.gz
```

### `zip`

`zip` creates or extracts a zip archive.

```bash

# Create a zip archive named "foo.zip" from the file "foo"

zip foo.zip foo

# Extract the zip archive named "foo.zip" to the current directory

unzip foo.zip
```

### `unzip`

`unzip` extracts a zip archive.

```bash

# Extract the zip archive named "foo.zip" to the current directory

unzip foo.zip
```

## References

- [Top 50 Linux Commands - Digital Ocean][1]
- [How To Use Find and Locate to Search for Files on a Linux VPS - Digital Ocean][2]

[1]: https://www.digitalocean.com/community/tutorials/linux-commands
[2]: https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-linux
