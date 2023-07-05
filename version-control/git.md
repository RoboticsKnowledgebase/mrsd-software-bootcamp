# Git

## What is Git?

Git is a distributed revision control and source code management system with an emphasis on speed. Every Git working directory is a full-fledged repository with complete history and full version tracking capabilities, and is not dependent on network access or a central server. Git is free software distributed under the terms of the GNU GPLv2.

Git is primarily a command-line tool but there are simplified graphical user interface applications that make it easier to work with. Starting with a GUI client is a great way to mitigate git's steep learning curve.

## Why do I need Git?

As a roboticist, you will be working with a lot of code. You will be writing code, modifying code, and sharing code with other people. You will also be working on multiple projects at the same time. Git is a tool that helps you manage all of this code. It allows you to keep track of all of the changes that you make to your code, and share your code with other people. It also allows you to work on multiple projects at the same time, and it allows you to switch between projects easily.

## Git Terminology

### Repository

A repository is a directory that contains your project files which is managed by git. Each repository contains a collection of files and directories along with the history of changes made to those files and directories. Repositories can exist locally on your computer or as a remote copy on another computer. Repositories can also talk to each other over the internet and sync changes. A local git repository behaves exactly like a regular directory in your file system which you can add, remove and edit files in. The only difference is that git can keep track of all the changes that happen to the files in that directory. You will also notice that a git repository has a hidden directory called `.git` which contains all the information git needs to keep track of the changes to the files in that directory.

### Commit

A commit, or revision or change-set, is a set of modifications made to a file or a set of files. Every time you want to save the state of a project directory with git, you would do what is called the "commit" operation which creates a new commit object. Each commit object is named a unique hash value that allows git to keep record of what changes were made, when and by who. During commit creation, the user is asked to provide a brief summary of what changes went into that particular change-set.

Example git commit message showing the commit hash, author, date and commit message:

```text
commit 175437538623b381727c4046862cd252bb44569b
Author: John Doelan <johndoe@domain.net>
Date:   Mon Apr 17 03:45:54 2023 -0400

    Add a page for Linux fundamentals

    Add a page for Linux basics, covering an introduction to Linux, shell,
    file system and directory structure.
```

### Branch

A branch is when a new line of development is created that diverges from the main line of development. This alternative line of development can continue without altering the main line. Going back to the example of save points, you can think of a branch as where you make a save point in your game and then decide to try out a risky move in the game. If the risky move doesn't pan out, then you can just go back to the save point. The key thing that makes branches incredibly powerful is that you can make save points on one branch, and then switch to a different branch and make save points there, too.

### Fork

A fork is a personal copy of another user's repository that lives on your account. Forks allow you to freely make changes to a project without affecting the original. Forks remain attached to the original, allowing you to submit a pull request to the original's author to update with your changes. You can also keep your fork up to date by pulling in updates from the original.

### Pull Request

Pull requests are proposed changes to a repository submitted by a user and accepted or rejected by a repository's collaborators. Like issues, pull requests each have their own discussion forum.

## Learning Resources

### Basics

- [GitHub Learning Lab](https://lab.github.com/) offers some excellent courses on mastering the basics of git on their platform. Their [Introduction to GitHub](https://lab.github.com/githubtraining/introduction-to-github) course is great place to get started.

- [GitHub's Getting Started Guide](https://help.github.com/)
  Walks you through creating a repository on GitHub and basics of git.

- [Learn Git Branching](https://learngitbranching.js.org/):
  A browser-based game designed to introduce you to some of the more advanced concepts.

- [Git Immersion](http://gitimmersion.com/):
A hands-on tutorial that sets you up with a toy project and holds your hand through project development. Contains many useful aliases and shortcuts for faster workflow.

- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials):
One of the best reading resources around git and version control. Contains a very good set of tutorials but more importantly has a comprehensive set of articles around the important topics in git and even the history of version control systems. Focuses on providing a detailed explanation of how git works rather than simply listing the commands.

### Intermediate

- [Managing Merge Conflicts](https://lab.github.com/githubtraining/managing-merge-conflicts)
- [Reviewing Pull Requests](https://lab.github.com/githubtraining/reviewing-pull-requests)
- [GitHub Actions Basics](https://lab.github.com/githubtraining/github-actions:-hello-world)
- [Cherry Picking Commits](https://www.atlassian.com/git/tutorials/cherry-pick)
- [Rebasing Branches](https://docs.github.com/en/get-started/using-git/about-git-rebase)
- [Git Blame](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-blame)

### Advanced

- [Git Reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)
- [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [Hooks, Enforcing Commit-Message Formats & ACLs](https://git-scm.com/book/en/v2/Customizing-Git-An-Example-Git-Enforced-Policy)
- [A Beginner's Guide to Git Bisect](https://www.metaltoad.com/blog/beginners-guide-git-bisect-process-elimination)
- [Continuous Integration Using GitHub Actions](https://lab.github.com/githubtraining/github-actions:-continuous-integration)

## Free Repository Hosting Providers

- ### [GitHub](https://www.github.com/)

  A well-supported and popular hosting provider for git repositories. Their desktop application [GitHub Desktop](https://desktop.github.com/) is a high-quality, feature-rich GUI for Windows and Mac. GitHub offers unlimited public and private repositories and ability to create an 'organization' for free to host team projects, with limited monthly credits for automated builds. GitHub excels at providing a great experience around git and source code management, with good options for builds and deployment integrations.

  [GitHub Education Pack](https://education.github.com/pack) provides access to a bundle of popular development tools and services which GitHub and its partners are providing for free (or for a discounted price) to students.

- ### [GitLab](https://gitlab.com/explore)

  The other big player in the version control space and the first choice for Enterprise git deployments. Offers free unlimited public and private repositories with unlimited collaborators. Offers some nifty features that GitHub doesn't offer in their free tier such as protected branches, pages and wikis. Offers a self-hosting option if you want to run your own git server. Their platform is geared towards serving a complete and comprehensive DevOps workflow that is not just restricted to source code management.

- ### [BitBucket](https://bitbucket.org/)

  Another popular service, unlimited private repositories for up to 5 collaborators.
  - [Getting Started Guide](https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+101)

## Popular GUI Clients

- [GitHub Desktop](https://desktop.github.com/)
  High-quality, well-supported GUI for Windows & Mac.
- [SourceTree](https://www.sourcetreeapp.com/)
  A feature-rich GUI for Windows & Mac.
- [GitKraken](https://www.gitkraken.com/)
  A powerful git client for Linux, Windows & Mac.
- [GitExtensions](https://gitextensions.github.io/)
  Also supports Linux, Windows & Mac.

## References & Help

- [Atlassian Git Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet): A handy set of commands to have around your desk for those quick command look ups.

- [How to Undo Almost Anything with Git](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/): A blog post from GitHub that lists some scary scenarios in git and how to undo almost anything.

- [Dangit, Git!?](https://dangitgit.com/): Quick references for getting out of bad situations in git. Very powerful set of fixes, but doesn't provide a good explanation of what happened / how the fix works - read before you blindly follow the instructions.

- [Official Git Documentation](http://git-scm.com/documentation)
Extremely thorough documentation of git. It can be quite dense if you're new to git, but this the most authoritative and updated documentation for git CLI usage. Best used to look up command-line usage, parameters and their rationale.

- Man pages: The git command line interface ships with a very good set of man pages accessible by running `man git` on the terminal and is available wherever git is installed. If you're not familiar with man pages, you can read about it [here](https://itsfoss.com/linux-man-page-guide/).
