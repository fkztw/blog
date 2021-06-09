Title: Be careful when using grep on CircleCI
Slug: be-careful-when-using-grep-on-circleci
Date: 2021-06-09 22:09:43
Authors: m157q
Category: Note
Tags: CircleCI, grep, shell
Summary: `grep` will exit 1 when no matching could be found. You won't notice this until you run it on CircleCI and the build job exit 1 with no error message at all.


Quote from the man page of `grep`:
> EXIT STATUS  
>      Normally the exit status is 0 if a line is selected,  
>      1 if no lines were selected, and 2 if an error occurred.  
>      However, if the  -q  or  --quiet  or --silent is used and a line is selected,  
>      the exit status is 0 even if an error occurred.  


## TL;DR

`(grep $something || true)`

To force grep exit 0 when no mathing could be found.
This also works with `grep -v` when you want to find the invert matching result.

---

## Details

If your `grep` command might be ends with no matching,
and you need the output of `grep` to combine with `awk`, `cut`, `xargs`, ...
you should use `grep` on CircleCI like this:
```sh
(grep ... || true)
```

```sh
(grep ... || :)
```

This `()` syntax works for bash, sh, zsh

For example:
```sh
${COMMAND_WITH_UNSURE_OUTPUT} | (grep ${TARGET_STRING} || true) | cut -d ' ' -f 1 | xargs ...
```

This will force grep return 0 even if no matching,
and you could still pipe the output to another command.
Unlike `grep -q` which returns 0 but no output could be used.

---

## Alternatives

These commands do not have same effect.
Might vary from different shells, use at your own risk and make sure you know what you are doing.

```sh
(grep $something || true)
{grep $something || true;}

(grep $something || test $? = 1)
{grep $something || test $? = 1;}

(grep $something || [[ $? == 1 ]])
{grep $something || [[ $? == 1 ]];}

(grep $something || :)
{grep $something || :;}
```

- `:` Do nothing beyond expanding arguments and performing redirections. The return status is zero.
    - <https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#Bourne-Shell-Builtins>

More discussions in here: <https://unix.stackexchange.com/questions/330660/prevent-grep-from-exiting-in-case-of-nomatch>

---

## Things about CircleCI

You might want to ask:
"But, I pipe the output to another command and the result of `echo $?` is 0."

According to <https://circleci.com/docs/2.0/configuration-reference/#default-shell-options>
CircleCI uses `/bin/bash -eo pipefail` for linux job.
It will check the exit code of every command between pipes,
not just the `$?` after the whole line of commands exectued.

> `-e`  
> Exit immediately if a pipeline (which may consist of a single simple command), a subshell command enclosed in parentheses, or one of the commands executed as part of a command list enclosed by braces exits with a non-zero status.

> `-o pipefail`  
> If pipefail is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. The shell waits for all commands in the pipeline to terminate before returning a value.

Once your `grep` doesn't find any matching,
You will get this error on CircleCI:

```text
Exited with code exit status 1
CircleCI received exit code 1
```
