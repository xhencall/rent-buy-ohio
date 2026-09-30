# Contributing

1. Claim an issue and identify its dependencies. Members 1–3 consult the geography contract before source selection.
2. Branch from current `main`; use the suggested workstream name or an issue-specific suffix. Never push directly to `main`.
3. Preserve raw downloads. Add only code, documentation and metadata to Git. Review source redistribution terms before proposing any data publication.
4. Update the dictionary, source manifest and tracker with each collection change. In the sheet use Not Started → In Progress → Review → Done, with Blocked available. Done requires reviewed data and provenance, not merely a working URL.
5. Use Python snake_case, functions with English docstrings, explicit units, deterministic seeds where relevant, and configuration instead of hard-coded local paths. Prefer small scripts over hidden notebook state.
6. Run `python src/validate_metadata.py`. Add focused checks for any transformation you implement, including duplicate keys, incompatible geography, missing periods and nonconsecutive growth years.
7. Open a PR linked with `Closes #<issue>`. Describe the change, input provenance, validation and remaining gaps. Request one independent review. Resolve comments before squash merge.

## Working agreement

GitHub is the source of truth for tasks and durable decisions. The Google Sheet is the variable collection log; link issues in Notes rather than copying issue discussions. Slack is for coordination. Summarize decisions back into the repository. Hold a short weekly progress/blocker meeting and review one sample source handoff before bulk collection.

Use role names until actual GitHub usernames are supplied. The repository owner must invite collaborators explicitly; public visibility permits reading but not writing. Recommended main protection: require PRs, one approval, resolved conversations and the metadata check. Protection enforcement depends on repository settings and is not established by this file.

Do not commit API keys, `.env`, private notes, downloads or large generated outputs. Keep any keys in environment variables. The project license is pending team choice; do not imply a license for source data.
