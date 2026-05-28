---
title: "Why AI Hallucinates"
description: "One of the most surprising things about modern AI is how confident it can sound when it is wrong."
order: 11
season: 1
slug: "11-why-ai-hallucinates"
pubDate: "2026-01-11"
---
One of the most surprising things about modern AI is how confident it can sound when it is wrong.

An LLM can produce:

- a fake citation

- an incorrect fact

- a broken code example

- a made-up API

- a misleading explanation

- a confident answer to a question it does not truly know

This behavior is usually called hallucination.

The word sounds dramatic, but the underlying idea is practical:

An AI hallucination happens when a model generates output that appears plausible but is not actually correct.

To understand why this happens, we need to connect several ideas from Season 1.

LLMs generate text token by token.

They predict likely continuations.

They use context windows.

They do not automatically verify truth.

Once you see those pieces together, hallucinations become much easier to understand.

---

# The Core Reason

The simplest explanation is this:

> LLMs are trained to generate likely text, not guaranteed truth.

That sentence is important.

During training, a language model learns patterns in text.

It learns how answers are written.

It learns grammar, structure, style, facts, code patterns, and reasoning patterns.

But the basic generation process is still prediction.

Given the current context, what token should come next?

If the model has enough reliable context, it may produce a correct answer.

If the model has incomplete, outdated, ambiguous, or misleading context, it may still produce an answer that sounds right.

That is where hallucinations come from.

---

# The Student Analogy

Imagine a student taking an exam.

The student does not fully know the answer, but they know what a good answer is supposed to sound like.

So they write something polished, structured, and confident.

The paragraph sounds impressive.

But the facts may be wrong.

LLMs can behave similarly.

They are very good at producing text in the shape of an answer.

But producing answer-shaped text is not the same as knowing the answer is true.

This is why confidence is not the same as correctness.

---

# Hallucinations Are Not Random

Hallucinations often feel strange because they are not pure nonsense.

They are usually plausible.

For example, a model may invent a research paper title that sounds real.

It may create a function name that fits a library's naming style.

It may cite a court case that resembles real legal citations.

It may explain a concept using a familiar structure but include one wrong detail.

This happens because the model has learned patterns.

It knows what things usually look like.

But pattern completion can produce convincing falsehoods.

That is what makes hallucinations risky.

They often look reasonable at first glance.

---

# Missing Context Causes Hallucinations

Context is one of the biggest factors.

If you ask:

What did my team decide in yesterday's meeting?

but you do not provide meeting notes, the model does not actually know.

It may say it cannot answer.

Or it may infer something from the conversation.

Or, in a poorly designed system, it may invent a plausible answer.

The model can only use what is available in its context or what is stored in connected tools.

If the needed information is missing, the risk of hallucination increases.

This is why good AI systems often include retrieval, tool use, citations, or database lookups.

They give the model better grounding.

---

# Outdated Knowledge Causes Hallucinations

Many models have a training cutoff.

That means their internal knowledge may not include recent events, new library versions, current prices, new APIs, or updated documentation.

If you ask about something recent and the model does not have live access to a source, it may answer from outdated patterns.

This is especially risky for:

- software libraries

- legal rules

- medical information

- financial data

- current events

- company policies

In production systems, engineers must be careful about when a model should answer from internal knowledge and when it should retrieve fresh information.

---

# Ambiguous Prompts Cause Hallucinations

Sometimes the problem is not the model alone.

Sometimes the prompt is unclear.

For example:

Explain the best model for my project.

What project?

What constraints?

What budget?

What latency requirement?

What data type?

If the prompt does not provide enough detail, the model may fill in the blanks.

That can be useful for brainstorming.

But it can be dangerous when accuracy matters.

Clear prompts reduce hallucination risk because they reduce the number of assumptions the model has to make.

---

# How Engineers Reduce Hallucinations

Hallucinations cannot be eliminated completely in every open-ended setting.

But they can be reduced.

Common strategies include:

- providing better context

- using retrieval from trusted sources

- requiring citations

- connecting tools for live data

- validating outputs with tests

- constraining the response format

- asking the model to admit uncertainty

- using human review for high-risk cases

For example, a customer support bot should not invent refund policies.

It should retrieve the official policy and answer from that.

A coding assistant should not invent library methods.

It should rely on actual documentation, type definitions, or codebase context.

Grounding matters.

---

# Hallucinations In Code

Code hallucinations are common.

An LLM may generate:

- a function that does not exist

- an import from the wrong package

- an outdated API call

- code that looks correct but fails at runtime

- a security-sensitive mistake

This is why testing matters.

AI-generated code should be treated like code from a junior teammate who types very fast.

It can be useful.

It can save time.

But it still needs review, execution, and verification.

In software engineering, the compiler, test suite, linter, and runtime are grounding tools.

They help separate plausible code from working code.

---

# Visual Explanation

Imagine the model as a powerful text engine.

It has:

- learned patterns from training

- current context from the prompt

- instructions from the system

- possibly tool results or retrieved documents

When the answer is grounded in reliable context, the output is more likely to be correct.

When grounding is weak, the model may rely more on pattern completion.

Pattern completion can sound fluent.

But fluency does not guarantee truth.

That is the mental model to keep.

---

# Mini Project

Try this exercise.

Ask an AI model a question about a library, tool, or API you know well.

Then verify the answer against official documentation.

Look for:

- invented methods

- missing parameters

- outdated syntax

- incorrect assumptions

This exercise teaches an important AI engineering habit:

Trust the model for acceleration.

Trust verification for correctness.

That mindset will make you much better at building with AI.

---

# Key Takeaways

- Hallucinations are plausible but incorrect AI outputs.

- LLMs generate likely text, not guaranteed truth.

- Missing context increases hallucination risk.

- Outdated knowledge can lead to wrong answers.

- Ambiguous prompts make the model fill in gaps.

- Retrieval, tools, citations, tests, and validation reduce hallucinations.

- Fluent output is not the same as correct output.

- AI engineers design systems that ground model outputs in reliable information.

---

# What's Next

We have now covered the core foundations of modern AI systems.

We started with AI itself.

Then we moved through neural networks, transformers, token generation, tokenization, embeddings, training, inference, GPUs, context windows, and hallucinations.

Before moving into prompt engineering, we need to connect all of these ideas into one mental model.

That is what we will do in the final article of Season 1:

# The Mental Model Of Modern AI

