---
title: "How a Retrieval Pipeline Works"
description: "So far in Season 3, we have studied the main pieces of retrieval:"
order: 30
season: 3
slug: "30-how-a-retrieval-pipeline-works"
pubDate: "2026-01-30"
---
So far in Season 3, we have studied the main pieces of retrieval:

- embeddings

- semantic search

- vector similarity

- vector databases

- document chunking

Now we need to connect those pieces into a pipeline.

A retrieval pipeline is the process that takes source knowledge, prepares it, stores it, searches it, and returns relevant information.

Retrieval is the foundation of RAG.

Before an LLM can answer using your documents, your system needs to retrieve the right documents.

That is what the retrieval pipeline does.

---

# The Two Sides Of Retrieval

A retrieval pipeline usually has two main sides:

1. Ingestion

2. Querying

Ingestion happens before the user asks a question.

It prepares and stores knowledge.

Querying happens when the user asks something.

It searches the stored knowledge and returns relevant context.

These two sides work together.

If ingestion is poor, querying will be poor.

If querying is poor, the LLM receives weak context.

---

# Ingestion Step 1: Load Documents

First, the system loads documents.

These might be:

- PDFs

- Markdown files

- web pages

- support tickets

- product documentation

- code files

- transcripts

- database records

The goal is to bring the source knowledge into a processable format.

This can be harder than it sounds.

Real documents may have messy formatting, tables, headers, footers, images, or scanned text.

Document loading is often the first place retrieval quality can suffer.

---

# Ingestion Step 2: Clean And Normalize

Next, the system cleans the content.

This may include:

- removing repeated headers

- fixing broken line breaks

- extracting text from tables

- removing irrelevant boilerplate

- preserving section headings

- normalizing whitespace

Clean input creates better chunks.

Better chunks create better embeddings.

Better embeddings create better retrieval.

This chain matters.

RAG quality begins before the LLM ever sees a prompt.

---

# Ingestion Step 3: Chunk Documents

After cleaning, the system splits documents into chunks.

As we discussed in the previous article, chunking affects retrieval quality.

The system should try to preserve meaning.

Good chunks are:

- large enough to make sense

- small enough to retrieve precisely

- connected to useful metadata

- aligned with document structure when possible

Each chunk becomes a searchable unit.

The retrieval system is only as good as the chunks it can retrieve.

---

# Ingestion Step 4: Create Embeddings

Next, each chunk is converted into an embedding.

The embedding model turns the chunk into a vector.

That vector represents the meaning of the chunk numerically.

For example:

Chunk text:

"Refunds are available within 30 days of purchase."

Embedding:

[0.18, -0.22, 0.91, ...]

The actual numbers are not meant for humans to interpret.

They are used for similarity search.

---

# Ingestion Step 5: Store In A Vector Database

The chunk, embedding, and metadata are stored.

A stored record may include:

- chunk ID

- chunk text

- embedding

- source document

- section title

- page number

- permissions

- timestamp

This creates the searchable knowledge base.

Once ingestion is complete, the system is ready to answer user queries.

---

# Ingestion Step 6: Reindex When Knowledge Changes

Retrieval pipelines are not one-time scripts.

Knowledge changes.

Documents are edited.

New pages are added.

Old files are removed.

When that happens, the index must be updated.

For small systems, you might rebuild the whole index.

For larger systems, you may update only changed documents.

The goal is to keep stored chunks and embeddings aligned with the current source material.

If the index is stale, retrieval can return outdated context.

Outdated context leads to outdated answers.

---

# Query Step 1: Embed The User Question

When a user asks a question, the system converts the question into an embedding.

Example:

User question:

Can I get my money back after 20 days?

The embedding model converts that question into a vector.

Now the system can compare the question vector to stored chunk vectors.

This is where semantic search begins.

---

# Query Step 2: Search For Similar Chunks

The vector database searches for chunks with embeddings similar to the query embedding.

The system may retrieve:

- top 3 chunks

- top 5 chunks

- top 10 chunks

It may also apply metadata filters.

For example:

- region = US

- document_type = policy

- product = subscription

The goal is to retrieve context that is relevant and trustworthy.

---

# Query Step 3: Return Context

The retrieved chunks are returned to the application.

At this point, the system may:

- rank results

- remove duplicates

- apply permissions

- format context for the prompt

- attach citations

Then the context can be sent to the LLM.

This is the handoff from retrieval to generation.

In RAG, this handoff is critical.

The LLM can only answer well if the retrieved context is useful.

---

# Query Step 4: Inspect And Improve

Retrieval pipelines should be observable.

That means you should be able to inspect what happened for a user question.

Useful debugging information includes:

- the original question

- the query embedding model used

- retrieved chunk IDs

- similarity scores

- metadata filters applied

- final context sent to the model

This information helps you improve the system.

If the wrong chunks are retrieved, you can adjust chunking, metadata, top-K, filters, or search method.

Without inspection, retrieval problems become hard to diagnose.

Good retrieval pipelines are not black boxes.

They leave a trail you can debug.

---

# Mini Project

Design a retrieval pipeline for a small FAQ chatbot.

Write the steps:

1. Load FAQ documents.

2. Clean text.

3. Split by question and answer pairs.

4. Create embeddings.

5. Store chunks with category metadata.

6. Embed user question.

7. Retrieve top 3 similar chunks.

8. Send chunks to the LLM.

This exercise gives you the full retrieval mental model.

---

# Key Takeaways

- Retrieval pipelines have ingestion and querying sides.

- Ingestion prepares and stores knowledge before user questions arrive.

- Querying searches stored knowledge at request time.

- Cleaning, chunking, embedding, and metadata all affect retrieval quality.

- The vector database stores embeddings and related chunk information.

- Retrieved chunks become context for the LLM.

- RAG depends heavily on retrieval pipeline quality.

---

# What's Next

Now we are ready to define RAG clearly.

We have all the pieces:

- embeddings

- vector search

- chunks

- retrieval pipelines

In the next article, we will answer:

# What Is RAG?
