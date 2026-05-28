---
title: "Season 5 Wrap-Up: The Mental Model of MCP"
description: "We have reached the end of Season 5."
order: 60
season: 5
slug: "60-season-5-wrap-up-the-mental-model-of-mcp"
pubDate: "2026-03-01"
---
We have reached the end of Season 5.

This season built on everything that came before it.

Season 1 taught us how modern AI systems work.

Season 2 taught us prompt engineering.

Season 3 taught us retrieval and RAG.

Season 4 taught us tool calling and agents.

Season 5 taught us MCP.

MCP matters because AI systems are becoming more connected.

They need tools.

They need resources.

They need prompts.

They need secure ways to interact with external systems.

MCP gives these interactions a more standard protocol shape.

---

# MCP In One Sentence

MCP is a protocol that helps AI applications connect to external context and capabilities through servers that expose tools, resources, and prompts.

That sentence contains the whole season.

AI applications need external context.

External systems expose capabilities.

MCP defines how they can connect.

It does not replace the model.

It does not replace application design.

It creates an interoperability layer.

That is the mental model.

---

# Why MCP Exists

MCP exists because custom integrations do not scale well.

If every AI app builds its own custom connector for every tool, the ecosystem becomes fragmented.

Developers repeat work.

Security patterns vary.

Tool discovery becomes messy.

Context sharing becomes inconsistent.

MCP helps by creating a shared protocol for connecting AI hosts to capability servers.

This encourages reusable servers and cleaner boundaries.

It is an infrastructure idea for the agentic AI era.

---

# Hosts, Clients, And Servers

The architecture has three main roles.

The host is the AI application users interact with.

The client is the protocol component that connects to a server.

The server exposes capabilities.

A host may create multiple clients.

Each client connects to one server.

Each server may expose tools, resources, and prompts.

This architecture creates modularity.

The host manages experience.

The client manages connection.

The server owns integration logic.

---

# Tools, Resources, And Prompts

The core MCP primitives are:

- tools

- resources

- prompts

Tools perform actions or computations.

Resources provide contextual data.

Prompts provide reusable interaction templates.

These primitives connect directly to earlier seasons.

Tools connect to agents.

Resources connect to RAG and context.

Prompts connect to prompt engineering.

MCP does not introduce a completely separate world.

It organizes ideas we have already learned.

---

# Data Layer And Transport Layer

MCP has a data layer and a transport layer.

The data layer defines structured protocol messages.

It includes lifecycle management, capability negotiation, tools, resources, prompts, and notifications.

The transport layer defines how messages move.

For example:

Stdio can support local process communication.

Streamable HTTP can support remote servers.

This separation helps MCP work across different environments.

Local development tools and remote enterprise services can both fit into the model.

---

# Discovery Before Use

One important MCP idea is discovery.

Before a host uses a server's tools, it can discover what tools exist.

Tool definitions include names, descriptions, and input schemas.

This lets the host understand capabilities before exposing them to the model.

Discovery makes AI systems more dynamic.

It also makes tool ecosystems more scalable.

But discovery is not the same as permission.

A discovered tool still needs authorization, validation, and sometimes user approval.

---

# Resources Provide Context

Resources help AI systems read useful information.

They may include:

- files

- schemas

- docs

- records

- API responses

- project metadata

Resources are important because AI quality depends heavily on context.

But resources must be selected carefully.

Too little context leads to weak answers.

Too much context creates noise and risk.

Sensitive resources require access control.

MCP exposes resources.

Hosts decide how to use them.

---

# Prompts Package Workflows

MCP prompts turn reusable prompt workflows into server-exposed primitives.

A server can provide prompts tailored to its domain.

For example:

- review a pull request

- summarize meetings

- inspect an incident

- query a database safely

This connects MCP to Season 2's prompt library idea.

Prompts are no longer only personal snippets.

They can become discoverable workflow templates exposed by servers.

That makes AI workflows easier to reuse.

---

# Security Is Central

MCP can expose powerful capabilities.

That means security is central.

Important principles include:

- least privilege

- scoped server access

- tool argument validation

- user approval for risky actions

- resource permissions

- prompt injection awareness

- audit logs

MCP does not automatically make a system safe.

It gives structure.

Engineers must still design permissions, guardrails, and monitoring.

The more capable the system, the more important the safeguards.

---

# MCP And Future AI Systems

MCP points toward a future where AI systems connect to many capabilities through reusable servers.

Coding agents may connect to files, GitHub, tests, and documentation.

Research agents may connect to papers, notes, citation tools, and search.

Enterprise assistants may connect to internal systems through permissioned servers.

This future requires:

- good tool design

- good context design

- secure access

- evaluation

- human oversight

MCP is part of the foundation.

It is not the whole building.

---

# The Season 5 Mental Model

Here is the complete mental model:

AI applications need external context and capabilities.

MCP provides a protocol for connecting to them.

Hosts coordinate the user-facing AI experience.

Clients connect hosts to servers.

Servers expose tools, resources, and prompts.

Tools enable action.

Resources provide context.

Prompts package workflows.

The data layer defines message meaning.

The transport layer moves messages.

Security and permissions keep the system bounded.

That is MCP from an AI engineering perspective.

---

# Mini Project

Design a complete MCP-based assistant on paper.

Choose one:

- coding assistant

- research assistant

- customer support assistant

- operations assistant

Define:

- host

- MCP servers

- tools

- resources

- prompts

- permissions

- approval points

- evaluation tests

This exercise connects the whole season.

It also prepares you for production AI engineering later in the series.

---

# Key Takeaways

- MCP standardizes how AI applications connect to tools, resources, and prompts.

- MCP uses a host-client-server architecture.

- Tools enable action.

- Resources provide context.

- Prompts provide reusable workflows.

- MCP supports local and remote server patterns.

- Tool discovery helps hosts understand available capabilities.

- Security, permissions, and evaluation are essential.

- MCP is an interoperability layer for connected AI systems.

---

# What's Next

Now that we understand prompting, retrieval, agents, tools, and MCP, we are ready for another major area:

# Fine-Tuning and Optimization

In Season 6, we will study how models can be adapted and optimized.

We will cover:

- fine-tuning

- instruction tuning

- LoRA

- model evaluation

- quantization

- latency and cost optimization

- when not to fine-tune

The next article will begin with:

# What Is Fine-Tuning?

