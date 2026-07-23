# 2026-07-21T15:02:47.876
import vitis

client = vitis.create_client()
client.set_workspace(path="chal_ja_bhai")

platform = client.get_component(name="platform")
status = platform.build()

status = client.add_platform_repos(platform=["d:\Desktop\Accelerator\chal_ja_bhai\platform"])

comp = client.create_app_component(name="led_app",platform = "$COMPONENT_LOCATION/../platform/export/platform/platform.xpfm",domain = "standalone_ps7_cortexa9_0")

status = platform.build()

comp = client.get_component(name="led_app")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

vitis.dispose()

vitis.dispose()

