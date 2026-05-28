---
title: "Mini Project: Design a Production AI Readiness Checklist"
description: "Before launching an AI feature, you need a readiness checklist."
order: 83
season: 7
slug: "83-mini-project-design-a-production-ai-readiness-checklist"
pubDate: "2026-03-24"
---
Before launching an AI feature, you need a readiness checklist.

Not because checklists are exciting.

Because production systems fail when important basics are missed.

AI readiness includes more than model quality.

It includes prompts, retrieval, tools, security, privacy, cost, latency, monitoring, evals, fallbacks, and operations.

This article builds a practical checklist you can reuse.

The example will be a document Q&A assistant for internal company policies.

---

# The Scenario

We are launching an internal AI assistant.

Users can ask questions about company policies.

The system uses RAG to retrieve policy documents.

The model answers with citations.

The assistant should not answer from unsupported knowledge.

It should refuse when the documents do not contain the answer.

It should respect document permissions.

This is a realistic production AI feature.

Now let's design the checklist.

---

# 1. Scope Checklist

Define what the system should and should not do.

Questions:

- what questions should it answer?

- what documents are in scope?

- what documents are out of scope?

- should it answer policy interpretation questions?

- should it provide legal or HR advice?

- when should it escalate?

Clear scope prevents product confusion.

If scope is vague, users will expect too much and the model may over-answer.

---

# 2. Data Checklist

Check the source documents.

Questions:

- are documents current?

- are duplicates removed?

- are outdated policies excluded?

- are permissions attached?

- are document owners identified?

- is there a refresh process?

RAG quality depends on source quality.

Bad documents create bad answers.

Production readiness starts with data readiness.

---

# 3. Retrieval Checklist

Check retrieval behavior.

Questions:

- are chunks understandable?

- are metadata filters working?

- are permissions enforced before retrieval?

- does retrieval find expected sources?

- are citations available?

- are unanswerable questions handled?

Retrieval should be evaluated before launch.

Do not only inspect final answers.

Inspect retrieved chunks.

---

# 4. Prompt And Answer Checklist

Check model behavior.

Questions:

- does the prompt require source grounding?

- does the model cite sources?

- does it refuse when context is missing?

- does it avoid unsupported claims?

- is the tone appropriate?

- is output easy to read?

The prompt should clearly define how the model uses context.

It should also define what to do when context is insufficient.

---

# 5. Evaluation Checklist

Create evals.

Include:

- common questions

- edge cases

- unanswerable questions

- permission tests

- citation tests

- prompt injection tests

- regression tests

Set launch criteria.

For example:

The assistant must cite the correct source for at least a target percentage of eval questions.

Launch should be based on evidence.

---

# 6. Security And Privacy Checklist

Check sensitive data controls.

Questions:

- are user permissions enforced?

- are logs redacted?

- is retention defined?

- are prompt injection risks considered?

- can users access only allowed documents?

- are admin-only policies protected?

Security must be tested, not assumed.

The model should not see unauthorized context.

---

# 7. Monitoring Checklist

Prepare production monitoring.

Track:

- latency

- cost

- retrieval failures

- citation failures

- user feedback

- hallucination reports

- escalation rate

- error rate

Define who reviews metrics and how often.

Monitoring without ownership does not help.

---

# 8. Fallback Checklist

Define failure behavior.

If retrieval fails:

What happens?

If the model output is unsupported:

What happens?

If the user asks an out-of-scope question:

What happens?

If policy documents conflict:

What happens?

Fallbacks should be clear before launch.

Graceful failure is production quality.

---

# 9. Launch Checklist

Launch safely.

Use:

- internal testing

- feature flag

- beta users

- canary rollout

- rollback plan

- support escalation path

- incident response owner

Do not launch all at once without control.

AI features should be released in stages.

---

# Engineering Lens

The checklist should be useful during a real launch review.

That means each item should be answerable.

Avoid vague questions like "Is the system safe?"

Use specific questions:

- What data can the model access?

- What tools can it call?

- What happens when retrieval fails?

- What outputs are validated?

- What metrics are monitored after launch?

- Who owns incidents?

- What is the rollback path?

A good readiness checklist creates shared language across engineering, product, design, security, and operations.

It makes hidden assumptions visible before users depend on the feature.

# Practical Example

For a support assistant, the checklist might reveal that logging is ready but fallback behavior is not.

It might reveal that the eval set covers common questions but not refund edge cases.

It might reveal that the model can access sensitive account notes without a clear retention policy.

These discoveries are not failures.

They are exactly why the checklist exists.

Finding the gap before launch is much cheaper than finding it through user harm.

# Mini Project

Adapt this checklist to a different AI feature:

- coding assistant

- customer support bot

- meeting summarizer

- sales assistant

- research agent

For your chosen feature, write the readiness checklist categories and two questions under each.

This turns the season into a launch artifact.

---

# Key Takeaways

- Production AI readiness requires more than model quality.

- Scope, data, retrieval, prompts, evals, security, monitoring, fallbacks, and launch process all matter.

- RAG systems need source and retrieval checks.

- Security and privacy must be tested.

- Monitoring needs ownership.

- Fallbacks should be designed before launch.

- Launch should use staged rollout and rollback controls.

---

# What's Next

We have now covered the practical foundations of production AI engineering.

In the final article of Season 7, we will connect everything into one mental model:

# The Mental Model of Production AI
