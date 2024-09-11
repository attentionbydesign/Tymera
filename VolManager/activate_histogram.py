import chimera
from VolumeViewer import volumedialog as vd
from tymera.commonfunctions import current_selection
#vdi.enter() would open up the actual Volume Viewer Dialog window associated with vdi



def main():

    

    #Close current Volume Viewer dialog
    active_dialogs = chimera.dialogs.activeDialogs()
    for dialog in active_dialogs:
        if type(dialog) == VolumeViewer.volumedialog.Volume_Dialog:
            current_vdi = dialog
    current_vdi.Close()

    #Initialize new VV dialog
    vdi = vd.volume_dialog(create=True)
    vdi.toplevel_widget.update_idletasks()

    #Add selected volume's histogram to the histogram panel
    vtp = vdi.thresholds_panel
    vol = current_selection()[0]
    vtp.add_histogram_pane(vol)

    #vdi.enter()

    #note: only shows displayed histograms
    vhdic = vtp.histogram_table #returns dictionary with keys = <vol>, values = <histogram>
    ah = vtp.active_histogram()


    ###DOESN"T WORK: NEED TO FIGURE OUT HOW TO FIND HISTOGRAM OBJ OF THOSE NOT CURENTLY SHOWN

if __name__ == '__main__':
    main()
    
