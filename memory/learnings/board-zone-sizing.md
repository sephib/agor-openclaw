# Board Zone Sizing Standards

## Issue Discovered: 2026-06-17

When creating zones for the "Buff - Financial Management" board, initial zone dimensions were too small to properly accommodate worktree cards, causing visual misalignment and overflow.

## Root Cause

Zones were created with **450px width**, which is insufficient for standard Agor worktree card rendering.

## Correct Zone Dimensions

### Standard Single-Column Zones
- **Width:** 600px (matches worktree card width)
- **Height:** 400px (standard work zone)
- **Height (archive/done zones):** 750-850px (taller to hold more completed items)

### Zone Spacing
- **Horizontal gap between zones:** 50px minimum
- **Vertical gap between rows:** 50px minimum

### Standard Grid Layouts

**3-column layout (recommended):**
```
Column 1: x=50
Column 2: x=700  (50 + 600 + 50)
Column 3: x=1350 (50 + 600 + 50 + 600 + 50)
Done column: x=2000 (50 + 600 + 50 + 600 + 50 + 600 + 50)
```

**2-row layout:**
```
Row 1: y=50
Row 2: y=500  (50 + 400 + 50)
```

## Evidence from Existing Boards

Analysis of the "Jounce-speckit" board (ed856893-92ff-40d0-8cba-6bdba005549b) shows working zones with:
- Widths ranging from 575-795px
- Heights from 950-1880px (varied by purpose)

The 600px width standard consistently accommodates worktree cards without overflow.

## When Creating New Boards

**DO:**
- Use 600px width for all single-column zones
- Maintain consistent 50px spacing
- Use 400px height for standard work zones
- Use 750-850px height for Done/Archive zones
- Calculate x positions: `x = 50 + (600 + 50) * column_index`

**DON'T:**
- Use widths below 575px
- Create zones smaller than 450x350px
- Overlap zones or use inconsistent spacing
- Forget to account for card padding needs

## Applied Fix

Buff board zones updated:
- Width: 450px → 600px
- Height: 350px → 400px (work zones), 750px → 850px (Done zone)
- Spacing adjusted to maintain clean grid

Result: Cards now fit naturally within zones with proper visual alignment.

## Reference

- Issue board: `019eceea-5e52-7faa-aa5f-fdeaf5d68f9e` (Buff - Financial Management)
- Fixed: 2026-06-17
- Tool: `agor_boards_update` with `upsertObjects`
