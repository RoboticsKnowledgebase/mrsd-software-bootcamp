# Remote Access with SSH

## Setting Up a Firewall

If you are exposing your server to the internet, it is important to set up a firewall to protect it from unauthorized access. Ubuntu ships with a firewall called `ufw` (Uncomplicated Firewall) that is easy to configure.

To enable `ufw` firewall, run:

```bash
sudo ufw enable
```

You can check the status of the firewall with this command:

```bash
sudo ufw status
```

## Enable Remote Login with SSH

To enable remote login with SSH, you need to install the `openssh-server` package.

To install the `openssh-server` package, run:

```bash
sudo apt update
sudo apt install openssh-server
```

Allow SSH traffic through 'ufw' firewall:

```bash
sudo ufw allow ssh
```

### Security Recommendations

#### Disable Logging in as Root User

It is recommended to disable logging in as the root user because it is a common target for brute-force attacks.

To disable root login, open the SSH daemon configuration file:

```bash
sudo nano /etc/ssh/sshd_config
```

Find the line that contains `PermitRootLogin` and modify it to ensure that users can only connect with their own credentials:

```bash
PermitRootLogin no
```

Restart the SSH daemon:

```bash
sudo systemctl restart sshd
```

#### Set Up SSH Key-Based Authentication

SSH key-based authentication is more secure than password-based authentication because it is not vulnerable to brute-force attacks.

Setting up ssh key-based authentication involves generating a public-private key pair on your local machine and copying the public key to the remote server.

To generate a new SSH key pair, run (on your local machine):

```bash
ssh-keygen
```

To copy the public key to the remote host, run (on your local machine):

```bash
ssh-copy-id username@remote_host
```

## Disabling Password Authentication

To disable password authentication, open the SSH daemon configuration file (on the remote server):

```bash
sudo nano /etc/ssh/sshd_config
```

Find the line that contains `PasswordAuthentication` and modify it to ensure that users can only connect with their own credentials:

```bash
PasswordAuthentication no
```

Restart the SSH daemon (on the remote server):

```bash
sudo systemctl restart sshd
```

Test the new configuration by logging in without a password (on your local machine):

```bash
ssh username@remote_host
```

### Changing the SSH Port

Changing the SSH port is a good idea because it makes it harder for attackers to find your SSH port and launch brute-force attacks.

To change the SSH port, open the SSH daemon configuration file (on the remote server):

```bash
sudo nano /etc/ssh/sshd_config
```

Find the line that contains `Port` and modify it to the desired port number:

```bash
Port 7777
```

Restart the SSH daemon (on the remote server):

```bash
sudo systemctl restart sshd
```

Test the new configuration by logging in with the new port number (on your local machine):

```bash
ssh username@remote_host -p 7777
```

## References

- [How To Use SSH to Connect to a Remote Server | Digital Ocean][1]
- [SSH Essentials: Working with SSH Servers, Clients, and Keys | Digital Ocean][2]
- [How To Configure SSH Key-Based Authentication on a Linux Server | Digital Ocean][3]
- [Initial Server Setup with Ubuntu 22.04 | Digital Ocean][4]

[1]: https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server
[2]: https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys
[3]: https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server
[4]: https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04
