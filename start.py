from crawler import Crawler
import urllib3



urllib3.disable_warnings()


def main():
    crawler = Crawler()
    crawler.read_list()
    crawler.write_object()


if __name__ == "__main__":
    main()
