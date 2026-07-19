---
name: har-derive-client
description: >-
  Use when the user wants a CLI or API client for a website that lacks a public
  SDK, asks to record browser network traffic into a HAR, reverse-engineer an
  undocumented API from DevTools/HAR, replace repeated browser automation with
  direct HTTP calls, or build a quick site-specific tool the way agents capture
  a flow once then derive a client.
---

# HAR Derive Client

## Goal

Capture a real browser session as a HAR, extract the meaningful API calls, and
derive a small programmatic client (CLI or library) so later work hits HTTP
directly instead of driving a browser every time.

## When to Use

Use this skill when the user asks to:

- Build a CLI or SDK for a site with no public API docs.
- Record network requests / export a HAR while an agent uses the browser.
- Reverse-engineer endpoints from DevTools traffic.
- Stop browser-automating a repetitive web flow and call the underlying API.
- "Do the HAR → client trick" / capture once, reuse as HTTP.

Example prompts:

- "Record a HAR while ordering on this site, then make a CLI."
- "Don't keep controlling the browser — derive a client from the network traffic."
- "Reverse-engineer this app's API from a HAR and wrap it in TypeScript."
- "Build a quick Uber-Eats-style CLI from the live site."

**Do not use** when:

- A public OpenAPI/SDK already covers the need — use that instead.
- The task is a one-off click with no reuse value.
- The user only wants a screenshot or UI walkthrough, not an API client.

## Workflow

### 1. Define the target flow

Before opening a browser, write down:

| Item | Example |
|------|---------|
| Goal action | Search restaurants, place order, list inbox |
| Success signal | JSON list of results, 200 on submit |
| Auth needed? | Logged-out / cookie / OAuth / API key |
| Output shape | CLI commands + JSON stdout |

Confirm with the user if the scope is unclear. Prefer the smallest flow that
covers the verbs they need.

### 2. Capture traffic as HAR

Drive the browser (agent browser tool, Playwright, or manual DevTools) through
**only** the target flow.

While capturing:

1. Open Network tooling; enable "Preserve log" if the page navigates.
2. Prefer capturing XHR/fetch; note the API host(s) if visible.
3. Complete the happy path once; avoid unrelated tabs and clicks.
4. Export **Save all as HAR** (or equivalent) to a local path, e.g.
   `./captures/<site>-<flow>.har`.

If the agent can write HAR programmatically (Playwright `recordHar`, CDP
Network domain, browser MCP export), prefer that over a manual export.

### 3. Redact secrets before analysis

Treat every HAR as credentialed until proven otherwise.

1. Copy the HAR to a working file; keep the raw capture out of git.
2. Scrub values (keep header **names** so auth shape stays visible):
   - `Authorization`, `Cookie`, `Set-Cookie`
   - `X-API-Key`, `X-CSRF-Token`, and similar
   - JWT-shaped strings (`eyJ...`), AWS `AKIA...`, Stripe `sk_live_` / `sk_test_`
   - Refresh tokens, session IDs in query strings or bodies
3. Never paste raw HAR into chat, tickets, or commits until redacted.
4. Document where live credentials will come from at runtime (env vars, existing
   browser session export the user controls) — do not hardcode them.

### 4. Filter noise and inventory endpoints

HARs are mostly noise. Keep API-shaped traffic; drop the rest.

**Drop:**

- Static assets (`.js`, `.css`, images, fonts, source maps)
- Analytics / ads / tag managers
- CORS preflights (`OPTIONS`)
- Telemetry and error beacons

**Keep and cluster:**

- JSON (or obvious RPC) requests to the product's API hosts
- One sample per `METHOD + normalized path` (collapse IDs:
  `/users/42` → `/users/{id}`)

Produce a short inventory table:

| Method | Path | Role | Auth | Request notes | Response notes |
|--------|------|------|------|---------------|----------------|
| GET | `/api/search` | search | cookie | `q` query | array of places |
| POST | `/api/cart` | add item | cookie | JSON body | cart id |

If the inventory is empty, re-capture with clearer filters or a longer flow —
do not invent endpoints.

### 5. Derive the client

From the inventory (not from guesses), implement a thin client:

1. **Transport** — `fetch` / `curl` / language HTTP library; one shared request
   helper for base URL, headers, and error handling.
2. **Auth** — mirror the capture: cookie jar, bearer token from env, or
   header set the site used. Fail fast with a clear message if auth is missing.
3. **Methods** — one function or CLI subcommand per user-facing verb
   (`search`, `getCart`, `checkout`), named after intent, not raw paths.
4. **Types** — infer request/response types from real HAR payloads; mark
   uncertain fields optional rather than inventing.
5. **CLI surface** (when asked for a tool) — JSON on stdout, human text on
   stderr, exit non-zero on HTTP/auth failures so agents can pipe to `jq`.

Minimal CLI shape:

```bash
# Example contract — adapt names to the site
bun cli.ts search "fast food"
bun cli.ts search "fast food" | jq '.[0:10]'
```

Prefer a few solid commands over a complete mirror of the website.

### 6. Verify against the live API

1. Replay each derived call with the user's real auth (never commit it).
2. Diff status codes and response shapes against the HAR samples.
3. Fix path/header/body mismatches until the client matches observed traffic.
4. Re-run the user's original goal through the client only — **no browser**
   unless auth bootstrap or CAPTCHA still requires it.

If replay fails with 401/403, fix auth acquisition; do not fall back to
permanent browser automation without saying so.

### 7. Hand off

Deliver:

- Client / CLI entrypoint and how to pass auth
- Endpoint inventory (the table from step 4)
- Note that private APIs drift — re-capture HAR when calls break
- Reminder: respect the site's terms; this is for personal/automation use the
  user is accountable for

## Guardrails

- Never commit HAR files, cookies, tokens, or session dumps to git.
- Never leave live secrets in generated client code, fixtures, or README examples.
- Never invent endpoints or fields that did not appear in the capture.
- Never keep using browser control for the hot path once the client works —
  browser is for capture and auth bootstrap only.
- Never claim the client is an official SDK or supported API.
- Never disable TLS verification or ignore certificate errors to "make it work."
- Never exfiltrate captured credentials to third-party paste/LLM services; prefer
  local redaction and local generation.
- If the site's terms or the user forbid reverse engineering, stop and report
  rather than proceeding.

## Completion Checklist

- [ ] Target flow and success signal were defined before capture.
- [ ] A HAR was captured for that flow (or an existing HAR was used).
- [ ] Secrets were redacted; raw HAR is not committed.
- [ ] Noise was filtered; an endpoint inventory was produced from real traffic.
- [ ] A thin client/CLI was derived from the inventory with env-based auth.
- [ ] Live replay matched HAR status/shape for the supported verbs.
- [ ] The user's goal runs through the client without browser automation.
- [ ] Drift and ToS caveats were stated in the handoff.
