# Git Pull-Request Workflow Exercise

1. To begin the exercise, sign into the account you made in the previous exercise on [GitHub](github.md).

2. Fork the repository at [mrsd-practice-git](https://github.com/RoboticsKnowledgebase/mrsd-practice-git) to your own account

3. Install `git` on your local machine

4. Clone your forked repository to your local development machine by running:

    ```bash
    git clone https://github.com/RoboticsKnowledgebase/mrsd-practice-git
    ```

1. Create a new local branch based off `main` branch

    ```bash
    git checkout -b new-branch-name
    ```

2. Open the `contributors.md` file using your favorite text editor, and adding your name and GitHub username in a new line

    ```text
    John Doelan (johndoe)
    ```

3. Stage and commit your changes

    ```bash
    git add contributors.md
    git commit -m "Add johndoe to contributors list"
    ```

4. Push changes to your repository on GitHub

    ```bash
    git push origin new-branch-name
    ```

5. Raise a pull request against this repository requesting to pull changes from your new branch into the `main` branch

6. Wait for the pull request to be reviewed, make any changes suggested by the repository maintainer and wait for the pull request to be merged.
