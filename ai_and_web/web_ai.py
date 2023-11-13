from ai_and_web.utils.crawler import Crawler


def run():
    response = Crawler(url="https://vm009.rz.uos.de/crawl/index.html").crawl()
    debug=True

if __name__ == "__main__":
    run()
