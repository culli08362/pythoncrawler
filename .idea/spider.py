from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:

    # class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file + Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('first spider', Spider.base_url)

    @staticmethod
    def boot(self):
        Create_project_dir(spider.project_name)
        create_data_files(spider.project_name, spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print(thread_name + 'crawling' + page_url)
            print('Queue' + str(len(spider.queue)) + '| Crawled ' + str(len(spider.queue)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            spider.queue.remove(page_url)
            spider.crawled.ass(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('content-type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except:
            Print('Error: can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
