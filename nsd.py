
2
chatgpt
def __init__(self, blender=None, render=None, transform=None):
  self.blender = blender
  self.render = render
  self.transform = transform
  self.parent = True
  self.graph = None
  self.children = []
class RootTranslationNode(TranslationNode):
"""Acts as the root node of a translation graph"""
def __init__(self):
self.transform = None
self.render = None
self.blender = None
self.children = []
self.parent = None
@property
def name(self):
return "<ROOT>"
"""
translation.py
Holds the translation tree that we use to step to/from blender/edm forms
"""
from inspect import isgenerator
from .utils import get_all_parents, get_root_object
_prefixLookup = {"transform": "tf", "CONNECTORS": "cn", "RENDER_NODES": "rn", "SHELL_NODES": "shell", "LIGHT_NODES": "light"}
class TranslationNode(object):
 """Holds a triple of blender object, render node and transform nodes.
Each TranslationNode maps to maximum ONE blender object maximum ONE renderNode
and maximum ONE transform node. It may map to more than one type, in cases
where they are directly equatable.
 """
blender = None
render = None
transform = None
graph = None
@property
def name(self):
if self.blender:
return "bl:" + self.blender.name
