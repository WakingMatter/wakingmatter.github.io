---
title: Intelligence should accumulate
description: The harder problem is how experience should change what an agent does next. A note on preservation, inheritance and evaluation.
pubDate: 2026-09-15
updatedDate: 2026-10-16
---

An agent can complete a task without leaving its successor better prepared for the next one. Logs may survive. A summary may be retrieved. Neither establishes that the next decision will improve. That gap, between retaining a trace and using experience well, is the problem we want to work on.

This is a strange way to spend effort. In almost every other domain where learning matters, the point is not to demonstrate capability once. It is to keep it.

Science makes an institutional bet: later work should be cheaper, sharper, or more ambitious because earlier work was kept in a form that others can use. Firms, crafts, and legal systems make the same bet in different materials. A tradition is, among other things, a way of not paying the full cost of understanding a second time.

A notebook, a transcript or an evaluation score may preserve a result without preserving what made it useful. When a model, workflow or team changes, later work may have to reconstruct the reasoning behind it. We are interested in making that inheritance explicit and testable.

The problem already has names. Continual and lifelong learning: new tasks without erasing old ones. Distillation and adapters: capability moved into another network, or a small patch that can be swapped. Retrieval and external memory: facts and traces kept outside the weights. Replay: re-exposure so a learner does not forget. Model merging: separately trained parameters combined into one. Cumulative culture, the human analogue: later people do not rediscover what earlier people kept.

These fields already address substantial parts of the problem. Our question is how their lessons should inform an agent system whose decisions depend on a changing world, and how to check whether its retained experience is earning its place.

The design questions are concrete. What should stay local, and what should travel? How would we tell compounding from a pile of memories that only makes later work slower?

We take the gap to be a design problem. Waking Matter is building systems for agents that improve with experience. Our conviction is that useful learning should survive sessions and compound across agents, models and time. The work is to make that conviction hold up in systems we can inspect and experiments we can repeat.

## Memory is not enough

The harder question is how prior experience should change the next allocation of retrieval, attention, compute and action. An agent might retrieve a different source, test an assumption before acting, try another branch, stop earlier or escalate to a person. Sometimes the useful change is to forget, reset or distrust what it learned before.

A test of that idea needs to admit three outcomes: experience helps, has no useful effect, or hurts. It also needs to separate retained experience from extra context, extra compute and advice that was available before the experience. Otherwise an apparent learning gain can be a change in resources or instructions.

Repeated real-world workflows offer a concrete place to ask these questions. Outcomes can be checked, facts can change, and the cost of repeated errors or unnecessary escalation can be made visible.

## Preservation is not storage

To preserve learning is not merely to keep weights, logs, or documents. Storage is cheap. What is scarce is a representation that remains usable when the surrounding system changes: when a model is replaced, when a task distribution shifts, when a new agent arrives without the conversation that produced the last useful distinction.

A checkpoint is a snapshot of a particular mind in a particular training regime. A transcript is a snapshot of a particular dialogue. Neither is automatically an inheritance. Preservation, in the sense we mean, is the work of lifting something out of the context that produced it without washing away what made it valuable. That is closer to curation, or to the design of instruments, than to backup.

There are at least two failure modes to test: keeping so much that the useful distinction is buried, and compressing so aggressively that a later agent must reconstruct the reasoning from a slogan.

The difficulty is not only technical. What counts as *useful* learning is a judgment, and judgments go stale. A preserved distinction that was right for last year's task can become a prejudice. Preservation without a way to revise is how institutions calcify. The design problem is therefore double: keep what is worth keeping, and keep it in a form that can be disagreed with.

Locality is not the same problem as revision. Some learning should never leave the room: privacy, a failed path that should die rather than be inherited, a fact that is only true here. We do not have an account of that boundary. We leave it open.

## Inherit useful learning. Keep the right to reset.

If preservation is the vessel, inheritance is the habit. Useful prior learning should be available to new work as a matter of course. It should also be possible to inspect it, challenge it and start fresh. We want continuity without giving the past permanent authority.

That is harder than it sounds. Starting over is often faster in the local sense. A new model is better on a public benchmark. A new agent is unencumbered by yesterday's ontology. A new file is easier than reading the old one. The incentives of demonstrating capability can cut against the incentives of accumulation.

There is a corresponding technical difficulty. Inheritance requires interfaces that survive change: between models of different families, between agents with different tools, between human judgment and machine traces. It requires some account of what is worth passing on, and some way to notice when an inherited piece of learning has gone stale. Larger context windows can make more history available. The system still needs a policy for what deserves authority and when that authority should end.

We are interested in the boring machinery of inheritance: how an agent, a model, or a group might take on prior learning without having been present for it, and how that transfer can be inspected rather than believed. An inheritance that cannot be examined is not an inheritance. It is a rumor with better production values.

This also changes what an "agent" is for.[^agent] If each run is a sealed performance, the unit of design is the episode. If learning is meant to accumulate, the unit of design is the line of work that outlasts any one episode, including the humans who still do most of the keeping.

## Compounding is a property of the system

The third term is compounding. It is the reason the first two are worth the trouble. If later work is not actually cheaper, clearer, or more ambitious because earlier work was kept, then we have built an archive, not a system for cumulative intelligence.

Compounding can fail even when storage and retrieval succeed. A growing pile of memories can make an agent slower, more cautious, or more confused. An inherited procedure can ossify. A model adapted to yesterday's tasks can punish tomorrow's. Accumulation without selection is drift. Selection without memory is amnesia. The useful region is narrow, and it is a property of the whole arrangement of representations, incentives, evaluation and time.

This is why we speak of systems rather than of a model, a memory module, or a product. The question is whether later work is cheaper or clearer because earlier work was kept, and whether that remains true when any one part of the arrangement is replaced.

Evaluation, in that light, cannot only ask whether a system can do a task from a cold start. Cold-start competence is real. It answers a different question from whether repeated work improves with experience. Cumulative intelligence would also have to show that a second, third, and tenth encounter with a related world is not billed at full price: in tokens, in human attention, or in repeated mistakes. We do not offer such a measure here. We note only that without one, it is easy to mistake a sequence of impressive debuts for a tradition.

## The standard we are building toward

There is a fashionable alternative: treat each new demonstration as a reset, and call the rising envelope of those demonstrations progress. Some of that progress is real. Benchmarks move. Models that did not exist five years ago now do work that would have seemed implausible. We have no interest in denying it.

What we doubt is that a sequence of isolated peaks is the same thing as intelligence that accumulates. A civilization that had to rediscover metallurgy in every generation would still produce impressive furnaces. It would not produce a metallurgy.

Useful learning costs data, human attention and failed attempts. We believe that investment should carry forward. Our ambition is to make useful inheritance ordinary: systems that retain what earns its place, revise what no longer holds and become more capable through repeated work.

Experiments will tell us which forms deserve to survive. Some representations will fail with a new model. Some apparent compounding will turn out to be bookkeeping. We will keep the results that withstand scrutiny and change the systems that do not. That is how conviction becomes capability.

Intelligence should accumulate. The rest is design.

[^agent]: We use *agent* in the ordinary systems sense: a process that acts over time with tools and a goal, whether the actor is a model, a script, a person, or some mixture. Nothing here depends on a stronger claim about autonomy.
