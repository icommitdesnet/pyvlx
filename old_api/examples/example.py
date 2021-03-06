"""Example implementation for PyVLX."""
import asyncio
from pyvlx import PyVLX


async def main():
    """Load devices and scenes, run first scene."""
    pyvlx = PyVLX('pyvlx.yaml')
    # Alternative:
    # pyvlx = PyVLX(host="192.168.2.127", password="velux123", timeout=60)

    await pyvlx.load_devices()
    print(pyvlx.devices[1])
    print(pyvlx.devices['Fenster 4'])

    await pyvlx.load_scenes()
    print(pyvlx.scenes[0])
    print(pyvlx.scenes['Bath Closed'])

    # opening/ closing windows by running scenes, yay!
    await pyvlx.scenes[1].run()

    await pyvlx.disconnect()


# pylint: disable=invalid-name
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
