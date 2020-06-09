Title: Podman Error: setup user: cannot set uid to unmapped user in user namespace  
Slug: podman-error-setup-user-cannot-set-uid-to-unmapped-user-in-user-namespace  
Date: 2020-02-07 20:14:31  
Authors: m157q  
Category: Note  
Tags: podman, docker  
Summary: Started to use Podman recently. Got stucked on the non-root user environment for hours. Write down some notices here.  
Modified: 2020-06-09 19:57:31  
  
  
# Error Messages  
  
- `setup user: cannot set uid to unmapped user in user namespace`  
- `starting container process caused "setup user: invalid argument": oci runtime error`  
  
# TL;DR  
  
1. Generate and modify `/etc/subuid` and `/etc/subgid` files first.  
    - Can use `sudo usermod --add-subuids 100000-165536 --add-subgids 100000-165536 ${YOUR_USERNAME}` to modify these two files.  
2. `podman system migrate`  
    - **THIS IS VERY IMPORTANT!**  
    - Lots of resources didn't tell you that you should execute this command after modifying `/etc/subuid` and `/etc/subgid` to make it works for Podman. (Or maybe the problem is I should read the tutorial for Podman first. Anyway.)  
    - If you have built the images before executing `podman system migarte`, you should re-build those images again without using image cache. Or, you can just use `podman rmi` to delete those images and re-build them.  
        - Including the base image like Ubuntu, Debian, Arch Linux which you pulled from somewhere. Yes, you should delete it and re-build. Otherwise, you will still get the error.  
3. `podman unshare cat /proc/self/uid_map` to check if it works.  
    - Should be like this:  
    ```  
    $ podman unshare cat /proc/self/uid_map  
             0       1000          1  
             1     100000      65536  
    ```  
4. `podman build` with existing Dockerfile  
  
---  
  
# Meaning in `/etc/subuid` and `/etc/subgid`  
  
Take `/etc/subuid` as example:  
  
```  
user:100000:65536  
```  
  
- `user` is the username of the system user. Can be `uid` as well.  
- `100000` is the system UID for the container UID to start with.  
- `65536` is the number of UIDs allowed to be mapped.  
- Which means UID `100000~165535` on system are allowed for mapping to system user `user` while running container as this system user.  
- UID 0 in the container will be UID 100000 on the system. UID 1 in the container will be UID 100001 on the system etc.  
- Which related to the command `podman unshare cat /proc/self/uid_map` mentioned above.  
  
Change the UID above to GID for `/etc/subgid`  
  
---  
  
# References  
  
- [Running rootless Podman as a non-root user | Enable Sysadmin](https://www.redhat.com/sysadmin/rootless-podman-makes-sense)  
- [Running Linux containers as a non-root with Podman - Fedora Magazine](https://fedoramagazine.org/running-containers-with-podman/)  
- [How does rootless Podman work? | Opensource.com](https://opensource.com/article/19/2/how-does-rootless-podman-work)  
- [What do the contents of /etc/subuid mean in the context of docker - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/397092/what-do-the-contents-of-etc-subuid-mean-in-the-context-of-docker)  
