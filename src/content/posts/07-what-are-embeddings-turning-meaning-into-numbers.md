---
title: "What Are Embeddings? Turning Meaning Into Numbers"
description: "In the previous article, we learned that LLMs process tokens."
order: 7
season: 1
slug: "07-what-are-embeddings-turning-meaning-into-numbers"
pubDate: "2026-01-07"
---
In the previous article, we learned that LLMs process tokens.

Tokens are the pieces of text that enter the model.

But tokens by themselves are not enough.

A model needs more than pieces.

It needs meaning.

It needs a way to understand that:

- "dog" is closer to "puppy" than to "airplane"

- "doctor" is related to "hospital"

- "Python" might mean a programming language or a snake depending on context

- "AI engineering" is connected to models, data, prompts, systems, and deployment

So how does a machine represent meaning?

The answer is:

# embeddings

Embeddings are one of the most important ideas in modern AI.

They are also one of the first concepts that feels abstract to beginners.

But the core intuition is simple:

> An embedding turns meaning into numbers.

---

# Why Meaning Needs To Become Numbers

Computers do not naturally understand words.

They understand numbers.

So if we want a model to work with language, we need to convert language into numerical form.

But not just any numbers.

We need numbers that preserve relationships.

For example, suppose we assign random numbers:

- cat = 17

- dog = 942

- pizza = 31

- tiger = 508

These numbers do not tell us anything useful.

They do not show that cats and dogs are both animals.

They do not show that cats and tigers are related.

They do not represent meaning.

Embeddings solve this by placing concepts into a numerical space where similar ideas are closer together.

---

# The Map Analogy

Imagine a map.

On a normal map, cities have locations.

New York is closer to Boston than to Tokyo.

San Francisco is closer to Los Angeles than to London.

Distance on the map means something.

Embeddings work like a map of meaning.

Instead of placing cities in geographic space, embeddings place words, sentences, or documents in semantic space.

In that space:

- "cat" is near "dog"

- "doctor" is near "nurse"

- "king" is near "queen"

- "database" is near "storage"

- "transformer" is near "attention"

The distance between embeddings tells us something about similarity.

That is the big idea.

---

# What Does An Embedding Look Like?

An embedding is usually a list of numbers.

For example:

cat might become something like:

[0.12, -0.45, 0.88, 0.31, ...]

In real systems, embeddings often have hundreds or thousands of dimensions.

A dimension is just one position in that list of numbers.

You do not usually interpret each number directly.

Instead, the full vector captures meaning as a pattern.

This is similar to how a face is not defined by one pixel.

A face is represented by the pattern across many pixels.

An embedding represents meaning through the pattern across many numbers.

---

# Words, Sentences, And Documents Can All Have Embeddings

Embeddings are not limited to single words.

Modern AI systems can create embeddings for:

- tokens

- words

- sentences

- paragraphs

- documents

- images

- audio

- code

This is extremely powerful.

If two paragraphs discuss similar ideas, their embeddings can be close together even if they use different words.

For example:

"How do I reset my password?"

and

"I cannot log into my account."

These sentences do not use the exact same words.

But they are semantically related.

Embeddings help AI systems recognize that relationship.

---

# Why Embeddings Matter For LLMs

Inside an LLM, tokens are converted into numerical representations before the transformer processes them.

The model cannot perform attention over raw text.

It needs vectors.

Embeddings give the model a starting representation of each token.

Then the transformer layers update those representations based on context.

For example, consider the word:

bank

In one sentence:

I deposited money at the bank.

In another sentence:

The boat stopped near the river bank.

The same word has different meanings.

Modern models use context to adjust the representation.

That is why embeddings and transformers work together.

Embeddings provide numerical meaning.

Attention updates that meaning based on surrounding tokens.

---

# Real-World Usage Examples

Embeddings are used far beyond text generation.

They power many practical AI systems.

Search is one major example.

Traditional search often looks for exact keyword matches.

If you search for "cheap laptop," it may look for pages containing those exact words.

Semantic search is different.

It uses embeddings to search by meaning.

So a search for:

affordable computer for college

might find documents about:

budget laptops for students

even though the exact words are different.

This is one of the reasons embeddings are central to modern AI applications.

They help systems compare meaning, not just text.

---

# Embeddings And Recommendations

Embeddings also help recommendation systems.

Imagine a movie platform.

Each movie can be represented as an embedding based on:

- genre

- plot

- actors

- user behavior

- themes

Each user can also be represented based on what they watch.

If a user's embedding is close to certain movie embeddings, the system may recommend those movies.

The same idea applies to:

- products

- songs

- articles

- courses

- jobs

- code examples

Embeddings create a way to compare complex things numerically.

---

# Visual Explanation

Imagine a giant invisible space.

Every concept has a location.

Animals cluster in one region.

Programming concepts cluster in another.

Medical terms cluster somewhere else.

Concepts that share meaning are near each other.

Concepts that are unrelated are farther apart.

When we create an embedding, we are giving a concept coordinates in that space.

Those coordinates are not latitude and longitude.

They are long lists of numbers.

But the intuition is the same:

Location represents relationship.

---

# Mini Project

Try this mental exercise.

Group these words by meaning:

- car

- truck

- banana

- apple

- Python

- JavaScript

- hospital

- nurse

You would probably group them as:

- vehicles: car, truck

- fruit: banana, apple

- programming: Python, JavaScript

- healthcare: hospital, nurse

Embeddings allow machines to form similar groupings numerically.

The machine does not need to use your exact category labels.

It learns relationships from patterns in data.

---

# Key Takeaways

- Embeddings turn meaning into numbers.

- An embedding is usually a vector, which is a list of numbers.

- Similar meanings have embeddings that are close together.

- Embeddings can represent words, sentences, documents, images, audio, and code.

- LLMs use embeddings to convert tokens into numerical representations.

- Semantic search and recommendations rely heavily on embeddings.

- Embeddings are a foundation for later topics like vector databases and RAG.

---

# What's Next

We now understand three important pieces:

- tokens are how text is broken down

- embeddings are how meaning becomes numerical

- transformers process those representations using attention

But there is another distinction beginners often miss.

There is a big difference between teaching a model and using a model.

In the next article, we will explore:

# Training vs Inference

