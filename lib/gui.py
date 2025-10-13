# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false

from lib.private import get_field
from lib.instance import mc
from lib.javatypes import Component

class Title:
    @staticmethod
    def get() -> str | None:
        title = get_field(mc.gui, "title")
        if title is not None:
            title = title.tryCollapseToString()
        return title

    @staticmethod
    def set(text: str):
        mc.gui.setTitle(Component.literal(text))

class Subtitle:
    @staticmethod
    def get() -> str | None:
        subtitle = get_field(mc.gui, "subtitle")
        if subtitle is not None:
            subtitle = subtitle.tryCollapseToString()
        return subtitle

    @staticmethod
    def set(text: str):
        mc.gui.setSubtitle(Component.literal(text))

class Actionbar:
    @staticmethod
    def get() -> str | None:
        overlayMessageString = get_field(mc.gui, "overlayMessageString")
        if overlayMessageString is not None:
            overlayMessageString = overlayMessageString.tryCollapseToString()
        return overlayMessageString  # type: ignore

    @staticmethod
    def set(text: str, tinted: bool = False):
        mc.gui.setOverlayMessage(Component.literal(text), tinted)

class TitleTimes:
    @staticmethod
    def set(fade_in: int, stay: int, fade_out: int):
        """ Sets the timing for the title and subtitle display (in ticks) """
        mc.gui.setTimes(fade_in, stay, fade_out)

    @staticmethod
    def reset():
        mc.gui.resetTitleTimes()

def clear_titles():
    """ Clear title and subtitle """
    mc.gui.clearTitles()
