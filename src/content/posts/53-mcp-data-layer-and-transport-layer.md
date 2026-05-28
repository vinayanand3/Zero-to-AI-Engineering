---
title: "MCP Data Layer and Transport Layer"
description: "So far, we have looked at MCP from the application perspective."
order: 53
season: 5
slug: "53-mcp-data-layer-and-transport-layer"
pubDate: "2026-02-22"
---
So far, we have looked at MCP from the application perspective.

We know there are hosts, clients, and servers.

We know servers can expose tools, resources, and prompts.

Now we need to understand MCP at a slightly deeper systems level.

MCP has two important layers:

- data layer

- transport layer

The data layer defines what messages mean.

The transport layer defines how messages move.

This distinction is useful because protocols often separate message meaning from communication mechanics.

---

# The Simple Mental Model

Imagine sending a package.

The data layer is what is inside the package.

The transport layer is how the package gets delivered.

For MCP:

The data layer defines protocol messages, lifecycle, capabilities, tools, resources, prompts, and notifications.

The transport layer defines how the client and server communicate, such as local process streams or network transport.

Separating these layers makes MCP more flexible.

The same core protocol ideas can work across different communication methods.

---

# The Data Layer

The MCP data layer is based on JSON-RPC.

You do not need to memorize JSON-RPC details as a beginner.

The important idea is that clients and servers exchange structured messages.

These messages can represent:

- initialization

- capability negotiation

- listing tools

- calling tools

- listing resources

- retrieving prompts

- notifications

- progress updates

Structured messages make the interaction predictable.

The client and server both know what kinds of requests and responses exist.

---

# Lifecycle Management

MCP connections have a lifecycle.

A client connects to a server.

They initialize the session.

They negotiate capabilities.

They exchange messages.

Eventually, the connection ends.

Capability negotiation matters because not every server supports every feature.

For example, one server may expose tools.

Another may expose resources.

Another may support tool list change notifications.

The host should understand what each server can do before relying on it.

This makes the system more robust.

---

# Server Features

The data layer includes server features.

These are the capabilities a server can provide to a client.

The most important ones for this season are:

- tools

- resources

- prompts

Servers may also support notifications, progress tracking, and other utility features.

From an AI engineering perspective, server features are how external systems become usable by AI hosts.

They are the structured bridge between the host and the external capability.

---

# Client Features

MCP also includes client features.

This is easy to miss.

Servers do not only provide things to clients.

In some cases, servers may ask clients for certain capabilities.

For example, a server may request sampling from the host's model.

The details can become advanced, but the high-level idea is important:

MCP is not only a one-way tool list.

It defines structured interactions between clients and servers.

That makes richer workflows possible.

---

# The Transport Layer

The transport layer handles communication.

MCP supports different transport mechanisms.

Two important ones are:

- stdio transport

- Streamable HTTP transport

Stdio is useful for local servers.

The host launches a process and communicates through standard input and output.

This can be fast and simple for local tools.

Streamable HTTP is useful for remote servers.

It supports communication over HTTP and can support streaming behavior.

This is better suited for hosted services and remote integrations.

---

# Local vs Remote Thinking

Transport choices affect architecture.

Local servers are useful for:

- filesystem access

- local project tools

- local development environments

- command-line workflows

Remote servers are useful for:

- SaaS integrations

- enterprise APIs

- hosted databases

- monitoring platforms

- shared organizational tools

The protocol allows both patterns.

The right choice depends on the system, security needs, and user experience.

---

# Why This Matters For Beginners

You do not need to implement the protocol from scratch to understand MCP.

SDKs handle many details.

But understanding the layers helps you reason about the system.

If tool discovery fails, is it a data layer issue or a connection issue?

If a remote server cannot authenticate, that is likely transport or authorization related.

If a tool argument is invalid, that is data layer behavior.

Good mental models make debugging easier.

---

# Layers Help Teams Communicate

The layer model also helps teams discuss problems clearly.

If a tool call has the wrong argument, that is not the same kind of problem as a broken network connection.

If a server does not advertise a capability, that is different from the host choosing not to expose it to the model.

Using precise language helps:

- data layer issue

- transport issue

- permission issue

- host behavior issue

- server behavior issue

This kind of clarity matters when AI systems become production systems.

---

# Mini Project

Pick one MCP server idea.

For example:

GitHub server.

Now answer:

- would it be local or remote?

- what transport might make sense?

- what tools would it expose?

- what resources would it expose?

- what capabilities would the client need to discover?

This exercise helps connect layers to practical design.

---

# Key Takeaways

- MCP has a data layer and a transport layer.

- The data layer defines structured protocol messages and meanings.

- The data layer includes lifecycle management, capability negotiation, tools, resources, prompts, and notifications.

- The transport layer defines how clients and servers communicate.

- Stdio transport is common for local servers.

- Streamable HTTP is useful for remote servers.

- Understanding layers helps with architecture and debugging.

---

# What's Next

Now that we understand MCP's layers, we can zoom into one of its most important behaviors:

tool discovery.

Before a model can use tools, the host needs to know what tools exist.

That is what we will explore next:

# How MCP Tool Discovery Works
