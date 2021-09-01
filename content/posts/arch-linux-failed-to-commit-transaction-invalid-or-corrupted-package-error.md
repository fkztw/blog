Title: [Arch Linux] Failed to commit transaction (invalid or corrupted package) error  
Slug: arch-linux-failed-to-commit-transaction-invalid-or-corrupted-package-error  
Date: 2021-09-01 23:02:14  
Authors: m157q  
Category: Note  
Tags: Note, Arch Linux, yay, pacman  
Summary: Got really annoyed when I run `yay -Syu` and encounter this error. And MORE HATE FOR MYSELF because I always forget how to fix this. That's the reason why I am here typing on my keyboard writing this post. I HAVE TO WRITE IT DOWN!  


# TL;DR

`# find /var/cache/pacman/pkg/ -iname "*.part" -delete`

And...
WHALA!


---

# Detail

> Look for .part files (partially downloaded packages) in /var/cache/pacman/pkg/ and remove them (often caused by usage of a custom XferCommand in pacman.conf).

---

# Some commands might help

- `pacman -Sy archlinux-keyring`
- `pacman-key --refresh-keys`

---

# References

- [\[SOLVED\] Invalid or Corrupted package (PGP signature) / Pacman & Package Upgrade Issues / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=233480)
- [pacman - ArchWiki](https://wiki.archlinux.org/title/Pacman#.22Failed_to_commit_transaction_.28invalid_or_corrupted_package.29.22_error)
