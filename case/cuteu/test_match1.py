# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
sys.path.append(os.getcwd())
from pageproject.cuteu.match_page import MatchPage
from base.base_log import logger
import allure
from case.cuteu.common import Publicservice
# @pytest.fixture(scope='class')
# def init_driver():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.quit()
#@pytest.mark.usefixtures("init_drivera")
class Testmatch:
    def test_msg(self,init_driver):
        #Publicservice().first_install_warrant(init_driver['driver'])
        # Publicservice().mobile_phone(init_driver['driver'])
        #点击消息按钮
        logger.info("执行前")
        MatchPage(init_driver['driver']).match()
        #self.driver.find_element_by_id('com.cuteu.videochat:id/btnTabMessage').click()
        MatchPage(init_driver['driver']).msglist(1)
        logger.info("执行后")
