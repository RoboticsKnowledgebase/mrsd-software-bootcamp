# Version Control Systems

Version control or source control is the practice of tracking and managing changes to software code. Version control software(VCS) are software tools that help software teams manage changes to source code over time. ([1])

A VCS also offers collaborative utilities to share and integrate these changes in source files to other VCS users. A VCS will track the addition, deletion, and modification of files in a directory hierarchy. Such a directory structure within which all source file and metadata changes are tracked is called a _repository_. With each source file, a VCS will track additions, deletions and modifications of the lines of text within that file.

There exist several different version control systems, each with their own pros and cons:

- Git
- Subversion (SVN)
- Mercurial (Hg)
- Perforce

## Key Concepts in Version Control Software

### Repository Model

Repository model is the way in which the VCS stores the history of changes to the source code. There are two main repository models:

- **Centralized / Client-Server Model**: In this model, there is a central server that stores the entire history of the codebase. Developers can checkout a copy of the codebase from the central server and work on it locally. When they are done, they can commit their changes back to the central server. This model is used by Subversion and Perforce.

- **Distributed Model**: In this model, every developer has a complete copy of the codebase and its history on their local machine. This allows developers to work on the codebase without needing to be connected to the internet or a central server. This model is used by Git and Mercurial.

## References

- [What is Version Control? | Atlassian][1]
- [Version Control Software | BitBucket][2]
- [Version Control | GitLab][3]

[1]: https://www.atlassian.com/git/tutorials/what-is-version-control
[2]: https://bitbucket.org/product/version-control-software
[3]: https://about.gitlab.com/topics/version-control/
