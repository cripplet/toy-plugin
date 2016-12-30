import functools
import importlib

class BaseObject(object):
  def __init__(self, *args, **kwargs):
    self._name = 'dynamic module'
    self._metadata = {}
    self._modules = set()

  @property
  def name(self):
    return self._name

  @property
  def metadata(self):
    return self._metadata

  @property
  def modules(self):
    return self._modules

  def __getattr__(self, key):
    if not key in self.__dict__ and key not in self.modules:
      try:
        setattr(self, key, importlib.import_module(
            'modules.' + key, __name__).Property(self))
        self.modules.add(key)
        return self.__getattribute__(key)
      except ImportError:
        raise AttributeError(
            "type object '%s' has no attribute "
            "'%s'" % (type(self).__name__, key))


if __name__ == "__main__":
  b = BaseObject()
  b.metadata['name'] = 'BaseObject'
  assert b.foo_plugin()['name'] == 'BaseObject'
