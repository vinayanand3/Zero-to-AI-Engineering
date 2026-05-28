---
title: "What Is Prompt Engineering Really?"
description: "In Season 1, we built the foundation."
order: 13
season: 2
slug: "13-what-is-prompt-engineering-really"
pubDate: "2026-01-13"
---
In Season 1, we built the foundation.

We learned that LLMs generate text one token at a time.

We learned that they rely on tokens, embeddings, transformers, context windows, and training.

We also learned something extremely important:

LLMs do not automatically know what you want.

They respond based on the information and instructions you give them.

That brings us to Season 2.

## Prompt engineering

Unfortunately, prompt engineering is often explained in a shallow way.

People describe it like a collection of magic phrases:

- "Act as an expert"

- "Think step by step"

- "Make it better"

- "Use best practices"

But real prompt engineering is not about memorizing phrases.

It is about designing clear communication between humans and AI systems.

That is the mental model we will use in this season.

<p class="section-break">. . .</p>

## The Simplest Definition

Prompt engineering is the practice of giving an AI model the right instructions, context, constraints, and output expectations so it can produce a useful result.

A prompt is not just a question.

A prompt can include:

- the task

- background context

- input data

- examples

- constraints

- tone

- audience

- output format

- success criteria

When you combine these well, the model performs much better.

When you leave them out, the model has to guess.

And when the model guesses, output quality becomes unpredictable.

<p class="section-break">. . .</p>

## Prompting Is Communication Design

Imagine asking a human teammate:

Write something about AI.

That is vague.

What kind of writing?

For whom?

How long?

What should it cover?

Should it be technical or beginner-friendly?

Should it include examples?

Should it avoid hype?

Now compare that with:

Write a 1,200-word beginner-friendly article explaining what prompt engineering is. The audience is software developers new to AI. Use practical examples, avoid hype, and end with three key takeaways.

That request is much clearer.

The second prompt gives direction.

The model does not have to invent the assignment.

It can focus on completing it.

<p class="section-break">. . .</p>

## Why Prompt Engineering Matters

Prompt engineering matters because LLMs are general-purpose systems.

The same model can:

- summarize documents

- write code

- generate test cases

- explain concepts

- classify feedback

- extract structured data

- brainstorm product ideas

- draft emails

- compare options

That flexibility is powerful.

But it also creates ambiguity.

If the model can do many things, you need to clearly specify which thing you want.

Prompt engineering is how you narrow the model's behavior toward a useful outcome.

<p class="section-break">. . .</p>

## Prompting Is Not Just For Chatbots

Beginners often think prompting only means typing into ChatGPT.

But prompt engineering appears throughout AI products.

A customer support bot uses prompts.

A coding assistant uses prompts.

A document summarizer uses prompts.

A RAG system uses prompts.

An AI agent uses prompts.

A tool-calling workflow uses prompts.

In production AI systems, prompts are often hidden from the user.

The user clicks a button.

Behind the scenes, the application builds a prompt with instructions, context, retrieved documents, user input, and output rules.

That hidden prompt shapes the behavior of the system.

So prompt engineering is not just a user skill.

It is an application design skill.

<p class="section-break">. . .</p>

## The Model Needs A Job Description

One useful way to think about a prompt is as a temporary job description.

You are telling the model:

- what role to play

- what task to perform

- what information to use

- what rules to follow

- what output to produce

If the job description is unclear, the result will be inconsistent.

If the job description is overloaded, the model may miss something.

If the job description conflicts with itself, the model may choose one instruction and ignore another.

Good prompts reduce ambiguity.

They make the task easier for the model to complete correctly.

<p class="section-break">. . .</p>

## Prompt Engineering And Context

Prompt engineering connects directly to context windows.

In Season 1, we learned that the model can only use what is inside the active context.

That means the prompt is part of the model's working space.

If you include useful context, the model can use it.

If you leave out important context, the model may fill in gaps.

For example:

Bad prompt:

Summarize this for my team.

Better prompt:

Summarize the following meeting notes for a software engineering team. Focus on decisions, owners, deadlines, and unresolved questions. Use bullets.

The second prompt gives the model a clearer target.

It also tells the model what matters.

That is prompt engineering.

<p class="section-break">. . .</p>

## Prompt Engineering Is Not A Replacement For Verification

Good prompts improve output quality.

But they do not guarantee correctness.

Remember hallucinations from Season 1.

LLMs can still produce plausible mistakes.

Prompt engineering helps reduce risk by giving clearer instructions and better context.

But AI engineers still need:

- tests

- citations

- source documents

- validation

- human review

- tool checks

Prompting is one layer of reliability.

It is not the entire reliability system.

This is especially important for code, legal, medical, financial, and safety-critical tasks.

<p class="section-break">. . .</p>

## A Simple Prompt Improvement Example

Weak prompt:

Explain transformers.

Better prompt:

Explain transformers to a beginner who understands basic programming but not machine learning. Use an analogy first, then explain attention, tokens, and why transformers scale well. Avoid equations. End with five key takeaways.

Notice what changed.

The better prompt includes:

- audience

- knowledge level

- topic scope

- structure

- constraints

- output ending

The model has less guessing to do.

The result will usually be more useful.

<p class="section-break">. . .</p>

## Mini Project

Take one vague prompt you have used before.

For example:

Help me write an article.

Now rewrite it with:

- the audience

- the topic

- the desired structure

- the tone

- the length

- what to avoid

- what the final output should look like

Compare the two prompts.

The improved version should feel less like a wish and more like a clear assignment.

That is the beginning of prompt engineering.

<p class="section-break">. . .</p>

## Key Takeaways

- Prompt engineering is structured communication with AI systems.

- A prompt can include instructions, context, examples, constraints, and output format.

- Good prompts reduce ambiguity.

- Prompting matters in chatbots, coding tools, RAG systems, agents, and production applications.

- Prompt engineering improves reliability, but it does not replace verification.

- The goal is not magic phrasing. The goal is clear task design.

<p class="section-break">. . .</p>

## What's Next

Now that we understand what prompt engineering really is, we need to study the most basic ingredient:

clear instructions.

Most bad AI outputs begin with unclear requests.

So in the next article, we will explore:

## Why Clear Instructions Matter in AI Prompts
