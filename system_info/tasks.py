# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import os
import logging
import traceback
from celery import shared_task
from system_info.meta_data.std_channel import StdChannel


logger = logging.getLogger(__name__)


@shared_task
def load_channel_name(std_csv, alias_csv, enable=False):
    logger.info("load channel name enable %s", enable)
    if not enable:
        logging.debug("no need flush std channel")
        return

    if not os.path.exists(std_csv) or not os.path.isfile(std_csv):
        logger.error("not found std csv file %s", std_csv)
        return

    if not os.path.exists(alias_csv) or not os.path.isfile(alias_csv):
        logger.error("not found alias csv file %s", alias_csv)
        return

    try:
        std_channel = StdChannel(std_csv=std_csv, alias_csv=alias_csv)
        std_channel.save()
    except:
        logger.error("load_channel_name exception %s", traceback.format_exc())

