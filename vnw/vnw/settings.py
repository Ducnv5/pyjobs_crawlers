import os


BOT_NAME = 'vnw'
BOT_VERSION = '1.0.5'

SPIDER_MODULES = ['vnw.spiders']
NEWSPIDER_MODULE = 'vnw.spiders'
ITEM_PIPELINES = {
        'vnw.pipelines.ValidatePipeline': 500,
}

USER_AGENT = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,"
              " like Gecko) Chrome/48.0.2564.116 Safari/537.36")

is_prod = os.environ.get('PYJOBS_IS_PROD', False)
if is_prod:
    ITEM_PIPELINES.update({
            'vnw.pipelines.APIPipeline': 1000,
    })
    DOWNLOAD_DELAY = 2
    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,  # NOQA
        'vnw.rotate_useragent.RotateUserAgentMiddleware': 400
    }

    try:
        import prodsettings as prod
    except ImportError:
        pass
    else:
        VIETNAMWORK_USERNAME = prod.custom.get('VIETNAMWORK_USERNAME', '')
        VIETNAMWORK_PASSWORD = prod.custom.get('VIETNAMWORK_PASSWORD', '')
