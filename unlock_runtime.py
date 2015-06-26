__author__ = 'Graham Voysey'

from yapsy.PluginManager import PluginManager
import logging
logging.basicConfig(level=logging.DEBUG)
def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["apps"])
    manager.collectPlugins()

    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        manager.activatePluginByName(plugin.name)
        plugin.plugin_object.print_status()

if __name__ == "__main__":
    main()