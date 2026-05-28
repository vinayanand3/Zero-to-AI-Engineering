---
title: "What Is RAG?"
description: "RAG is one of the most important ideas in practical AI engineering."
order: 31
season: 3
slug: "31-what-is-rag"
pubDate: "2026-01-31"
---
RAG is one of the most important ideas in practical AI engineering.

It stands for:

## Retrieval-Augmented Generation

The name sounds complicated.

But the core idea is simple.

Before the model answers, retrieve relevant information and include it in the prompt.

That is RAG.

It combines retrieval with generation.

Retrieval finds useful knowledge.

Generation uses that knowledge to produce an answer.

Once you understand this pattern, many modern AI applications become easier to understand.

<p class="section-break">. . .</p>

## Why RAG Exists

LLMs are powerful, but they have limitations.

They may not know:

- your private company documents

- your latest product policies

- your internal codebase

- recent updates

- customer-specific information

- proprietary data

They also have context limits.

You cannot always paste every document into the prompt.

RAG helps solve this.

Instead of asking the model to answer from memory, the system retrieves relevant information first.

Then the model answers using that information.

<p class="section-break">. . .</p>

## The Simple RAG Flow

A basic RAG system works like this:

1. User asks a question.

2. The system searches for relevant documents.

3. The system adds those documents to the prompt.

4. The LLM generates an answer.

5. The answer may include citations or references.

Example:

User:

What is our refund policy after 30 days?

System retrieves:

Refund policy document, section 4.

LLM answers:

According to the refund policy, refunds after 30 days are only available under specific exceptions...

The answer is grounded in retrieved context.

That is the point.

<p class="section-break">. . .</p>

## RAG Is Like Open-Book Answering

A useful analogy is an open-book exam.

A closed-book student answers from memory.

An open-book student can look up the relevant page before answering.

RAG gives the model an open book.

The LLM still needs to write the answer.

But retrieval gives it better material to use.

This reduces reliance on internal model knowledge.

It also makes the system more adaptable because you can update the documents without retraining the model.

<p class="section-break">. . .</p>

## RAG vs Fine-Tuning

Beginners often ask:

Should I use RAG or fine-tuning?

These solve different problems.

RAG is useful when the model needs access to external knowledge.

Examples:

- company policies

- product documentation

- legal documents

- knowledge bases

- manuals

- support articles

Fine-tuning is useful when you want to change model behavior, style, or task performance.

Examples:

- domain-specific response style

- specialized classification

- consistent formatting

- narrow task adaptation

If the problem is missing knowledge, start by thinking about RAG.

If the problem is behavior, style, or task specialization, fine-tuning may be relevant.

We will cover fine-tuning in a later season.

<p class="section-break">. . .</p>

## What RAG Is Not

RAG is not the same as giving the model permanent memory.

It does not update the model's weights.

It does not make the model automatically understand every document perfectly.

It does not guarantee the answer is correct.

RAG is a retrieval and prompting pattern.

It finds relevant information and gives that information to the model at answer time.

That distinction matters.

If retrieval fails, RAG fails.

If the prompt is weak, RAG can still fail.

If the source documents are wrong, RAG can confidently repeat wrong information.

RAG is powerful, but it is still a system that must be designed and evaluated.

<p class="section-break">. . .</p>

## Why RAG Reduces Hallucinations

RAG can reduce hallucinations because it gives the model source material.

Instead of generating purely from learned patterns, the model can answer from retrieved context.

But RAG does not eliminate hallucinations completely.

The system can still fail if:

- retrieval returns the wrong chunks

- chunks are missing key information

- the prompt is poorly written

- the model ignores context

- source documents are outdated

- the question requires reasoning beyond the retrieved text

RAG improves grounding.

It does not guarantee correctness.

Good RAG systems still need evaluation and validation.

<p class="section-break">. . .</p>

## RAG And Fresh Knowledge

Another reason RAG is useful is freshness.

A model's internal knowledge may be old.

But a retrieval system can search documents that were updated today.

For example, a product policy might change this morning.

Instead of retraining a model, you update the knowledge base and refresh the index.

Now the RAG system can retrieve the latest policy.

This is one of the biggest practical advantages of RAG.

It separates model capability from knowledge storage.

The model provides language and reasoning ability.

The retrieval layer provides current information.

<p class="section-break">. . .</p>

## What RAG Is Used For

RAG is used in many real applications:

- chat with documents

- customer support assistants

- internal company knowledge bots

- legal research tools

- medical literature assistants

- codebase question answering

- product documentation chat

- research summarization

- enterprise search

The common pattern is:

There is a large body of knowledge.

The user asks a question.

The system retrieves relevant parts.

The LLM answers using those parts.

<p class="section-break">. . .</p>

## The Main Components

A RAG system usually includes:

- documents or knowledge sources

- document loader

- text cleaning

- chunking

- embedding model

- vector database

- retrieval logic

- prompt template

- LLM

- response validation or citation

This is why RAG is not just "add documents to ChatGPT."

It is a system.

Each component affects quality.

<p class="section-break">. . .</p>

## Mini Project

Imagine building a RAG assistant for your personal notes.

Write down:

- what documents you would include

- how you would split them

- what metadata you would store

- what questions users might ask

- how many chunks you would retrieve

- what the final prompt should tell the model

This exercise helps you think like a system designer.

RAG is not only about calling an LLM.

It is about designing the knowledge flow around the LLM.

<p class="section-break">. . .</p>

## Key Takeaways

- RAG stands for Retrieval-Augmented Generation.

- RAG retrieves relevant information before generating an answer.

- It helps LLMs answer using external or private knowledge.

- RAG is useful when knowledge changes or lives outside the model.

- RAG can reduce hallucinations, but it does not eliminate them.

- RAG is a system made of ingestion, retrieval, prompting, generation, and validation.

- Retrieval quality strongly affects final answer quality.

<p class="section-break">. . .</p>

## What's Next

Now that we know what RAG is, we need to look at its architecture.

In the next article, we will break down:

## The Architecture of a RAG System
