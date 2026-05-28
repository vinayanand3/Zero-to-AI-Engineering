---
title: "Resources in MCP: Giving AI Systems Context"
description: "Tools allow AI systems to act."
order: 55
season: 5
slug: "55-resources-in-mcp-giving-ai-systems-context"
pubDate: "2026-02-24"
---
Tools allow AI systems to act.

Resources allow AI systems to read.

In MCP, resources are a standard way for servers to expose contextual data to clients.

This is important because AI systems need context to produce useful answers.

Sometimes that context should come from a tool call.

Sometimes it should come from a readable resource.

Examples include:

- files

- database schemas

- documentation

- API responses

- project metadata

- knowledge base articles

Resources help AI applications understand the environment around the task.

<p class="section-break">. . .</p>

## The Simple Definition

An MCP resource is a data source exposed by a server for context.

Each resource has a URI.

The URI identifies the resource.

The resource also has a content type, such as text or another MIME type.

For example:

file:///project/README.md

or:

resource://database/schema

The exact URI depends on the server.

The important idea is that resources give clients a standard way to find and load context.

<p class="section-break">. . .</p>

## Resources vs Tools

Resources and tools are different.

A resource provides data.

A tool performs an action.

Example resource:

database schema

Example tool:

run database query

Example resource:

project README

Example tool:

create GitHub issue

This distinction matters because read-oriented context is often safer and more passive than executable actions.

Not everything should be a tool.

Sometimes the model just needs context.

<p class="section-break">. . .</p>

## How Resources Help AI Applications

Resources can help AI applications:

- understand project structure

- read selected documents

- inspect schemas

- access reference material

- ground answers in source content

- prepare better tool calls

For example, before asking a model to generate a database query, the host may include the database schema as a resource.

That schema helps the model understand available tables and fields.

Without it, the model may invent column names.

Resources reduce guessing by providing context.

<p class="section-break">. . .</p>

## Resources And RAG

Resources connect naturally to RAG.

In Season 3, we learned that RAG systems retrieve relevant context and place it in the prompt.

MCP resources can provide some of that context.

For example:

A documentation server might expose pages as resources.

A file server might expose project files as resources.

A database server might expose schema resources.

The host application decides how to select, retrieve, and insert these resources into the model context.

MCP defines a way to expose them.

The host decides how to use them.

<p class="section-break">. . .</p>

## Application-Driven Context

Resources are often application-driven.

That means the host application may decide what resources to show or include.

For example, an IDE might let the user select files.

A document assistant might show a resource picker.

A coding agent might automatically include files related to the current task.

The protocol does not force one user interface.

Different hosts can expose resources differently.

The key idea is that resources are available through a standard protocol shape.

<p class="section-break">. . .</p>

## Resource Metadata Matters

Useful resources need metadata.

Metadata may include:

- URI

- name

- description

- MIME type

- last updated time

- source system

- access permissions

Metadata helps the host decide how to present and use resources.

It also helps users trust context.

For example, a stale policy document should not be treated the same as a policy updated yesterday.

Context quality matters.

<p class="section-break">. . .</p>

## Resource Security

Resources can contain sensitive information.

That means access control matters.

A server should not expose resources to users who should not see them.

A host should be careful about inserting sensitive resources into model context.

For example:

If a user asks about a public support article, the model probably does not need private customer records.

As with tools, resources should follow least privilege.

Give the model the context it needs.

Do not give it everything.

<p class="section-break">. . .</p>

## Resources Should Be Useful Alone

A good resource should be understandable when included in model context.

If a resource contains only a fragment without labels, the model may misinterpret it.

For example:

Bad resource content:

30 days

Better resource content:

Refund window: 30 days from purchase date.

The second version carries meaning.

This connects back to chunking from Season 3.

Resources should preserve enough structure, labels, and metadata to remain useful when read outside their original location.

Context quality affects answer quality.

<p class="section-break">. . .</p>

## Mini Project

Design resources for a coding assistant MCP server.

Possible resources:

- current file

- project README

- package manifest

- test output

- API documentation

- coding standards

For each resource, write:

- URI idea

- description

- when it should be included

- whether it may contain sensitive information

This helps you think about resources as context design.

<p class="section-break">. . .</p>

## Key Takeaways

- MCP resources expose contextual data to AI applications.

- Resources are usually read-oriented.

- Resources are different from tools because they provide data rather than actions.

- Resources can support RAG, coding assistants, database work, and document understanding.

- Hosts decide how resources are selected and included.

- Resource metadata and permissions matter.

- Good resource design reduces model guessing.

<p class="section-break">. . .</p>

## What's Next

MCP servers can expose tools and resources.

They can also expose reusable prompts.

That brings us back to prompt engineering, but now in a protocol context.

In the next article, we will explore:

## Prompts in MCP: Reusable AI Workflows
