+++
title = 'Make a Website With Hugo'
date = 2024-08-14T01:20:19+00:00
draft = false
categories = ["programming"]
tags = ["hugo", "web"]
+++
# The Site Project
To start with, create a `site` project with the [`hugo`](https://gohugo.io) program, assuming you'd like to call it `heim`:
```
hugo new site heim
cd heim
```
# Hugo Modules
`hugo` has changed a lot since I used it for the first time. `hugo` now supports importing modules/repos directly using `git`, much like `go`'s module system. Now, in order to use a theme, instead of going through the hassle of setting up `git submodule`, `hugo` can manage all the process for you. You can initialize `hugo` module support with this command:
```
hugo mod init heim
```
Add the theme that you want to use to `hugo.toml`. I'm adding `typo`:
```
theme = "github.com/tomfran/typo"
[module]
  [[module.imports]]
    path = 'github.com/tomfran/typo'
```
And download the `typo` theme as a module:
```
hugo mod get
```
# Config and Homepage
As indicated in the [wiki](https://github.com/tomfran/typo/wiki/Setup), a sample `hugo.toml` can be downloaded from another [repository](https://github.com/tomfran/blog/blob/main/hugo.toml). Download the `hugo.toml` file to the project's root directory, and edit it accordingly:
```
curl -L 'https://github.com/tomfran/blog/raw/main/hugo.toml' -o hugo.toml
$EDITOR hugo.toml
```
As for the homepage, create a [markdown](https://daringfireball.net/projects/markdown/) file `_index.md` in the `content` directory, and edit it like the following:
```
+++
title = 'Heim'
draft = false
+++
# Homepage
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure 
dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.
```
# Blog Posts
Every blog post is a markdown file, and they are rendered to HTML by `hugo` during the site generation. To create your first post, simply create another markdown file in the `content/posts` directory. Run this command to create a post template:
```
hugo new content/posts/first-post.md
```
After you finish editing your first post, you can now serve the website locally with `hugo`'s development server:
```
hugo server -D
```
# Deployment and More
I will write more about production deployment and other related topics later.