# Website update notifications

`.github/workflows/notify-website.yml` sends `agent-skills-updated` repository
dispatch events to `designxdevelop/dxd-2026` after relevant pushes to `main`,
published releases, or a manual workflow run. Packaging must pass first.
The payload identifies the checked-out source commit and plugin version.
Release events use the release tag's revision; manual runs use the selected ref.

## Activation

1. In `dxd-2026`, add a workflow on its default branch that listens for:

   ```yaml
   on:
     repository_dispatch:
       types: [agent-skills-updated]
   ```

2. Create a fine-grained token restricted to `designxdevelop/dxd-2026` with
   **Contents: write**, or an equivalent GitHub App installation token.
   The source repository's built-in `GITHUB_TOKEN` cannot dispatch across repos.
3. Store it in this repository's Actions secrets as
   `DXD_WEBSITE_DISPATCH_TOKEN`. Set it using GitHub settings or
   `gh secret set DXD_WEBSITE_DISPATCH_TOKEN --repo designxdevelop/agent-skills`.
   Never commit the credential. Rotate it before expiration.
4. Run **Notify website of skill updates** manually after the receiving workflow
   is merged, and verify the website refresh completes.

The receiving workflow should validate `client_payload.source_repository` and
the source SHA before use, fetch all source files from one revision, and invoke
the website's existing refresh and deployment process. Do not interpolate event
payload fields directly into shell commands. Serialize receiver refreshes and
resolve current source `main` when refreshing the live page, so delayed events
or releases of older revisions cannot roll the page back. Skip deployments when
the generated content is unchanged, preserve the last valid snapshot on errors,
and retain a daily scheduled refresh as a fallback.

An accepted dispatch only confirms GitHub received the event. It does not confirm
that a receiver exists or that the website deployed successfully. Missing
credentials and API failures fail the notifying workflow visibly.

Protocol:

```json
{
  "event_type": "agent-skills-updated",
  "client_payload": {
    "source_repository": "designxdevelop/agent-skills",
    "source_sha": "<full Git commit SHA>",
    "version": "<plugin version>"
  }
}
```

See [GitHub's repository dispatch API](https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event).
