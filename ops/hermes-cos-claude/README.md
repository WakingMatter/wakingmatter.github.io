# cos-claude

Isolated Hermes profile for the Waking Matter chief-of-staff Slack bot. The live home is this directory (`~/.hermes-cos-claude`). It is not a profile under `~/.hermes/profiles/`, so the existing multiplexed gateway does not serve it.

The existing Hermes Slack app (launchd label `ai.hermes.gateway`, bot user `U0C6BCSDCHJ`) is a different install. Do not restart it, and do not copy its Slack tokens.

## Model

- Provider id: `claude-subscription-directsdk-experimental`
- Display name: Claude Subscription DirectSDK (Experimental)
- Catalog install id: `claude-subscription-directsdk`
- Active test model: `haiku` (plugin alias for Haiku 5.5, native route `claude-haiku-5-5[1m]`)
- `fallback_providers` is empty. Auxiliary tasks are pinned to the same provider and `haiku`, with empty `fallback_chain`.
- Production model after tests pass: `claude-opus-5-5`. It is not set. Do not add it as a fallback. Change `model.default` by hand only after the Haiku test is accepted.
- Inference uses the official `claude` CLI login. This profile has no `ANTHROPIC_API_KEY` and no `ANTHROPIC_BASE_URL`.

## Shell

The terminal toolset is disabled, along with the other host execution toolsets (`code_execution`, `computer_use`, `debugging`, `file`). There is no Docker sandbox and no command-approval choice, because there is no shell.

Two-way door: to add a sandboxed shell later, remove `terminal` from `agent.disabled_toolsets` and set `terminal.backend` in this `config.yaml`. Do that in a separate change. Do not point the shell at the Waking Matter checkout until repo writes are an explicit decision.

`SOUL.md` is the CoS brief, loaded as standing instructions. It is user-immutable (`uchg`) so the bot cannot edit it. Clear the flag with `chflags nouchg SOUL.md` before replacing the brief.

## Slack

- `allow_bots: mentions` and `SLACK_ALLOW_BOTS=mentions`
- `strict_mention: true` (every channel message needs a fresh @mention; 1:1 DMs with Aditya do not)
- `SLACK_ALLOWED_CHANNELS=C0C5U0A1L6R` (`#ci-work`)
- `SLACK_ALLOWED_USERS=U0C6D8NTGNL` (Aditya only)
- Posts use the cos-claude bot token only. Do not set `SLACK_USER_TOKEN`.

`strict_mention: true` turns off Hermes thread auto-follow. A thread the bot already joined still needs a fresh @mention. That is the native knob Aditya set.

Slack tokens are not in this profile yet. Do not start the gateway until a new Slack app named `cos-claude` exists and its `xoxb-` / `xapp-` tokens are in this directory's `.env`.

## Spend cap

`telemetry/budget.yaml` sets a $5/day global cap, a soft alert at 80%, and a hard stop at 100% (`hermes-telemetry`, enforce mode, including estimated rows).

What the cap can do: once recorded spend for the local day reaches 80%, the plugin injects one warning; at 100% it blocks further tool calls.

What it cannot do: it cannot abort a model call already in flight. On this subscription provider, native `total_cost_usd` is list-price equivalent, not a Claude subscription invoice. The real spend is the Claude subscription / Agent SDK allowance. Extra-usage overage is an account setting; disable extra usage on the Claude account if overage billing is not wanted. If the pricing table treats the route as a flat subscription, the dollar cap will not track the subscription window.

## Native vs wrapper

Native: provider plugin, `haiku` pin, empty `fallback_providers`, `agent.disabled_toolsets`, Slack mention gates, allowlists, `security.redact_secrets`, locale overlay `locales/en.yaml` (gateway provider-failure strings become `CoS unavailable`), gbrain MCP `tools.include`.

Wrapper (this profile only, not host-wide):

- `plugins/cos-claude-guard` — at most 6 consecutive bot messages in a thread without a message from Aditya, then one ping to `U0C6D8NTGNL` and silence in that thread until he speaks; 20 posts/hour from this profile; exact text `CoS stop` from Aditya writes `COS_HALT` and `ESTOP` here and stays silent. Hermes `gateway.bot_loop_guard` does not implement that streak, the ping, or the hourly post cap.
- `hooks/turn-log` — local `logs/turns.jsonl` with secret-shaped strings redacted before append.
- The guard also rewrites known provider-failure text to `CoS unavailable` if the locale overlay did not already replace it.

## MCP

- gbrain: read-only tool allowlist, HTTP MCP on `127.0.0.1:18790`, credential from this profile's `.env` (`GBRAIN_MCP_AUTHORIZATION`). `trust: untrusted`.
- GitHub: not configured. The `gh` logins on this Mac have `repo` scope (write). There is no read-only WakingMatter token here.
- Slack: the gateway, not an MCP server.
- Nothing else.

Skill and memory self-creation are off (`skills` and `memory` toolsets disabled, `memory.memory_enabled: false`, curator off, background review off, write approval on).

## Process control

Gateway is not installed and not started.

After Slack tokens exist:

```sh
HERMES_HOME=$HOME/.hermes-cos-claude hermes gateway install
HERMES_HOME=$HOME/.hermes-cos-claude hermes gateway start
```

Stop this profile only:

```sh
HERMES_HOME=$HOME/.hermes-cos-claude hermes gateway stop
```

That talks to the launchd label for this home (`ai.hermes.gateway-` plus the first 8 hex chars of the SHA-256 of the resolved home path), not `ai.hermes.gateway`. Equivalent after install:

```sh
launchctl bootout gui/$(id -u)/ai.hermes.gateway-45a990f8
```

`45a990f8` is the service suffix for `/Users/a/.hermes-cos-claude`. Do not bootout `ai.hermes.gateway` (that is the existing bot).

`CoS stop` does not kill the process. It stops replies. Undo with:

```sh
rm $HOME/.hermes-cos-claude/COS_HALT $HOME/.hermes-cos-claude/ESTOP
```

## Blocker

`claude` is installed (2.1.317, which is new enough for the Haiku 5.5 alias). `claude auth status` reports logged out. The subscription provider will refuse turns until `claude auth login` succeeds. Do not set an Anthropic API key to get around that.
