"""Rewrite SOES-NG's English MCM translation file.

- Prefixes body-slot labels with their slot number: "Head" -> "[30] Head".
- Shortens "Unofficial (Typically X)" to "X (unofficial)" so labels fit the MCM column.
- Adds any new keys used by the patched scripts.

The file is UTF-16 LE with BOM and CRLF line endings (what SkyUI expects); both are preserved.
Usage: python translations.py <input.txt> <output.txt>
"""
import re
import sys

NEW_KEYS = {
    "$SkyOutEquSys_EmptySlot": "-",
}


def relabel(key: str, value: str) -> str:
    m = re.fullmatch(r"\$SkyOutEquSys_BodySlot(\d+)", key)
    if not m:
        return value
    u = re.fullmatch(r"Unofficial \(Typically (.+)\)", value)
    if u:
        value = u.group(1)  # drop the "Unofficial" qualifier to save space
    return f"[{m.group(1)}] {value}"


def main(src: str, dst: str) -> None:
    raw = open(src, "rb").read()
    text = raw.decode("utf-16")  # handles the BOM
    lines = text.split("\r\n")
    seen = set()
    out = []
    for line in lines:
        if "\t" in line and line.startswith("$"):
            key, value = line.split("\t", 1)
            seen.add(key)
            line = f"{key}\t{relabel(key, value)}"
        out.append(line)
    # Insert new keys before the trailing empty line, if any.
    trailer = []
    while out and out[-1] == "":
        trailer.append(out.pop())
    for key, value in NEW_KEYS.items():
        if key not in seen:
            out.append(f"{key}\t{value}")
    out.extend(trailer)
    with open(dst, "wb") as f:
        f.write("\r\n".join(out).encode("utf-16"))  # utf-16 writes a LE BOM on Windows/x86


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
