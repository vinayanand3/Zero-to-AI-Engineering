---
title: "What Is a Vector Database?"
description: "So far in Season 3, we have learned that embeddings turn meaning into numbers."
order: 28
season: 3
slug: "28-what-is-a-vector-database"
pubDate: "2026-01-28"
---
So far in Season 3, we have learned that embeddings turn meaning into numbers.

We also learned that semantic search compares embeddings to find related information.

But now we need to ask a practical engineering question:

Where do all these embeddings live?

If you have ten documents, you could store embeddings in a simple file.

But what if you have:

- ten thousand documents

- one million support tickets

- an entire codebase

- thousands of product pages

- years of internal knowledge

You need a system that can store embeddings and search them quickly.

That is where vector databases come in.

---

# The Simple Definition

A vector database is a database designed to store and search vectors.

In AI applications, those vectors are often embeddings.

A vector database lets you:

- store embeddings

- attach metadata

- search by similarity

- filter results

- update records

- retrieve relevant content quickly

It is a key component in many semantic search and RAG systems.

The vector database is not the LLM.

It is the retrieval layer that helps the LLM find useful information.

---

# Why Normal Databases Are Not Enough

Traditional databases are excellent for exact queries.

For example:

Find user where id = 123

Find orders where status = "paid"

Find documents created after January 1

These are structured queries.

Vector search is different.

It asks:

Find the records whose embeddings are most similar to this query embedding.

That is a nearest-neighbor search problem.

At small scale, you can compare the query vector to every stored vector.

At large scale, that becomes too slow.

Vector databases use specialized indexes to make similarity search efficient.

---

# What Gets Stored?

A vector database usually stores more than just the vector.

A record may include:

- an ID

- the embedding vector

- the original text or a reference to it

- metadata

- source document name

- page number

- timestamp

- permissions

For example:

ID: doc_123_chunk_4

Text: "Refunds are available within 30 days of purchase."

Embedding: [0.18, -0.22, 0.91, ...]

Metadata: product = "subscription", region = "US", source = "refund_policy.pdf"

The embedding helps search.

The text helps answer.

The metadata helps filter and cite.

---

# Where Should The Original Text Live?

Some systems store the original text directly in the vector database.

Other systems store only a reference to the text.

For small projects, storing text with the vector is simple and convenient.

For larger systems, the original content may live in a document store, database, or object storage system.

The vector database then stores an ID that points back to the source.

Both approaches can work.

The important requirement is that retrieval must return enough information to build the final prompt and cite the source.

Vectors help search.

Text helps answer.

---

# How a Vector Search Works

A typical vector search flow looks like this:

1. User asks a question.

2. The question is converted into an embedding.

3. The vector database searches for similar stored embeddings.

4. The database returns the closest records.

5. The application sends those records to the LLM as context.

This is one of the core flows behind RAG.

The vector database is responsible for finding candidate knowledge.

The LLM is responsible for generating the final answer using that knowledge.

---

# Metadata Filtering

Metadata filtering is one of the most important vector database features.

Imagine a company has refund policies for different countries.

A user asks:

What is the refund window in Canada?

Vector similarity might retrieve refund documents from multiple regions.

Metadata can filter results to:

region = Canada

This makes retrieval more precise.

Without metadata, the system may retrieve semantically related but incorrect information.

Good RAG systems depend heavily on good metadata.

---

# Updates And Deletes

Real knowledge changes.

Documents are edited.

Policies are replaced.

Pages are deleted.

That means a vector database needs an update strategy.

If a source document changes, the old chunks and embeddings may need to be replaced.

If a document is deleted, its vectors should not keep appearing in search results.

This sounds obvious, but it is a common production issue.

A stale vector index can make an AI assistant answer with outdated information.

When designing a vector database workflow, always ask:

How will new, changed, and deleted documents be handled?

Retrieval quality depends on keeping the index fresh.

---

# Vector Databases vs Embedding Models

Beginners sometimes confuse embedding models and vector databases.

They are different.

The embedding model converts text into vectors.

The vector database stores and searches those vectors.

The LLM generates responses.

These are separate roles.

A RAG system often uses all three:

- embedding model for representation

- vector database for retrieval

- LLM for answer generation

Understanding these roles helps you design systems clearly.

---

# Do You Always Need A Vector Database?

Not always.

For small projects, you can store embeddings in memory, a local file, or a normal database with vector support.

You might not need a separate vector database if:

- your dataset is tiny

- search volume is low

- latency requirements are relaxed

- your existing database supports vector search

But as the system grows, vector database features become more useful.

You may need indexing, filtering, updates, access control, and monitoring.

Choose infrastructure based on the problem, not hype.

---

# Mini Project

Imagine building a chatbot over a company handbook.

For each chunk of the handbook, what would you store?

Write a record design:

- chunk ID

- chunk text

- embedding

- source file

- section title

- page number

- department

- last updated date

This exercise helps you think beyond vectors.

A useful retrieval system stores enough information to search, filter, answer, and cite.

---

# Key Takeaways

- A vector database stores and searches embedding vectors.

- It enables fast similarity search at scale.

- Vector records usually include embeddings, text, metadata, and source references.

- Metadata filtering improves retrieval precision.

- Embedding models, vector databases, and LLMs have different roles.

- Small projects may not need a dedicated vector database.

- RAG systems often rely on vector databases for retrieval.

---

# What's Next

Before storing documents in a vector database, we need to prepare them.

Most documents are too large to embed as one piece.

So we split them into chunks.

In the next article, we will explore:

# Why Document Chunking Matters
