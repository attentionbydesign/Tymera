def volsel():
    import chimera
    from VolumeViewer import volume_list

    # Get the current selection in Chimera
    selected_items = chimera.selection.currentGraphs()

    # Filter the selected items to find volumes
    selected_volumes = [item for item in selected_items if isinstance(item, volume_list()[0].__class__)]

    if selected_volumes:
        vol = selected_volumes[0]
        return vol
    else:
        print("No volume selected")
