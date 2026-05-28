---
title: "The Anatomy of a Good Prompt"
description: "In the previous article, we learned why clear instructions matter."
order: 15
season: 2
slug: "15-the-anatomy-of-a-good-prompt"
pubDate: "2026-01-15"
---
In the previous article, we learned why clear instructions matter.

Now we need to go one level deeper.

What does a good prompt actually contain?

Beginners often think a prompt is just one sentence.

Sometimes it can be.

But for serious AI work, prompts often need structure.

A good prompt is like a well-written task brief.

It gives the model enough information to understand the job, perform it well, and return the result in a useful format.

In this article, we will break a good prompt into reusable parts.

Once you understand these parts, you can design prompts for many different use cases.

<p class="section-break">. . .</p>

## The Core Parts Of A Good Prompt

A strong prompt often includes:

- task

- context

- input data

- constraints

- examples

- output format

- quality criteria

You do not need every part every time.

For simple tasks, one or two parts may be enough.

For complex tasks, including more structure can dramatically improve results.

The goal is not to make prompts longer.

The goal is to make them clearer.

<p class="section-break">. . .</p>

## 1. Task

The task tells the model what to do.

This is the action verb.

Examples:

- summarize this article

- rewrite this email

- classify these support tickets

- extract action items

- generate test cases

- compare these options

- explain this concept

Weak task:

Help me with this.

Strong task:

Rewrite this paragraph to make it clearer for a beginner audience.

The task should be direct.

If the model does not know the job, everything else becomes harder.

<p class="section-break">. . .</p>

## 2. Context

Context explains the situation.

It gives background that affects the answer.

For example:

I am writing a Medium article for beginners learning AI engineering.

That context changes the output.

The model will likely use simpler explanations, more analogies, and less jargon.

Without context, it may write something too academic or too generic.

Useful context can include:

- audience

- goal

- business situation

- technical environment

- project constraints

- prior decisions

- user intent

Context helps the model understand why the task matters.

<p class="section-break">. . .</p>

## 3. Input Data

Input data is the material the model should work with.

Examples:

- an article to summarize

- meeting notes to extract from

- code to debug

- a list of customer comments

- a product description

- a resume

- a transcript

If the task depends on specific information, include that information clearly.

A common mistake is asking the model to summarize, analyze, or transform something without providing the actual content.

Bad prompt:

Summarize the meeting.

Better prompt:

Summarize the meeting transcript below. Focus on decisions, action items, owners, and deadlines.

Then include the transcript.

<p class="section-break">. . .</p>

## 4. Constraints

Constraints define boundaries.

They tell the model what to include, avoid, or limit.

Examples:

- keep it under 300 words

- avoid technical jargon

- do not add facts not present in the source

- use Python only

- do not use external libraries

- assume the reader is a beginner

- include tradeoffs

Constraints are useful because models are flexible.

If you do not define boundaries, the model may choose boundaries for you.

Sometimes that works.

Sometimes it creates the wrong output.

<p class="section-break">. . .</p>

## 5. Examples

Examples show the model what good output looks like.

This is especially useful when the task has a pattern.

For example, if you want customer feedback classified into categories, provide a few examples:

Input: "The app keeps crashing when I upload a file."

Output: Bug report

Input: "Can you add dark mode?"

Output: Feature request

Examples reduce ambiguity.

They show the model the style, structure, and mapping you want.

Later in this season, we will cover zero-shot, one-shot, and few-shot prompting in more detail.

<p class="section-break">. . .</p>

## 6. Output Format

Output format tells the model how to return the answer.

Examples:

- use five bullet points

- return JSON

- create a table

- write three paragraphs

- output only code

- include headings

- include a final recommendation

Format matters because the same answer can be useful or annoying depending on how it is presented.

If you need the result to be copied into another tool, format becomes even more important.

For production systems, structured outputs are often essential.

<p class="section-break">. . .</p>

## 7. Quality Criteria

Quality criteria tell the model how success will be judged.

Examples:

- prioritize accuracy over creativity

- make the explanation beginner-friendly

- include edge cases

- list assumptions

- identify risks

- keep the tone calm and professional

This is different from output format.

Output format controls shape.

Quality criteria controls judgment.

For example:

Return a checklist is a format instruction.

Focus on security risks is a quality criterion.

Both can matter.

<p class="section-break">. . .</p>

## A Complete Example

Here is a structured prompt:

You are helping me write a beginner-friendly AI engineering article.

Task: Explain embeddings.

Audience: Software developers who are new to machine learning.

Context: This is part of a progressive Medium series. Previous articles covered tokens and transformers.

Constraints: Avoid equations, avoid hype, and use practical examples.

Output format: Use sections with headings, a simple analogy, real-world examples, key takeaways, and a transition to RAG.

Quality criteria: The article should feel practical, clear, and approachable.

This is much stronger than:

Write about embeddings.

The model now has a clear assignment.

<p class="section-break">. . .</p>

## Mini Project

Create a prompt template with these fields:

- Task

- Audience

- Context

- Input

- Constraints

- Output format

- Quality criteria

Then use that template for a real task.

For example:

- summarizing an article

- rewriting an email

- planning a project

- generating test cases

You will quickly see which fields matter most for different tasks.

<p class="section-break">. . .</p>

## Key Takeaways

- A good prompt is a structured task brief.

- The main parts are task, context, input, constraints, examples, output format, and quality criteria.

- Not every prompt needs every part.

- More structure is useful when the task is complex or high-stakes.

- Output format controls shape.

- Quality criteria controls what "good" means.

- Strong prompts reduce guesswork.

<p class="section-break">. . .</p>

## What's Next

One of the most powerful prompt ingredients is examples.

Examples can teach the model what pattern to follow.

In the next article, we will explore:

## Zero-Shot, One-Shot, and Few-Shot Prompting
