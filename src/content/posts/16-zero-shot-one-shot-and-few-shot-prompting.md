---
title: "Zero-Shot, One-Shot, and Few-Shot Prompting"
description: "In the previous article, we broke down the anatomy of a good prompt."
order: 16
season: 2
slug: "16-zero-shot-one-shot-and-few-shot-prompting"
pubDate: "2026-01-16"
---
In the previous article, we broke down the anatomy of a good prompt.

One of the most useful pieces was examples.

Examples help the model understand the pattern you want.

That brings us to three common terms:

- zero-shot prompting

- one-shot prompting

- few-shot prompting

These terms sound academic at first.

But the idea is simple.

They describe how many examples you give the model before asking it to do the task.

No examples.

One example.

A few examples.

That is the basic idea.

---

# Zero-Shot Prompting

Zero-shot prompting means asking the model to do a task without giving examples.

Example:

Classify this customer message as Bug, Feature Request, Billing, or Other:

"The app crashes every time I upload a PDF."

The model has to understand the task and choose a category without seeing examples first.

This works well when:

- the task is simple

- the categories are obvious

- the model likely understands the domain

- the output format is clear

For many everyday tasks, zero-shot prompting is enough.

You do not always need examples.

---

# When Zero-Shot Works Well

Zero-shot prompting works well for common tasks like:

- summarization

- translation

- basic classification

- rewriting

- explanation

- brainstorming

- simple code generation

For example:

Summarize the following article in five bullets for a non-technical audience.

That prompt may work perfectly without examples.

The task is familiar.

The output is clear.

The audience is defined.

The model has enough information to proceed.

---

# When Zero-Shot Breaks Down

Zero-shot prompting becomes weaker when the task has a specific pattern the model may not infer.

For example:

Rewrite this feedback into our internal product insight format.

What is your internal format?

The model does not know unless you show it.

Another example:

Classify this support ticket using our custom severity levels.

If your severity levels are specific to your company, the model needs examples or detailed definitions.

Zero-shot prompting fails when the model has to guess your hidden rules.

---

# One-Shot Prompting

One-shot prompting means giving one example before asking the model to perform the task.

Example:

Classify customer messages into categories.

Example:

Message: "I was charged twice for my subscription."

Category: Billing

Now classify:

Message: "The app freezes when I click Export."

Category:

The example shows the pattern.

The model sees:

- input format

- output format

- category style

One example can often improve consistency.

---

# Few-Shot Prompting

Few-shot prompting means giving several examples.

Example:

Classify customer messages into Bug, Feature Request, Billing, or Other.

Message: "The app crashes when I upload a PDF."

Category: Bug

Message: "Can you add dark mode?"

Category: Feature Request

Message: "I was charged twice this month."

Category: Billing

Message: "Where can I change my password?"

Category: Other

Now classify:

Message: "The dashboard does not load after login."

Category:

This gives the model a clearer pattern.

It also shows boundaries between categories.

Few-shot prompting is especially useful for classification, extraction, formatting, and style transfer.

---

# Examples Teach The Shape Of The Output

Examples do not just teach content.

They teach shape.

If your examples use short labels, the model will likely use short labels.

If your examples use JSON, the model will likely return JSON.

If your examples include explanations, the model may include explanations.

This is why examples should match the output you actually want.

Do not give messy examples if you want clean output.

Do not include long explanations in examples if you want short answers.

The model learns from the pattern you show.

---

# Choosing Good Examples

Good examples should be:

- representative

- clear

- consistent

- relevant

- not too many

Representative means the examples cover realistic cases.

Clear means the correct answer is not confusing.

Consistent means the same format is used each time.

Relevant means examples match the task you are asking for.

Not too many means you avoid filling the context window with unnecessary examples.

Examples are useful, but they still consume tokens.

---

# When Examples Can Hurt

Examples are powerful, but they can also bias the model in the wrong direction.

If your examples are too narrow, the model may copy that narrow pattern even when the next input is different.

If your examples contain mistakes, the model may repeat those mistakes.

If your examples are inconsistent, the model may become inconsistent too.

For example, imagine a few-shot prompt where one example returns a short category and another returns a full sentence.

The model may not know which style you want.

That is why examples should be treated like training material inside the prompt.

They are not casual decoration.

They define the pattern.

Before using few-shot prompting in a real workflow, check whether the examples represent the range of inputs you expect.

Good examples guide.

Bad examples mislead.

---

# A Practical Before And After

Weak prompt:

Turn this into a task.

Better few-shot prompt:

Convert messy notes into clear tasks.

Example:

Note: "Need to fix login bug before Friday, Alex owns it."

Task: Fix login bug. Owner: Alex. Due: Friday.

Example:

Note: "Marketing wants landing page copy reviewed by Priya next week."

Task: Review landing page copy. Owner: Priya. Due: Next week.

Now convert:

Note: "Data export issue should be checked by Marcus tomorrow."

Task:

The better prompt shows exactly what transformation should happen.

---

# Mini Project

Choose a repeated task you do often.

For example:

- classifying notes

- rewriting emails

- extracting tasks

- creating article outlines

- reviewing code comments

Create three prompts:

1. Zero-shot version.

2. One-shot version.

3. Few-shot version.

Compare the outputs.

You will start to feel when examples help and when they are unnecessary.

---

# Key Takeaways

- Zero-shot prompting uses no examples.

- One-shot prompting uses one example.

- Few-shot prompting uses several examples.

- Examples help the model understand patterns, formats, and categories.

- Few-shot prompting is useful for classification, extraction, and structured transformations.

- Examples consume tokens, so use them intentionally.

- Good examples should be clear, consistent, and representative.

---

# What's Next

Examples are one way to guide a model.

Context is another.

In Season 1, we learned that context windows define what the model can see.

Now we will learn how context changes the quality of AI responses.

In the next article, we will explore:

# How Context Changes AI Responses
