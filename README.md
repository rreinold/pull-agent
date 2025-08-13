<div align="center">

# 🤖 pullagents.io

[![GitHub stars](https://img.shields.io/github/stars/rreinold/pull-agent?style=for-the-badge)](https://github.com/rreinold/pull-agent/stargazers)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-blue.svg?style=for-the-badge)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/rreinold/pull-agent?style=for-the-badge)](https://github.com/rreinold/pull-agent/issues)
[![GitHub release](https://img.shields.io/github/v/release/rreinold/pull-agent?style=for-the-badge)](https://github.com/rreinold/pull-agent/releases)

**🚀 Search and install specialized AI subagents for Claude Code from your terminal**

*Curated subagent definitions optimized for maximum effectiveness and safety with Claude Code*

🌐 **[Visit pullagent.io](https://pullagent.io)**

![Demo](out2.gif)

</div>

## ✨ Features

- 🔍 **Smart Search**: Match freeform text to specialized AI subagents
- 📦 **Easy Installation**: One-command setup with git aliases
- 🛡️ **Safety First**: Curated definitions optimized for Claude Code
- 🎯 **Role-Specific**: 20+ specialized agents for different use cases
- ⚡ **Fast**: Instant agent deployment to your projects

## 🚀 Quick Start

**Search for an agent:**
```bash
git agent product
git agent <FREEFORM_SEARCH>
```

**Install directly to your project:**
```bash
git agent product > .claude/agents/product.md
```

## 📦 Installation

Set up the git alias to enable `git agent` commands:

```bash
git config --global alias.agent \
'!gagent() { curl -sL "https://pullagent.io/api/$@" ;}; gagent'
```

That's it! Now you can use `git agent <search-term>` from any git repository.

## 🎭 Available Agents

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

## 🔥 Advanced Usage

Can search based on how it can help:

```bash
git agent really-good-at-security
git agent really-good-at-security > .claude/agents/security.md

git agent help-with-pmf
git agent help-with-pmf > .claude/agents/pmf.md
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to:

- Add new subagents
- Report issues  
- Submit improvements
- Follow our guidelines

## 📄 License

This project is licensed under the CC BY-NC 4.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [gitignore.io](https://gitignore.io)
- Built for the [Claude Code](https://claude.ai/code) community
- Thanks to all contributors who help improve AI agent definitions

## 📞 Support

- 🐛 [Report Issues](https://github.com/rreinold/pull-agent/issues)
- 💡 [Request Features](https://github.com/rreinold/pull-agent/issues/new)
- 📖 [Contributing Guide](CONTRIBUTING.md)
- ⭐ Star this repo if you find it useful!

---

<div align="center">

**Made with ❤️ for the Claude Code community**

[![Star this repo](https://img.shields.io/github/stars/rreinold/pull-agent?style=social)](https://github.com/rreinold/pull-agent/stargazers)

</div>