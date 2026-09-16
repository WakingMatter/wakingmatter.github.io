---
title: Intelligence should accumulate
description: Useful learning is expensive. Systems that cannot keep it are wasteful even when they are capable. A note on preservation, inheritance, and compounding — without a claim of novelty or results.
pubDate: 2026-09-15
---

Most computational work treats intelligence as a performance that can be repeated on demand. A model is trained, evaluated, deployed, and, before long, replaced. The traces of how it was used — the distinctions it learned in contact with a particular world — are usually discarded. The next system starts again, with more data perhaps, or a different architecture, but rarely with a usable inheritance.

This is a strange way to spend effort. In almost every other domain where learning matters, the point is not to demonstrate capability once. It is to keep it.

Science is the obvious example, and it is not a metaphor we should lean on too heavily. Papers, instruments, and negative results are imperfect vessels. Still, the institutional bet is clear: later work should be cheaper, sharper, or more ambitious because earlier work was kept in a form that others can use. Firms, crafts, and legal systems make the same bet in different materials. A tradition is, among other things, a way of not paying the full cost of understanding a second time.

Many of the systems now called intelligent are designed as if that cost were negligible. Each agent session is a sealed room. Each model version is a new population. Each organization that fine-tunes, prompts, or evaluates a model does so in artifacts that do not travel well: notebooks, dashboards, tribal knowledge, a handful of evaluation scores. The intelligence is real enough in the moment. It does not accumulate.

The problem already has names. Continual and lifelong learning ask how a model can take on new tasks without erasing old ones. Distillation and adapters move capability from one network into another, or into a small patch that can be swapped. Retrieval and external memory keep facts and traces outside the weights. Replay re-exposes a learner to earlier data so it does not forget. Model merging tries to combine separately trained parameters into one. Cumulative culture — the human analogue — is the slower process by which later people do not have to rediscover what earlier people kept.

Neighbors exist. The gap is not that no one has noticed accumulation. It is that these lines of work are still mostly separate, and that much of what is called intelligence in practice still throws the traces away.

Several questions remain open. We will not close them here. What should stay local — private traces, a failed path that ought to die, a distinction that is only true in one room? What should travel? How would we tell compounding from a pile of memories that only makes later work slower? Those are joints, not slogans.

We take the gap to be a design problem. Waking Matter exists to explore systems that can preserve, inherit, and compound useful learning across agents, models, and time. We do not claim that this framing is original, and we do not report results here. The aim of this note is only to make the problem specific enough to work on.

## Preservation is not storage

To preserve learning is not merely to keep weights, logs, or documents. Storage is cheap. What is scarce is a representation that remains usable when the surrounding system changes — when a model is replaced, when a task distribution shifts, when a new agent arrives without the conversation that produced the last useful distinction.

A checkpoint is a snapshot of a particular mind in a particular training regime. A transcript is a snapshot of a particular dialogue. Neither is automatically an inheritance. Preservation, in the sense we mean, is the work of lifting something out of the context that produced it without washing away what made it valuable. That is closer to curation, or to the design of instruments, than to backup.

It is also where most systems quietly fail. They keep everything and transmit almost nothing. Or they transmit a summary so compressed that the next agent must reconstruct the work from a slogan.

The difficulty is not only technical. What counts as *useful* learning is a judgment, and judgments go stale. A preserved distinction that was right for last year's task can become a prejudice. Preservation without a way to revise is how institutions calcify. The design problem is therefore double: keep what is worth keeping, and keep it in a form that can be disagreed with.

Locality is not the same problem as revision. A preserved distinction can go stale and still have been worth keeping for a while. Some learning should never leave the room: privacy, a failed path that should die rather than be inherited, a fact that is only true here. We do not have an account of that boundary. We leave it open.

## Inheritance has to be the default

If preservation is the vessel, inheritance is the habit. A system compounds only if new work begins from old work as a matter of course, not as a special project.

That is harder than it sounds. Starting over is often faster in the local sense. A new model is better on a public benchmark. A new agent is unencumbered by yesterday's ontology. A new file is easier than reading the old one. The incentives of demonstration — of showing that something can be done — cut against the incentives of accumulation.

There is a corresponding technical difficulty. Inheritance requires interfaces that survive change: between models of different families, between agents with different tools, between human judgment and machine traces. It requires some account of what is worth passing on, and some way to notice when an inherited piece of learning has gone stale. None of that is solved by larger context windows, though larger windows can hide the absence of a design.

We are interested in the boring machinery of inheritance: how an agent, a model, or a group might take on prior learning without having been present for it, and how that transfer can be inspected rather than believed. An inheritance that cannot be examined is not an inheritance. It is a rumor with better production values.

This also changes what an "agent" is for.[^agent] If each run is a sealed performance, the unit of design is the episode. If learning is meant to accumulate, the unit of design is the line of work that outlasts any one episode — including the humans who still do most of the keeping.

## Compounding is a property of the system

The third term is compounding. It is the reason the first two are worth the trouble. If later work is not actually cheaper, clearer, or more ambitious because earlier work was kept, then we have built an archive, not a system for cumulative intelligence.

Compounding can fail even when storage and retrieval succeed. A growing pile of memories can make an agent slower, more cautious, or more confused. An inherited procedure can ossify. A model adapted to yesterday's tasks can punish tomorrow's. Accumulation without selection is drift. Selection without memory is amnesia. The useful region is narrow, and it is a property of the whole arrangement — representations, incentives, evaluation, time — not of a single component.

This is why we speak of systems rather than of a model, a memory module, or a product. The question is whether later work is cheaper or clearer because earlier work was kept — and whether that remains true when any one part of the arrangement is replaced.

Evaluation, in that light, cannot only ask whether a system can do a task from a cold start. Cold-start competence is real, and it is what most public numbers measure. Cumulative intelligence would also have to show that a second, third, and tenth encounter with a related world is not billed at full price — in tokens, in human attention, or in repeated mistakes. We do not offer such a measure here. We note only that without one, it is easy to mistake a sequence of impressive debuts for a tradition.

## A quieter posture

There is a fashionable alternative: treat each new demonstration as a reset, and call the rising envelope of those demonstrations progress. Some of that progress is real. Benchmarks move. Models that did not exist five years ago now do work that would have seemed implausible. We have no interest in denying it.

What we doubt is that a sequence of isolated peaks is the same thing as intelligence that accumulates. A civilization that had to rediscover metallurgy in every generation would still produce impressive furnaces. It would not produce a metallurgy.

The analogy is imperfect, and we will not press it. The claim is modest. If useful learning is expensive — and it is, in data, in human attention, in failed attempts — then systems that cannot keep it are wasteful even when they are capable. The research problem is to make keeping it ordinary.

We will be wrong about some of the forms this should take. We expect to spend a long time on representations that do not survive contact with a new model, on inheritance that looks like copying, on compounding that is only bookkeeping. That is the work. It does not require a promise that the problem is unsolved by everyone else, or that we have already solved it.

Intelligence should accumulate. The rest is design.

[^agent]: We use *agent* in the ordinary systems sense: a process that acts over time with tools and a goal, whether the actor is a model, a script, a person, or some mixture. Nothing here depends on a stronger claim about autonomy.
