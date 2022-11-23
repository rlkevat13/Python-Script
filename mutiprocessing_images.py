import time
import requests
import logging
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool

urls = [
    {'configuration_name': 'ram_0', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_6gMPaVgIPuuJ7qC"},
    {'configuration_name': 'ram_1', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_5hyec3pXLIMxBf7"},
    {'configuration_name': 'ram_2', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_2b2UA3ggSdftrDL"},
    {'configuration_name': 'ram_3', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_b9GfpSj4xPudvtI"},
    {'configuration_name': 'ram_4', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_9Xo5dJaXdU2WSWi"},
    {'configuration_name': 'ram_5', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_5aQcJ4rlRluRGZL"},
    {'configuration_name': 'ram_6', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_86BIujc2Hkmaphz"},
    {'configuration_name': 'ram_7', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_eVXrsKFXP5kqWcl"},
    {'configuration_name': 'ram_8', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_dd7u6hBKavGMHHv"},
    {'configuration_name': 'ram_9', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_6hB84EwaqsqIvOK"},
    {'configuration_name': 'ram_10', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_1zaIsJa6TBL3nzU"},
    {'configuration_name': 'ram_11', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_a2TofcG6zUZvYqO"},
    {'configuration_name': 'ram_12', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3ZQdwEEfqArdDM2"},
    {'configuration_name': 'ram_13', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_1N3v4SLW9NGA6Gy"},
    {'configuration_name': 'ram_14', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_dmuXMoHZizovN8G"},
    {'configuration_name': 'ram_15', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_0OOewry6tLvxeLj"},
    {'configuration_name': 'ram_16', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_37uUgizhes5Obvo"},
    {'configuration_name': 'ram_17', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_2rbN16GpCKVcBNj"},
    {'configuration_name': 'ram_18', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3KRhnYss3apj9mm"},
    {'configuration_name': 'ram_19', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3J0yMhvH8CTh3ym"},
    {'configuration_name': 'ram_20', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3dzE2lorQr9qEey"},
    {'configuration_name': 'ram_21', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_bKM7q0JVlexrhHw"},
    {'configuration_name': 'ram_22', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_2aWYzT9kKyAzKsu"},
    {'configuration_name': 'ram_23', 'url': "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_cvxu1IQ4t0qa9hQ"}
]


def download_url(params):
    try:
        r = requests.get(params['url'], stream=True)
        file_path = "img/{0}.{1}".format(params['configuration_name'], r.headers['Content-Type'].split('/')[-1])
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
            f.close()
        return file_path
    except Exception as e:
        print('Exception in download_url():', e)


def download_parallel(args):
    cpus = cpu_count()
    print("There is {0} are available at your system".format(cpus))
    logging.info("There is {0} are available at your system".format(cpus))
    result = ThreadPool(cpus - 1).imap_unordered(download_url, args)
    start_t = time.time()
    for i in result:
        logging.info('file: {0}, take_time: {1}'.format(i.split('/')[-1], time.time()))
        print('file: {0}, take_time: {1}'.format(i.split('/')[-1], time.time()))
    end_t = time.time()
    logging.info('Take all over time for download are {0}'.format(end_t-start_t))
    print('Take all over time for download are {0}'.format(end_t-start_t))


download_parallel(urls)
# 14.631376028060913
