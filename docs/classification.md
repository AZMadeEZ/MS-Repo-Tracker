# Classification And Signal

The tracker currently uses lightweight local heuristics for repository category, activity signal, and event-level signal/noise fields.

## Repository Category

Inventory rows include `category`:

- `docs`
- `reference`
- `training`
- `samples`
- `other`

The durable inventory keeps `other` repositories so ecosystem coverage is preserved even when default reports focus on docs/reference/training/samples.

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

The next classification improvement should move category and product rules into explicit config files and emit explainable fields such as:

- `repo_type`
- `product_area`
- `audience`
- `classification_confidence`
- `classification_reason`
- `classification_version`
