# -*- coding: utf-8 -*-
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %Y- %m- %d %H: %M :%S',
    filename= 'test.log',
    filemode= 'w'
)