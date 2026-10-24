# SOES-NG — unofficial rebuild for Skyrim SE 1.7.104

Unofficial rebuild of the SKSE plugin from **Skyrim Outfit Equipment System NG** by koukibyou
(<https://www.nexusmods.com/skyrimspecialedition/mods/147011>,
source <https://github.com/koukisdevki/SkyrimOutfitEquipmentSystemNG>), so it loads on
Skyrim 1.7.99 / 1.7.104 instead of failing with
"must be recompiled for new address library".

## What changed

- Built against **CommonLibSSE-NG v12.1.0** (alandtse fork), which reads the Address Library v5
  format and declares v5 compatibility.
- On 1.7.99+ the internal **EquipObject hook is skipped by default**. Its patch offset inside the
  game's equip function was verified only up to 1.6.1170, and patching a wrong spot can crash
  the game. The hook only stops *other mods* from equipping extra items on *tracked NPCs*; it never
  affects the player. Outfits, importing, auto-switching and quick-slots work without it.
  To try it anyway, add to `SKSE/Plugins/SkyrimOutfitEquipmentSystemNG.ini`:

  ```ini
  [Gameplay]
  ForceEquipHookOn17=true
  ```

- Mod and outfit name lookups are case-insensitive (Papyrus hands names back with altered
  capitalisation, which made "Import from Mod" return nothing for mixed-case plugin names).
- Body-slot labels show their slot number, e.g. `[32] Body` (English translation file).
- Papyrus scripts are compiled in CI with [Caprica](https://github.com/nikitalita/Caprica)
  against public script headers; no Creation Kit needed. The package ships the compiled
  `Scripts/*.pex` it changes and the patched `Interface/Translations` file.
- Outfit categories: name outfits `Category/Sub/Name`. The quick-slot power shows them as a
  nested menu; the Outfits page shows folders with counts, a Back row, search across all
  categories, and "Move to category" / "Move to new category" actions. New outfits created
  inside a folder go into it.
- The outfit editor lists all 32 body slots on one scrolling page; armor pickers ("add from
  inventory", "add any armor") label and group items by body slot, e.g. `[37] Elven Boots`.
- New outfits start as favourites. The Outfits page comes first and opens by default.
- Categories page: rename/move, merge and remove categories (outfits follow; name clashes get a
  " (2)" suffix, nothing is deleted), plus "Sort uncategorised outfits by mod".
- Outfits page: select mode to tick outfits across folders and move them together; imports can
  go straight into a category (default: named after the mod).
- Plugin version 0.1.5. No changes to the ESP.

## Install (MO2)

1. Keep the original SOES-NG mod installed (ESP, scripts, MCM).
2. Install this package as a separate mod and place it **below** SOES-NG so its
   `SKSE/Plugins/SkyrimOutfitEquipmentSystemNG.dll` wins the conflict.
3. Requirements: SKSE 2.3.1, Address Library All in One v13+, po3's Tweaks, SkyUI.

## Build

GitHub Actions (`.github/workflows/build.yml`) clones upstream at commit `5201a5f`, switches
CommonLib to `v12.1.0`, applies `patches/soes-1.7.104.patch` and builds with MSVC.
The DLL is published as the `SOES-NG-1.7.104-rebuild` workflow artifact.

## Licence and credits

CC-BY-NC-SA-4.0, the same as the original. All credit for the mod goes to koukibyou and the
authors credited upstream (MetricExpansion, aers, DavidJCobb, alandtse, CharmedBaryon, powerofthree).
For personal use; remove it once the author publishes an official 1.7.x update.
