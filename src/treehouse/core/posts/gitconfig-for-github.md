+++
title = '`gitconfig` for GitHub'
date = 2024-08-15T15:35:46+00:00
draft = false
categories = ["programming"]
tags = ["git", "github"]
+++

To keep our personal email addresses private, GitHub provides a "no reply" email address(`number+username@users.noreply.github.com`) for every user, and you might want to put it to use.

Supposing you use `~/GitRepositories/GitHub` directory for GitHub, create a `gitconfig` file there and add a `user` section.
```
mkdir -p ~/GitRepositories/GitHub
cat <<EOF | tee ~/GitRepositories/GitHub/gitconfig
[user]
        email = number+username@users.noreply.github.com
        name = github-user
        
        # NOTE: If you have a GPG key,
        # to make commits signed by default
        # gpgsign = true


        # NOTE: Specify a signing key if git can't find a usable key.
        # signingkey = key-signature-goes-here 
EOF
```

Add an `includeIf` section to your global [`gitconfig`](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration) located at `~/.gitconfig`.
```
cat <<EOF | tee --append ~/.gitconfig
[includeIf "gitdir:~/GitRepositories/GitHub/"] # <- gitdir path
# NOTE: the gitdir path must end with a forward slash (/)
    path = ~/GitRepositories/GitHub/gitconfig
EOF
```

And that's it! Now every `git` repository in `~/GitRepositories/GitHub/` will use the custom `gitconfig`.