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

- Plugin version 0.1.5. No changes to the ESP or Papyrus scripts.

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
