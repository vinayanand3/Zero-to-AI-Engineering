---
title: "Mini Project: Build Your First AI Workflow With Prompts"
description: "So far in Season 2, we have learned the building blocks of prompt engineering."
order: 23
season: 2
slug: "23-mini-project-build-your-first-ai-workflow-with-prompts"
pubDate: "2026-01-23"
---
So far in Season 2, we have learned the building blocks of prompt engineering.

We covered:

- clear instructions

- prompt structure

- examples

- context

- reasoning prompts

- code prompts

- structured outputs

- common mistakes

- reusable prompt libraries

Now it is time to combine these ideas into a workflow.

A workflow is more than one prompt.

It is a sequence of steps that transforms input into a useful result.

This is where prompt engineering starts becoming system design.

---

# The Project

For this mini project, we will build a simple AI workflow:

Turn messy notes into a structured article plan.

This is a practical workflow because many people start with messy thoughts.

They may have:

- bullet notes

- rough ideas

- copied quotes

- topic fragments

- examples

- unclear ordering

The AI workflow will help turn that mess into something organized.

The final output will be:

- article title

- target audience

- main thesis

- outline

- examples

- key takeaways

- next-step transition

---

# Why Use A Workflow Instead Of One Prompt?

You could ask:

Turn these notes into an article.

Sometimes that works.

But for better quality, we can break the work into stages.

Stages make the process easier to review.

They also reduce the chance that the model skips important thinking.

Our workflow will have four steps:

1. Clean and group the notes.

2. Identify the core message.

3. Create the article outline.

4. Generate a final writing brief.

Each step has a clear job.

---

# Step 1: Clean And Group Notes

Prompt:

You are helping organize messy article notes.

Task: Clean and group the notes below into related themes.

Rules:

- Do not write the article yet.

- Do not add new ideas.

- Preserve useful details.

- Remove obvious duplicates.

Output format:

- Theme name

- Related notes

- Possible examples

Notes:

[PASTE NOTES HERE]

This step turns chaos into grouped material.

The instruction "Do not write the article yet" matters.

It keeps the model focused on organization.

---

# Step 2: Identify The Core Message

Now take the grouped notes and ask:

Based on these grouped notes, identify the core message of the article.

Return:

- one-sentence thesis

- target audience

- reader problem

- why this topic matters

- what the reader should understand by the end

Do not create the outline yet.

This step forces clarity.

Before writing an article, you need to know what it is really about.

The model helps extract that from the notes.

---

# Step 3: Create The Outline

Now create the outline:

Create a beginner-friendly article outline using the thesis and grouped notes below.

Audience:

[AUDIENCE]

Thesis:

[THESIS]

Grouped notes:

[GROUPED NOTES]

Output format:

- Strong hook

- Why this topic matters

- Beginner-friendly intuition

- Visual explanation

- Technical breakdown

- Real-world examples

- Mini project

- Key takeaways

- Transition to next article

This matches the structure of the AI engineering series.

The prompt gives the model both content and format.

---

# Step 4: Create The Final Writing Brief

The final step is not to write the full article yet.

It is to create a writing brief.

Prompt:

Create a writing brief from this outline.

The brief should include:

- final title

- target audience

- article goal

- tone

- required sections

- examples to include

- concepts to avoid

- key takeaways

- transition sentence to the next article

Keep it practical and beginner-friendly.

This brief becomes a reusable input for drafting.

It is cleaner than the original messy notes.

---

# What This Workflow Teaches

This workflow teaches several prompt engineering principles.

First, break large tasks into stages.

Second, give each prompt one clear job.

Third, use structured outputs.

Fourth, carry useful context from one step to the next.

Fifth, review intermediate results before moving on.

That is how prompt engineering becomes reliable.

You are not hoping one giant prompt does everything perfectly.

You are designing a process.

---

# Where This Becomes AI Engineering

This workflow could eventually become a real application.

Imagine a simple tool where a user pastes messy notes.

The system runs:

- note grouping

- thesis extraction

- outline generation

- writing brief creation

Each step could be a separate model call.

Each output could be reviewed or edited by the user.

That is an AI workflow.

The prompt is not just text.

It is part of a system.

This is the bridge from prompt engineering to AI application design.

---

# How to Improve the Workflow

You can improve this workflow by adding:

- examples of good outlines

- a saved writing style guide

- length constraints

- source material

- review criteria

- quality checks

- human approval between steps

You can also add a final review prompt:

Review this writing brief for clarity, missing context, weak transitions, and beginner accessibility. Suggest improvements before drafting.

That turns the workflow into a feedback loop.

Good AI systems often include feedback loops.

---

# Mini Project

Run this workflow yourself.

Use any messy notes you have.

They could be about:

- an article

- a project idea

- a meeting

- a course plan

- a product feature

Move through all four steps.

Do not skip straight to drafting.

Review each intermediate output.

Then ask:

Did the workflow produce a better result than one big prompt?

For most complex tasks, the answer will be yes.

---

# Key Takeaways

- A prompt workflow is a sequence of prompts that produce a useful result.

- Large tasks often work better when broken into stages.

- Each step should have one clear job.

- Structured outputs make intermediate results easier to review.

- Context can be carried from one step to the next.

- Prompt engineering becomes more powerful when treated as system design.

- Practical AI products often use workflows like this behind the scenes.

---

# What's Next

We have now completed the practical core of Season 2.

We started with prompt basics and ended with a reusable AI workflow.

Now we need to step back and connect the bigger idea:

Prompt engineering is not just writing better prompts.

It is the beginning of designing AI systems.

That is what we will explore in the Season 2 wrap-up:

# Prompt Engineering as System Design
