---
title: "Evaluations as the Test Suite for AI Systems"
description: "Traditional software has tests."
order: 75
season: 7
slug: "75-evaluations-as-the-test-suite-for-ai-systems"
pubDate: "2026-03-16"
---
Traditional software has tests.

AI systems need evaluations.

Evaluations, often called evals, are structured checks that measure whether an AI system behaves correctly.

They help answer:

Did the model follow the prompt?

Did retrieval find the right context?

Did the agent use the right tool?

Did the answer stay grounded?

Did the system refuse when it should?

Without evals, every prompt change, model change, retrieval change, or tool change becomes risky.

Evals are the test suite for AI behavior.

---

# Why Normal Tests Are Not Enough

Traditional tests work well for deterministic code.

Input goes in.

Expected output comes out.

AI systems are often probabilistic.

There may be multiple acceptable answers.

The wording may vary.

The model may behave slightly differently across runs.

That does not mean testing is impossible.

It means we need evaluation criteria that match AI behavior.

Sometimes exact match works.

Sometimes a rubric is better.

Sometimes human review is needed.

---

# What Evals Can Test

Evals can test many parts of an AI system:

- answer correctness

- retrieval quality

- citation accuracy

- output format

- tool selection

- tool arguments

- refusal behavior

- safety behavior

- latency

- cost

Good evals target specific behaviors.

Do not only ask:

Is the answer good?

Ask:

Did the system do the thing we needed it to do?

---

# Create A Test Set

An eval starts with a test set.

A test set contains examples.

Each example may include:

- input

- expected behavior

- expected source

- allowed output format

- rubric

- notes

For a RAG system, the test set may include expected source documents.

For a classifier, it may include expected labels.

For an agent, it may include expected tools and arguments.

The test set should represent real usage.

---

# Include Failure Cases

Do not only test happy paths.

Include:

- ambiguous inputs

- missing context

- unanswerable questions

- malicious prompts

- tool errors

- invalid data

- edge cases

Failure cases reveal system reliability.

A production AI system must know when to answer, when to refuse, when to ask for clarification, and when to escalate.

Happy-path evals are not enough.

---

# Automated Evals

Some evals can be automated.

Examples:

- JSON validity

- exact category match

- citation source match

- required fields present

- tool name match

- latency threshold

- cost threshold

Automated evals are useful because they can run repeatedly.

They are great for regression testing.

But automated evals may miss nuance.

Use them where the expected behavior is clear.

---

# Human Evals

Some qualities require human judgment.

Examples:

- helpfulness

- tone

- clarity

- completeness

- reasoning quality

- trustworthiness

Human evals should use rubrics.

Instead of asking reviewers:

Is this good?

Ask them to score:

- accuracy

- clarity

- source support

- tone

- actionability

Structured human review creates better evidence.

---

# Regression Testing

Evals are especially useful for regression testing.

Every time you change:

- prompt

- model

- retrieval settings

- chunking

- tool descriptions

- output format

run evals again.

This helps catch unintended changes.

Maybe the new prompt improves tone but worsens citation accuracy.

Maybe a new model is cheaper but fails more edge cases.

Evals reveal tradeoffs.

---

# Engineering Lens

Treat evals like a living test suite.

At first, your eval set may be small.

That is fine.

Start with the most important user journeys and the riskiest failure cases.

Every time the system fails in production, ask whether that failure should become a new eval case.

Every time the prompt changes, run the evals.

Every time the model changes, run the evals.

Every time retrieval changes, run the evals.

This habit turns painful incidents into reusable protection.

The eval suite becomes institutional memory.

It records what the team has learned about the system's behavior.

That is why evals are not only a launch requirement.

They are how AI systems keep improving after launch.

# Practical Example

Imagine your RAG assistant fails when a user asks about cancellation rules.

After fixing the prompt or retrieval pipeline, add that exact case to the eval set.

Then add a few variations:

- a short question

- a vague question

- a question with the wrong product name

- a question where the correct answer is not available

Now the failure becomes reusable protection.

# One More Check

Before trusting an eval, ask whether it would catch a failure users actually care about.

An eval that is easy to pass but unrelated to user value creates false confidence.

# Mini Project

Create an eval set for a document Q&A system.

Include five questions:

- two easy questions

- one multi-document question

- one unanswerable question

- one adversarial question

For each question, define:

- expected source

- expected behavior

- pass criteria

This is the beginning of an AI test suite.

---

# Key Takeaways

- Evals are tests for AI system behavior.

- AI systems need evals because outputs can vary.

- Evals can test correctness, retrieval, format, tool use, refusals, safety, latency, and cost.

- Test sets should include happy paths and failure cases.

- Automated evals are repeatable.

- Human evals need rubrics.

- Regression testing helps prevent prompt, model, or retrieval changes from breaking behavior.

---

# What's Next

Evals help us test changes.

But production systems also need ongoing monitoring.

In the next article, we will explore:

# Monitoring AI Quality Over Time
