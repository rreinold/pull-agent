# 🤝 Contributing to pullagents.io

We welcome contributions! Here's how you can help make pullagents.io better for everyone.

## 🚀 How to Contribute

### 1. Fork & Clone
```bash
git fork https://github.com/rreinold/pull-agent
git clone https://github.com/YOUR_USERNAME/pull-agent
cd pull-agent
```

### 2. Create a New Subagent
- Add your agent definition to the `subagents/` directory
- Follow the naming convention: `kebab-case.md`
- Use the template below as a starting point

### 3. Test Your Agent
- Test thoroughly with Claude Code
- Ensure the agent works as expected
- Verify safety and effectiveness

### 4. Submit a Pull Request
- Create a descriptive PR title
- Include details about your agent's purpose
- Reference any related issues

## 📝 Subagent Template

Create your new agent file in `subagents/your-agent-name.md`:

```markdown
# Your Agent Name

## Role
Brief description of the agent's primary role and purpose.

## Capabilities
- List key capabilities
- What this agent excels at
- Specific use cases

## Tools
List of tools this agent has access to (if applicable):
- Tool 1
- Tool 2

## Example Usage
Brief example of when and how to use this agent.

## Guidelines
Any specific guidelines or best practices for this agent.
```

## ✅ Guidelines for New Agents

### Naming Convention
- Use `kebab-case` for filenames (e.g., `product-manager.md`)
- Keep names descriptive but concise
- Avoid special characters or spaces

### Content Requirements
- **Clear Role Definition**: What does this agent do?
- **Specific Capabilities**: What can it help with?
- **Use Cases**: When should someone use this agent?
- **Safety Considerations**: Any important limitations or warnings

### Quality Standards
- Test with Claude Code before submitting
- Ensure the agent provides value beyond generic assistance
- Write clear, concise descriptions
- Follow markdown formatting standards

## 🔍 Review Process

1. **Automated Checks**: Basic formatting and structure validation
2. **Manual Review**: Community and maintainer review
3. **Testing**: Verification that the agent works as intended
4. **Approval**: Merge once all checks pass

## 🐛 Reporting Issues

Found a bug or have a suggestion? Please:

1. Check existing issues first
2. Use the appropriate issue template
3. Provide clear reproduction steps
4. Include relevant context

## 💡 Feature Requests

Have an idea for a new feature or improvement?

1. Open a feature request issue
2. Describe the problem you're trying to solve
3. Suggest potential solutions
4. Discuss with the community

## 📞 Getting Help

- 💬 Join discussions in the Issues section
- 📖 Check the README for basic usage
- 🔍 Search existing issues and PRs

## 🙏 Recognition

All contributors will be recognized in our documentation and releases. Thank you for helping make pullagents.io better!

---

By contributing, you agree that your contributions will be licensed under the same license as the project (CC BY-NC 4.0 License).