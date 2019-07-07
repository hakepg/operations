'''
class Product:

    def __init__(self,innerproduct):
        self.ProductId = innerproduct.ProductId
        self.ProductName = innerproduct.ProductName
        self.ProductPrice = innerproduct.ProductPrice
        self.ProductModel = innerproduct.ProductModel

        try:
            if getattr(innerproduct,'customizable'):
                self.productCustome = innerproduct.customizable
        except:
            pass

        try:
            if getattr(innerproduct,'discountamnt'):
                self.productdiscount = innerproduct.discountamnt
        except:
            pass


    class InnerProduct:
        def __init__(self,id,nam,price,model):
            self.ProductId = id
            self.ProductName = nam
            self.ProductPrice = price
            self.ProductModel = model

        def setCustomeFeature(self, flag):
            self.customizable = flag
            return self

        def setDiscountAmount(self, discount):
            self.discountAmnt = discount
            return self

        def build(self):
            return Product(self)

if __name__ == '__main__':
    ob = Product.InnerProduct(id=10, nam="Mobile", model="AA", price=20393).build()
    print('object:', ob.__dict__)

    ob1 = Product.InnerProduct(id=10, nam="Mobile", model="AA", price=20393).setCustomeFeature("aa").build()
    print('object1:', ob1.__dict__)
    ob2 = Product.InnerProduct(id=10, nam="Mobile", model="AA", price=20393).setDiscountAmount(1000).build()
    print('object2:', ob2.__dict__)

    ob3 = Product.InnerProduct(id=10, nam="Mobile", model="AA", price=20393).setDiscountAmount(1000).setCustomeFeature("Yes").build()
    print('object3:', ob3.__dict__)
'''


import abc


class Director:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class Product:
    """
    Represent the complex object under construction.
    """

    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product


if __name__ == "__main__":
    main()