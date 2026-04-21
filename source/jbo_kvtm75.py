import itertools

_ticker = itertools.cycle(["[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]"])


def md1k_v0s9(signature: str) -> int:
    return sum(ord(ch) for ch in signature) % 97


def jnr_7rxo(seed: int) -> str:
    palette = ["neon", "amber", "cyan", "violet", "mono"]
    return palette[seed % len(palette)]


def render_tick(signature: str) -> str:
    x = md1k_v0s9(signature)
    style = jnr_7rxo(x)
    return f"{next(_ticker)} mode={style} pulse={x}"
