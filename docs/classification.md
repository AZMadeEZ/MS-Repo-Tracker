# Classification And Signal

The tracker uses lightweight local heuristics for repository category, taxonomy fields, activity signal, and event-level signal/noise fields.

## Repository Category

Inventory rows include `category`:

- `docs`
- `reference`
- `training`
- `samples`
- `other`

The durable inventory keeps `other` repositories so ecosystem coverage is preserved even when default reports focus on docs/reference/training/samples.

## Activity Signal

## Taxonomy Config

Classification rules live in:

- `config/classification_rules.json`
- `config/repo_overrides.json`

Inventory rows include:

- `repo_type`
- `product_area`
- `audience`
- `classification_confidence`
- `classification_reason`
- `classification_version`

These fields are derived locally and do not add GitHub API calls. Older inventory CSVs without these fields are upgraded in memory when loaded by the inventory script.

## Activity Signal

Digest activity scoring considers:

- human-authored commits
- bot-only or dependency-only changes
- release activity
- security language
- watchlist hits
- category
- product matches from `watchlist.yml`

These signals are local and do not add GitHub API calls.

## Event Classification

Event records include first-pass fields:

- `actor_type`
- `change_type`
- `noise_level`
- `customer_visible`
- `notability_score`
- `notability_reason`

These fields are heuristic. They are intended to improve sorting and summarization, not to be treated as final ground truth.

## Watchlist

`watchlist.yml` controls elevated repositories, organizations, keywords, and product areas. Watchlist changes affect signal scoring and report presentation but do not change the inventory baseline.

## Future Improvement

The next classification improvement should tune the rules with real report review feedback and add targeted repo overrides for high-value Microsoft ecosystem repositories.
