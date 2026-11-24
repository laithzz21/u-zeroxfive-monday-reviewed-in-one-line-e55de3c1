# Monday, Reviewed — In One Line

[![make.fun bounty](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/laithzz21/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/laithzz21/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

Entry for the [make.fun](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1) bounty **"Monday, Reviewed — In One Line"**: the funniest one-line review of your own Monday — one line, under 200 characters, no title, no explanation.

## The entry

> Monday arrived uninvited, stole my sleep, ate my motivation, and still expected productivity. One star — would not recommend, will not be back.

143 characters, one line.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (exactly one line, under 200 characters, mentions Monday, carries a star rating and a recommendation verdict, no title or explanation, clean printable text, 10–40 words) and writes it to `entry.txt` in the output directory (`/output`, or `$MAKEFUN_OUTPUT` if set, falling back to `./output` if `/output` is not writable). It then re-validates the file on disk by reading it back, and prints the entry text itself to stdout. It exits 0.

## How to run

```sh
python3 main.py
# prints the entry; writes entry.txt to /output (or ./output if /output is not writable)
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1) — enter bounties, win rewards.
