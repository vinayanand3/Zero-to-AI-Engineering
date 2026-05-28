---
title: "How Do AI Systems Compare Meaning?"
description: "In the previous article, we learned that semantic search finds information by meaning."
order: 27
season: 3
slug: "27-how-do-ai-systems-compare-meaning"
pubDate: "2026-01-27"
---
In the previous article, we learned that semantic search finds information by meaning.

But that raises an important question:

# How does software compare meaning?

Humans compare meaning naturally.

We know that "refund" and "money back" are related.

We know that "login issue" and "cannot access my account" are similar.

But computers need a numerical method.

That is where vector similarity comes in.

Vector similarity is the technique that allows AI systems to compare embeddings and decide which pieces of text are most related.

---

# Embeddings Are Vectors

An embedding is a vector.

A vector is a list of numbers.

For example:

[0.12, -0.45, 0.88, 0.31]

Real embeddings usually have many more numbers.

They may have hundreds or thousands of dimensions.

Each piece of text gets converted into a vector.

Then the system compares vectors.

If two vectors are close, the meanings are likely related.

If they are far apart, the meanings are likely different.

That is the basic idea.

---

# The Map Analogy Again

Imagine a map.

New York and Boston are close.

New York and Tokyo are far apart.

Distance tells us something about geography.

Embedding space works similarly, but for meaning.

"Password reset" and "account recovery" should be close.

"Password reset" and "banana recipe" should be far apart.

Vector similarity is how the system measures that closeness.

The exact math can vary, but the intuition is simple:

closer vectors usually mean more similar meaning.

---

# Common Similarity Methods

There are several ways to compare vectors.

Common methods include:

- cosine similarity

- dot product

- Euclidean distance

You do not need to master the math yet.

But you should understand the intuition.

Cosine similarity compares direction.

Dot product compares alignment and magnitude.

Euclidean distance compares physical distance in vector space.

Different systems may use different methods depending on the embedding model and database.

As an AI engineer, the important habit is to know which similarity method your system uses.

---

# A Simple Example

Suppose a user asks:

How do I stop being charged?

The query becomes an embedding.

Your knowledge base has three document embeddings:

- cancel subscription

- update profile photo

- reset password

The system compares the query embedding to each document embedding.

The closest match should be:

cancel subscription

That document is then returned as a search result.

The LLM can use it as context.

This is how vector similarity becomes useful in real applications.

---

# Similarity Is Not The Same As Truth

This is important.

Vector similarity tells us what is related.

It does not guarantee the retrieved text answers the question correctly.

A document can be semantically similar but still not contain the needed answer.

For example, a document about refund policy may be similar to a question about refunds.

But it might not mention the exact 30-day rule the user needs.

That is why retrieval systems need evaluation.

Similarity is a starting point.

It is not full understanding.

---

# Top-K Retrieval

Semantic search systems often return the top K results.

K means how many results to retrieve.

For example:

- top 3 documents

- top 5 chunks

- top 10 results

If K is too small, the system may miss important context.

If K is too large, the prompt may include irrelevant information.

Choosing K is a practical engineering decision.

It affects cost, accuracy, latency, and context quality.

This is one of the first knobs engineers tune in retrieval systems.

---

# Ranking Matters

Retrieval is not only about finding a relevant result.

It is also about ranking the best result near the top.

If the right chunk appears at result number 20, but your system only sends the top 5 chunks to the LLM, the answer may still fail.

That is why ranking quality matters.

Good retrieval systems try to place the most useful evidence near the top of the result list.

Some systems add a reranking step after the first vector search.

The first search finds candidate chunks.

The reranker sorts those candidates more carefully.

This adds cost and latency, but it can improve answer quality.

As always, the engineering question is not whether a technique sounds advanced.

The question is whether it improves the system for your use case.

---

# Similarity Thresholds

Some systems also use a similarity threshold.

That means:

Only return results if they are similar enough.

This helps avoid weak matches.

For example, if a user asks a question unrelated to your documents, the system should not force a bad answer.

It may be better to say:

I could not find relevant information in the provided knowledge base.

Thresholds help retrieval systems know when not to answer.

That is just as important as knowing when to answer.

---

# Metadata Still Matters

Vector similarity is powerful, but metadata can improve search.

Metadata might include:

- document type

- author

- date

- department

- product area

- access permissions

- language

For example, if a user asks about the refund policy for Europe, metadata can help filter documents by region.

Without metadata, the system might retrieve a similar but wrong policy.

Good retrieval often combines vector similarity with filters.

---

# Mini Project

Think of a question:

How do I cancel my plan?

Now imagine three documents:

1. Canceling your subscription

2. Resetting your password

3. Updating billing address

Rank them by semantic similarity to the question.

You would likely choose:

1. Canceling your subscription

2. Updating billing address

3. Resetting your password

That ranking is what vector search tries to do mathematically.

---

# Key Takeaways

- AI systems compare meaning by comparing embedding vectors.

- Similar vectors usually represent similar meanings.

- Common similarity methods include cosine similarity, dot product, and Euclidean distance.

- Similarity helps retrieve relevant content, but it does not guarantee truth.

- Top-K controls how many results are retrieved.

- Similarity thresholds help avoid weak matches.

- Metadata filters make retrieval more precise.

---

# What's Next

Now that we understand semantic search and vector similarity, we need a place to store and search embeddings efficiently.

That brings us to vector databases.

In the next article, we will explore:

# What Is a Vector Database?
