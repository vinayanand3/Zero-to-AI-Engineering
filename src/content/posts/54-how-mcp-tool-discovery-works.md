---
title: "How MCP Tool Discovery Works"
description: "In Season 4, we learned that tools let AI systems take action."
order: 54
season: 5
slug: "54-how-mcp-tool-discovery-works"
pubDate: "2026-02-23"
---
In Season 4, we learned that tools let AI systems take action.

But there is an important question:

How does an AI application know which tools are available?

In a small custom app, a developer might hard-code a tool list.

But MCP is designed for a broader ecosystem.

Hosts can connect to different servers.

Servers can expose different tools.

Those tools may change over time.

That means the client needs a way to discover tools.

Tool discovery is one of MCP's most important ideas.

<p class="section-break">. . .</p>

## Why Discovery Matters

Imagine an AI host connected to three MCP servers:

- filesystem server

- GitHub server

- database server

Each server exposes different tools.

The filesystem server might expose file read and search tools.

The GitHub server might expose issue and pull request tools.

The database server might expose query tools.

The host needs to know what is available before the model can use anything.

Discovery solves this.

The client asks the server:

What tools do you provide?

The server returns a structured list.

<p class="section-break">. . .</p>

## The Basic Flow

A simplified MCP tool discovery flow looks like this:

1. Host connects to server through an MCP client.

2. Client initializes the session.

3. Client learns server capabilities.

4. Client asks for available tools.

5. Server returns tool definitions.

6. Host registers tools for model use.

7. Model can request tool calls when appropriate.

This is cleaner than manually writing every tool into every AI application.

The server describes what it offers.

The host decides how to use it.

<p class="section-break">. . .</p>

## What A Tool Definition Includes

A tool definition usually includes:

- name

- description

- input schema

The name tells the system what the tool is called.

The description helps the model understand when to use it.

The input schema defines the expected arguments.

For example:

Tool:

search_issues

Description:

Search repository issues by text query and status.

Input schema:

- repository: string

- query: string

- status: open or closed

This structure helps the model choose and call the tool correctly.

<p class="section-break">. . .</p>

## Descriptions Matter

Tool descriptions are not decoration.

They guide model behavior.

A vague description can cause poor tool selection.

Bad description:

Search stuff.

Better description:

Search open and closed GitHub issues in a repository using a text query.

The better description tells the model:

- what system it searches

- what input it needs

- what result to expect

Good descriptions improve tool selection.

Poor descriptions create confusion.

<p class="section-break">. . .</p>

## Input Schemas Matter

Input schemas help validate tool calls.

They define required and optional arguments.

They also define types.

For example:

- order_id must be a string

- limit must be a number

- status must be one of a known set

This helps both the model and the application.

The model sees what arguments to produce.

The application can validate before execution.

Schemas are one of the ways tool calling becomes safer and more structured.

<p class="section-break">. . .</p>

## Dynamic Tool Lists

In some systems, available tools can change.

A server may add a tool.

A tool may become temporarily unavailable.

Permissions may change.

MCP supports patterns where servers can notify clients that tool lists changed.

Then the client can request the updated list.

This matters for dynamic environments.

AI applications should not assume the tool universe is always fixed.

Capabilities can change.

The host needs a way to stay current.

<p class="section-break">. . .</p>

## Tool Discovery Does Not Mean Tool Permission

Just because a tool exists does not mean every user should use it.

Discovery tells the host what the server can expose.

Permissions decide what the user or model should access.

For example:

A database server may expose an admin query tool.

That does not mean every user should have access to it.

The host and server still need permission checks.

Discovery is about capability awareness.

Authorization is about allowed use.

Do not confuse them.

<p class="section-break">. . .</p>

## Discovery Helps Tool Management

As the number of tools grows, hosts need better ways to manage them.

An AI application may not want to show every discovered tool to the model at once.

Too many tools can confuse the model and increase prompt size.

A host may filter tools by:

- current task

- user permissions

- active workspace

- selected server

- risk level

Tool discovery gives the host raw capability information.

Tool management decides what should actually be available in a given conversation.

This distinction becomes important as agent systems scale.

<p class="section-break">. . .</p>

## Mini Project

Design tool definitions for a task manager MCP server.

Create three tools:

- list_tasks

- create_task

- mark_task_done

For each tool, write:

- name

- description

- required arguments

- optional arguments

- example user request

This exercise shows how tool discovery depends on good tool definitions.

<p class="section-break">. . .</p>

## Key Takeaways

- Tool discovery lets MCP clients learn what tools a server provides.

- Discovery usually happens after connection and initialization.

- Tool definitions include names, descriptions, and input schemas.

- Descriptions help the model choose tools.

- Schemas help structure and validate tool arguments.

- Tool lists may change over time.

- Discovery does not replace permissions or approval.

<p class="section-break">. . .</p>

## What's Next

Tools are one MCP primitive.

But AI systems also need context that is not necessarily executable.

That brings us to resources.

In the next article, we will explore:

## Resources in MCP: Giving AI Systems Context
