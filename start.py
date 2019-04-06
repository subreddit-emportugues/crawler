from __future__ import absolute_import
from crawler import Crawler


def main():
    crawler = Crawler()
    crawler.read_list()
    crawler.write_object()


if __name__ == u"__main__":
    main()
