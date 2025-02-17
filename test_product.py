import pytest
import products


def test_correct_init():
    """
    Tests if a Product instance is correctly initiated
    when parameters are correctly passed.
    """
    example_product = products.Product("bed", 10, 100)
    assert example_product.name == "bed"
    assert example_product.price == 10
    assert example_product.quantity == 100
    assert example_product.active == True


def test_incorrect_price_init():
    """
    Tests that in case user passes incorrect price,
    the Product instance is not activated.
    """

    # price is a string
    example_product = products.Product("bed", "10", 100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False

    # price is negative
    example_product = products.Product("bed", -122, 100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False

    # price is 0
    example_product = products.Product("bed", 0, 100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False


def test_incorrect_quantity_init():
    """
    Tests that in case user passes incorrect quantity,
    the Product instance is not activated.
    """
    # quantity is a string
    example_product = products.Product("bed", 10, "100")
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False


    # quantity is negative
    example_product = products.Product("bed", 10, -100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False

    # quantity is 0
    example_product = products.Product("bed", 10, 0)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False


def test_incorrect_name_init():
    """
    Tests that in case user passes incorrect name,
    the Product instance is not activated.
    """
    # name is not a string
    example_product = products.Product(1, 10, 100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False

    # name is empty
    example_product = products.Product("", 10, 100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False

    # name is too short
    example_product = products.Product("b", 10, 100)
    assert example_product.name is None
    assert example_product.price == 0
    assert example_product.quantity == 0
    assert example_product.active == False


def test_deactivation():
    """
    Tests if a product inactive, when its quantity drops to 0.
    """
    example_product = products.Product("bed", 10, 100)
    assert example_product.active == True
    example_product.set_quantity(0)
    assert example_product.active == False


def test_quantity_change():
    """
    Tests if after a purchase,
    product's quantity changes and if correctly.
    """
    example_product = products.Product("bed", 10, 100)
    example_product.buy(10)
    new_quantity = example_product.get_quantity()
    assert new_quantity == 100 - 10


def test_overbuying():
    """
    Tests if when user buys more product units than is available,
    an exception is raised.
    """
    example_product = products.Product("bed", 10, 100)
    assert example_product.buy(101) == 0

pytest.main()

# with pytest.raises(ValueError(f"Invalid parameter(s). {name} not added to the store")):
#     example_product = products.Product("bed", 10, "100")
