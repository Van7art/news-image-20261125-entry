# news-image-20261125-entry

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Van7art/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Van7art/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image summary of the world's news on Wednesday 25 November 2026,
drawn as a classic broadsheet front page titled **THE WORLD**. Variant A
of the news-image-20261125 entry for make.fun.

## The image

`entry.png` (1024×1024) is a newspaper front page titled **THE WORLD**:

- **Lead story:** Zelenskyy confirms Ukraine struck the Russian cargo
  ship Sparta II in the Gulf of Finland — a "legitimate target"
  carrying weapons; Norway urges caution. Illustrated with a drawn
  burning cargo ship at sea (PIL shapes only; no photographs, no real
  people depicted).
- **The day in brief:** nine further stories in a 3×3 grid, each with
  a short headline, a one-line deck, and a small drawn icon.
- **Also today:** a 5.6-magnitude quake in Nepal, Sarkozy's corruption
  case ordered to trial, and US consumer confidence at a two-year high.

## Stories covered

1. Zelenskyy confirms Ukraine hit the Russian ship Sparta II (Gulf of Finland)
2. Huawei found guilty of stealing trade secrets in a US trial
3. CIA and the Director of National Intelligence's office hit by a cyberattack
4. NATO to deploy early-warning aircraft in Poland
5. Trump awards Rudy Giuliani the Presidential Medal of Freedom
6. New US tariffs set to land after an excess-capacity probe
7. WHO evacuates staff from an Ebola hospital in DR Congo amid fighting
8. Houthi drone hits a tower in Riyadh — 11 injured
9. England level the T20 series in Australia (8-wicket win, chasing 185)
10. Putin: retaliation "inevitable" after Ukraine hit Russian oil plants
11. 5.6-magnitude earthquake hits Nepal's Koshi Province
12. Sarkozy corruption case ordered to trial (first hearing 1 April 2027)
13. US consumer confidence jumps to its highest in nearly two years

All thirteen stories are from Wednesday 25 November 2026. See `NOTES.md`
for one-line source notes and the run record.

## Variants

Three variants were built in `vA/`, `vB/`, and `vC/`; variant A (this
broadsheet) was chosen: it carries the most stories (13), has the
clearest hierarchy, and rendered without any text overlap. Variant B is
a bold magazine cover and variant C is a world map with numbered pins.

## Run it

```sh
python3 gen.py            # regenerate entry.png (needs Pillow)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library and copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It
needs no network access and is fully deterministic — repeated runs write
identical bytes.

## License

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
