class Producto:
  def __init__(self, *args, **kwargs):
    self.sku = kwargs.sku
    self.clave_ = kwargs.sku
    print(f'{kwargs}')


p = Producto()