def setPlaceholder(widget, placeholderText):
    """
    For wx/qt/web, enable the placeholder setting.
    For tk, use alternative implementation.
    Implementation note:
        Normally I would check attributes with hasattr,
        Even though it is SimpleGUIWeb, there are still attributes for Qt, so I have taken a workaround.
    """
    if getattr(widget, "WxTextCtrl", None): 
        textCtrl = widget.WxTextCtrl 
        textCtrl.SetHint(placeholderText)
        return
    if getattr(widget, "QT_QLineEdit", None): 
        lineEdit = widget.QT_QLineEdit 
        lineEdit.setPlaceholderText(placeholderText)
        return
    if getattr(widget, "Widget", None) and hasattr(widget.Widget, "attributes"): 
        textInput = widget.Widget 
        textInput.attributes["placeholder"] = placeholderText
        return
    if getattr(widget, "TKEntry", None):
        entry = widget.TKEntry
        def resetCursor(event=None):
            if entry.get() == placeholderText:
                entry.after_idle(entry.icursor, 0)
        def startInput(event=None):
            if entry.get() == placeholderText:
                entry.delete(0, "end")
                entry.config(fg="black")
            else:
                entry.after_idle(showPlaceholder)
        def showPlaceholder(event=None):
            if entry.get() == placeholderText or not entry.get():
                entry.delete(0, "end")
                entry.insert(0, placeholderText)
                entry.config(fg="gray50")
                entry.after_idle(entry.icursor, 0)
        entry.bind("<FocusIn>", resetCursor)
        entry.bind("<FocusOut>", showPlaceholder)
        entry.bind("<Button-1>", resetCursor)
        entry.bind("<Key>", startInput)
        showPlaceholder()
        def get_value():
            text = entry.get()
            return text if text != placeholderText else ""
        widget.Get = get_value
        return
    import warnings
    warnings.warn("Unknown GUI Platform, setPlaceholder was ignored.")