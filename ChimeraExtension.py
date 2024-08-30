# -----------------------------------------------------------------------------
# Class to register the Tymera plugin in Chimera.
# The plugin will be located in Custom Plugins menu
#
import chimera.extension

# -----------------------------------------------------------------------------
#
class Tymera_EMO(chimera.extension.EMO):

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
