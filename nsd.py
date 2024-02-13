1
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
