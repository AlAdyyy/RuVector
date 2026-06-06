# Subagent Orchestration Prompts

Source: `crates/rvAgent/rvagent-subagents/src/prompts.rs`

## Task Tool Description
Used in the tool registry to describe the `task` tool.

```markdown
Launch a new agent that has access to the same tools as you. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries, use the task tool to perform the search for you.

When you use the task tool, you should provide a detailed natural language description of what you want the agent to do, including any relevant context from the conversation so far.

The available subagent types are:
{available_agents}

IMPORTANT: Each invocation of the task tool creates a NEW agent with no memory of previous invocations. Do not reference previous task results — instead, include all necessary context in the description.

You should use subagent_type to select the most appropriate agent for the task. If unsure, use "general-purpose".
```

## Task System Prompt
Appended to the parent agent's system message when subagent middleware is active.

```markdown
You have access to a `task` tool that lets you spawn subagents. Use it when:
- You need to search for files or content and want thorough results
- The task can be parallelized (e.g., searching multiple directories)
- You want to delegate a self-contained subtask
- The subtask requires a different set of tools or capabilities

Each subagent runs in isolation: it cannot see your conversation history, todos, or structured responses. You must pass all relevant context in the task description.

When spawning multiple tasks, you can invoke the task tool multiple times in a single response — they will execute concurrently.
```
