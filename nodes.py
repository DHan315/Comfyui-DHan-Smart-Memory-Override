import logging
logger = logging.getLogger(__name__)

def _set_disabled(disabled: bool):
    import comfy.model_management as mm
    prev = bool(getattr(mm, "DISABLE_SMART_MEMORY", False))
    mm.DISABLE_SMART_MEMORY = bool(disabled)
    try:
        from comfy.cli_args import args
        args.disable_smart_memory = bool(disabled)
    except Exception:
        pass
    logger.info(
        "[Smart Memory Override] Smart Memory %s (DISABLE_SMART_MEMORY=%s).",
        "DISABLED" if disabled else "ENABLED",
        bool(disabled),
    )
    return prev

class DisableSmartMemoryModel:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"model": ("MODEL",)}}
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "run"
    CATEGORY = "Comfyui-DHan/Memory"
    DESCRIPTION = (
        "Disables ComfyUI Smart Memory globally at runtime, then passes MODEL through. "
        "Targets the same DISABLE_SMART_MEMORY flag initialized by --disable-smart-memory."
    )
    def run(self, model):
        _set_disabled(True)
        return (model,)

class SmartMemoryOverrideModel:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "model": ("MODEL",),
            "smart_memory": (["disable", "enable"], {"default": "disable"}),
        }}
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "run"
    CATEGORY = "Comfyui-DHan/Memory"
    DESCRIPTION = (
        "Runtime Smart Memory control. This is global ComfyUI state, not per-model."
    )
    def run(self, model, smart_memory):
        _set_disabled(smart_memory == "disable")
        return (model,)

class EnableSmartMemoryModel:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"model": ("MODEL",)}}
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "run"
    CATEGORY = "Comfyui-DHan/Memory"
    DESCRIPTION = "Re-enables ComfyUI Smart Memory globally at runtime."
    def run(self, model):
        _set_disabled(False)
        return (model,)

NODE_CLASS_MAPPINGS = {
    "DisableSmartMemoryModel": DisableSmartMemoryModel,
    "SmartMemoryOverrideModel": SmartMemoryOverrideModel,
    "EnableSmartMemoryModel": EnableSmartMemoryModel,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DisableSmartMemoryModel": "DHan-Disable Smart Memory (Model)",
    "SmartMemoryOverrideModel": "DHan-Smart Memory Override (Model)",
    "EnableSmartMemoryModel": "DHan-Enable Smart Memory (Model)",
}
