---
title: "What Are Tokens? The Hidden Language of LLMs"
description: "In the previous article, we learned that Large Language Models generate text by predicting the next token."
order: 6
season: 1
slug: "06-what-are-tokens-the-hidden-language-of-llms"
pubDate: "2026-01-06"
---
#### What Are Tokens? The Hidden Language of LLMs

In the previous article, we learned that Large Language Models generate text by predicting the next token.

That raises an obvious question:

#### What exactly is a token?

Most beginners assume LLMs read words the same way humans do.

But they do not.

When you type a prompt into ChatGPT, Claude, Gemini, or any other LLM, the model does not directly see sentences, paragraphs, or words.

It sees tokens.

Tokens are the hidden units of language inside modern AI systems.

And once you understand them, many confusing parts of LLMs start making sense.

Why do models have context limits?

Why does pricing depend on input and output size?

Why can one short word sometimes become multiple pieces?

Why do models sometimes struggle with character counting?

The answer often comes back to tokens.

<p class="section-break">. . .</p>

#### The Simplest Definition

A token is a small piece of text that an AI model uses as a basic unit.

A token can be:

- a word
- part of a word
- punctuation
- a number
- a symbol
- a space plus a word

For example:

The sentence:

AI engineering is practical.

might become something like:

- AI
- engineering
- is
- practical
- .

That looks simple.

But tokenization is not always that clean.

A word like “unbelievable” might be split into:

- un
- believable

Or a technical word might be split into even smaller pieces.

The model does not care whether humans consider something a full word.

It cares about the token pieces created by its tokenizer.

<p class="section-break">. . .</p>

#### Why Do LLMs Use Tokens Instead Of Words?

Human language is messy.

There are:

- millions of possible words
- names
- slang terms
- code symbols
- URLs
- emojis
- misspellings
- new technical terms

If a model only understood full words, it would constantly run into unknown words.

Tokens solve this problem.

Instead of needing every possible word, the model can combine smaller pieces.

For example, if it understands pieces like:

- auto
- bio
- graph
- y

it can handle words related to autobiography, biography, and graph-based terms more flexibly.

Tokenization gives models a practical way to process open-ended language.

<p class="section-break">. . .</p>

#### Tokenization Is Like Cutting Text Into Lego Pieces

One useful analogy is Lego blocks.

You do not need a unique Lego piece for every possible building.

You need a set of reusable pieces that can be combined in many ways.

Tokens work similarly.

The tokenizer breaks text into reusable pieces.

The model then learns patterns between those pieces.

Some pieces are common:

- the
- and
- is
- to

Some are technical:

- function
- import
- transformer
- embedding

Some are fragments:

- ing
- tion
- pre
- sub

This lets the model work with normal language, code, math expressions, and strange inputs using the same general system.

<p class="section-break">. . .</p>

#### Tokens And Cost

Many AI APIs charge based on tokens.

Usually there are two categories:

- input tokens
- output tokens

Input tokens are the tokens you send to the model.

Output tokens are the tokens the model generates back.

For example, if you paste a long document into a prompt, that document becomes input tokens.

If the model writes a long response, that response becomes output tokens.

This matters because every token requires computation.

The more tokens the model processes, the more work it has to do.

That is why short prompts are usually cheaper than long prompts.

It is also why summarizing a large document costs more than asking a short factual question.

Tokens are not just a technical detail.

They are part of the economics of AI systems.

<p class="section-break">. . .</p>

#### Tokens And Context Windows

Tokens also explain context windows.

A context window is the maximum amount of text a model can consider at once.

But that limit is usually measured in tokens, not words.

For example, a model might support:

- 8,000 tokens
- 32,000 tokens
- 128,000 tokens
- 1 million tokens

This means the model can process that many tokens in the conversation or request.

If the input becomes too large, something has to happen.

The system may:

- reject the request
- truncate older text
- summarize earlier context
- require a smaller input

This is why long conversations can eventually lose earlier details.

The model is not carrying infinite memory.

It is working within a token budget.

<p class="section-break">. . .</p>

#### Tokens And Strange Model Behavior

Tokens also explain why LLMs sometimes struggle with tasks that seem simple to humans.

For example:

How many letters are in the word “**strawberry**”?

Humans see individual letters clearly.

But the model may not process the word as separate letters.

It may process it as one token or a few subword tokens.

So character-level tasks can be awkward.

The model is not naturally counting letters the way you do.

It is operating on token pieces.

This is also why prompts involving exact formatting, hidden characters, or unusual spacing can behave unexpectedly.

The token representation may not match your visual intuition.

<p class="section-break">. . .</p>

#### Tokens In Code

Tokens are especially important in coding assistants.

Code contains:

- variable names
- punctuation
- indentation
- symbols
- operators
- brackets
- comments

A line like:

def calculate_total(price, tax):

is broken into tokens too.

The model learns patterns in code tokens the same way it learns patterns in language tokens.

This is why LLMs can complete functions, explain errors, and generate code.

They have learned the statistical structure of code.

They know which token sequences commonly appear in working programs.

<p class="section-break">. . .</p>

#### Visual Explanation

Imagine a three-step pipeline:

Text you type

Tokenization

Model processing

The model never directly receives your raw sentence in the human sense.

Your sentence is first converted into token IDs.

Each token maps to a number.

Then the model processes those numbers.

So the actual flow is:

**Human text -> tokens -> token IDs -> model -> predicted token IDs -> tokens -> human text**

This is one of the most important hidden pipelines in LLM systems.

The model lives in numbers.

The tokenizer is the bridge between human language and model computation.

<p class="section-break">. . .</p>

#### Mini Project

Try this simple exercise.

Write three prompts:

1. A short question.
2. A long paragraph.
3. A code snippet.

Now estimate which one will use the most tokens.

Usually, the long paragraph and code snippet will use more tokens than the short question.

Then think about how that affects:

- cost
- speed
- context size
- model attention

This is the beginning of thinking like an AI engineer.

You are not only asking, “What should I prompt?”

You are asking, “How much information am I asking the system to process?”

<p class="section-break">. . .</p>

#### Key Takeaways

- LLMs process tokens, not raw words.
- A token can be a word, part of a word, punctuation, or symbol.
- Tokenization converts text into model-readable pieces.
- Tokens affect cost, speed, and context limits.
- Context windows are measured in tokens.
- Some strange LLM behavior comes from the difference between human text and tokenized text.
- Tokenization is the bridge between language and computation.

<p class="section-break">. . .</p>

#### What’s Next

Tokens explain how text enters the model.

But tokens alone are not enough.

The model also needs a way to represent meaning.

It needs to understand that “car” and “vehicle” are related.

It needs to know that “king” and “queen” are connected.

It needs to compare concepts numerically.

That brings us to one of the most important ideas in modern AI:

#### Embeddings
