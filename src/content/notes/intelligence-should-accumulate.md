---
title: Intelligence should accumulate
description: What should survive a task, what should pass to the next system, and when should the past lose authority?
pubDate: 2026-09-15
updatedDate: 2026-10-16
---

An agent can finish a task without leaving its successor better prepared. The logs may survive. A summary may be retrieved. The next agent may still repeat the same mistake.

That is an expensive way to work. Useful learning costs data, human attention and failed attempts. We believe that investment should carry forward.

Science gives this ambition a familiar form. A later researcher should be able to ask a harder question because someone preserved a method, an instrument or a result. Firms and crafts depend on similar forms of inheritance. Their value lies in making knowledge usable by someone who was not there when it was acquired.

For agent systems, the question is what that inheritance should consist of, and how to know when it helps.

## Memory has to change a decision

Consider an agent that handles a recurring operational report. On one run, a source turns out to be outdated and a person corrects the result. This is a hypothetical example, not a deployment claim.

Saving the correction is a start. The useful consequence might be a freshness check on the next run, a different source or a request for confirmation. It might also be wrong to apply the correction elsewhere: the exception may have belonged to that report alone.

The design problem connects experience to action. What should the agent retrieve? Which assumption should it test? How much effort should it spend, and when should it stop or ask a person?

Keeping a longer transcript does not settle those choices. Neither does deleting history by default. We need ways to retain what matters and control how it influences the next decision.

## Preserve the reason, not just the answer

A useful record needs enough context to be challenged. Where did the claim come from? Under what conditions did the procedure work? What would invalidate it?

There are two familiar failures. Keep everything, and the useful distinction can disappear in the volume. Compress too aggressively, and a later system inherits a rule without the reasoning that made it useful.

The same problem becomes harder when a model is replaced, tools change or a new agent takes over. A representation tied to one conversation may travel badly. What should pass between systems, and what should remain local, are separate design decisions.

Some knowledge should not travel at all. It may be private, specific to one setting or too poorly supported to justify reuse. The ability to preserve information needs a corresponding ability to limit its authority.

## Keep the right to reset

Inheritance should make useful prior work available. It should also leave the next system free to inspect it, revise it or start again.

A procedure can become stale. An exception can be mistaken for a general rule. Repeated retrieval can make an unsupported claim feel established. Continuity is valuable only while the system can detect and correct those failures.

This is one reason we are working on explicit memory boundaries. [Agent Memory Contracts](https://github.com/avs-io/agent-memory-contracts) separates source evidence, candidate claims and the decision to accept a claim into trusted memory. It makes that decision inspectable. It does not establish that the claim is true or that accepting it improves performance.

The further question is how those records should influence retrieval, attention, compute and action as the world changes.

## Measure what the past contributes

An agent with history may outperform a fresh agent because it received more context, more compute or better instructions. That is useful, but it does not isolate the contribution of experience.

Evaluation should compare those alternatives. It should measure outcomes, cost, repeated mistakes and human intervention. It should include changed conditions, where a previously helpful memory can become harmful.

Three outcomes have to remain possible: prior experience helps, has no useful effect or hurts. A test that cannot reveal the latter two cannot tell us what deserves to be retained.

Repeated workflows give this question practical stakes. Does the second encounter require less reconstruction? Does the tenth avoid a mistake that the first exposed? Can the system revise a rule without losing everything useful around it?

Those are research questions, not results we are claiming here.

## The ambition

Continual learning, retrieval, replay, distillation and adaptive control already address parts of this problem. Waking Matter's work is to bring those lessons to agent systems whose tools, tasks and sources change, and make the consequences testable.

The ambition is larger than a memory store. It is a line of work that becomes more capable across sessions, agents and models, without giving the past permanent authority.

Some representations will fail to transfer. Some apparent gains will disappear under a better comparison. We will keep what withstands that scrutiny and revise what does not.

Intelligence should accumulate. That is the standard we are building toward.
