---
title: "What Is an AI Agent?"
description: "The word \"agent\" is used everywhere in AI."
order: 40
season: 4
slug: "40-what-is-an-ai-agent"
pubDate: "2026-02-09"
---
The word "agent" is used everywhere in AI.

Sometimes it means a simple chatbot.

Sometimes it means an automation workflow.

Sometimes it means a system that can use tools, plan steps, and work toward a goal.

Because the term is used loosely, beginners often get confused.

In this series, we will use a practical definition:

> An AI agent is an AI system that can work toward a goal by deciding what steps to take, using tools, and adapting based on results.

That definition is not about hype.

It is about behavior.

An agent is more than a single response.

It is a system that can operate through a loop.

---

# A Chatbot vs An Agent

A basic chatbot responds to messages.

User asks.

Model answers.

That can be useful.

But an agent does more.

An agent may:

- understand a goal

- make a plan

- choose tools

- execute steps

- observe results

- adjust the plan

- continue until the task is done

For example:

Chatbot:

You should email the customer.

Agent:

Drafts the email, asks for confirmation, sends it, logs the result, and updates the ticket.

The difference is action over time.

---

# The Agent Loop

Many agents follow a loop:

1. Receive a goal.

2. Decide the next step.

3. Use a tool or produce output.

4. Observe the result.

5. Decide what to do next.

6. Stop when the goal is complete.

This loop is sometimes called a reason-act-observe loop.

The exact names vary.

The idea is simple:

Think about what to do.

Act.

Observe what happened.

Continue.

This loop is what makes agents different from one-shot prompts.

---

# Agents Need Tools

An agent without tools is limited.

It can plan and explain, but it cannot interact much with the world.

Tools give agents capabilities.

For example, a research agent may need:

- search tool

- webpage reader

- note writer

- citation checker

A coding agent may need:

- file reader

- file editor

- test runner

- terminal

- version control

The model decides what to do.

The tools make it possible.

---

# Agents Need State

Agents also need state.

State means information about what has happened so far.

For example:

- current goal

- completed steps

- tool results

- errors

- user preferences

- intermediate notes

Without state, the agent forgets its progress.

State can live in the conversation context, memory, files, databases, or workflow systems.

Good agent design requires deciding what state should be preserved and where it should live.

---

# Agents Need Stopping Conditions

An agent should know when to stop.

This sounds obvious, but it is important.

Without stopping conditions, an agent may loop, overwork the task, or keep calling tools unnecessarily.

Stopping conditions may include:

- task completed

- user approval required

- tool error cannot be resolved

- maximum steps reached

- confidence too low

- missing required information

Agents need boundaries.

Useful autonomy is not unlimited autonomy.

---

# Agents Need A Clear Goal

Agents perform better when the goal is explicit.

Weak goal:

Help with my project.

Better goal:

Review the project plan, identify missing risks, and produce a revised checklist without changing the timeline.

The clearer goal tells the agent:

- what to inspect

- what output to produce

- what not to change

Vague goals create wandering behavior.

The agent may take unnecessary steps or solve the wrong problem.

Good agent design begins by defining the goal, success criteria, and boundaries.

If those are unclear, autonomy becomes guesswork.

---

# Real Agent Examples

Practical agents include:

- coding agents that edit files and run tests

- research agents that gather sources and summarize findings

- support agents that look up policies and draft responses

- operations agents that inspect dashboards and create incident reports

- sales agents that update CRM records

- personal assistants that manage tasks and calendars

These systems vary in complexity.

Some are simple workflows.

Some are more autonomous.

The key is that they work through steps, tools, and feedback.

---

# Agents Are Not Magic Workers

Agents can be useful, but they are not magic.

They can make mistakes.

They can choose the wrong tool.

They can misunderstand goals.

They can loop.

They can act too early.

They can produce plausible but wrong progress reports.

That is why agent design needs:

- permissions

- confirmations

- logs

- evaluations

- step limits

- human review

The more power an agent has, the more guardrails it needs.

---

# Autonomy Exists On A Spectrum

Agents do not need to be fully autonomous to be useful.

Some agents only suggest next steps.

Some prepare actions but wait for approval.

Some can complete low-risk tasks automatically.

Some can run longer workflows with limited supervision.

This spectrum matters.

For a beginner AI engineer, the goal is not to build the most autonomous system possible.

The goal is to choose the right level of autonomy for the risk and value of the task.

Practical agent design is about controlled autonomy.

---

# Mini Project

Choose a task:

Plan a weekend trip.

Now define an agent for it.

What is the goal?

What tools does it need?

What state should it remember?

When should it ask for confirmation?

When should it stop?

You will see that agent design is not just prompting.

It is workflow design.

---

# Key Takeaways

- An AI agent works toward a goal through steps, tools, and feedback.

- Agents are different from basic chatbots because they can act over time.

- Many agents follow a decide, act, observe, continue loop.

- Agents need tools, state, and stopping conditions.

- More autonomy requires stronger guardrails.

- Agent design is workflow design, not just prompt writing.

---

# What's Next

Now that we know what an agent is, we need to understand its most important internal pattern:

the agent loop.

In the next article, we will explore:

# The Agent Loop: Plan, Act, Observe
