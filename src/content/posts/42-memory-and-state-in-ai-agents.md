---
title: "Memory and State in AI Agents"
description: "Agents need to remember what is happening."
order: 42
season: 4
slug: "42-memory-and-state-in-ai-agents"
pubDate: "2026-02-11"
---
Agents need to remember what is happening.

Not necessarily forever.

But they need enough state to work through a task.

If an agent reads a file, runs a tool, receives an error, and then forgets everything, it cannot act intelligently.

That is why memory and state matter.

These words are often used loosely, so we need to define them clearly.

State is information about the current task.

Memory is information preserved beyond the immediate step or conversation.

Both can be useful.

Both can be risky if designed poorly.

---

# What Is State?

State is the working information an agent uses while completing a task.

Examples:

- current goal

- current plan

- completed steps

- tool results

- open questions

- errors encountered

- files changed

- user approvals

State helps the agent know where it is in the workflow.

For example, a coding agent should know which files it inspected and which tests failed.

Without state, it may repeat itself or lose track of progress.

---

# What Is Memory?

Memory usually means information stored for later use.

Examples:

- user preferences

- project conventions

- past decisions

- known facts

- summaries of prior sessions

- learned workflow patterns

Memory can make agents more helpful.

For example, an assistant might remember that you prefer concise summaries.

A coding agent might remember that a project uses a specific testing framework.

But memory must be handled carefully.

Wrong memory can create wrong behavior.

Sensitive memory can create privacy risk.

---

# Context Window vs Memory

In Season 1, we learned about context windows.

Context is what the model can see right now.

Memory is information that may be stored elsewhere and later inserted into context.

This distinction matters.

If something is not in the active context, the model may not use it.

If memory exists but is never retrieved, it does not help.

If too much memory is inserted, it can clutter the prompt.

Memory systems need retrieval and selection.

Useful memory is not just storage.

It is the right information at the right time.

---

# Short-Term State

Short-term state supports the current task.

Example:

Goal:

Fix failing login test.

Short-term state:

- failing test name

- error message

- files inspected

- suspected cause

- attempted fix

- latest test result

This state may not need to live forever.

It is useful while the task is active.

Once the task is done, it may be summarized or discarded.

Short-term state keeps the agent oriented.

---

# Long-Term Memory

Long-term memory persists across tasks or sessions.

Examples:

- user likes Markdown summaries

- project uses pytest

- deployment requires approval

- customer support tone should be formal

Long-term memory can improve personalization and continuity.

But it must be accurate.

If the system remembers something outdated, the agent may behave incorrectly.

For example, a project may switch from one framework to another.

Old memory becomes harmful.

Good memory systems need update and deletion strategies.

---

# Memory Should Be Summarized

Agents do not need to remember everything in full detail.

Often, a summary is more useful than raw history.

For example, instead of storing every message from a long project discussion, the system might store:

- project goal

- decisions made

- unresolved questions

- user preferences

- important constraints

Summaries reduce noise.

They also save context space.

But summaries can lose details, so they should be created carefully.

For important workflows, the system may keep both raw records and summarized memory.

The raw record supports audit and recovery.

The summary supports efficient future context.

---

# Memory Needs Permissions

Not everything should be remembered.

Users should know when important information is stored.

Sensitive information should be protected.

Examples of risky memory:

- passwords

- private customer data

- financial details

- health information

- confidential company information

Agent memory should follow privacy and security rules.

A useful question is:

Would the user expect this information to be saved and reused later?

If not, be careful.

Memory is powerful, but it creates responsibility.

---

# State Should Be Inspectable

For important agents, state should be inspectable.

You should be able to answer:

- what goal is the agent pursuing?

- what has it already done?

- what tool results did it receive?

- what assumptions is it making?

- what will it do next?

This helps with debugging and trust.

If an agent behaves strangely, hidden state makes the problem harder to diagnose.

Visible state makes the system easier to reason about.

---

# Memory Should Have A Purpose

Do not add memory just because it sounds advanced.

Each memory should help the agent perform a future task better.

For example:

Remembering a user's preferred report format may be useful.

Remembering every casual message may not be useful.

Before storing memory, ask:

How will this be used later?

When should it expire?

Can the user change or delete it?

Purposeful memory improves agents.

Uncontrolled memory creates clutter and risk.

---

# Mini Project

Design state for a research agent.

It needs to write a short report.

List what it should track:

- research question

- sources found

- sources rejected

- key facts

- open questions

- draft outline

- final citations

Now decide what should become long-term memory.

Probably not every source.

Maybe only user preferences or reusable research style.

That distinction is the core lesson.

---

# Key Takeaways

- Agents need state to track current task progress.

- Memory stores information for future use.

- Context is what the model sees now.

- Memory only helps if relevant parts are retrieved into context.

- Short-term state supports active workflows.

- Long-term memory can improve continuity but creates privacy and accuracy risks.

- State should be inspectable for debugging and trust.

---

# What's Next

Agents can use tools and remember state.

But we also need to decide how much freedom they should have.

In the next article, we will explore:

# Human Approval and Agent Guardrails
