# Bounding Box Calibration Plan
*Created: March 6, 2026*

## Status Update — March 6, 2026

Progress since this plan was drafted:

- ✅ Implemented OSM qualification pipeline in `topo-map-creator`:
  - `scripts/osm-seed-manifest.ts`
  - `scripts/audit-osm-coverage.ts`
  - `pnpm audit:osm-coverage`
- ✅ Audit artifacts now generated per run:
  - `output/osm-coverage.json`
  - `output/osm-coverage-report.md`
- ✅ Determinism check added (`--determinism-check`)

Latest full-catalog audit snapshot (March 6, 2026):
- `pass=17, warn=0, fail=8`
- `osm_sufficient_for_literal_boundaries=false`

Interpretation:
- OSM resolves most national parks + ski areas with polygon boundaries.
- `mount-hood` and `half-dome` resolve as point peaks (coordinates present,
  literal polygon boundaries absent under strict policy).
- Some failures are transient Overpass reliability/rate-limit errors (`429/504/fetch`),
  not necessarily missing geometry.

This means the immediate task is now policy lock-in for no-manual-intervention
boundary discovery (strict OSM-only vs synthetic peak fallback vs hybrid source),
then proceed to final bounds calibration.

## The Problem

Current bounding boxes in `scripts/locations.ts` were hand-estimated. Several are
off-center — the Smokies test showed large empty areas because the box included flat
Tennessee Valley terrain instead of centering on the main ridge. All 25 locations need
mathematically derived bounds that tightly fit their actual interesting terrain.

## The Approach

Write a one-time Node script (`scripts/calibrate-bounds.ts`) that:
1. Fetches authoritative geographic boundary polygons for each location
2. Computes a tight bounding box from the polygon
3. Applies the cos(lat) square correction so the rendered canvas is square
4. Outputs updated `locations.ts` entries ready to drop in

---

## Step 1 — Classify all 25 locations by data source

Two APIs cover all 25 locations:

**NPS API** (`developer.nps.gov/api/v1`) — official park boundaries as GeoJSON.
Free, no auth required for basic queries. Returns the exact legal park polygon.

| Location ID | NPS Park Code |
|---|---|
| grand-canyon | grca |
| yosemite | yose |
| yellowstone | yell |
| zion | zion |
| great-smoky-mountains | grsm |
| grand-teton | grte |
| glacier | glac |
| rocky-mountain | romo |
| acadia | acad |
| olympic | olym |
| mount-rainier | mora |
| arches-canyonlands | arch + cany |
| joshua-tree | jotr |
| crater-lake | crla |
| bryce-canyon | brca |
| hawaii-volcanoes | havo |
| denali | dena |
| mount-hood | — (National Forest, use OSM) |
| half-dome | — (feature within Yosemite, use OSM) |

**OpenStreetMap Overpass API** (`overpass-api.de`) — boundary polygons for named
places, mountains, ski areas, lakes. Free, no auth. Use `relation` queries by name.

| Location ID | OSM Query Strategy |
|---|---|
| jackson-hole | relation name="Jackson Hole Mountain Resort" |
| breckenridge | relation name="Breckenridge Ski Resort" |
| aspen | relation name="Aspen Snowmass" |
| vail | relation name="Vail Mountain" |
| lake-tahoe | relation name="Lake Tahoe" (the lake itself as center) |
| park-city | relation name="Park City Mountain Resort" |
| mount-hood | peak node "Mount Hood" + fixed radius |
| half-dome | peak node "Half Dome" + fixed radius |

---

## Step 2 — Fetch boundary polygon and derive raw bounding box

For each location, the script does:

```
polygon → find min/max lat and min/max lng → raw bbox
```

For NPS parks with complex multi-polygon boundaries (e.g. Arches + Canyonlands
combined), take the union of all polygon extents.

For point features (Mount Hood peak, Half Dome peak), use the point coordinates
plus a fixed radius (e.g. 15 miles) to construct the polygon equivalent.

---

## Step 3 — Apply square correction

Our canvas is 6400×6400 (square). Geographic degrees aren't square — a degree of
longitude is shorter than a degree of latitude at most latitudes due to Earth's
curvature. We already have `calculateBoundingBox()` in `lib/topo-core.ts` that
handles this using the cos(lat) formula.

From the raw bbox:
1. Compute center lat/lng
2. Use the E-W span (in miles) as `coverageMiles`
3. Call `calculateBoundingBox(centerLat, centerLng, coverageMiles, 1.0)` to get
   a square-corrected bbox

This ensures the rendered image has equal visual scale in both directions.

---

## Step 4 — Add padding

Apply 8% padding on all sides so contour lines aren't clipped right at the edge:

```
paddedNorth = center + (rawNorth - center) * 1.08
paddedSouth = center - (center - rawSouth) * 1.08
(same for E/W)
```

---

## Step 5 — Output updated locations.ts entries

The script prints (or writes directly) the updated `bounds` for each location in
the exact format used by `locations.ts`. Claude or the user can then review the
diff and commit.

---

## Step 6 — Sanity check: flag suspiciously large or small boxes

After computing all 25 bounds, the script should flag any where:
- Total lat span > 5° (probably too big, capturing too much flat terrain)
- Total lat span < 0.1° (probably too small, missing context)
- E-W span differs from N-S span by more than 20% before square correction
  (could indicate a data quality issue)

---

## Step 7 — Visual spot-check in map builder (optional but recommended)

For any flagged locations, open `topo-map-creator` locally and manually paste in
the computed bounds to visually verify the box sits on the right terrain before
running the full batch.

---

## Implementation Notes

- Script lives at `scripts/calibrate-bounds.ts`, runs once via `pnpm calibrate:bounds`
- NPS API endpoint: `https://developer.nps.gov/api/v1/parks?parkCode={code}&fields=entrances`
  — actually boundary GeoJSON is at a different endpoint, need to verify (see below)
- NPS boundary data may need to come from the NPS GeoJSON repository on GitHub:
  `https://github.com/nationalparkservice/data` or the ArcGIS REST service the NPS uses
- OSM Overpass query format for a named relation:
  ```
  [out:json];relation["name"="Grand Canyon National Park"]["boundary"="national_park"];out geom;
  ```
- Both APIs are accessible from the user's local machine (not Claude's VM which has
  no outbound internet) — script must be run locally like the map generation script

---

## Open Questions to Resolve During Implementation

| Question | Notes |
|---|---|
| Does NPS developer API return boundary polygons directly? | May need to use NPS ArcGIS endpoint or GitHub GeoJSON repo instead |
| OSM ski area boundaries — how complete are they? | Some resorts may only have a point, not a full boundary polygon. Fallback: use ski area center point + terrain radius |
| Arches + Canyonlands — combined or separate locations? | Currently one entry `arches-canyonlands` — probably want to union both park polygons |
| Half Dome — how large a radius? | It's a specific rock face, not a park. ~8-mile radius centered on the peak probably right |
| Lake Tahoe — use the lake boundary or the surrounding ski/resort area? | The lake itself is the landmark; surrounding terrain determines the topo interest |

---

## Files to Modify

| File | Change |
|---|---|
| `scripts/calibrate-bounds.ts` | New — the one-time calibration script |
| `scripts/locations.ts` | Updated `bounds` for all 25 locations (output of script) |
| `package.json` | Add `"calibrate:bounds": "tsx scripts/calibrate-bounds.ts"` script |
| `topo-map-business/HANDOFF.md` | Note that bounds are now auto-derived, not hand-estimated |

---

## Sequence When Picking This Up

1. Run `pnpm audit:osm-coverage` and review `output/osm-coverage-report.md`
2. Lock production policy for peak/landmark boundaries (strict literal vs synthetic fallback)
3. Stabilize Overpass reliability handling (retry/mirror strategy) until gate is repeatable
4. Run `scripts/calibrate-bounds.ts` using the approved source policy
5. Review output diff vs current `scripts/locations.ts`
6. Re-run test images for Smokies + one other to validate framing
7. If good, run full 25-location batch
