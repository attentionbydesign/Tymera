# -----------------------------------------------------------------------------
# Class to register the Tymera plugin in Chimera.
# The plugin will be located in Custom Plugins menu
#
import chimera.extension

# -----------------------------------------------------------------------------
#
class Tymera_EMO(chimera.extension.EMO):
    #This syntax means that the Tymera_EMO class INHERITS the properties of the class <chimera.extension.EMO>.  Thus, you can easily define a class to register your custom plugin without needing to write much chimera-specific code.
    #i.e., Tymera_EMO is a child class,while in parentheses is the parent class

    def name(self):
        return 'Tymera'
    def description(self):
        return 'Custom library for UCSF Chimera'
    def categories(self):
        return ['Custom Plugins']
    def icon(self):
        return None
    def activate(self):
        self.module('tymera_init').initialize()
        return None

chimera.extension.manager.registerExtension(Tymera_EMO(__file__))
