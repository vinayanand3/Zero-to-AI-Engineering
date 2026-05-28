---
title: "How Do LLMs Actually Generate Text?"
description: "In the previous article, we looked at why transformers changed AI forever."
order: 5
season: 1
slug: "05-how-do-llms-actually-generate-text"
pubDate: "2026-01-05"
---
In the previous article, we looked at why transformers changed AI forever.

We saw that transformers gave AI systems a new way to understand relationships between tokens using attention.

That breakthrough made modern Large Language Models possible.

But now we need to answer the question most people are really curious about:

# How does an LLM actually generate text?

When you ask ChatGPT a question, it feels like the model is thinking, reasoning, and writing a response the way a human would.

But underneath the surface, something more specific is happening.

The model is not pulling a finished answer from a database.

It is not searching the internet by default.

It is not remembering a perfect copy of every article it has ever seen.

At the core, an LLM is doing one surprisingly simple thing:

> It predicts the next token.

That idea sounds almost too small to explain modern AI.

But once you understand it properly, LLMs become much less mysterious.

---

# The Simplest Mental Model

Imagine I write this sentence:

The capital of France is

Your brain immediately expects the next word to be:

Paris

Why?

Because you have seen enough language, facts, and patterns to know what usually comes next.

LLMs work in a similar direction.

They receive a sequence of tokens and predict what token is most likely to come next.

Then they add that token to the sequence.

Then they predict the next token again.

Then again.

And again.

This repeated process creates the full response.

So when an LLM writes a paragraph, it is not generating the entire paragraph in one step.

It is building the answer token by token.

---

# What Is a Token Again?

Before going further, remember that LLMs do not directly operate on words.

They operate on tokens.

A token can be:

- a full word

- part of a word

- punctuation

- a space pattern

- a symbol

For example, the sentence:

Artificial intelligence is powerful.

might be broken into tokens like:

- Artificial

- intelligence

- is

- powerful

- .

In other cases, a longer word may be split into smaller pieces.

The important point is this:

The model reads tokens, processes tokens, and predicts tokens.

Text generation is really token generation.

---

# The Next-Token Prediction Loop

Here is the basic generation loop:

1. You give the model some input.

2. The input is converted into tokens.

3. The transformer processes those tokens.

4. The model predicts likely next tokens.

5. One token is selected.

6. That token is added to the text.

7. The process repeats.

For example:

Prompt:

The best way to learn AI is

Possible next tokens:

- to

- by

- through

- practice

- understanding

The model assigns probabilities to possible next tokens.

Maybe it decides "to" is most likely.

Now the text becomes:

The best way to learn AI is to

Then the model predicts again.

Possible next tokens:

- build

- start

- understand

- practice

Maybe it chooses "build."

Now the text becomes:

The best way to learn AI is to build

Repeat this thousands of times, and you get a full answer.

---

# Where Do The Probabilities Come From?

This is where training matters.

During training, the model is shown enormous amounts of text.

Books.

Articles.

Code.

Documentation.

Conversations.

Web pages.

The model is repeatedly given a sequence and asked:

What token should come next?

If the model predicts incorrectly, its internal weights are adjusted.

Over time, it becomes better at predicting patterns in language.

Not just grammar.

Also:

- facts

- style

- reasoning patterns

- code structure

- explanations

- question-answer formats

- relationships between ideas

This is why next-token prediction becomes powerful.

The task sounds simple, but the patterns required to do it well are extremely rich.

To predict the next token in a complex answer, the model often needs to represent meaning, context, structure, and reasoning.

---

# A Simple Example

Suppose the prompt is:

Explain neural networks to a beginner.

The model might start by predicting:

A

Then:

neural

Then:

network

Then:

is

Then:

a

Then:

system

Eventually, the output becomes:

A neural network is a system that learns patterns from data.

This feels like a complete sentence because each token was selected based on the previous context.

The model is constantly asking:

Given everything so far, what token should come next?

That is the engine behind generation.

---

# Is The Model Just Guessing?

In one sense, yes.

But it is not guessing randomly.

It is making a highly informed prediction based on patterns learned during training.

Think about autocomplete on your phone.

If you type:

I am going to the grocery

your phone might suggest:

store

That is next-word prediction.

LLMs are a much more powerful version of this idea.

They predict across much larger contexts, with much deeper representations, and with far more learned knowledge.

Phone autocomplete predicts common phrases.

LLMs predict language using deep patterns about the world, code, reasoning, and communication.

---

# Why Responses Can Be Different Each Time

If next-token prediction is based on probabilities, there may be several reasonable next tokens.

For example:

AI is changing the world by

Possible continuations:

- automating tasks

- improving productivity

- transforming software

- helping people learn

All of these are reasonable.

The model does not always have to pick the single most likely token.

Depending on settings, it may sample from multiple likely options.

This is why the same prompt can produce different answers.

The model is not always following one fixed path.

It is moving through a probability landscape.

Some paths are more likely.

Some are more creative.

Some are less reliable.

This is also why generation settings matter.

Higher randomness can make outputs more creative.

Lower randomness can make outputs more predictable.

---

# Why This Creates The Illusion Of Thinking

When an LLM generates a thoughtful answer, it can feel like the system is thinking in the human sense.

But what we are seeing is a learned language system producing structured output from context.

It has learned patterns like:

- how explanations are organized

- how arguments are built

- how code is written

- how questions are answered

- how reasoning usually appears in text

This does not mean the model has human consciousness.

It means the model has learned extremely powerful statistical and semantic patterns.

That distinction matters.

LLMs can produce useful reasoning-like behavior.

But they can also make mistakes with confidence.

That is because they are generating likely text, not directly verifying truth at every step.

We will return to this later when we discuss hallucinations.

---

# Real-World Usage Examples

Next-token prediction powers many things people now use daily:

- chat assistants

- code completion

- email drafting

- document summarization

- search answer generation

- tutoring systems

- customer support bots

- agent planning

In every case, the system receives context and generates useful continuation text.

The context may be a question, a document, a code file, a conversation, or a tool result.

The output is still produced token by token.

---

# Mini Project

Try this exercise manually.

Write this phrase:

The most important thing about AI engineering is

Now list five possible next words:

- understanding

- building

- learning

- systems

- practice

Then choose one and continue the sentence.

At each step, ask:

What would be a reasonable next word?

You are doing a tiny human version of next-token prediction.

Of course, an LLM does this with billions of learned parameters and thousands of tokens of context.

But the core loop is similar.

---

# Key Takeaways

- LLMs generate text one token at a time.

- The core task is next-token prediction.

- Tokens are pieces of text, not always full words.

- The model assigns probabilities to possible next tokens.

- Training teaches the model patterns in language, code, facts, and reasoning.

- Different outputs can happen because generation can sample from multiple likely paths.

- LLMs can appear to think, but they are generating likely continuations from context.

---

# What's Next

Now that we understand that LLMs generate text using tokens, we need to slow down and understand tokens properly.

Because tokens are the hidden language of LLMs.

They affect cost.

They affect context windows.

They affect how models read text.

And they explain many strange behaviors beginners notice when using AI systems.

In the next article, we will answer:

# What Are Tokens?

