---
title: "How to Evaluate a RAG System"
description: "Building a RAG demo is easy."
order: 34
season: 3
slug: "34-how-to-evaluate-a-rag-system"
pubDate: "2026-02-03"
---
Building a RAG demo is easy.

Building a reliable RAG system is harder.

The difference is evaluation.

A demo only needs to work for a few impressive examples.

A real system needs to work across many realistic questions, edge cases, and failure modes.

If you do not evaluate RAG, you are guessing.

The model may sound good.

The answer may look polished.

But the system may still retrieve the wrong context, miss key information, or hallucinate.

Evaluation is how AI engineering becomes disciplined.

---

# What Are We Evaluating?

A RAG system has two major parts to evaluate:

1. Retrieval

2. Generation

Retrieval asks:

Did the system find the right information?

Generation asks:

Did the model use that information correctly to answer?

These are different problems.

If the answer is wrong, you need to know where the failure happened.

Was retrieval bad?

Was generation bad?

Was the source document bad?

Evaluation helps separate these causes.

---

# Retrieval Evaluation

Retrieval evaluation checks whether the system retrieved useful chunks.

For each test question, ask:

- Did the correct chunk appear in the results?

- Was it ranked near the top?

- Were irrelevant chunks retrieved?

- Did metadata filters work?

- Were permissions respected?

Example:

Question:

Can I get a refund after 20 days?

Expected source:

refund_policy.md, Refund Window section

If the system retrieves unrelated billing setup documentation, retrieval failed.

The LLM cannot reliably answer if it receives the wrong context.

---

# Generation Evaluation

Generation evaluation checks the final answer.

Ask:

- Does the answer directly address the question?

- Is it supported by the retrieved context?

- Does it avoid unsupported claims?

- Does it cite the right source?

- Does it say "I do not know" when context is missing?

- Is the answer clear for the user?

A RAG answer should be grounded.

That means the answer should be traceable to the retrieved information.

If the model adds details that are not in the context, that is a problem.

---

# Create A Test Set

The first step in evaluation is creating a test set.

A test set contains realistic questions and expected answers or sources.

Include:

- simple questions

- complex questions

- ambiguous questions

- questions with no answer in the documents

- questions requiring exact details

- questions requiring multiple chunks

For each question, record:

- expected source chunk

- expected answer

- acceptable variations

- failure notes

This becomes your RAG benchmark.

---

# Test Questions With No Answer

This is important.

Do not only test questions that have answers.

Also test questions where the documents do not contain the answer.

Example:

Does the refund policy cover purchases made through third-party resellers?

If the policy does not mention resellers, the system should say the provided documents do not specify.

It should not invent a policy.

Good RAG systems know when not to answer.

That behavior must be tested.

---

# Common Metrics

RAG evaluation can use many metrics.

At a beginner level, focus on practical checks:

- retrieval hit rate

- answer correctness

- citation accuracy

- hallucination rate

- refusal accuracy

- user usefulness

Retrieval hit rate asks:

Did the right chunk appear in the retrieved results?

Citation accuracy asks:

Did the answer cite the correct source?

Refusal accuracy asks:

Did the system refuse when the answer was not in the documents?

These checks are simple but powerful.

---

# Create Regression Tests

Once you have a test set, keep using it.

Every time you change the system, run the same questions again.

This helps catch regressions.

For example, a new chunking strategy might improve some answers but break others.

A new prompt might reduce hallucinations but make answers too cautious.

A new embedding model might improve semantic matching but hurt exact terminology.

Without regression tests, these changes are hard to judge.

A small repeatable test set is better than relying on impressions.

It gives you a stable way to compare versions of the system.

---

# Inspect Retrieved Chunks

When debugging RAG, always inspect retrieved chunks.

Do not only look at the final answer.

For each failed answer, ask:

- What chunks were retrieved?

- Were they relevant?

- Was the correct chunk missing?

- Was the chunk too small?

- Was the chunk too large?

- Was metadata filtering wrong?

- Did the model ignore good context?

This tells you what to fix.

If retrieval is bad, improve chunking, embeddings, filters, or search settings.

If retrieval is good but answers are bad, improve the prompt or model behavior.

---

# Evaluate Over Time

RAG systems can degrade.

Documents change.

Policies update.

New content is added.

Embedding models change.

User questions evolve.

That means evaluation should not be a one-time activity.

Run test sets regularly.

Track quality over time.

When you change chunking, retrieval settings, prompts, or models, evaluate again.

This is how you avoid silent regressions.

---

# Mini Project

Create a small RAG evaluation table.

Columns:

- Question

- Expected Source

- Expected Answer

- Retrieved Source

- Final Answer Correct?

- Notes

Add five questions.

Make one question unanswerable from the documents.

This simple table is enough to start thinking like an AI engineer.

You are no longer just asking:

Does the demo look good?

You are asking:

Does the system reliably retrieve and answer correctly?

---

# Key Takeaways

- RAG evaluation checks retrieval and generation separately.

- Retrieval asks whether the system found the right chunks.

- Generation asks whether the model used context correctly.

- A test set should include answerable and unanswerable questions.

- Inspect retrieved chunks when debugging failures.

- Useful checks include retrieval hit rate, answer correctness, citation accuracy, hallucination rate, and refusal accuracy.

- RAG systems should be evaluated over time as documents and settings change.

---

# What's Next

Now that we know how to evaluate RAG, we need to study how it fails.

Most RAG failures are not mysterious.

They follow patterns.

In the next article, we will explore:

# Common RAG Failure Modes
