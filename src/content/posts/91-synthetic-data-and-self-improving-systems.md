---
title: "Synthetic Data and Self-Improving Systems"
description: "AI systems need data."
order: 91
season: 8
slug: "91-synthetic-data-and-self-improving-systems"
pubDate: "2026-04-01"
---
AI systems need data.

But high-quality data can be expensive, limited, or hard to collect.

This is why synthetic data has become important.

Synthetic data is data generated artificially rather than collected directly from the real world.

For AI, that often means using models to create training examples, test cases, simulations, or variations.

Synthetic data can be useful.

It can also be risky.

If generated data is low quality, biased, or unrealistic, it can make systems worse.

So we need a careful mental model.

---

# The Simple Definition

Synthetic data is artificially generated data used for training, evaluation, or testing.

Examples:

- generated customer support tickets

- synthetic question-answer pairs

- simulated conversations

- generated code tasks

- paraphrased examples

- artificial edge cases

The goal is to expand or improve a dataset.

But generated data must still be checked.

Synthetic does not automatically mean good.

---

# Why Synthetic Data Helps

Synthetic data can help when real data is limited.

It can be used to:

- create more examples

- balance underrepresented categories

- generate edge cases

- simulate rare failures

- create evaluation questions

- augment instruction tuning data

For example, if a support classifier has very few Cancellation examples, synthetic examples may help expand that category.

But the examples should be reviewed.

Otherwise, the model may learn unrealistic patterns.

---

# Synthetic Data For Evaluation

Synthetic data can help create eval sets.

For example:

You can generate:

- adversarial prompts

- ambiguous questions

- unanswerable questions

- edge cases

- format stress tests

This is useful because teams often forget to test difficult cases.

Synthetic eval generation can reveal gaps.

But synthetic evals should not be the only evals.

Real user data is still important.

The best test sets often combine real and synthetic examples.

---

# Self-Training

Self-training is a pattern where a model helps generate or label data for further training.

For example:

The model labels many examples.

High-confidence examples are reviewed or filtered.

Those examples are used to train another model.

This can scale data creation.

But it can also amplify errors.

If the model labels examples incorrectly, the next model may learn those mistakes.

Self-training requires quality control.

---

# The Risk Of Model Collapse

If models train too heavily on low-quality synthetic data, quality can degrade.

The data may become less diverse.

Errors may reinforce themselves.

Outputs may become more generic.

This is one reason real data and human review remain important.

Synthetic data should improve coverage, not replace reality completely.

The goal is not just more data.

The goal is better learning signal.

---

# Quality Filters

Synthetic data needs filtering.

Useful checks include:

- correctness

- diversity

- realism

- label accuracy

- format validity

- bias review

- duplicate removal

- human sampling

Generated data should pass quality gates before training or evaluation.

Treat synthetic data like any other dataset:

inspect it, clean it, and test its effect.

---

# Engineering Lens

Synthetic data is useful when it expands coverage without replacing reality.

For example, you can generate variations of support tickets, edge cases for structured extraction, or adversarial examples for evaluation.

But synthetic data should be treated as a draft, not truth.

A generated example can contain hidden mistakes.

It can reflect the model's existing biases.

It can make the dataset look larger without making it more diverse.

This is why quality filters matter.

Use human review for important samples.

Compare synthetic data against real production data.

Track which examples are synthetic.

Test whether adding them actually improves performance.

Synthetic data is a tool for coverage, not a shortcut around judgment.

# Practical Example

Suppose your extraction system fails on unusual invoice formats.

You can generate synthetic invoices with different layouts, missing fields, odd vendor names, and messy line items.

Those examples may help test the system against more variety.

But you should still compare them with real invoices.

If the synthetic examples are too clean, they will not help.

If they are unrealistic, they may teach the system the wrong patterns.

Synthetic data is strongest when it is guided by real failure analysis.

# One More Check

Keep synthetic data labeled in your datasets.

If performance improves, you want to know which kind of data helped.

If performance gets worse, you need to trace the source of the bad examples.

This is especially important when synthetic examples are generated in batches.

One bad generation pattern can quietly spread through many samples.

# Mini Project

Design synthetic data for a support classifier.

Choose one underrepresented category.

Generate ten example messages.

Then review:

- are they realistic?

- are they diverse?

- are labels clear?

- are any examples too similar?

- would a human support agent agree?

This exercise shows why synthetic data needs review.

---

# Key Takeaways

- Synthetic data is artificially generated data.

- It can help with training, testing, and evaluation.

- Synthetic data can expand edge cases and underrepresented categories.

- Self-training can scale data creation but may amplify errors.

- Low-quality synthetic data can hurt models.

- Quality filters and human review are important.

- Real data and synthetic data should often be combined.

---

# What's Next

Another major advanced topic is alignment.

How do we train systems to behave in ways humans prefer and trust?

In the next article, we will explore:

# Alignment, RLHF, and Human Feedback
