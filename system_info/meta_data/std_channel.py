# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from system_info.models import StdChName, AliasChName
from django.core.exceptions import ObjectDoesNotExist
import logging
import traceback

logger = logging.getLogger(__name__)


class StdChannel(object):

    def __init__(self, std_csv, alias_csv):
        self._std_csv = std_csv
        self._alias_csv = alias_csv

        self._std_dict = dict()
        self._alias_dict = dict()

    def load_std_ch(self):
        with open(self._std_csv) as f:
            for i, line in enumerate(f, 0):
                if 0 == i:
                    continue
                line_info = line.strip().split(',')
                std_id = line_info[0]
                std_name = line_info[1]

                std_ch_name = StdChName(
                    ch_id=std_id,
                    name=std_name,
                )
                std_ch_name.save()

    def load_alias_ch(self):
        with open(self._alias_csv) as f:
            for i, line in enumerate(f, 0):
                if 0 == i:
                    continue

                line_info = line.strip().split(',')
                alias = line_info[1]
                std_id = line_info[2]

                try:
                    std_ch_obj = StdChName.objects.get(ch_id=std_id)
                except ObjectDoesNotExist:
                    logger.warning("load_alias_ch std no exist %s:%s", std_id, alias)
                    continue
                except:
                    logger.error("load_alias_ch unknown error %s:%s error(%s)", std_id, alias, traceback.format_exc())
                    continue

                try:
                    AliasChName.objects.get(name=alias)
                    continue
                except ObjectDoesNotExist:
                    alias_ch_obj = AliasChName(
                        std_ch=std_ch_obj,
                        name=alias
                    )
                    alias_ch_obj.save()
                except:
                    logger.error("load_alias_ch save alias unknown error %s:%s error(%s)",
                                 std_id, alias, traceback.format_exc())

    def save(self):
        self.load_std_ch()
        self.load_alias_ch()

