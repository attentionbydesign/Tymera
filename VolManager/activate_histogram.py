import chimera
from VolumeViewer import volumedialog as vd

vdi = vd.Volume_Dialog()
vdi.toplevel_widget.update_idletasks()

#vdi.enter() would open up the actual Volume Viewer Dialog window associated with vdi

vtp = vdi.thresholds_panel

#note: only shows displayed histograms
vhdic = vtp.histogram_table #returns dictionary with keys = <vol>, values = <histogram>

ah = vtp.active_histogram()
