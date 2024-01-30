#!/bin/bash

# modificaquei para ir pra home

# git fetch --set-upstream origin backup

# # cd data/cs-relatorios-repasses
cd /home/cnmfs/cs-relatorios-repasses
git fetch --set-upstream origin master
git add /home/cnmfs/cs-relatorios-repasses/relatorios
git commit -m "add relatorios automaticamente"
git push --set-upstream origin master --force 
git push
cd /home/cnmfs//ciadosorriso-pyspark  


# #git remote add origin https://github.com/camillanapoles/cs-relatorios-repasses

# #git push --set-upstream origin master 
# git push --set-upstream origin master --force 

# cd ../ciadosorriso-pyspark

# Configure local branch to track a remote branch.
# git branch -u cs-relatorios-repasses/master


# Change remote URL
# The syntax is: git remote set-url REMOTE-ID REMOTE-URL
# git add /home/cnmfs/cs-relatorios-repasses/relatorios
# git commit -m "add relatorios automaticamente"
# git remote set-url --add --push all https://github.com/camillanapoles/cs-relatorios-repasses
# git push --set-upstream cs-relatorios-repasses master
