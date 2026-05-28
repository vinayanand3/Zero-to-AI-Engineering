---
title: "What Is a Context Window?"
description: "When you use an LLM, it can remember parts of the conversation."
order: 10
season: 1
slug: "10-what-is-a-context-window"
pubDate: "2026-01-10"
---
When you use an LLM, it can remember parts of the conversation.

You can ask a question.

Then ask a follow-up.

Then refer to something you said earlier.

The model often understands what you mean.

This makes it feel like the model has memory.

But the reality is more specific.

The model is working with a context window.

Understanding context windows is essential for AI engineering because context controls what the model can see at one time.

If the right information is inside the context window, the model can use it.

If the information is outside the context window, the model may not have access to it.

That simple idea explains many strengths and limitations of modern LLMs.

<p class="section-break">. . .</p>

## The Simplest Definition

A context window is the maximum amount of information an LLM can process at once.

That information may include:

- your prompt

- previous messages

- system instructions

- documents

- code

- tool results

- generated output

The context window is usually measured in tokens.

Not words.

Not pages.

Tokens.

This connects directly to what we learned earlier.

LLMs process token sequences, so their limits are token limits.

<p class="section-break">. . .</p>

## The Whiteboard Analogy

Imagine solving a problem on a whiteboard.

Everything written on the whiteboard is visible to you.

You can refer to it, connect ideas, and use it while solving the problem.

But the whiteboard has limited space.

If it fills up, you either erase something, summarize it, or move to a bigger board.

An LLM context window works similarly.

The model can use what is currently on its whiteboard.

But it does not automatically have infinite access to everything ever said or written.

The context window is the working space.

<p class="section-break">. . .</p>

## Context Is Not The Same As Memory

This is one of the most important beginner distinctions.

If you tell a model your name earlier in a conversation, it may use your name later.

That does not necessarily mean the model permanently learned your name.

It may simply be that your name is still in the context window.

Temporary context feels like memory.

But it is not the same as updating the model's weights or storing a long-term memory record.

In real AI applications, engineers often build separate memory systems using databases, files, retrieval systems, or user profiles.

The model itself works with the context it receives at inference time.

<p class="section-break">. . .</p>

## Why Context Windows Matter

Context windows affect what AI systems can do.

A small context window may work well for:

- short questions

- simple summaries

- quick code explanations

- small conversations

A larger context window enables:

- analyzing long documents

- working across large code files

- comparing multiple sources

- maintaining longer conversations

- processing complex instructions

But bigger context is not automatically better in every situation.

Large context can increase cost.

It can slow down responses.

It can include irrelevant information.

And if the prompt is messy, the model may focus on the wrong details.

AI engineering is not just about adding more context.

It is about adding the right context.

<p class="section-break">. . .</p>

## What Happens When Context Gets Too Long?

When a conversation or input exceeds the context window, the system has to handle it somehow.

Possible strategies include:

- rejecting the request

- cutting off older messages

- summarizing previous content

- retrieving only relevant parts

- asking the user to shorten the input

Different products handle this differently.

This is why long chats sometimes seem to forget earlier details.

The earlier information may no longer be available in the active context.

The model cannot use information it cannot see.

That sentence is worth remembering.

<p class="section-break">. . .</p>

## Context Windows And RAG

Later in this series, we will study RAG, which stands for Retrieval-Augmented Generation.

The basic idea is simple:

Instead of stuffing everything into the prompt, retrieve the most relevant pieces of information and place those pieces into the context window.

For example, if you have 10,000 company documents, you usually do not send all of them to the model.

You search for the most relevant sections.

Then you provide those sections as context.

The LLM uses that retrieved context to answer.

This is one of the main reasons context windows matter so much.

They create the boundary for what information can be used at one time.

<p class="section-break">. . .</p>

## Context Windows And Coding

Coding assistants also depend heavily on context.

If the model can see:

- the current file

- related files

- error messages

- function definitions

- project conventions

it can produce much better code suggestions.

If it only sees a small snippet, it may miss important details.

This is why AI coding tools spend so much effort deciding what code to include in context.

The quality of the output depends heavily on the quality of the context.

Poor context leads to poor suggestions.

Relevant context leads to much better assistance.

<p class="section-break">. . .</p>

## Visual Explanation

Think of the LLM as sitting inside a room.

The context window is everything placed on the table in front of it.

If a document is on the table, the model can use it.

If an instruction is on the table, the model can follow it.

If a code file is on the table, the model can reason about it.

But if something is outside the room, the model does not automatically know it.

AI engineers design systems that decide what gets placed on the table.

That is a huge part of building useful AI applications.

<p class="section-break">. . .</p>

## Mini Project

Try this experiment with any chatbot.

Start a conversation and tell it three details:

- your favorite programming language

- a project idea

- a constraint for the project

Then ask a few follow-up questions that refer to those details.

The model will likely use them well.

Now imagine the conversation becomes hundreds of pages long.

Ask yourself:

Which details should stay in context?

Which should be summarized?

Which should be stored elsewhere?

That is the beginning of context engineering.

<p class="section-break">. . .</p>

## Key Takeaways

- A context window is the amount of information a model can process at once.

- Context windows are measured in tokens.

- Context is not the same as permanent memory.

- The model can only use information available in the active context.

- Larger context helps, but it can increase cost and complexity.

- RAG systems use retrieval to place relevant information into context.

- Good AI applications manage context carefully.

<p class="section-break">. . .</p>

## What's Next

Now we understand that LLMs generate likely tokens using the context available to them.

But this raises an important problem.

What happens when the model generates something that sounds correct, but is actually wrong?

That problem is called hallucination.

In the next article, we will explore:

## Why AI Hallucinates
