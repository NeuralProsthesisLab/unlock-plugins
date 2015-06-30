__author__ = 'Graham Voysey'
# ref https://web.archive.org/web/20130731202108/http://lateral.netmanagers.com.ar/weblog/posts/BB923.html
from yapsy.PluginManager import PluginManager
from apps.plugin_one.plugin_one import PluginOne
import core
import logging
logging.basicConfig(level=logging.DEBUG)
def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager() #categories_filter={"testers": PluginOne}
    manager.setPluginPlaces(["apps"])
    manager.collectPlugins()

    #Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        manager.activatePluginByName(plugin.name)
        logging.debug("UNLOCK found plugin: " + plugin.name + ", with description: " +plugin.description);

if __name__ == "__main__":
    main()
