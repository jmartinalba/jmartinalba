import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

import dadoJgo_main

class HandlerManejador:

##    def __ini__(self):
##        """La función de esta clase es llamar a modulos involucrados en la
##construcción del juego del CRAPS.
##
##           Modulos: dadoJgo_main, dadoJgo_main y guiDado           
##            Clases: dodo y constante    
##
##"""
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def on_button_jugar_clicked(self, button):
        dadoJgo_main.jugar(builder)
    def on_button_continuar_clicked(self, button):
       dadoJgo_main.inicializar(builder)
    def on_button_salir_clicked(self, button):
        sys.exit(0)
builder = Gtk.Builder()
builder.add_from_file("src/gladeGui/jgoDado.glade")
window = builder.get_object("ventana_main")
builder.connect_signals(HandlerManejador())
window.show_all()

Gtk.main()




##Nowadays, the probably more prevalent format is the reStructuredText
##(reST) format that is used by Sphinx to generate documentation.



##When a module is loaded from a file in Python, __file__ is set to its path. You
##can then use that with other functions to find the directory that the file is
##located in. Si mantengo la  estructura /home/cnad/Programacion/py_prj y llevo el
##proyecto a otro equipo con /home/control/Programacion/py_prj, requiero la ruta
##actual y agregar el nombre del paquete para agregarlo a  la ruta de busqueda de
##modulos, en sys.path.append







##https://www.pornhub.com/view_video.php?viewkey=1154905636
##https://www.pornhub.com/view_video.php?viewkey=ph5de195d7b95d4
##https://www.pornhub.com/view_video.php?viewkey=ph5c5333be75338
##https://www.pornhub.com/view_video.php?viewkey=ph5de193b472658
##https://www.pornhub.com/view_video.php?viewkey=930554575
##https://www.pornhub.com/view_video.php?viewkey=1376176790