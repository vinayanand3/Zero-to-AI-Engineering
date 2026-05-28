---
title: "What Is MCP?"
description: "In Season 4, we learned how AI systems move from answering questions to taking action."
order: 49
season: 5
slug: "49-what-is-mcp"
pubDate: "2026-02-18"
---
In Season 4, we learned how AI systems move from answering questions to taking action.

We covered tool calling, agents, memory, guardrails, multi-tool workflows, and agent evaluation.

Now we need to ask a bigger systems question:

How should AI applications connect to all these tools and sources of context?

If every AI app builds its own custom integration system, the ecosystem becomes messy quickly.

Every tool needs a custom connector.

Every app needs custom logic.

Every integration has its own security model.

That does not scale well.

This is where MCP enters the picture.

MCP stands for:

# Model Context Protocol

It is a protocol for connecting AI applications to external tools, data, and reusable prompts in a more standardized way.

---

# The Simple Definition

MCP is a standard protocol that lets AI applications connect to external context and capabilities.

That context may include:

- tools

- files

- databases

- APIs

- documentation

- prompts

- application-specific data

Instead of every AI application inventing its own way to connect to every tool, MCP defines a common pattern.

This makes it easier for AI applications and external systems to work together.

The goal is not to replace LLMs.

The goal is to help LLM-powered applications access the right context and capabilities.

---

# Why MCP Matters

Modern AI applications are becoming more connected.

A coding assistant may need access to:

- files

- terminals

- GitHub

- issue trackers

- documentation

- test results

A business assistant may need access to:

- calendars

- email

- CRM systems

- databases

- internal policies

- analytics dashboards

Without a standard protocol, each connection becomes custom work.

MCP creates a shared way for these systems to expose capabilities to AI applications.

That is why MCP matters for agentic AI.

---

# MCP Is About Context Exchange

The word "context" in MCP is important.

In earlier seasons, we learned that context shapes model behavior.

The model can only use what is available to it.

MCP helps external systems provide that context in a structured way.

For example, a database MCP server might expose:

- a resource containing the database schema

- a tool for querying records

- a prompt for safe database analysis

The AI application can discover and use those capabilities through the protocol.

This makes context exchange more organized.

---

# MCP And Tool Calling

MCP connects directly to tool calling.

In Season 4, we learned that tools let models perform actions.

MCP gives applications a standardized way to discover and call tools provided by servers.

For example:

An MCP server might expose:

get_open_issues(repository)

or:

search_docs(query)

The AI host can discover those tools, understand their input schemas, and make them available to the model.

MCP does not remove the need for guardrails.

It gives a cleaner structure for connecting tools.

---

# MCP Is Not The Model

This is important.

MCP is not an LLM.

It is not a new model architecture.

It is not a prompt trick.

It is a protocol.

It helps AI applications connect to external systems.

The model still generates language.

The application still manages the user experience.

The MCP server exposes capabilities.

The MCP client connects to that server.

The host coordinates everything.

We will break down that architecture in the next few articles.

---

# MCP Is Also Not A Full Agent Framework

MCP does not decide how an agent plans, reasons, remembers, or evaluates work.

Those decisions still belong to the host application and the AI system around it.

MCP focuses on connection.

It defines how external capabilities can be exposed and used.

For example, MCP can help a coding assistant access a filesystem server or GitHub server.

But MCP does not automatically decide when the assistant should edit a file, run tests, or ask for approval.

That is agent design.

This distinction keeps the concept clear.

MCP is infrastructure for context and capability exchange.

It is not the entire AI product.

---

# A Simple Analogy

Think of MCP like a standardized adapter system.

Imagine every device needed a completely different charging cable.

That would be frustrating.

A standard connector makes it easier for devices and chargers to work together.

MCP plays a similar role for AI applications and external capabilities.

It gives a common way for tools, resources, and prompts to be exposed to AI systems.

The standard does not decide what every application does.

It defines how they can connect.

---

# Mini Project

Choose one AI assistant idea.

For example:

- coding assistant

- research assistant

- sales assistant

- personal productivity assistant

List five external systems it might need.

Then label each as:

- tool

- resource

- prompt template

For example, a coding assistant might need:

- file reader: resource

- test runner: tool

- GitHub issue search: tool

- project README: resource

- code review checklist: prompt

This exercise prepares you for MCP's core primitives.

---

# Key Takeaways

- MCP stands for Model Context Protocol.

- MCP helps AI applications connect to external tools, data, and prompts.

- MCP is a protocol, not a model.

- It supports more standardized context exchange.

- MCP matters because AI applications increasingly need many external integrations.

- MCP connects naturally to tool calling, agents, and RAG.

---

# What's Next

Now that we understand MCP at a high level, we need to understand the problem it solves.

Why do AI systems need a standard protocol for tools and context?

That is what we will explore next:

# Why AI Systems Need a Standard Tool Protocol
