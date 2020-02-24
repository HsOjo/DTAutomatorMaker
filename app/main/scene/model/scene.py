from typing import List

from app.base.model import BaseModel
from .feature import FeatureModel
from .object import ObjectModel


class SceneModel(BaseModel):
    _sub_model = dict(
        features=(list, FeatureModel),
        objects=(list, ObjectModel),
    )
    _ignore_attrs = ['img_path']

    def __init__(self, event: dict):
        self._event = event
        self.name = ''
        self.img = ''
        self.features = []  # type: List[FeatureModel]
        self.objects = []  # type: List[ObjectModel]

    @property
    def img_path(self):
        return self._event['get_path'](self.img)
