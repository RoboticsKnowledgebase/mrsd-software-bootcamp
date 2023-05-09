# Job Control in Linux

## Introduction

In this lesson we will learn how to manage processes in Linux. We will learn how to run processes in the background, how to pause and resume them, and how to run them in the foreground again.

## Prerequisites

- [Linux 101](../linux/linux-101.md)
- [CLI Tools](../linux/cli-tools.md)

## Exercises

To begin the exercise, ensure you have `python3` installed and download the mock script that mimics a robot driver program.

```bash
wget https://raw.githubusercontent.com/nevalsar/mrsd-practice-git/main/autonomous-robot-mock.py -O robot-driver.py
```

You also need to ensure that the script is executable by setting executable permissions.

```bash
chmod +x robot-driver.py
```

Test that you're able to execute the script by running it.

```bash
./robot-driver.py 5
```

### Running processes in the background

#### Using `&` at the end of the command

1. Run the `sleep` command in the background by appending `&` at the end of the command

    ```bash
    ./robot-driver.py 10 &
    ```

    You will notice that the terminal is not blocked and you can run other commands.

1. List the jobs running in the background to verify

    ```bash
    jobs
    ```

#### Using `Ctrl + Z`

1. Run a command in the foreground

    ```bash
    ./robot-driver.py 10
    ```

    You will notice that the terminal is blocked by the process running in foreground and you cannot run other commands.

1. Move the foreground command to background by pressing `Ctrl + Z`

    You will notice that the terminal is not blocked anymore and you can run other commands.

1. List the jobs running in the background to verify

    ```bash
    jobs
    ```

### Moving a background process to the foreground

1. Run a command in the background by appending `&` at the end of the command

    ```bash
    ./robot-driver.py 10 &
    ```

1. Move the process to foreground using `fg`:

    ```bash
    fg
    ```

    You will notice that now the terminal is blocked by the process running in foreground and you cannot run other commands.

### Pausing and resuming processes

1. Run the `sleep` command in the background by appending `&` at the end of the command

    ```bash
    ./robot-driver.py 10 &
    ```

1. Get the PID of the `robot-driver.py` program

    ```bash
    jobs -l
    ```

    You will notice that the PID of the running program is listed against its name. Note it down.

1. Pause the command by sending it the `SIGSTOP` signal

    ```bash
    kill -STOP <pid>
    ```

1. Resume the `sleep` command by sending it the `SIGCONT` signal

    ```bash
    kill -CONT <pid>
    ```
