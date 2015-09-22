"""
1. Initialize pyglet window/runtime
2. Process DAQ plugins
3. Process Decoder plugins
4. Process App plugins
"""
from yapsy.PluginManager import PluginManager

from core.pyglet_window import PygletWindow
from plugins.drivers.daqplugin import DAQPlugin
from plugins.apps.appplugin import AppPlugin
from plugins.decoders.decoderplugin import DecoderPlugin


if __name__ == "__main__":
    manager = PluginManager()
    manager.setPluginPlaces(['plugins'])
    manager.setCategoriesFilter({'DAQ': DAQPlugin,
                                 'App': AppPlugin,
                                 'Decoder': DecoderPlugin})
    manager.collectPlugins()

    window = PygletWindow(manager)

    # for plugin in manager.getPluginsOfCategory('DAQ'):
    #     manager.activatePluginByName(plugin.name)
    #     plugin.plugin_object.open()
    #     plugin.plugin_object.init()
    #
    # for plugin in manager.getPluginsOfCategory('Decoder'):
    #     manager.activatePluginByName(plugin.name)

    for plugin in manager.getPluginsOfCategory('App'):
        manager.activatePluginByName(plugin.name)
        plugin.plugin_object.register(window)

    window.start()
