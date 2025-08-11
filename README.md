# pullagents.io 


```
git agent marketing
git agent senior-dev
git agent <any text>

git agent architect > .claude/architect.md
```


## Installation

git config --global alias.agent \
'!ga() { curl -sL pull-agent-production.up.railway.app/api/$@ ;}; ga'
```
#!/bin/bash

git config --global alias.agent \
'!ga() { curl -sL pull-agent-production.up.railway.app/api/$@ ;}; ga'
