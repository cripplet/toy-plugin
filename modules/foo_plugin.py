class BaseProperty(object):
  def __init__(self, ref):
    self._ref = ref

  @property
  def ref(self):
    return self._ref

  @property
  def injected(self, *args, **kwargs):
    raise NotImplemented('This is an abstract method.')

  # actual called property
  def __call__(self, *args, **kwargs):
    return self.injected(*args, **kwargs)

class Property(BaseProperty):
  def injected(self, *args, **kwargs):
    return self.ref.metadata
