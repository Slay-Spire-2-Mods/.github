import hashlib


_MODULE_POOL = [
    "overlay_sync",
    "session_watcher",
    "telemetry_ghost",
    "profile_bridge",
    "runtime_skin",
    "hotkey_mesh",
]


def load_mod_registry(signature: str) -> list[str]:
    h = hashlib.md5(signature.encode("utf-8")).hexdigest()
    pivot = int(h[:6], 16) % len(_MODULE_POOL)
    out = []
    for i in range(3):
        out.append(_MODULE_POOL[(pivot + i) % len(_MODULE_POOL)])
    return out
