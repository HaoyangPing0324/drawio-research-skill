# Contributing

## Scope

Improve the skill's ability to produce accurate, editable, readable research schematics. Keep skill instructions, references, prompts, code comments, and figure labels in English. Maintain `README.zh-CN.md` as the Chinese translation of `README.md`. Explicit user instructions can still request other figure-label languages.

## Useful contributions

- A reproducible failure where a figure violated its supplied content or constraints.
- Better guidance for compact layouts, clear connectors, meaningful iconography, or publication typography.
- A portable check that detects a real failure and reports its coverage honestly.
- Corrections to source attribution, licensing information, or documented tool behavior.

Do not add generic instructions merely to make the skill longer. Do not turn one project's coordinates, hardware stack, or visual preference into a universal requirement. Keep detailed material in references and the entrypoint concise.

## Review checklist

1. Explain the concrete problem and the expected behavior after the change.
2. Identify whether the rule is mandatory, a default, or a conditional example.
3. Keep user content and authorized scope above generic skill preferences.
4. Update relevant links, usage instructions, and tool limitations.
5. Run `python3 -m unittest discover -s tests -v` for structural tool changes.
6. Run `python3 scripts/check_repository.py` for links, language, metadata, and portability checks.
7. For browser-tool changes, run `DRS_BROWSER_TESTS=1 python3 -m unittest discover -s tests -v` after browser setup. Test supported label representations and a deliberate collision; do not report a zero-label run as a pass.
8. For an actual figure change, export and visually inspect the result at its intended size.

## Attribution and contributions

Follow the Apache License 2.0 and preserve applicable notices. Contributions intentionally submitted for inclusion are covered by the license's contribution terms unless explicitly stated otherwise. Do not submit assets or copied text without permission to distribute them. Record third-party provenance and applicable terms; a README credit alone does not grant reuse rights.

## Examples and external actions

A request to improve this skill is not automatically a request to draw new figures. Add demonstration artwork only when requested or agreed as part of the change. Do not publish private manuscript material or alter unrelated approved diagrams. Repository publishing is a separate operation from preparing local files.

## Repository contents

Keep the reusable skill, references, presets, templates, optional scripts and tests, documentation, license, and original README artwork in Git. The DeepSeek report example includes its editable source, exports, builder, source mapping, and review records so readers can inspect the published demonstration. Its subject is an example, not a requirement for future figures.

Keep downloaded reports, extracted text, screenshots, drafts, installed dependencies, browser test output, and caches out of Git. The original report PDF is not redistributed as a repository asset. `.gitignore` covers the local `work/` directory and common generated files; inspect the staged diff before committing. A manually uploaded archive does not use `.gitignore`.
