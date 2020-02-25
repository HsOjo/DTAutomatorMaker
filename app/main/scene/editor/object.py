from typing import List

from .rect import RectEditor
from ..model import ObjectModel
from ..object import AdvanceRect


def _sync(func):
    def wrapper(self: 'ObjectEditor', *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.sync()
        return result

    return wrapper


class ObjectEditor(RectEditor):
    def __init__(self, event):
        super().__init__(event)
        self._objects = None  # type: List[ObjectModel]

    @property
    def current_object(self):
        return self._rects.get(self._current_rect)

    def load_objects(self, objects: List[ObjectModel]):
        self._objects = objects
        rects = {}
        for object in objects:
            rect = self.new_rect(object.rect, False)
            rects[rect] = object
        self._rects = rects
        self.set_current_rect(None, False)

    def set_current_rect(self, rect, sync=True):
        super().set_current_rect(rect)

        if sync and rect in self._rects:
            self.event['select_object'](self.rects.index(rect))

    @_sync
    def add_item(self, rect):
        if self._objects is None:
            return False
        name = ''
        names = [object.name for object in self._objects]
        for i in range(10000):
            name = 'Untitiled_%s' % i
            if name not in names:
                break

        object = ObjectModel()
        object.name = name
        object.rect = [*rect]
        self._rects[rect] = object
        self._objects.append(object)
        return True

    @_sync
    def callback_rect_moving(self, rect_moving: AdvanceRect, moving):
        super().callback_rect_moving(rect_moving, moving)

    @_sync
    def callback_adjust(self, rect_adjust: AdvanceRect, adjust: bool):
        super().callback_adjust(rect_adjust, adjust)

    def sync(self):
        for rect, object in self._rects.items():
            rect: AdvanceRect
            object: ObjectModel
            object.rect = [*rect]
        self.event['sync_objects'](self._objects)
