from typing import Dict

from PyQt5.QtGui import QColor

from app.base.widget.graphics import Rect
from .base import BaseEditor
from ..object import AdvanceRect


class RectEditor(BaseEditor):
    COLOR_NEW = QColor(0, 255, 0)
    COLOR_UNFOCUS = QColor(255, 255, 0)
    COLOR_UNFOCUS_MOVING = QColor(255, 255, 0, 128)
    COLOR_FOCUS = QColor(255, 128, 0)

    def __init__(self, event):
        super().__init__(event)
        self._rects = {}  # type: Dict[AdvanceRect]
        self._current_rect = None  # type: AdvanceRect
        self._new_rect = Rect(self.event)
        self._new_rect.set_color(self.COLOR_NEW)

        self._creating = False

    @property
    def rects(self):
        return list(self._rects.keys())

    def select(self, index):
        rects = self.rects
        if 0 <= index < len(rects):
            self.set_current_rect(rects[index], sync=False)

    def set_current_rect(self, rect, sync=True):
        if self._current_rect is not None:
            self._current_rect.set_color(self.COLOR_UNFOCUS)
            self._current_rect.set_focus(False)

        self._current_rect = rect
        if rect is not None:
            rect.set_color(self.COLOR_NEW if rect == self._new_rect else self.COLOR_FOCUS)
            rect.set_focus(True)

        if sync and rect in self._rects:
            self.event['select_feature'](self.rects.index(rect))

    def update(self):
        mouse = self.mouse
        rect_new = self._new_rect

        if self._creating:
            rect_new.set_size(mouse.x - rect_new.x, mouse.y - rect_new.y)
            if mouse.release(mouse.BUTTON_LEFT):
                self.new_rect()
                self._creating = False
        else:
            for rect in self._rects:
                rect.update()

            if self._current_rect is not None:
                if not self._current_rect.focus:
                    self.set_current_rect(None)

            if self._current_rect is None:
                if mouse.down(mouse.BUTTON_LEFT):
                    for rect in reversed(self.rects):
                        if rect.check_point(*mouse.position):
                            self.set_current_rect(rect)
                            break
                    if self._current_rect is None:
                        rect_new.set_position(*mouse.position)
                        rect_new.set_size(0, 0)
                        self._creating = True
                    else:
                        self._current_rect.update()

    def new_rect(self, rect=None, sync=True):
        rect = AdvanceRect(self.event, *(self._new_rect if rect is None else rect))
        rect.set_size(*rect.size, convert_negative=True)
        rect.set_focus_color(self.COLOR_FOCUS, self.COLOR_UNFOCUS)
        rect.set_callback_moving(lambda b: self.callback_rect_moving(rect, b))
        if sync:
            if self.add_item(rect):
                self.set_current_rect(rect)

        return rect

    def add_item(self, rect):
        self._rects[rect] = None
        return True

    def draw(self):
        for rect in self._rects:
            rect.draw()
        if self._creating:
            self._new_rect.draw()

    def callback_rect_moving(self, rect_moving: AdvanceRect, moving):
        for rect in self._rects:
            if moving:
                if rect != rect_moving:
                    rect.set_color(self.COLOR_UNFOCUS_MOVING)
            else:
                if rect != rect_moving:
                    rect.set_color(self.COLOR_UNFOCUS)