# pullagents.io 


```
git agent marketing
git agent senior-dev
git agent <any text>

git agent architect > .claude/architect.md
```


## Installation

```bash
git config --global alias.agent \
'!gagent() { curl -sL pull-agent-production.up.railway.app/api/$@ ;}; gagent'
```
