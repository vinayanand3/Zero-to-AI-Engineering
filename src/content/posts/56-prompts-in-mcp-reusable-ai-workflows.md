---
title: "Prompts in MCP: Reusable AI Workflows"
description: "In Season 2, we learned that good prompts are reusable assets."
order: 56
season: 5
slug: "56-prompts-in-mcp-reusable-ai-workflows"
pubDate: "2026-02-25"
---
In Season 2, we learned that good prompts are reusable assets.

A strong prompt can encode a workflow.

It can define the task, context, constraints, output format, and quality criteria.

MCP brings this idea into a protocol setting.

MCP servers can expose prompts.

These prompts are reusable templates that clients can discover and use.

This matters because a server often knows the best way to work with its own tools and resources.

Instead of leaving every user to invent prompts from scratch, the server can provide useful prompt workflows.

<p class="section-break">. . .</p>

## The Simple Definition

An MCP prompt is a reusable instruction template exposed by a server.

It can help structure model interactions.

Examples:

- summarize my meetings

- inspect an incident

- review a pull request

- query this database safely

- plan a vacation

- generate a support response

The prompt may include arguments.

For example:

review_pull_request(pr_number)

The client can retrieve the prompt and fill in the argument.

The model then receives a structured workflow.

<p class="section-break">. . .</p>

## Prompts vs Tools

Prompts and tools are different.

A tool performs an action.

A prompt guides the model.

Example tool:

search_flights(origin, destination, date)

Example prompt:

plan_a_trip(destination, dates, budget)

The prompt may instruct the model to use several tools and resources.

It may define the process:

Check calendar availability, search flights, compare hotels, then summarize options.

The prompt organizes the workflow.

The tools execute parts of it.

<p class="section-break">. . .</p>

## Prompts vs Resources

Resources provide data.

Prompts provide instructions.

Example resource:

meeting transcript

Example prompt:

summarize_meeting(transcript)

The resource is the content.

The prompt tells the model what to do with that content.

Good AI systems often need both.

The model needs information and instructions.

MCP lets servers expose both through standard primitives.

<p class="section-break">. . .</p>

## Why Server-Provided Prompts Matter

The server often knows its domain.

A database server may know how queries should be written safely.

A calendar server may know what information is needed to schedule meetings.

A support server may know the required format for ticket summaries.

Server-provided prompts can package that domain knowledge.

They help users and models interact with the server more effectively.

This is similar to a prompt library, but attached to the system that provides the relevant capabilities.

<p class="section-break">. . .</p>

## User-Controlled Workflows

Prompts are often user-controlled.

That means the user may explicitly select a prompt.

For example, a host might show prompts as commands:

- summarize meeting

- draft response

- review code

- plan trip

The user chooses the workflow.

The host retrieves the prompt.

The model follows the prompt using available context and tools.

This makes workflows discoverable.

Users do not need to remember every possible prompt.

They can choose from templates.

<p class="section-break">. . .</p>

## Embedded Resources

Prompts can also include or reference resources.

For example, a prompt for reviewing API usage might include server-managed documentation as context.

This is powerful because the prompt can bring together:

- instructions

- resource context

- tool guidance

The result is a more complete workflow.

Instead of a generic prompt, the server can provide a workflow tailored to its own data and tools.

That is where MCP prompts become especially useful.

<p class="section-break">. . .</p>

## Prompt Security

Prompts can also create risk.

If a prompt includes untrusted content, it may introduce prompt injection issues.

If a prompt references sensitive resources, access control matters.

If a prompt encourages unsafe tool use, the workflow can become risky.

So prompts should be designed and reviewed carefully.

As always:

Prompts guide behavior.

Software enforces boundaries.

MCP prompts are useful, but they still need validation, permissions, and evaluation.

<p class="section-break">. . .</p>

## Prompts Should Match Server Capabilities

An MCP prompt is most useful when it matches what the server can actually provide.

For example, a calendar server can provide a prompt for planning a meeting because it has calendar-related tools and resources.

A database server can provide a prompt for safely analyzing tables because it has schema resources and query tools.

But a prompt that assumes unavailable tools will frustrate users and confuse the model.

Good MCP prompts should be designed around real server capabilities.

They should guide the model toward actions and context the server can support.

This makes prompts practical instead of generic.

<p class="section-break">. . .</p>

## Mini Project

Design three prompts for a project management MCP server.

Possible prompts:

- summarize_project_status

- create_weekly_update

- identify_blockers

For each prompt, define:

- purpose

- required arguments

- resources it should use

- tools it may call

- output format

This exercise connects prompt engineering to MCP design.

<p class="section-break">. . .</p>

## Key Takeaways

- MCP prompts are reusable instruction templates exposed by servers.

- Prompts guide model behavior, while tools perform actions.

- Resources provide data, while prompts tell the model what to do with data.

- Server-provided prompts can package domain-specific workflow knowledge.

- Prompts can make workflows discoverable to users.

- Prompts may include or reference resources.

- Prompt security and validation still matter.

<p class="section-break">. . .</p>

## What's Next

Now that we understand tools, resources, and prompts, we can design a simple MCP server conceptually.

In the next article, we will walk through:

## Building Your First MCP Server Conceptually
