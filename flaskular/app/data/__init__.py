from product_mock import ProductMock
from product_category_mock import ProductCategoryMock
from lxml import etree
import os


mock_data = etree.parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../feed.xml'), etree.XMLParser(recover=True))
product_mock = ProductMock(mock_data)
product_category_mock = ProductCategoryMock(mock_data)
