git setup
==========

ssh-keygen
copy public key to git ssh ui
in the ui we can see the url, copy the url 

cd to c:\pk
//the below command will create a folder called src and checks out the code to it 
git clone git@github.com:githubuserpk/gcp.git src


created README.md file with some content in c:\pk\src


c:\pk\src>git status
now we can see the changed riles in red color as it is a untracked file (ie new file)


//stage the file to local repository 
git add README.md

now, README.md is shown in green, it is staged locally

git commit -m "message here"

git push origin master
now changes are reflected in github remote master


git remote -v 
shows nick names for all git access
output: 
origin  git@github.com:githubuserpk/gcp.git (fetch)
origin  git@github.com:githubuserpk/gcp.git (push)

Branching:  create a new branch
===========
git checkout -b fb_gcpdev

updated README.md file 
git add README.md
git commit -m "added message here"
git push origin <branch_name>, actual command is given below:
git push origin fb_gcpdev

if you checkout master, you will see previous version of the file

merge:
=====
git checkout fb_gcpdev
git push origin fb_gcpdev








