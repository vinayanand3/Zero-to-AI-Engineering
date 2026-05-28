---
title: "The Architecture of a RAG System"
description: "In the previous article, we defined RAG as RetrievalAugmented Generation."
order: 32
season: 3
slug: "32-the-architecture-of-a-rag-system"
pubDate: "2026-02-01"
---
In the previous article, we defined RAG as Retrieval-Augmented Generation.

Now we need to look at the system architecture.

RAG is not one model.

RAG is a pipeline.

It connects documents, embeddings, search, prompts, and LLM generation.

This is where AI engineering becomes systems engineering.

The quality of a RAG application depends on how well these pieces work together.

In this article, we will break down the main architecture.

---

# The Two Main Phases

A RAG system usually has two phases:

1. Indexing phase

2. Answering phase

The indexing phase prepares knowledge before users ask questions.

The answering phase runs when a user asks a question.

This distinction is important.

Some work happens offline or in the background.

Some work happens live during the user request.

Good architecture separates these responsibilities clearly.

---

# Indexing Phase

The indexing phase prepares documents for retrieval.

It usually includes:

- loading documents

- cleaning text

- splitting into chunks

- creating embeddings

- storing chunks and embeddings

- storing metadata

This phase creates the searchable knowledge base.

If indexing is poor, the rest of the system suffers.

For example, if documents are chunked badly, retrieval may return incomplete or confusing context.

If metadata is missing, filtering and citations become harder.

---

# Answering Phase

The answering phase starts when a user asks a question.

It usually includes:

- receiving the question

- embedding the question

- retrieving relevant chunks

- formatting retrieved context

- building the final prompt

- calling the LLM

- returning an answer

- optionally including citations

This is the user-facing part of RAG.

It needs to be accurate, fast, and reliable.

Latency matters here because the user is waiting.

---

# Core Component 1: Knowledge Sources

The knowledge source is where the information comes from.

Examples:

- PDFs

- websites

- internal wikis

- Markdown files

- database records

- tickets

- code repositories

- transcripts

The quality of the source matters.

If the source documents are outdated, contradictory, or poorly written, the RAG system will inherit those problems.

RAG does not magically fix bad knowledge.

It retrieves from it.

---

# Core Component 2: Chunk Store

After documents are loaded and chunked, each chunk needs to be stored.

A chunk store may contain:

- chunk text

- source document

- section title

- page number

- created date

- permissions

- embedding vector

Sometimes the text and metadata are stored in the vector database.

Sometimes the vector database stores references to another database.

The exact design depends on the application.

The principle is simple:

You need to retrieve the text and its source when answering.

---

# Core Component 3: Retriever

The retriever is responsible for finding relevant chunks.

It may use:

- vector search

- keyword search

- hybrid search

- metadata filters

- reranking

The retriever is one of the most important components in the system.

If it retrieves weak context, the LLM starts from weak evidence.

Many RAG problems are actually retrieval problems.

That is why debugging RAG often starts by inspecting retrieved chunks.

---

# Core Component 4: Prompt Builder

The prompt builder combines:

- system instructions

- user question

- retrieved context

- formatting rules

- citation instructions

This step matters more than beginners expect.

The LLM needs to know how to use the retrieved context.

For example:

Answer the question using only the provided context. If the context does not contain the answer, say that the answer is not available in the provided documents.

That instruction helps reduce unsupported answers.

The prompt builder turns retrieval results into usable model input.

---

# Core Component 5: Citations And Source Display

Many RAG applications should show where an answer came from.

This may mean:

- source document names

- section titles

- page numbers

- links

- quoted snippets

Citations help users trust and verify answers.

They also help developers debug.

If the model gives a strange answer, the citation tells you which source influenced it.

For internal tools, source display can be just as important as the answer itself.

Users often need to know not only what the answer is, but where it came from.

---

# Core Component 6: Generator

The generator is the LLM.

It reads the final prompt and produces the answer.

The generator should:

- answer the user question

- use retrieved context

- follow the output format

- avoid unsupported claims

- cite sources if required

The LLM is important, but it is only one part of the RAG system.

Changing the model may help.

But if retrieval is poor, a better model may still struggle.

---

# Core Component 7: Evaluation

RAG systems need evaluation.

You need to measure:

- did retrieval find the right chunks?

- did the answer use the chunks correctly?

- did the answer hallucinate?

- were citations accurate?

- did the system refuse when context was missing?

Without evaluation, you are guessing.

Production RAG needs test questions, expected sources, and quality checks.

We will cover evaluation later in this season.

---

# Mini Project

Draw a simple RAG architecture:

Indexing:

Documents -> cleaner -> chunker -> embedding model -> vector database

Answering:

User question -> embedding model -> retriever -> prompt builder -> LLM -> answer

Now label where quality can fail.

You will likely find many points:

- bad documents

- bad chunks

- wrong embeddings

- weak retrieval

- poor prompt

- unsupported generation

That is why RAG is a system design problem.

---

# Key Takeaways

- RAG has an indexing phase and an answering phase.

- Indexing prepares knowledge for retrieval.

- Answering retrieves context and generates a response.

- Core components include knowledge sources, chunk store, retriever, prompt builder, generator, and evaluation.

- Retrieval quality strongly affects answer quality.

- The LLM is only one part of the architecture.

- RAG systems must be evaluated, not just demonstrated.

---

# What's Next

Now that we understand RAG architecture, we can walk through a simple build.

In the next article, we will explore:

# Building a Simple RAG System
