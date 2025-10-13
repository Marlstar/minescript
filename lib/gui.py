import lib.private

def get_title() -> str | None:
    """
    Retrieves the title

    Returns:
        str or None: The title, or None if not available.
    """
    title = private.get_field(mc.gui, "title")
    if title is not None:
        title = title.tryCollapseToString()
    return title  # type: ignore

def get_subtitle() -> str | None:
    """
    Retrieves the subtitle

    Returns:
        str or None: The subtitle, or None if not available.
    """
    subtitle = private.get_field(mc.gui, "subtitle")
    if subtitle is not None:
        subtitle = subtitle.tryCollapseToString()
    return subtitle  # type: ignore

def get_actionbar() -> str | None:
    """
    Retrieves and clears the current action bar (overlay message) string from the Minecraft GUI.

    Returns:
        str or None: The current overlay message string if present, otherwise None.
    """
    overlayMessageString = private.get_field(mc.gui, "overlayMessageString")
    if overlayMessageString is not None:
        overlayMessageString = overlayMessageString.tryCollapseToString()
        mc.gui.setOverlayMessage(None, False)
    return overlayMessageString  # type: ignore

def set_title(text: str) -> None:
    """
    Sets the title to the specified text.

    Args:
        text (str): The text to set as the title.

    Returns:
        None
    """
    mc.gui.setTitle(Component.literal(text))

def set_subtitle(text: str) -> None:
    """
    Sets the subtitle to the specified text.

    Args:
        text (str): The text to set as the subtitle.

    Returns:
        None
    """
    mc.gui.setSubtitle(Component.literal(text))

def set_actionbar(text: str, tinted: bool = False) -> None:
    """
    Sets the actionbar to the specified text.

    Args:
        text (str): The text to set as the actionbar.

    Returns:
        None
    """
    mc.gui.setOverlayMessage(Component.literal(text), tinted)

def set_title_times(fadeInTicks: int, stayTicks: int, fadeOutTicks: int) -> None:
    """
    Sets the timing for the title and subtitle display.

    Args:
        fadeInTicks (int): Number of ticks for the title to fade in.
        stayTicks (int): Number of ticks for the title to stay visible.
        fadeOutTicks (int): Number of ticks for the title to fade out.

    Returns:
        None
    """
    mc.gui.setTimes(fadeInTicks, stayTicks, fadeOutTicks)

def reset_title_times() -> None:
    """
    Resets the title and subtitle display times to the default values.

    Returns:
        None
    """
    mc.gui.resetTitleTimes()

def clear_titles() -> None:
    """
    Clear the title and subtitle.

    Returns:
        None
    """
    mc.gui.clearTitles()
