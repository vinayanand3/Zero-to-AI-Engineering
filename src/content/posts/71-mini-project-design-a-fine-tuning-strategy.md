---
title: "Mini Project: Design a Fine-Tuning Strategy"
description: "We have covered finetuning, data, instruction tuning, LoRA, quantization, evaluation, failure modes, and optimization."
order: 71
season: 6
slug: "71-mini-project-design-a-fine-tuning-strategy"
pubDate: "2026-03-12"
---
We have covered fine-tuning, data, instruction tuning, LoRA, quantization, evaluation, failure modes, and optimization.

Now let us combine those ideas into a practical design exercise.

The goal is not to train a model in this article.

The goal is to design a fine-tuning strategy.

Good AI engineers do not start by running training.

They start by understanding the problem, choosing the right technique, preparing data, and defining evaluation.

That is what we will practice here.

<p class="section-break">. . .</p>

## The Scenario

Imagine a customer support team has a problem.

They receive thousands of support messages every week.

They want an AI system that can classify each message into one of these categories:

- Billing

- Bug

- Feature Request

- Account Access

- Cancellation

- Other

The current prompt-based system works, but it is inconsistent.

Similar messages sometimes get different labels.

The team wants better consistency.

Should they fine-tune?

Maybe.

Let's design the strategy.

<p class="section-break">. . .</p>

## Step 1: Diagnose The Problem

First, define the failure.

The issue is not missing knowledge.

The categories are known.

The issue is repeated classification behavior.

This is a reasonable fine-tuning candidate.

But before fine-tuning, we should check:

- can better prompting fix it?

- can few-shot examples improve it?

- can output validation catch invalid labels?

- are category definitions clear?

Fine-tuning should not be used to hide unclear taxonomy.

If humans do not agree on labels, the model will struggle too.

<p class="section-break">. . .</p>

## Step 2: Define Label Rules

Before creating data, define each label.

Example:

Billing:

Payment issues, invoice questions, refund questions, failed charges.

Bug:

Something is broken or not working as expected.

Feature Request:

The user asks for new functionality or improvement.

Account Access:

Login, password, account recovery, permission issues.

Cancellation:

The user wants to cancel, downgrade, or stop service.

Other:

Anything that does not fit.

Clear definitions improve label consistency.

<p class="section-break">. . .</p>

## Step 3: Build The Dataset

Now collect examples.

For each support message, create:

Input:

Customer message.

Output:

Correct label.

The dataset should include:

- common examples

- edge cases

- short messages

- long messages

- mixed intent messages

- ambiguous messages

- examples for every category

Do not only collect easy examples.

Real support messages are messy.

The dataset should reflect that.

<p class="section-break">. . .</p>

## Step 4: Clean And Review

Before training, clean the dataset.

Remove duplicates.

Fix incorrect labels.

Standardize output format.

Remove sensitive customer information.

Check category balance.

Review ambiguous examples with humans.

This step may take more time than training.

That is normal.

Fine-tuning quality depends heavily on data quality.

<p class="section-break">. . .</p>

## Step 5: Create A Test Set

Set aside examples for evaluation.

The model should not train on these.

The test set should include:

- normal cases

- edge cases

- ambiguous messages

- mixed intent messages

- out-of-scope messages

For each test example, define the expected label.

This lets you compare:

- original prompt-based system

- improved prompt

- fine-tuned model

Fine-tuning should beat the baseline enough to justify complexity.

<p class="section-break">. . .</p>

## Step 6: Choose The Adaptation Method

Now decide how to adapt.

Options:

- full fine-tuning

- LoRA

- no fine-tuning, better prompting only

For a classification task, LoRA or another efficient adaptation method may be enough.

The best choice depends on:

- model size

- available infrastructure

- cost

- data volume

- deployment constraints

The strategy should be practical, not just technically impressive.

<p class="section-break">. . .</p>

## Step 7: Evaluate And Monitor

After training, evaluate:

- label accuracy

- per-category accuracy

- confusion between labels

- invalid output rate

- performance on edge cases

- latency

- cost

Then monitor after deployment.

Real messages may differ from the test set.

New product features may create new categories.

Customer language may change.

Fine-tuning is not one-and-done.

It needs maintenance.

<p class="section-break">. . .</p>

## Engineering Lens

When you finish the strategy, review it like an engineering design document.

Ask whether each decision has evidence behind it.

If the plan says fine-tuning is needed, point to examples that prompting and RAG failed to fix.

If the plan says LoRA is enough, explain why adapter-based deployment fits the workflow.

If the plan says quantization is acceptable, show how quality will be measured after compression.

If the plan says the dataset is ready, describe how it was cleaned and how label consistency was checked.

This turns the mini project from a theoretical exercise into a production-style proposal.

The best fine-tuning strategy is not the most ambitious one.

It is the one that identifies the smallest reliable change that solves the real problem.

## Mini Project

Use this same strategy for another task:

- email intent classification

- resume field extraction

- brand voice rewriting

- bug report severity classification

Write:

- problem

- labels or target format

- dataset design

- test set

- baseline

- fine-tuning method

- evaluation metrics

This is the real skill:

designing the fine-tuning workflow before training.

<p class="section-break">. . .</p>

## Key Takeaways

- Fine-tuning strategy starts with diagnosing the problem.

- Repeated classification behavior can be a good fine-tuning candidate.

- Label definitions must be clear.

- Dataset quality is critical.

- Test data should be separate from training data.

- Fine-tuning should be compared against prompting baselines.

- Evaluation should include edge cases, invalid outputs, latency, and cost.

- Deployment requires monitoring and maintenance.

<p class="section-break">. . .</p>

## What's Next

We have now covered the practical foundations of model adaptation.

In the final article of Season 6, we will connect everything into one mental model:

## The Mental Model of Model Adaptation
