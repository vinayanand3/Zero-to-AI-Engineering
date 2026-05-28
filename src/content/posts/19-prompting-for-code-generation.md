---
title: "Prompting for Code Generation"
description: "Code generation is one of the most useful applications of LLMs."
order: 19
season: 2
slug: "19-prompting-for-code-generation"
pubDate: "2026-01-19"
---
Code generation is one of the most useful applications of LLMs.

Modern AI tools can:

- write functions

- explain code

- generate tests

- debug errors

- refactor files

- create scripts

- review pull requests

But coding with AI is not the same as asking the model to "write code" and trusting whatever comes back.

Good code prompts require context, constraints, and verification.

The model can accelerate you.

It should not replace engineering judgment.

<p class="section-break">. . .</p>

## The Weak Prompt Problem

Consider this prompt:

Write a login system.

That is far too broad.

What language?

What framework?

What database?

What authentication method?

What security requirements?

What UI?

What error handling?

What tests?

The model may produce something that looks useful but does not fit your actual project.

In code generation, missing context is especially dangerous because code can look correct while being wrong.

<p class="section-break">. . .</p>

## A Better Coding Prompt

A stronger prompt would be:

Write a TypeScript function that validates a password reset token. The function should accept a token string and current timestamp, check whether the token exists, verify it has not expired, and return a typed result object. Do not use external libraries. Include tests for valid token, expired token, missing token, and malformed token.

This prompt gives:

- language

- task

- input

- behavior

- constraints

- output expectation

- test cases

The model now has a much clearer target.

<p class="section-break">. . .</p>

## Provide Existing Code Context

If you are working inside an existing project, include relevant code.

The model needs to see:

- function signatures

- types

- imports

- framework conventions

- error messages

- related files

- expected behavior

Bad prompt:

Fix this function.

Better prompt:

Fix the function below. It currently throws when the input array is empty. The expected behavior is to return an empty array. Keep the public function signature unchanged. Add one test for the empty input case.

Then include the function.

This helps the model make a focused change instead of inventing a new design.

<p class="section-break">. . .</p>

## Specify Constraints

Code exists inside constraints.

Your prompt should mention them.

Examples:

- use Python standard library only

- keep this compatible with Node 20

- do not change the public API

- preserve existing behavior

- follow React hooks rules

- use async and await

- avoid global state

- do not add dependencies

Constraints prevent the model from choosing solutions that are technically possible but wrong for your project.

This is especially important in production codebases.

<p class="section-break">. . .</p>

## Ask For Tests

One of the best coding prompt habits is asking for tests.

Example:

Implement the function and include unit tests for normal input, empty input, invalid input, and duplicate values.

Tests force the model to think about behavior.

They also give you a way to verify the result.

AI-generated code without tests may still be useful, but it is harder to trust.

The test suite is where plausible code meets reality.

<p class="section-break">. . .</p>

## Ask For Edge Cases

Models often handle the happy path first.

That is not enough.

Ask for edge cases explicitly.

Examples:

- empty input

- null or undefined values

- duplicate records

- invalid dates

- network failures

- permission errors

- large inputs

- timeout behavior

Prompt:

Before writing the code, list the edge cases this function should handle. Then implement the function and tests.

This helps surface hidden requirements.

<p class="section-break">. . .</p>

## Ask For Small Changes First

When working in an existing codebase, avoid asking the model to rewrite too much at once.

Large code changes are harder to review and easier to get wrong.

A better pattern is:

Make the smallest change that fixes this bug.

Or:

Add this behavior without changing the public API.

Small prompts create smaller diffs.

Smaller diffs are easier to test, review, and revert.

This matters in real engineering work.

AI can generate a lot of code quickly, but more code is not automatically better.

The best AI coding prompts often narrow the task so the model changes only what needs to change.

<p class="section-break">. . .</p>

## Be Careful With Invented APIs

LLMs sometimes invent functions, packages, or methods that look real.

This is common when working with:

- newer libraries

- changing APIs

- framework-specific behavior

- cloud services

- internal code

If the model suggests an API, verify it.

For current documentation, use official docs.

For local code, search the repo.

For generated code, run it.

Never assume an import exists just because the model wrote it confidently.

<p class="section-break">. . .</p>

## Use The Model For Review

Code prompting is not only for generation.

You can also ask the model to review code.

Example:

Review this function for correctness, edge cases, readability, and security risks. Do not rewrite it yet. First list issues with line references and explain why each issue matters.

This separates review from implementation.

It can help you see problems before editing.

You can also ask:

What tests are missing?

What assumptions does this code make?

Where could this fail in production?

These prompts build engineering judgment.

<p class="section-break">. . .</p>

## A Practical Code Prompt Template

Use this structure:

Task:

Language and framework:

Existing code:

Expected behavior:

Constraints:

Edge cases:

Tests required:

Output format:

For example:

Task: Add pagination to this function.

Language and framework: TypeScript, Express.

Existing code: paste function.

Expected behavior: support page and pageSize query parameters.

Constraints: do not change response field names.

Edge cases: missing page, invalid page, pageSize above 100.

Tests required: include unit tests for each edge case.

Output format: show code first, then explain changes.

<p class="section-break">. . .</p>

## Mini Project

Choose a small coding task.

Write two prompts:

1. A vague prompt.

2. A structured prompt using the template above.

Compare the generated code.

Then run or mentally review:

- Does it compile?

- Does it handle edge cases?

- Does it use real APIs?

- Does it fit the project constraints?

This is how you turn AI coding from guessing into engineering.

<p class="section-break">. . .</p>

## Key Takeaways

- Code prompts need context, constraints, and expected behavior.

- Include relevant existing code when working in a real project.

- Ask for tests and edge cases.

- Be careful with invented APIs.

- Use AI for review, not just generation.

- Always verify generated code with tests, linters, compilers, or runtime checks.

- AI coding is most powerful when paired with engineering discipline.

<p class="section-break">. . .</p>

## What's Next

Code is one kind of structured output.

But AI systems often need many structured formats:

- JSON

- tables

- checklists

- summaries

- schemas

In the next article, we will explore:

## Prompting for Structured Outputs
