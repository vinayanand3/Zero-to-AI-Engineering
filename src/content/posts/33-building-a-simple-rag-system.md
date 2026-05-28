---
title: "Building a Simple RAG System"
description: "Now that we understand RAG architecture, let us walk through a simple build."
order: 33
season: 3
slug: "33-building-a-simple-rag-system"
pubDate: "2026-02-02"
---
Now that we understand RAG architecture, let us walk through a simple build.

This article will stay beginner-friendly.

The goal is not to cover every framework or production detail.

The goal is to understand the flow.

A simple RAG system has one job:

Answer questions using a small collection of documents.

To do that, it needs to:

- load documents

- split them into chunks

- create embeddings

- store embeddings

- retrieve relevant chunks

- send context to an LLM

- generate an answer

That is the core loop.

---

# The Example Project

Imagine we have a small knowledge base for an AI engineering course.

It contains three documents:

- course_overview.md

- refund_policy.md

- weekly_schedule.md

We want users to ask questions like:

- What will I learn in the course?

- Can I get a refund after two weeks?

- When is the project due?

The LLM should answer from the documents, not from general guessing.

That is a perfect small RAG use case.

---

# Step 1: Load The Documents

First, the system reads the documents.

For a small project, this could be as simple as reading Markdown files from a folder.

Each document should keep metadata:

- file name

- title

- section

- last updated date

Even in a small project, metadata helps.

It lets you cite sources and debug retrieval.

If the model gives a strange answer, you can inspect which document chunks were retrieved.

---

# Step 2: Split Into Chunks

Next, split the documents into chunks.

For Markdown files, a simple approach is splitting by headings or paragraphs.

Example chunks:

- Refund eligibility

- Refund time window

- Course module list

- Final project deadline

Each chunk should be understandable on its own.

If a chunk is too small, it may lose context.

If it is too large, it may include unrelated information.

Chunking is one of the first quality decisions in RAG.

---

# Step 3: Create Embeddings

Now each chunk is sent to an embedding model.

The embedding model returns a vector.

That vector represents the meaning of the chunk.

For example:

Chunk:

"Refunds are available within 14 days of purchase if less than 25 percent of the course has been completed."

Embedding:

[0.14, -0.72, 0.33, ...]

The vector is not meant to be read by humans.

It is used for similarity search.

---

# Step 4: Store The Chunks

Store each chunk with:

- chunk ID

- text

- embedding

- source file

- section title

For a tiny project, you could store this in memory.

For a larger project, you might use a vector database.

The storage choice depends on scale.

The concept is the same:

You need to search chunks by embedding similarity and retrieve their text.

---

# Step 5: Embed The User Question

When the user asks a question, embed the question too.

Question:

Can I get my money back after two weeks?

This becomes a query vector.

Now the system can compare the question vector to stored chunk vectors.

The most similar chunks should be about refunds.

This is semantic retrieval.

---

# Step 6: Retrieve Relevant Chunks

The system retrieves the top matching chunks.

For example:

Top result:

"Refunds are available within 14 days of purchase if less than 25 percent of the course has been completed."

Second result:

"Refund requests can be submitted through the billing portal."

These chunks become context for the LLM.

The model does not need to know the refund policy from training.

The system provides it.

---

# Step 7: Build The Prompt

Now create a prompt.

Example:

Use the provided context to answer the user's question. If the context does not contain the answer, say that the answer is not available in the provided documents.

Context:

[retrieved chunks]

Question:

[user question]

Answer:

This prompt tells the model how to behave.

It should use the retrieved context.

It should not invent unsupported details.

---

# Step 8: Generate The Answer

The LLM receives the prompt and generates the final answer.

Example answer:

Based on the refund policy, refunds are available within 14 days of purchase if less than 25 percent of the course has been completed. If you are past two weeks, the provided policy does not specify that a refund is available.

That answer is grounded in the retrieved context.

This is the full RAG loop.

---

# Step 9: Show Sources

A useful RAG answer should often show sources.

For example:

Source:

refund_policy.md, Refund Window section

This helps the user verify the answer.

It also makes the system feel more transparent.

If the answer is wrong, sources make debugging easier.

You can inspect whether the retrieved chunk was wrong, outdated, or misunderstood.

For learning projects, source display can be simple.

For production systems, it may need clickable links, page numbers, permissions, and source freshness indicators.

The key idea is the same:

Do not hide the evidence.

---

# What To Log

Even in a simple RAG system, logging helps.

Log:

- user question

- retrieved chunk IDs

- similarity scores

- final prompt

- final answer

This helps debug failures.

If the answer is wrong, you can ask:

Did retrieval find the right chunks?

Did the prompt include them clearly?

Did the model ignore the context?

Logging turns RAG debugging from guessing into inspection.

---

# Mini Project

Create a tiny RAG design for three personal notes.

For each note, define:

- title

- chunks

- metadata

Then write a sample user question.

Choose which chunks should be retrieved.

Finally, write the prompt that would send those chunks to the LLM.

You do not need to code it yet.

The goal is to understand the system flow.

---

# Key Takeaways

- A simple RAG system answers questions using retrieved documents.

- The core steps are loading, chunking, embedding, storing, retrieving, prompting, and generating.

- The user question and document chunks are both embedded.

- Similarity search finds relevant chunks.

- Retrieved chunks become context for the LLM.

- Logging retrieved chunks and prompts is essential for debugging.

- RAG quality depends on the whole pipeline, not only the LLM.

---

# What's Next

Once a RAG system works, the next question is:

How do we know whether it works well?

That brings us to evaluation.

In the next article, we will explore:

# How to Evaluate a RAG System
