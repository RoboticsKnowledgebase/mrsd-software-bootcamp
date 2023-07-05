# GitHub

GitHub is a web-based Git repository hosting service. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.

To complete the following steps, you need to have a GitHub account. If you don't have one, you can create one for free at [github.com](github.com).

## GitHub Student Developer Pack

GitHub offers a student developer pack that gives students free access to the best developer tools in one place so they can learn by doing. To get started, go to [education.github.com/pack](https://education.github.com/pack) and sign up with a new or existing account. You will be asked to verify your student status. Once you have completed the steps to verify your student status, you will be able to access the student developer pack.

## Exercises

## Git Workflow Exercise

1. To begin the exercise, sign up for an account on [GitHub](https://github.com).

1. Fork the repository at [mrsd-practice-git](https://github.com/RoboticsKnowledgebase/mrsd-practice-git) to your own account

1. Install `git` on your local machine

1. Clone your forked repository to your local development machine by running:

    ```bash
    git clone https://github.com/RoboticsKnowledgebase/mrsd-practice-git
    ```

1. Create a new local branch based off `main` branch

    ```bash
    git checkout -b new-branch-name
    ```

1. Open the `contributors.md` file using your favorite text editor, and adding your name and GitHub username in a new line

    ```text
    John Doelan (johndoe)
    ```

1. Stage and commit your changes

    ```bash
    git add contributors.md
    git commit -m "Add johndoe to contributors list"
    ```

1. Push changes to your repository on GitHub

    ```bash
    git push origin new-branch-name
    ```

1. Raise a pull request against this repository requesting to pull changes from your new branch into the `main` branch

1. Wait for the pull request to be reviewed, make any changes suggested by the repository maintainer and wait for the pull request to be merged.
