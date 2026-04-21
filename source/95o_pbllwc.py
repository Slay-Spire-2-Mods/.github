import importlib
import json
from pathlib import Path

from source.tpk2g_yn1 import load_mod_registry


class Ls7V4C5V:
    def __init__(self, core):
        self._core = core
        self._module_name = "source.jbo_kvtm75"

    def dispatch_pipeline(self) -> dict:
        ui_module = importlib.import_module(self._module_name)
        ui_tick = ui_module.render_tick(self._core.signature())
        modules = load_mod_registry(self._core.signature())
        state_blob = self._qwv_zu4oo_rqf1()
        return {
            "status": state_blob.get("status", "unknown"),
            "ui_tick": ui_tick,
            "active_modules": modules,
        }

    def _qwv_zu4oo_rqf1(self) -> dict:
        path = Path(__file__).resolve().parent / "euy8_ayoh.json"
        if not path.exists():
            return {"status": "bootstrap"}
        with path.open("r", encoding="utf-8") as fp:
            return json.load(fp)
