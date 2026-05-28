---
title: "Prompting for Better Reasoning"
description: "LLMs are often used for reasoning tasks."
order: 18
season: 2
slug: "18-prompting-for-better-reasoning"
pubDate: "2026-01-18"
---
LLMs are often used for reasoning tasks.

People ask them to:

- compare options

- debug problems

- explain tradeoffs

- plan projects

- analyze decisions

- identify risks

- solve coding issues

Sometimes the results are impressive.

Sometimes they are shallow, overconfident, or wrong.

The difference often comes down to how the task is framed.

Prompting for better reasoning is not about forcing the model to sound smarter.

It is about giving the model a better process.

<p class="section-break">. . .</p>

## Reasoning Needs Structure

If you ask:

What should I do?

the model may give a generic answer.

But if you ask:

Compare these three options using cost, complexity, risk, and long-term maintainability. State your assumptions, then give a recommendation.

the model has a structure to follow.

Reasoning improves when the prompt defines:

- the options

- the criteria

- the assumptions

- the constraints

- the desired output

Without structure, the model may produce a fluent opinion instead of a useful analysis.

<p class="section-break">. . .</p>

## Ask For Assumptions

One of the best ways to improve reasoning is to ask the model to state assumptions.

Example:

Before giving a recommendation, list the assumptions you are making.

This is useful because many answers depend on hidden assumptions.

For example, if you ask which database to use, the answer depends on:

- data size

- traffic

- consistency needs

- team experience

- budget

- deployment environment

If those details are missing, the model must assume them.

Asking for assumptions makes that visible.

Visible assumptions are easier to review.

<p class="section-break">. . .</p>

## Ask For Tradeoffs

Good engineering decisions involve tradeoffs.

There is rarely one perfect answer.

Prompt:

Compare using a managed vector database versus Postgres with vector search. Include tradeoffs for cost, operational complexity, scaling, and developer experience.

This kind of prompt produces a more useful answer than:

Which vector database is best?

The word "best" is often too vague.

Best for what?

A tradeoff prompt forces the model to compare dimensions.

That is closer to real engineering thinking.

<p class="section-break">. . .</p>

## Ask For Risks

Models often produce optimistic answers unless you ask for risks.

For planning tasks, include:

Identify major risks and mitigation steps.

For code tasks, include:

Identify edge cases and failure modes.

For product tasks, include:

List user experience risks and operational risks.

Risk prompts help uncover issues that a simple answer might skip.

This does not guarantee the model catches everything.

But it improves the odds.

<p class="section-break">. . .</p>

## Ask For A Decision Framework

When a problem is complex, ask the model to create a decision framework.

Example:

Create a decision framework for choosing between fine-tuning, RAG, and prompt engineering. Use criteria such as data freshness, cost, latency, privacy, and maintenance.

A framework helps organize the answer.

Instead of jumping to a conclusion, the model evaluates the problem through criteria.

This is useful for:

- architecture decisions

- tool selection

- vendor comparisons

- project prioritization

- debugging strategies

Structured reasoning beats vague advice.

<p class="section-break">. . .</p>

## Ask The Model To Challenge The Answer

Another useful technique is asking the model to critique its own recommendation.

For example:

After giving the recommendation, identify the strongest argument against it.

This helps reduce one-sided answers.

It is especially useful when the model gives a confident recommendation too quickly.

You can also ask:

What information is missing that would make this recommendation stronger?

That question is valuable because many real decisions are limited by incomplete information.

A good reasoning assistant should not only answer.

It should also show what would need to be verified.

This makes the output more useful for engineering decisions, product planning, and debugging.

<p class="section-break">. . .</p>

## Break Large Problems Into Smaller Parts

LLMs often perform better when large tasks are decomposed.

Instead of:

Design an AI assistant for my company.

Try:

First, identify the user groups and their top workflows. Then propose the assistant capabilities. Then list data sources needed. Then identify risks and evaluation criteria.

This gives the model a path.

Each step builds on the previous one.

Large reasoning tasks need scaffolding.

Scaffolding is just structure that helps the model stay organized.

<p class="section-break">. . .</p>

## Be Careful With "Think Step By Step"

You may have seen prompts that say:

Think step by step.

This can sometimes help.

But it is not magic.

A better approach is to define the steps you actually want.

For example:

Analyze the issue in this order:

1. Restate the problem.

2. Identify likely causes.

3. Rank causes by probability.

4. Suggest tests to confirm each cause.

5. Recommend the first fix to try.

This is stronger than simply asking the model to think step by step.

You are giving it an engineering process.

<p class="section-break">. . .</p>

## Reasoning Still Needs Verification

LLM reasoning can be useful, but it is not guaranteed.

The model may:

- miss facts

- make weak assumptions

- overstate confidence

- ignore edge cases

- choose the wrong criteria

- produce plausible but flawed logic

That is why reasoning outputs should be reviewed.

For code, run tests.

For architecture, check constraints.

For research, verify sources.

For business decisions, compare against real data.

Prompting improves reasoning, but verification still matters.

<p class="section-break">. . .</p>

## A Practical Reasoning Prompt Template

Use this template:

I need help reasoning through a decision.

Goal:

Options:

Constraints:

Criteria:

Known facts:

Please:

1. State assumptions.

2. Compare options across the criteria.

3. Identify risks.

4. Recommend a path.

5. Explain what would change your recommendation.

That last line is important.

It shows which facts matter most.

Good reasoning should be conditional, not blindly confident.

<p class="section-break">. . .</p>

## Mini Project

Pick a real decision:

- which course to take next

- which project to build

- which framework to use

- which AI feature to prioritize

Write a reasoning prompt using:

- goal

- options

- constraints

- criteria

- assumptions

- risks

Then review the answer.

Ask yourself:

Did the model reason, or did it just sound reasonable?

That distinction matters.

<p class="section-break">. . .</p>

## Key Takeaways

- Reasoning prompts need structure.

- Ask for assumptions to reveal hidden guesses.

- Ask for tradeoffs instead of vague "best" answers.

- Ask for risks and failure modes.

- Break large problems into smaller steps.

- Define the reasoning process instead of relying on magic phrases.

- Always verify important reasoning outputs.

<p class="section-break">. . .</p>

## What's Next

Reasoning prompts are useful across many domains.

One of the most practical domains is software engineering.

In the next article, we will focus on:

## Prompting for Code Generation
