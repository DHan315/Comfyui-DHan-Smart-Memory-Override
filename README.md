# ComfyUI Smart Memory Override v1.0.0

This targets ComfyUI Smart Memory, not Dynamic VRAM.

Use:
Klein Model Loader -> Disable Smart Memory (Model) -> sampler

It sets:
comfy.model_management.DISABLE_SMART_MEMORY = True

This is the same runtime variable initialized by the ComfyUI launch flag:
--disable-smart-memory

Important: Smart Memory is global ComfyUI state. Once changed, it stays changed
until another override node changes it or ComfyUI restarts.

For a clean Klein A/B test, do not also use the old Disable Dynamic VRAM node.
