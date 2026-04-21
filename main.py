from source.gy70_c7x import Ru66Ag4X64
from source.95o_pbllwc import Ls7V4C5V


def bootstrap():
    core = Ru66Ag4X64(salt="9kiakshkkg7ewxt75sh1", build="b-41bg3-2029")
    router = Ls7V4C5V(core)
    result = router.dispatch_pipeline()
    print("Session:", core.signature())
    print("Status :", result["status"])
    print("UI Tick:", result["ui_tick"])
    print("Mods   :", ",".join(result["active_modules"]))


if __name__ == "__main__":
    bootstrap()
