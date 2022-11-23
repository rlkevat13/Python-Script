import logging
import requests


urls = [
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_6gMPaVgIPuuJ7qC",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_5hyec3pXLIMxBf7",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_2b2UA3ggSdftrDL",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_b9GfpSj4xPudvtI",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_9Xo5dJaXdU2WSWi",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_5aQcJ4rlRluRGZL",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_86BIujc2Hkmaphz",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_eVXrsKFXP5kqWcl",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_dd7u6hBKavGMHHv",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_6hB84EwaqsqIvOK",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_1zaIsJa6TBL3nzU",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_a2TofcG6zUZvYqO",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3ZQdwEEfqArdDM2",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_1N3v4SLW9NGA6Gy",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_dmuXMoHZizovN8G",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_0OOewry6tLvxeLj",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_37uUgizhes5Obvo",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_2rbN16GpCKVcBNj",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3KRhnYss3apj9mm",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3J0yMhvH8CTh3ym",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_3dzE2lorQr9qEey",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_bKM7q0JVlexrhHw",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_2aWYzT9kKyAzKsu",
    "https://intuify.co1.qualtrics.com/ControlPanel/Graphic.php?IM=IM_cvxu1IQ4t0qa9hQ"
]

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()

for i in urls:
    r = s.get(i)
    print(r.status_code, s.headers)
s.close()
