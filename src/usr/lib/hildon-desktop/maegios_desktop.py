import gtk
import gobject
import maegios

hd_plugin_type = maegios.MaegiosPlugin

# The code below is just for testing purposes.
# It allows to run the widget as a standalone process.
if __name__ == "__main__":
    gtk.gdk.threads_init()
    gobject.type_register(hd_plugin_type)
    obj = gobject.new(hd_plugin_type, plugin_id = "MaegiosDesktopWidget")
    obj.show_all()
    gtk.main()

