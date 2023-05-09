# Job Control in Linux

## Introduction

In this lesson we will learn how to manage processes in Linux. We will learn how to run processes in the background, how to pause and resume them, and how to run them in the foreground again.

## Prerequisites

- [Linux 101](../linux/linux-101.md)
- [CLI Tools](../linux/cli-tools.md)

## Exercises

### Running processes in the background

#### Using `&` at the end of the command

1. Run the `sleep` command in the background by appending `&` at the end of the command

    ```bash
    sleep 100 &
    ```

    You will notice that the terminal is not blocked and you can run other commands.

1. List the jobs running in the background

    ```bash
    jobs
    ```

#### Using `Ctrl + Z`

1. Run the `sleep` command in the foreground

    ```bash
    sleep 100
    ```

    You will notice that the terminal is blocked by the process running in foreground and you cannot run other commands.

1. Pause the `sleep` command by pressing `Ctrl + Z`

    You will notice that the terminal is not blocked anymore and you can run other commands.

1. List the jobs running in the background

    ```bash
    jobs
    ```

### Moving a background process to the foreground

1. Run the `sleep` command in the background by appending `&` at the end of the command

    ```bash
    sleep 100 &
    ```

1. Run the `sleep` command in the foreground again

    ```bash
    fg
    ```

    You will notice that now the terminal is blocked by the process running in foreground and you cannot run other commands.

### Pausing and resuming processes

1. Run the `sleep` command in the background by appending `&` at the end of the command

    ```bash
    sleep 100 &
    ```

1. Get the PID of the `sleep` command

    ```bash
    jobs -l
    ```

    You will notice that the PID of the `sleep` command is listed.

1. Pause the `sleep` command by sending it the `SIGSTOP` signal

    ```bash
    kill -STOP <pid>
    ```

1. Resume the `sleep` command by sending it the `SIGCONT` signal

    ```bash
    kill -CONT <pid>
    ```
