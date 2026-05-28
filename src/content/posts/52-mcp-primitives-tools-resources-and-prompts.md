---
title: "MCP Primitives: Tools, Resources, and Prompts"
description: "MCP servers expose capabilities through primitives."
order: 52
season: 5
slug: "52-mcp-primitives-tools-resources-and-prompts"
pubDate: "2026-02-21"
---
MCP servers expose capabilities through primitives.

A primitive is a basic building block that the protocol understands.

The three most important server-side primitives are:

- tools

- resources

- prompts

These map directly to ideas we have already studied.

Tools connect to Season 4.

Resources connect to context and RAG from Season 3.

Prompts connect to prompt engineering from Season 2.

MCP brings these ideas together into one protocol model.

<p class="section-break">. . .</p>

## Tools

Tools are executable functions.

They allow AI applications to take actions or request computed results.

Examples:

- search a database

- create a calendar event

- send a message

- run a test

- query an API

- inspect an issue tracker

Tools usually have input schemas.

That means the client can understand what arguments the tool expects.

For example:

create_task(title, due_date)

The model can decide when the tool is useful, but the application and server execute it.

<p class="section-break">. . .</p>

## Resources

Resources provide contextual data.

They are usually read-oriented.

Examples:

- file contents

- database schemas

- documentation pages

- API responses

- project metadata

- knowledge base articles

Resources help AI applications understand the environment.

For example, a database server might expose the database schema as a resource.

The model can use that schema as context before deciding how to query.

Resources are important because not all context should be a tool call.

Sometimes the model just needs to read information.

<p class="section-break">. . .</p>

## Prompts

Prompts are reusable interaction templates.

They help structure how the model should work with a server or domain.

Examples:

- summarize meeting notes

- plan a vacation

- review a pull request

- query a database safely

- create an incident report

In MCP, a server can expose prompts that clients can discover and use.

This is similar to a prompt library, but connected to a server.

The prompt may be designed specifically for the tools and resources that server provides.

That makes prompts more reusable and discoverable.

<p class="section-break">. . .</p>

## Who Controls Each Primitive?

A useful mental model:

Tools are often model-invoked.

The model decides when a tool may help.

Resources are often application-selected.

The host decides what context should be included.

Prompts are often user-selected.

The user may choose a workflow template.

This is not a strict rule for every implementation, but it is a useful starting point.

Different primitives have different interaction patterns.

Understanding that helps you design better AI systems.

<p class="section-break">. . .</p>

## Example: Database MCP Server

Imagine an MCP server for a company database.

It might expose:

Tool:

run_readonly_query(sql)

Resource:

database_schema

Prompt:

analyze_sales_data

The resource gives context.

The prompt gives workflow guidance.

The tool executes a controlled action.

Together, they create a safer and more useful interface than a single vague database tool.

This is the power of primitives.

<p class="section-break">. . .</p>

## Example: Travel Planning Server

A travel server might expose:

Tools:

- search_flights

- book_hotel

- update_calendar

Resources:

- travel preferences

- calendar availability

- loyalty program information

Prompts:

- plan weekend trip

- summarize travel options

The model can combine tools and resources to help the user plan.

The prompt can guide the full workflow.

MCP gives these pieces a standard shape.

<p class="section-break">. . .</p>

## Why Primitives Matter

Without primitives, every integration is just custom behavior.

With primitives, clients can understand what a server offers.

They can list tools.

They can retrieve resources.

They can use prompt templates.

This makes integrations more discoverable.

It also makes agent systems more modular.

Instead of hard-coding everything into one AI application, capabilities can live in servers.

The host can connect to those servers and use what they expose.

<p class="section-break">. . .</p>

## Choosing The Right Primitive

A common design mistake is turning everything into a tool.

That is not always the right choice.

If the model only needs to read information, use a resource.

If the model needs to perform an action, use a tool.

If the user needs a reusable workflow, use a prompt.

For example:

Database schema should usually be a resource.

Run query should be a tool.

Analyze sales trends should probably be a prompt that uses the schema and query tool.

Choosing the right primitive makes the server easier to understand and safer to use.

Good MCP design starts with clear responsibility.

<p class="section-break">. . .</p>

## Mini Project

Design an MCP server for a personal notes system.

List:

Tools:

- search_notes

- create_note

- update_note

Resources:

- note folders

- selected note contents

- tag list

Prompts:

- summarize notes

- create study guide

- extract action items

This exercise shows how tools, resources, and prompts work together.

<p class="section-break">. . .</p>

## Key Takeaways

- MCP servers expose capabilities through primitives.

- The core server primitives are tools, resources, and prompts.

- Tools perform actions or computations.

- Resources provide contextual data.

- Prompts provide reusable interaction templates.

- These primitives connect directly to earlier seasons on prompting, RAG, and agents.

- Good MCP servers expose focused primitives that work together.

<p class="section-break">. . .</p>

## What's Next

Now that we understand MCP primitives, we need to look one layer deeper.

How does MCP structure communication?

That brings us to the data layer and transport layer.

In the next article, we will explore:

## MCP Data Layer and Transport Layer
