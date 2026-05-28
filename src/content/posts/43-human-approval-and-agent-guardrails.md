---
title: "Human Approval and Agent Guardrails"
description: "Agents become more useful when they can act."
order: 43
season: 4
slug: "43-human-approval-and-agent-guardrails"
pubDate: "2026-02-12"
---
Agents become more useful when they can act.

They also become more risky.

An agent that only drafts text has limited downside.

An agent that can send emails, update databases, delete files, or charge credit cards needs stronger controls.

That is where human approval and guardrails come in.

Good agent design is not about giving the model unlimited freedom.

It is about giving the system the right amount of autonomy for the task.

Some actions can happen automatically.

Some actions should require approval.

Some actions should never be allowed.

<p class="section-break">. . .</p>

## Why Guardrails Matter

Agents can make mistakes.

They may misunderstand the user.

They may call the wrong tool.

They may pass incorrect arguments.

They may continue after a failure.

They may act on incomplete information.

If the action is low-risk, the mistake may be minor.

If the action is high-risk, the mistake can be serious.

Guardrails reduce the chance that model mistakes become real-world damage.

<p class="section-break">. . .</p>

## Read Actions vs Write Actions

A useful distinction is read actions versus write actions.

Read actions fetch information.

Examples:

- search documents

- read calendar availability

- look up order status

- inspect a file

Write actions change something.

Examples:

- send an email

- delete a file

- update a database

- create a calendar event

- issue a refund

Write actions are usually riskier.

They often need confirmation, permissions, or stricter validation.

<p class="section-break">. . .</p>

## Approval Points

An approval point is a moment where the agent must ask before continuing.

Examples:

- before sending an external email

- before deleting or overwriting files

- before making a purchase

- before publishing content

- before changing production data

- before contacting a customer

Approval points give humans control over important decisions.

The agent can prepare the action.

The human approves it.

Then the system executes.

This pattern is common in reliable agent workflows.

<p class="section-break">. . .</p>

## Risk Levels

Not every action needs the same level of control.

It helps to classify actions by risk.

Low risk:

- summarize a document

- search public information

- draft a message

Medium risk:

- update a task

- schedule a meeting

- add a note to a ticket

High risk:

- send an external email

- delete data

- issue a refund

- change production settings

Low-risk actions may be automatic.

High-risk actions should require stronger approval.

Risk levels make guardrails practical instead of vague.

<p class="section-break">. . .</p>

## Tool Permissions

Not every agent should have every tool.

A research agent may need search and document reading.

It does not need payment tools.

A customer support agent may need ticket lookup and policy search.

It may not need database write access.

Tool permissions should match the job.

This is the principle of least privilege.

Give the agent the minimum capabilities needed to complete the task.

Less access means less risk.

<p class="section-break">. . .</p>

## Validate Tool Arguments

Guardrails also include validation.

If the model calls:

send_email(to, subject, body)

the application should validate:

- is the recipient allowed?

- is the subject present?

- is the body present?

- does this require approval?

- is the user authorized?

The model should not be trusted to enforce all rules by itself.

Software should enforce important constraints.

Prompts guide behavior.

Code enforces boundaries.

<p class="section-break">. . .</p>

## Step Limits

Agents should often have step limits.

For example:

- maximum 10 tool calls

- maximum 3 retries

- maximum 5 minutes

- stop after repeated errors

Step limits prevent runaway loops.

They also control cost.

If an agent cannot finish within reasonable limits, it should stop and explain what happened.

This is better than silently looping or wasting resources.

<p class="section-break">. . .</p>

## Guardrails Should Be Tested

Guardrails are not useful if they only exist on paper.

They should be tested with realistic risky requests.

For example:

- ask the agent to send an email without confirmation

- ask it to delete important data

- ask it to access a restricted record

- ask it to continue after a tool error

The expected behavior should be clear.

The agent should refuse, ask for approval, or escalate depending on the case.

Testing guardrails early prevents surprises later.

Agent safety should be verified, not assumed.

Testing should include normal users and adversarial users.

Normal users reveal usability problems.

Adversarial users reveal whether the system can be pushed into unsafe behavior.

Both are useful before an agent is trusted with real actions.

<p class="section-break">. . .</p>

## Logging And Audit Trails

Agents should leave a record of important actions.

Logs may include:

- user request

- tools called

- arguments used

- approvals requested

- approvals granted

- results returned

- final outcome

For low-risk personal tools, simple logs may be enough.

For business systems, audit trails can be essential.

If something goes wrong, you need to know what happened.

<p class="section-break">. . .</p>

## Mini Project

Design guardrails for an email agent.

The agent can:

- draft emails

- search contacts

- summarize threads

- send emails

Decide:

- which actions are automatic

- which actions need approval

- which actions are forbidden

- what should be logged

- what validations are required

You will see that agent safety is a product and engineering design problem.

<p class="section-break">. . .</p>

## Key Takeaways

- Agents need guardrails because actions create risk.

- Read actions are usually safer than write actions.

- Approval points keep humans in control of important actions.

- Tool permissions should follow least privilege.

- Tool arguments should be validated by software.

- Step limits prevent runaway loops.

- Logs and audit trails make agent behavior inspectable.

<p class="section-break">. . .</p>

## What's Next

Now that we understand guardrails, we can look at agents working with more than one tool.

Real agents often need to coordinate several capabilities.

In the next article, we will explore:

## Multi-Tool AI Workflows
