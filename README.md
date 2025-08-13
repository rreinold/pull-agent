# pullagents.io

Ability to search and install subagents into Claude Code from terminal. Subagents definitions are refined to be most effective and safe for use with Claude Code.

![](out2.gif)

## Usage

Matches freeform input text with a subagent role:

Preview:
```
git agent product
git agent <FREEFORM_SEARCH>
```

## Install Agent into Project:

```
git agent product > .claude/agents/product.md
```

## Installation

```bash
git config --global alias.agent \
'!gagent() { curl -sL "https://pullagent.io/api/$@" ;}; gagent'
```

## List of agents:

```
subagents
├── business-development.md
├── ceo.md
├── cfo.md
├── content-marketing-manager.md
├── coo.md
├── cto.md
├── customer-success-manager.md
├── data-analyst.md
├── devops-engineer.md
├── frontend-engineer.md
├── growth-marketing-manager.md
├── hr-manager.md
├── legal-compliance.md
├── product-manager.md
├── product-marketing-manager.md
├── qa-engineer.md
├── security-engineer.md
├── senior-backend-engineer.md
├── seo-sem-specialist.md
└── ux-designer.md
```

## Contributing

Please fork and PR for new subagents!

## Advanced

Can search based on how it can help:

```
git agent really-good-at-security
git agent really-good-at-security > .claude/agents/security.md

git agent help-with-pmf
git agent help-with-pmf > .claude/agents/pmf.md
```