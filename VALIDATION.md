# Validation record

Validated locally on 2026-11-18.

- Skill frontmatter and structure validator: passed.
- Repository required-file, Markdown-link, language-policy, JSON, and machine-path checks: passed. The Chinese README is the explicit language exception.
- Python/tool suite with optional browser tests enabled: 17 tests passed, no skips.
- Deliberate failure cases include missing endpoints, duplicate IDs, parent cycles, short and diagonal flow segments, out-of-frame geometry, nonfinite geometry, stale artifacts, zero detected SVG labels, overlapping text, and text/frame contact.
- Compressed Draw.io pages and wrapped cells were exercised.
- The requested DeepSeek report example passed structural and rendered checks, native/PNG pairing, PDF text/page inspection, and visual review. See its separate review record for exact scope and limitations.

The GitHub workflow runs portable structural checks and unit tests. Browser tests are opt-in because Chromium is not bundled. A CI pass is not a claim that future figures have been visually reviewed.
