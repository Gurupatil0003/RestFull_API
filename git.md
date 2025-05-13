Microsoft Windows [Version 10.0.26100.3915]
(c) Microsoft Corporation. All rights reserved.

C:\Users\LENOVO\Downloads\New folder (2)>code .

C:\Users\LENOVO\Downloads\New folder (2)>start .

C:\Users\LENOVO\Downloads\New folder (2)>git init
Initialized empty Git repository in C:/Users/LENOVO/Downloads/New folder (2)/.git/

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        learning.txt
        main.py
        main.tomato

nothing added to commit but untracked files present (use "git add" to track)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add main.py learning.txt

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   learning.txt
        new file:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.tomato


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "First commit"
[master (root-commit) 1505a68] First commit
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 learning.txt
 create mode 100644 main.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.tomato

nothing added to commit but untracked files present (use "git add" to track)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add main.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   main.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   learning.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.tomato


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "modifird main.py for even check"
[master 47dcbc2] modifird main.py for even check
 1 file changed, 3 insertions(+)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   index.js
        modified:   learning.txt
        new file:   main.tomato


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "added js file and appended learnings"
[master ef481f9] added js file and appended learnings
 3 files changed, 2 insertions(+)
 create mode 100644 index.js
 create mode 100644 main.tomato

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log   
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
ef481f9 (HEAD -> master) added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
ef481f9 (HEAD -> master) added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --Gurupatil0003
fatal: unrecognized argument: --Gurupatil0003

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --author=Mounesh Gouda
fatal: ambiguous argument 'Gouda': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --author=Gurupatil0003
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --author=Mounesh
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --grep="learning"
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline        
ef481f9 (HEAD -> master) added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --since=2025-05-13

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --since=2024-05-13
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>



```second one reminder

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   index.js
        modified:   learning.txt
        new file:   main.tomato


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "added js file and appended learnings"
[master ef481f9] added js file and appended learnings
 3 files changed, 2 insertions(+)
 create mode 100644 index.js
 create mode 100644 main.tomato

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log   
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
ef481f9 (HEAD -> master) added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
ef481f9 (HEAD -> master) added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --Gurupatil0003
fatal: unrecognized argument: --Gurupatil0003

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --author=Mounesh Gouda
fatal: ambiguous argument 'Gouda': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --author=Gurupatil0003
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --author=Mounesh
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --grep="learning"
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline        
ef481f9 (HEAD -> master) added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --since=2025-05-13

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --since=2024-05-13
commit ef481f9d4ca493092516971b2e585f32b0399121 (HEAD -> master)
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:55:41 2025 +0530

    added js file and appended learnings

commit 47dcbc2e259cfb1a8bba2f9157fccfa9ec266ce1
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:52:20 2025 +0530

    modifird main.py for even check

commit 1505a68335302a0a02568d58a33ad379abe25baa
Author: Mounesh Gouda <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 10:48:33 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global user.name
Mounesh Gouda

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global user.name "Guru"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global user.name       
Guru

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global user.email      
110026505+Gurupatil0003@users.noreply.github.com

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global core.editor "code --wait"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global list                     
error: key does not contain a section: list

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global --list
user.name=Guru
user.email=110026505+Gurupatil0003@users.noreply.github.com
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
core.editor=code --wait

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.a add

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global --list     
user.name=Guru
user.email=110026505+Gurupatil0003@users.noreply.github.com
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
core.editor=code --wait
alias.a=add

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git c -m "more changes"
git: 'c' is not a git command. See 'git --help'.

The most similar commands are
        clone
        commit
        gc

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "more changes"
[master 67c2dd9] more changes
 1 file changed, 3 insertions(+), 1 deletion(-)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git ci
git: 'ci' is not a git command. See 'git --help'.

The most similar command is
        gui

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git c 
git: 'c' is not a git command. See 'git --help'.

The most similar commands are
        clone
        commit
        gc

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.ls log --oneline --author=Gurupatil0003
usage: git config [<options>]

Config file location
    --[no-]global         use global config file
    --[no-]system         use system config file
    --[no-]local          use repository config file
    --[no-]worktree       use per-worktree config file
    -f, --[no-]file <file>
                          use given config file
    --[no-]blob <blob-id> read config from given blob object

Action
    --[no-]get            get value: name [value-pattern]
    --[no-]get-all        get all values: key [value-pattern]
    --[no-]get-regexp     get values for regexp: name-regex [value-pattern]
    --[no-]get-urlmatch   get value specific for the URL: section[.var] URL
    --[no-]replace-all    replace all matching variables: name value [value-pattern]
    --[no-]add            add a new variable: name value
    --[no-]unset          remove a variable: name [value-pattern]
    --[no-]unset-all      remove all matches: name [value-pattern]
    --[no-]rename-section rename section: old-name new-name
    --[no-]remove-section remove a section: name
    -l, --[no-]list       list all
    --[no-]fixed-value    use string equality when comparing values to 'value-pattern'
    -e, --[no-]edit       open an editor
    --[no-]get-color      find the color configured: slot [default]
    --[no-]get-colorbool  find the color setting: slot [stdout-is-tty]

Type
    -t, --[no-]type <type>
                          value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --bool-or-str         value is --bool or string
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --[no-]null       terminate values with NUL byte
    --[no-]name-only      show variable names only
    --[no-]includes       respect include directives on lookup
    --[no-]show-origin    show origin of config (file, standard input, blob, command line)
    --[no-]show-scope     show scope of config (worktree, local, global, system, command)
    --[no-]default <value>
                          with --get, use default value when missing entry


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.a log --oneline --author=Gurupatil0003 
usage: git config [<options>]

Config file location
    --[no-]global         use global config file
    --[no-]system         use system config file
    --[no-]local          use repository config file
    --[no-]worktree       use per-worktree config file
    -f, --[no-]file <file>
                          use given config file
    --[no-]blob <blob-id> read config from given blob object

Action
    --[no-]get            get value: name [value-pattern]
    --[no-]get-all        get all values: key [value-pattern]
    --[no-]get-regexp     get values for regexp: name-regex [value-pattern]
    --[no-]get-urlmatch   get value specific for the URL: section[.var] URL
    --[no-]replace-all    replace all matching variables: name value [value-pattern]
    --[no-]add            add a new variable: name value
    --[no-]unset          remove a variable: name [value-pattern]
    --[no-]unset-all      remove all matches: name [value-pattern]
    --[no-]rename-section rename section: old-name new-name
    --[no-]remove-section remove a section: name
    -l, --[no-]list       list all
    --[no-]fixed-value    use string equality when comparing values to 'value-pattern'
    -e, --[no-]edit       open an editor
    --[no-]get-color      find the color configured: slot [default]
    --[no-]get-colorbool  find the color setting: slot [stdout-is-tty]

Type
    -t, --[no-]type <type>
                          value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --bool-or-str         value is --bool or string
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --[no-]null       terminate values with NUL byte
    --[no-]name-only      show variable names only
    --[no-]includes       respect include directives on lookup
    --[no-]show-origin    show origin of config (file, standard input, blob, command line)
    --[no-]show-scope     show scope of config (worktree, local, global, system, command)
    --[no-]default <value>
                          with --get, use default value when missing entry


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.ls log --oneline --author=Gurupatil0003
usage: git config [<options>]

Config file location
    --[no-]global         use global config file
    --[no-]system         use system config file
    --[no-]local          use repository config file
    --[no-]worktree       use per-worktree config file
    -f, --[no-]file <file>
                          use given config file
    --[no-]blob <blob-id> read config from given blob object

Action
    --[no-]get            get value: name [value-pattern]
    --[no-]get-all        get all values: key [value-pattern]
    --[no-]get-regexp     get values for regexp: name-regex [value-pattern]
    --[no-]get-urlmatch   get value specific for the URL: section[.var] URL
    --[no-]replace-all    replace all matching variables: name value [value-pattern]
    --[no-]add            add a new variable: name value
    --[no-]unset          remove a variable: name [value-pattern]
    --[no-]unset-all      remove all matches: name [value-pattern]
    --[no-]rename-section rename section: old-name new-name
    --[no-]remove-section remove a section: name
    -l, --[no-]list       list all
    --[no-]fixed-value    use string equality when comparing values to 'value-pattern'
    -e, --[no-]edit       open an editor
    --[no-]get-color      find the color configured: slot [default]
    --[no-]get-colorbool  find the color setting: slot [stdout-is-tty]

Type
    -t, --[no-]type <type>
                          value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --bool-or-str         value is --bool or string
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --[no-]null       terminate values with NUL byte
    --[no-]name-only      show variable names only
    --[no-]includes       respect include directives on lookup
    --[no-]show-origin    show origin of config (file, standard input, blob, command line)
    --[no-]show-scope     show scope of config (worktree, local, global, system, command)
    --[no-]default <value>
                          with --get, use default value when missing entry


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.lm "log --online --grep==modify"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git lm
fatal: unrecognized argument: --online

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.lm "log --oneline --grep==modify"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.ls "log --oneline --author=Gurupatil0003"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.lm "log --oneline --grep==modify"        

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git c
git: 'c' is not a git command. See 'git --help'.

The most similar commands are
        clone
        commit
        gc

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global --list  
user.name=Guru
user.email=110026505+Gurupatil0003@users.noreply.github.com
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
core.editor=code --wait
alias.a=add
alias.lm=log --oneline --grep==modify
alias.ls=log --oneline --author=Gurupatil0003

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git config --global alias.neha "log --oneline"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git neha
67c2dd9 (HEAD -> master) more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
* master

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch --vv
error: unknown option `vv'
usage: git branch [<options>] [-r | -a] [--merged] [--no-merged]
   or: git branch [<options>] [-f] [--recurse-submodules] <branch-name> [<start-point>]
   or: git branch [<options>] [-l] [<pattern>...]
   or: git branch [<options>] [-r] (-d | -D) <branch-name>...
   or: git branch [<options>] (-m | -M) [<old-branch>] <new-branch>
   or: git branch [<options>] (-c | -C) [<old-branch>] <new-branch>
   or: git branch [<options>] [-r | -a] [--points-at]
   or: git branch [<options>] [-r | -a] [--format]

Generic options
    -v, --[no-]verbose    show hash and subject, give twice for upstream branch
    -q, --[no-]quiet      suppress informational messages
    -t, --[no-]track[=(direct|inherit)]
                          set branch tracking configuration
    -u, --[no-]set-upstream-to <upstream>
                          change the upstream info
    --[no-]unset-upstream unset the upstream info
    --[no-]color[=<when>] use colored output
    -r, --remotes         act on remote-tracking branches
    --contains <commit>   print only branches that contain the commit
    --no-contains <commit>
                          print only branches that don't contain the commit
    --[no-]abbrev[=<n>]   use <n> digits to display object names

Specific git-branch actions:
    -a, --all             list both remote-tracking and local branches
    -d, --[no-]delete     delete fully merged branch
    -D                    delete branch (even if not merged)
    -m, --[no-]move       move/rename a branch and its reflog
    -M                    move/rename a branch, even if target exists
    --[no-]omit-empty     do not output a newline after empty formatted refs
    -c, --[no-]copy       copy a branch and its reflog
    -C                    copy a branch, even if target exists
    -l, --[no-]list       list branch names
    --[no-]show-current   show current branch name
    --[no-]create-reflog  create the branch's reflog
    --[no-]edit-description
                          edit the description for the branch
    -f, --[no-]force      force creation, move/rename, deletion
    --merged <commit>     print only branches that are merged
    --no-merged <commit>  print only branches that are not merged
    --[no-]column[=<style>]
                          list branches in columns
    --[no-]sort <key>     field name to sort on
    --[no-]points-at <object>
                          print only branches of the object
    -i, --[no-]ignore-case
                          sorting and filtering are case insensitive
    --[no-]recurse-submodules
                          recurse through submodules
    --[no-]format <format>
                          format to use for the output


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch --vv
error: unknown option `vv'
usage: git branch [<options>] [-r | -a] [--merged] [--no-merged]
   or: git branch [<options>] [-f] [--recurse-submodules] <branch-name> [<start-point>]
   or: git branch [<options>] [-l] [<pattern>...]
   or: git branch [<options>] [-r] (-d | -D) <branch-name>...
   or: git branch [<options>] (-m | -M) [<old-branch>] <new-branch>
   or: git branch [<options>] (-c | -C) [<old-branch>] <new-branch>
   or: git branch [<options>] [-r | -a] [--points-at]
   or: git branch [<options>] [-r | -a] [--format]

Generic options
    -v, --[no-]verbose    show hash and subject, give twice for upstream branch
    -q, --[no-]quiet      suppress informational messages
    -t, --[no-]track[=(direct|inherit)]
                          set branch tracking configuration
    -u, --[no-]set-upstream-to <upstream>
                          change the upstream info
    --[no-]unset-upstream unset the upstream info
    --[no-]color[=<when>] use colored output
    -r, --remotes         act on remote-tracking branches
    --contains <commit>   print only branches that contain the commit
    --no-contains <commit>
                          print only branches that don't contain the commit
    --[no-]abbrev[=<n>]   use <n> digits to display object names

Specific git-branch actions:
    -a, --all             list both remote-tracking and local branches
    -d, --[no-]delete     delete fully merged branch
    -D                    delete branch (even if not merged)
    -m, --[no-]move       move/rename a branch and its reflog
    -M                    move/rename a branch, even if target exists
    --[no-]omit-empty     do not output a newline after empty formatted refs
    -c, --[no-]copy       copy a branch and its reflog
    -C                    copy a branch, even if target exists
    -l, --[no-]list       list branch names
    --[no-]show-current   show current branch name
    --[no-]create-reflog  create the branch's reflog
    --[no-]edit-description
                          edit the description for the branch
    -f, --[no-]force      force creation, move/rename, deletion
    --merged <commit>     print only branches that are merged
    --no-merged <commit>  print only branches that are not merged
    --[no-]column[=<style>]
                          list branches in columns
    --[no-]sort <key>     field name to sort on
    --[no-]points-at <object>
                          print only branches of the object
    -i, --[no-]ignore-case
                          sorting and filtering are case insensitive
    --[no-]recurse-submodules
                          recurse through submodules
    --[no-]format <format>
                          format to use for the output


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch --v 
* master 67c2dd9 more changes

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
67c2dd9 (HEAD -> master) more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch --v   
* master 67c2dd9 more changes

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c trail1
Switched to a new branch 'trail1'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
  master
* trail1

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch -v
  master 67c2dd9 more changes
* trail1 67c2dd9 more changes

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git status
On branch trail1
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py

nothing added to commit but untracked files present (use "git add" to track)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add app.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c9: added app.py"
[trail1 cae2632] c9: added app.py
 1 file changed, 5 insertions(+)
 create mode 100644 app.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
cae2632 (HEAD -> trail1) c9: added app.py
67c2dd9 (master) more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c10: modified py fun"
[trail1 6bc9ec8] c10: modified py fun
 1 file changed, 6 insertions(+), 1 deletion(-)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
6bc9ec8 (HEAD -> trail1) c10: modified py fun
cae2632 c9: added app.py
67c2dd9 (master) more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch -v 
  master 67c2dd9 more changes
* trail1 6bc9ec8 c10: modified py fun

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master 
Switched to branch 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
* master
  trail1

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch trail1
Switched to branch 'trail1'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
Switched to branch 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add demo.log

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c21: added log file"
[master d5ffbd3] c21: added log file
 1 file changed, 1 insertion(+)
 create mode 100644 demo.log

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
* master
  trail1

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch trail1
Switched to branch 'trail1'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch -m "feature1"

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch              
* feature1
  master

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
6bc9ec8 (HEAD -> feature1) c10: modified py fun
cae2632 c9: added app.py
67c2dd9 more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
Switched to branch 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c train2
Switched to a new branch 'train2'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c31:delter"
[train2 1bc30b5] c31:delter
 1 file changed, 1 deletion(-)
 delete mode 100644 demo.log

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
Switched to branch 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add demo.log

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c22:more logs"   
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch -D "trail2"
error: branch 'trail2' not found

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch -D "train2"
Deleted branch train2 (was 1bc30b5).

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
  feature1
* master

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git init            
Reinitialized existing Git repository in C:/Users/LENOVO/Downloads/New folder (2)/.git/

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "print('Hello')" > work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "First commit"
[master 3adb652] First commit
 1 file changed, 1 insertion(+)
 create mode 100644 work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>touch main.py
'touch' is not recognized as an internal or external command,
operable program or batch file.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add main.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "modifird main.py for even check"
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add learnings.txt
fatal: pathspec 'learnings.txt' did not match any files

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "added js file and appended learnings"
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c9: added app.py"
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py

nothing added to commit but untracked files present (use "git add" to track)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add app.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c9: added app.py"
[master 13b7ffa] c9: added app.py
 1 file changed, 2 insertions(+)
 create mode 100644 app.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git checkout -b feature1
fatal: a branch named 'feature1' already exists

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "print('Mounesh')" >> work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "work.py - Print Name"
[master 23bff02] work.py - Print Name
 1 file changed, 1 insertion(+)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "print('Div by 3:', 9 % 3 == 0)" >> work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "modify the work.py to check if a number is divisible by 3"
[master a26e325] modify the work.py to check if a number is divisible by 3
 1 file changed, 1 insertion(+)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "# This checks divisibility" >> work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "Add a comment to the work.py"
[master 4b9cedc] Add a comment to the work.py
 1 file changed, 1 insertion(+)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "Added Git learning" >> learnings.txt

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add learnings.txt

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "modify the learnings.txt"
[master 6611061] modify the learnings.txt
 1 file changed, 1 insertion(+)
 create mode 100644 learnings.txt

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add demo.log

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "added demo.log"
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>rm demo.log
'rm' is not recognized as an internal or external command,
operable program or batch file.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add demo.log

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "delete the demo.log"
On branch master
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git checkout master
Already on 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git merge feature1 -m "c21: added log file"
Auto-merging app.py
CONFLICT (add/add): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git merge feature1 -m "c21: added log file"
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git init
Reinitialized existing Git repository in C:/Users/LENOVO/Downloads/New folder (2)/.git/

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "print('Hello')" > work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c1: Initial commit with work.py"
U       app.py
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>echo "print('main change 1')" > main.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add main.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c2: main branch change 1"
U       app.py
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add main.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c2: main branch change 1"
U       app.py
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c2: master branch change 1" 
U       app.py
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c2: main branch change 1 (resolved merge conflict)"
U       app.py
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
fatal: cannot switch branch while merging
Consider "git merge --quit" or "git worktree add".

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch       
  feature1
* master

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git swithch feature1
git: 'swithch' is not a git command. See 'git --help'.

The most similar command is
        switch

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c new-branch-name
fatal: cannot switch branch while merging
Consider "git merge --quit" or "git worktree add".

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch -D feature1       
Deleted branch feature1 (was 6bc9ec8).

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c master
fatal: a branch named 'master' already exists

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c feature 
fatal: cannot switch branch while merging
Consider "git merge --quit" or "git worktree add".

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c feature
fatal: cannot switch branch while merging
Consider "git merge --quit" or "git worktree add".

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c fea            
fatal: cannot switch branch while merging
Consider "git merge --quit" or "git worktree add".

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git init 
Reinitialized existing Git repository in C:/Users/LENOVO/Downloads/New folder (2)/.git/

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c fea
fatal: cannot switch branch while merging
Consider "git merge --quit" or "git worktree add".

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git merge --quit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c fea
Switched to a new branch 'fea'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log
commit 66110615d1d9c23281c5e79da631aec3875eaf63 (HEAD -> fea, master)
Author: Guru <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 12:25:04 2025 +0530

    modify the learnings.txt

commit 4b9cedc3d6263ce331a97757c9c0cb5f30f277ca
Author: Guru <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 12:24:47 2025 +0530

    Add a comment to the work.py

commit a26e325e3afc4a3286a32371633ece37154b9dc8
Author: Guru <110026505+Gurupatil0003@users.noreply.github.com>
Date:   Tue May 13 12:24:23 2025 +0530


(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log -oneline
fatal: unrecognized argument: -oneline

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add work.py

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m c21:modified work.py"
app.py: needs merge
[fea 3d671a0] c21:modified
 1 file changed, 2 insertions(+), 3 deletions(-)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c modify
Switched to a new branch 'modify'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
  fea
  master
* modify

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c30:modified learning.txt"
[modify a3be74a] c30:modified learning.txt
 2 files changed, 15 insertions(+), 4 deletions(-)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c31: removed log file"
On branch modify
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c fea   
fatal: a branch named 'fea' already exists

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "c22:comment on work.py"
On branch modify
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    learning.txt
        deleted:    learnings.txt

no changes added to commit (use "git add" and/or "git commit -a")

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
D       learning.txt
D       learnings.txt
Switched to branch 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
Already on 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch -c beta-feature
Switched to a new branch 'beta-feature'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "b1"
[beta-feature f76fccd] b1
 1 file changed, 7 insertions(+)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "b2"
On branch beta-feature
nothing to commit, working tree clean

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
f76fccd (HEAD -> beta-feature) b1
5601ac9 (master) Remove temporary learning files
6611061 modify the learnings.txt
4b9cedc Add a comment to the work.py
a26e325 modify the work.py to check if a number is divisible by 3
23bff02 work.py - Print Name
13b7ffa c9: added app.py
3adb652 First commit
d5ffbd3 c21: added log file
67c2dd9 more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git switch master
Switched to branch 'master'

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "added JS"
[master 29af7b4] added JS
 1 file changed, 3 insertions(+), 1 deletion(-)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git branch
  beta-feature
  fea
* master
  modify

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git merge beta-feature
Merge made by the 'ort' strategy.
 index.js | 7 +++++++
 1 file changed, 7 insertions(+)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git add .

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git commit -m "new log"
[master 9f2290c] new log
 1 file changed, 4 insertions(+), 1 deletion(-)

(myenv) C:\Users\LENOVO\Downloads\New folder (2)>git log --oneline
9f2290c (HEAD -> master) new log
65dc52f m1:Merge branch 'beta-feature'
29af7b4 added JS
f76fccd (beta-feature) b1
5601ac9 Remove temporary learning files
6611061 modify the learnings.txt
4b9cedc Add a comment to the work.py
a26e325 modify the work.py to check if a number is divisible by 3
23bff02 work.py - Print Name
13b7ffa c9: added app.py
3adb652 First commit
d5ffbd3 c21: added log file
67c2dd9 more changes
ef481f9 added js file and appended learnings
47dcbc2 modifird main.py for even check
1505a68 First commit
