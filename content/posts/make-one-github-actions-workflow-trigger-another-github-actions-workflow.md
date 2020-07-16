Title: Make One GitHub Actions Workflow Trigger Another GitHub Actions Workflow
Slug: make-one-github-actions-workflow-trigger-another-github-actions-workflow
Date: 2020-07-16 16:35:20
Authors: m157q
Category: Note
Tags: GitHub, GitHub Actions
Summary: GitHub Actions restricts one workflow trigger another workflow in order to prevent users from accidentally creating recursive workflow. I spent some time on figuring how to do it.


# Preface

According to GitHub: [Users have to use Personal Access Token on the workflow which wants to trigger another GitHub Actions workflow.](make-one-github-action-workflow-trigger-another-github-action-workflow)

> When you use the repository's `GITHUB_TOKEN` to perform tasks on behalf of the GitHub Actions app, events triggered by the `GITHUB_TOKEN` will not create a new workflow run. This prevents you from accidentally creating recursive workflow runs. For example, if a workflow run pushes code using the repository's `GITHUB_TOKEN`, a new workflow will not run even when the repository contains a workflow configured to run when push events occur."

It looks easily, but there are lots of traps while doing so actually. I tried many different ways to achieve this and finally made it work.

There are other approaches like:

- using another bot user with new personal access token
- using GitHub App access token

But this post will only focus on using your own Personal Access Token.


# Solution

- Create a GitHub Personal Access Token with `repo` permissons at <https://github.com/settings/tokens>
- Copy that access token and paste it in the `Secrets - Settings` page of the target repo with the name `MY_GITHUB_TOKEN`
    - You can name the Secret with a different name. Just maek sure you write the name right later.
    - CAUTION: You cannot name your Secret starts with `GITHUB_` [because its preserve for GitHub Actions internal usage](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#naming-your-secrets).
    - Every GitHub Actions workflow has `GITHUB_TOKEN` in default.
- In the `yml` file of the workflow you want to trigger another workflow, you have to write these line in the **CHECKOUT** step:

```
    - name: Check out repo
      uses: actions/checkout@v2
      with:
        token: ${{ secrets.MY_GITHUB_TOKEN }}
        persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal access token
        fetch-depth: 0 # otherwise, you will failed to push refs to dest repo
```

- In the `yml` file of the workflow you want to trigger another workflow, you have to write these line in the **PUSH** step:

```
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.MY_GITHUB_TOKEN }}
        branch: 'source'    # default using 'master', change it if you want to push to another branch
```


# Result & Example

I am using one GitHub Actions workflow with `on:schedule` to auto-generate weekly post for my blog.  
Meanwhile, I have another workflow which will auto-build my blog when there is new commit being pushed. 
I want it work finely after a new weekly post being pushed.
Here's the `yml` file of that "auto-generate weekly post" workflow: <https://github.com/M157q/m157q.github.io/blob/source/.github/workflows/generate_weekly_post.yml>


# References

- [GitHub - ad-m/github-push-action: GitHub actions to push back to repository eg. updated code](https://github.com/ad-m/github-push-action)
- [GitHub - actions/checkout: Action for checking out a repo](https://github.com/actions/checkout)
- [Triggering a new workflow from another workflow - GitHub Actions - GitHub Support Community](https://github.community/t/triggering-a-new-workflow-from-another-workflow/16250)
- [Events that trigger workflows - GitHub Docs](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#triggering-new-workflows-using-a-personal-access-token)
- [Workflow syntax for GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#on)
- [Authenticating with the GITHUB_TOKEN - GitHub Docs](https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token)
