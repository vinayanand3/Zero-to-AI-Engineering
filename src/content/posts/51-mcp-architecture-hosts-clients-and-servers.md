---
title: "MCP Architecture: Hosts, Clients, and Servers"
description: "MCP becomes much easier to understand once you know its main participants."
order: 51
season: 5
slug: "51-mcp-architecture-hosts-clients-and-servers"
pubDate: "2026-02-20"
---
MCP becomes much easier to understand once you know its main participants.

The architecture has three key roles:

- host

- client

- server

These words sound simple, but the distinction matters.

The host is the AI application the user interacts with.

The client is the protocol connection managed by the host.

The server exposes tools, resources, and prompts.

Together, they create the structure that lets AI applications connect to external capabilities.

<p class="section-break">. . .</p>

## The Big Picture

MCP follows a client-server architecture, coordinated by a host application.

Think of it like this:

User uses an AI application.

That AI application is the MCP host.

The host creates one MCP client for each MCP server it connects to.

Each MCP server provides capabilities.

For example:

- filesystem server

- GitHub server

- database server

- calendar server

- monitoring server

The host coordinates the overall experience.

The clients maintain server connections.

The servers expose useful context and actions.

<p class="section-break">. . .</p>

## What Is An MCP Host?

The host is the application that users interact with.

Examples might include:

- an IDE

- a desktop AI assistant

- a coding agent

- a chat application

- an enterprise AI platform

The host manages the user experience.

It decides which MCP servers to connect to.

It coordinates multiple clients.

It decides what context and tools should be made available to the model.

The host is the container for the AI experience.

<p class="section-break">. . .</p>

## What Is An MCP Client?

An MCP client is a component created by the host to communicate with one MCP server.

If the host connects to three servers, it usually has three clients.

One client talks to the filesystem server.

Another client talks to the GitHub server.

Another client talks to the database server.

This separation matters because each connection has its own lifecycle, capabilities, and permissions.

The user may only see one AI application.

But behind the scenes, the host may manage multiple MCP clients.

<p class="section-break">. . .</p>

## What Is An MCP Server?

An MCP server is a program that exposes capabilities to AI applications.

It can expose:

- tools

- resources

- prompts

For example, a database MCP server might expose:

- a resource for database schema

- a tool for running approved queries

- a prompt for safe query analysis

The server owns the integration logic.

It knows how to talk to the external system.

The AI host does not need to know every detail of that system.

It uses the MCP server through the protocol.

<p class="section-break">. . .</p>

## Local And Remote Servers

MCP servers can be local or remote.

A local server may run on the same machine as the host.

For example:

- local filesystem server

- local Git server

- local project tools

A remote server may run somewhere else and communicate over the network.

For example:

- hosted monitoring platform

- cloud database connector

- SaaS integration

The protocol supports different transport mechanisms for these situations.

We will discuss transports later in the season.

<p class="section-break">. . .</p>

## Why This Architecture Matters

The host-client-server structure creates clear boundaries.

The host owns the AI experience.

The client owns the protocol connection.

The server owns the capabilities it exposes.

This separation is useful because it allows systems to evolve independently.

A server can add a new tool.

A host can connect to multiple servers.

A client can negotiate capabilities with a server.

The model can use capabilities discovered through the host.

This architecture supports reuse and modularity.

<p class="section-break">. . .</p>

## One Host, Many Servers

The most important pattern is that one host can connect to many servers.

A coding host might connect to:

- filesystem server

- Git server

- package documentation server

- issue tracker server

- test runner server

Each server stays focused.

The host brings their capabilities together into one user experience.

This avoids building one giant integration layer inside the host.

It also lets teams add or remove capabilities by changing server connections.

That modularity is one of MCP's main architectural benefits.

<p class="section-break">. . .</p>

## Example: Coding Assistant

Imagine an AI coding assistant inside an IDE.

The IDE is the host.

It connects to:

- filesystem MCP server

- GitHub MCP server

- test runner MCP server

- documentation MCP server

The IDE creates a client for each server.

The filesystem server exposes files as resources and file operations as tools.

The GitHub server exposes issue and pull request tools.

The documentation server exposes searchable docs.

The user experiences one assistant.

Behind the scenes, MCP organizes multiple connections.

<p class="section-break">. . .</p>

## Mini Project

Design an MCP architecture for a research assistant.

Identify:

- host

- servers

- client connections

- tools

- resources

- prompts

For example:

Host:

Research assistant app

Servers:

- paper search server

- notes server

- citation server

- file server

This exercise helps make the architecture concrete.

<p class="section-break">. . .</p>

## Key Takeaways

- MCP architecture has hosts, clients, and servers.

- The host is the AI application users interact with.

- The host creates clients to connect to servers.

- Each client maintains a connection to one server.

- Servers expose tools, resources, and prompts.

- Servers can be local or remote.

- The architecture creates clear boundaries between user experience, protocol connection, and external capabilities.

<p class="section-break">. . .</p>

## What's Next

Now that we understand the participants in MCP, we need to understand what servers actually expose.

MCP servers provide three major primitives:

tools, resources, and prompts.

That is what we will explore next:

## MCP Primitives: Tools, Resources, and Prompts
