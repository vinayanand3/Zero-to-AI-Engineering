---
title: "What Is Semantic Search?"
description: "Most people are familiar with search."
order: 26
season: 3
slug: "26-what-is-semantic-search"
pubDate: "2026-01-26"
---
Most people are familiar with search.

You type words into a search bar.

The system returns results.

But not all search works the same way.

Traditional search often looks for keyword matches.

Semantic search looks for meaning.

That difference matters because humans do not always use the same words as the documents they need.

Semantic search is one of the most important building blocks in modern AI applications.

It powers document chat, support bots, knowledge assistants, code search, recommendation systems, and RAG pipelines.

To understand RAG, you first need to understand semantic search.

<p class="section-break">. . .</p>

## The Simple Definition

Semantic search is search based on meaning instead of exact words.

A keyword search asks:

Which documents contain these words?

A semantic search asks:

Which documents are most related to this idea?

That shift is powerful.

It means a user can search naturally.

They do not need to guess the exact words used in the document.

The system can find related content even when the wording is different.

<p class="section-break">. . .</p>

## A Simple Example

Imagine a help center article titled:

How to reset your password

A user searches:

I cannot get into my account

There is no exact keyword match for "reset your password."

But the meaning is related.

A semantic search system can still return the password reset article.

That is the core advantage.

Semantic search understands that:

- cannot get into my account

- forgot password

- reset login credentials

- recover access

can all be related.

<p class="section-break">. . .</p>

## How Semantic Search Works

At a high level, semantic search has four steps:

1. Convert documents into embeddings.

2. Store those embeddings.

3. Convert the user's query into an embedding.

4. Find documents with embeddings closest to the query embedding.

The comparison is based on vector similarity.

We will cover vector similarity more deeply in the next article.

For now, think of it as asking:

Which document vectors are closest to the query vector?

Close usually means semantically related.

<p class="section-break">. . .</p>

## Why Embeddings Make This Possible

Embeddings place text into a meaning space.

If two pieces of text have similar meaning, their embeddings should be close.

That means we can compare:

- question to article

- user query to document chunk

- support ticket to category

- code comment to source file

- product description to customer intent

This turns search into a numerical comparison problem.

That is why embeddings are so important.

They make meaning searchable.

<p class="section-break">. . .</p>

## Semantic Search vs Keyword Search

Keyword search is not bad.

It is still useful.

It works well for:

- exact names

- IDs

- part numbers

- error codes

- quoted phrases

- dates

- unique terms

Semantic search works well for:

- natural language questions

- conceptual similarity

- fuzzy wording

- related ideas

- document discovery

- support content

In real systems, engineers often combine both.

This is called hybrid search.

Hybrid search can use keyword matching and embedding similarity together.

That often produces better results than either one alone.

<p class="section-break">. . .</p>

## Why Semantic Search Matters for AI Assistants

LLMs have context limits.

They cannot automatically read every document your company has.

So an AI assistant needs a way to find relevant information before answering.

Semantic search helps with that.

For example:

User asks:

What is our policy for refunds after 30 days?

The system searches the company knowledge base.

It retrieves the most relevant policy sections.

Then those sections are included in the prompt.

The LLM answers using that context.

That is the beginning of RAG.

Semantic search is the retrieval engine.

<p class="section-break">. . .</p>

## The Quality Of Search Matters

If semantic search retrieves the wrong documents, the AI answer will likely be weak.

This is an important AI engineering lesson:

The final LLM answer depends heavily on retrieval quality.

Bad retrieval can cause:

- incomplete answers

- wrong citations

- irrelevant context

- hallucinations

- user frustration

Good retrieval gives the model better material to work with.

That is why retrieval evaluation matters.

We will cover that later in this season.

<p class="section-break">. . .</p>

## Search Results Should Be Inspectable

When building semantic search, do not only look at the final answer.

Look at the search results themselves.

For each query, inspect:

- which chunks were returned

- whether they actually answer the question

- whether the best result is near the top

- whether irrelevant chunks are appearing

- whether metadata filters are working

This matters because semantic search can feel correct when the final generated answer sounds polished.

But polished output can hide weak retrieval.

AI engineers need to inspect the retrieval layer directly.

If search results are poor, the LLM is starting from weak evidence.

Debug search before blaming generation.

<p class="section-break">. . .</p>

## Visual Explanation

Imagine every document as a dot on a map.

Documents about similar topics are near each other.

Documents about unrelated topics are far apart.

When a user asks a question, the question becomes another dot.

The search system looks around that dot and finds nearby documents.

Those nearby documents are likely related to the user's meaning.

That is semantic search in one picture.

<p class="section-break">. . .</p>

## Mini Project

Pick a small set of documents or notes.

Write one search query using exact words from a document.

Then write another search query using different words but the same meaning.

Example:

Document title:

How to cancel a subscription

Exact query:

cancel subscription

Semantic query:

stop being charged every month

Ask yourself:

Would keyword search find both?

Would semantic search have a better chance?

This exercise builds retrieval intuition.

<p class="section-break">. . .</p>

## Key Takeaways

- Semantic search finds information by meaning, not just exact words.

- It uses embeddings to represent queries and documents numerically.

- Similar meanings should have nearby embeddings.

- Semantic search is useful for natural language queries and conceptual matching.

- Keyword search is still useful for exact terms, IDs, and codes.

- Many real systems combine semantic and keyword search.

- RAG systems depend heavily on retrieval quality.

<p class="section-break">. . .</p>

## What's Next

Semantic search depends on comparing embeddings.

That means we need to understand vector similarity.

In the next article, we will answer:

## How Do AI Systems Compare Meaning?
