"""Implement one particular client parser."""
import xml.etree.ElementTree as ET
from model import Product, Image


class ClientParser:
    """Client parser abstract class."""

    def __len__(self):
        """Get number of products.

        Return:
            int, number of products

        """
        raise NotImplementedError

    def __getitem__(self, idx):
        """Get the product of index `idx`.

        Iterate over the feed and extract needed information for the product
        at `idx` index.

        Return:
            Product, one product

        """
        raise NotImplementedError


class ClientAParser(ClientParser):
    """Client A parser."""

    def __init__(self, filename):
        """Client parser constructor."""
        self.tree = ET.parse(filename)

    def __len__(self):
        #TODO, implement "how to get number of products"
        pass

    def __getitem__(self, idx):
        #TODO, implement the parsing product at `idx`
        # For instance, get the following information and others from the XML:
        # category = 'Papyon'
        # price = 329.00
        # gender = "male"
        pass

    # auto generated doc from super class
    __len__.__doc__ = ClientParser.__len__.__doc__
    __getitem__.__doc__ = ClientParser.__getitem__.__doc__


if __name__ == '__main__':

    import time

    xml_filename = 'example_feed.xml'
    parser = ClientAParser(xml_filename)

    tic = time.time()
    # optimize and speed the whole xml parsing
    # you could use threading, multi processing and etc
    for idx in range(len(parser)):
        product = parser[idx]
    toc = time.time() - tic
    print('Elapsed {} secs'.format(toc))