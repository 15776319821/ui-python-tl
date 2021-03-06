import os
import sys

from elementloc.cuteu.msg.msg_loc import MsgLoc
sys.path.append(os.getcwd())
from base.base_action import BaseAction, logger


class MsgPage(BaseAction):
    '''消息页面一级页面操作'''
    def msg_jump(self):
        self.click_element(MsgLoc.msg_loc,"点击导航栏消息按钮")
    def msg_jump_assert(self):
        return self.is_exist(MsgLoc.interact_news)

    '''点击互动消息按钮'''
    def news_jump(self):
        self.click_element(MsgLoc.interact_news,"点击互动消息按钮")
    def news_jump_assert(self):
        return self.is_exist(MsgLoc.news_clear)
    def newspage_head(self):
        self.click_element(MsgLoc.news_head,"互动通知用户头像")
    def newspage_understand(self):
        self.click_element(MsgLoc.news_understand,"互动通知第一条消息")
    def newspage_understand_assert(self):
        return self.is_exist(MsgLoc.newspage_understand_assert)
    def newspage_clear(self):
        self.click_element(MsgLoc.news_clear,"互动通知清空按钮")
    def newspage_clear_assert(self):
        return self.is_exist(MsgLoc.news_clear_yes)
    def newspage_clear_yes(self):
        self.click_element(MsgLoc.news_clear_yes,"确认清空互动消息")
    def newspage_clear_no(self):
        self.click_element(MsgLoc.news_clear_no, "取消清空互动消息")

    '''点击CuteU团队按钮'''
    def CuteUTeam_jump(self):
        self.click_element(MsgLoc.CuteU_team,"点击CuteU团队按钮")
    def CuteUTeam_jump_assert(self):
        return self.is_exist(MsgLoc.CuteU_team_assert)

    '''点击消息页面第一个用户'''
    def CuteU_user(self):
        self.click_element(MsgLoc.msg_user, "点击消息页面第一个用户")
    def CuteU_user_assert(self):
        return self.is_exist(MsgLoc.user_page)

    '''查看他的资料页'''
    def user_page(self):
        self.click_element(MsgLoc.user_page,"查看他的资料页")
    def user_page_assert(self):
        return self.is_exist(MsgLoc.user_page_assert)

    '''聊天框'''
    def user_msg(self):
        self.click_element(MsgLoc.user_msg,"聊天框")
        self.input_text(MsgLoc.user_msg,"123123","img_doc")
    def user_send(self):
        self.click_element(MsgLoc.user_send, "发送按钮")

    '''麦克风按钮'''
    def user_voice(self):
        self.click_element(MsgLoc.user_voice,"麦克风按钮")
    def user_voice_assert(self):
        return self.is_exist(MsgLoc.voice_send)
    def voice_send(self):
        self.longClick(MsgLoc.voice_send,"点击说话")

    '''图片按钮'''
    def user_img(self):
        self.click_element(MsgLoc.user_img,"图片按钮")
    def user_img_assert(self):
        return self.is_exist(MsgLoc.user_photo)
    def user_img_choose(self):
        self.click_element(MsgLoc.user_photo,"选择图片")
    def user_photo_assert(self):
        return self.is_exist(MsgLoc.user_secret)
    def user_secret(self):
        self.click_element(MsgLoc.user_secret,"小秘密")
    def img_send(self):
        self.click_element(MsgLoc.img_send,"图片发送")

    '''视频聊天'''
    def user_video(self):
        self.click_element(MsgLoc.user_video,"视频聊天")
    def video_cancel(self):
        self.click_element(MsgLoc.video_cancel,"发起视频后挂断")
    def user_video_assert(self):
        return self.is_exist(MsgLoc.video_cancel)

    '''语音聊天'''
    def user_call(self):
        self.click_element(MsgLoc.user_call,"语音聊天")
    def call_cancel(self):
        self.click_element(MsgLoc.call_cancel,"发起语音后挂断")
    def user_call_assert(self):
        return self.is_exist(MsgLoc.call_cancel)

    '''送礼物'''
    def user_gift(self):
        self.click_element(MsgLoc.user_gift,"礼物按钮")
    def gift_choose(self):
        self.click_element(MsgLoc.gift_choose, "选择礼物")
    def gift_send(self):
        self.click_element(MsgLoc.gift_send, "礼物发送")
    def user_gift_assert(self):
        return self.is_exist(MsgLoc.gift_send)

    '''红包'''
    def user_red(self):
        self.click_element(MsgLoc.user_red,"红包按钮")
    def user_red_assert(self):
        return self.is_exist(MsgLoc.red_custom)
    def red_custom(self):
        self.click_element(MsgLoc.red_custom, "定制内容礼物选择")
    def red_input(self):
        self.click_element(MsgLoc.red_input, "视频红包输入内容")
        self.input_text(MsgLoc.user_msg, "123123", "img_doc")
    def red_upload(self):
        self.click_element(MsgLoc.red_upload, "不允许本地上传")
    def red_recharge(self):
        self.click_element(MsgLoc.red_recharge, "充值")
    def red_send(self):
        self.click_element(MsgLoc.red_send, "发送")

    '''更多'''
    def user_more(self):
        self.click_element(MsgLoc.user_more,"更多")
    def user_more_assert(self):
        return self.is_exist(MsgLoc.msg_more_user)
    def msg_more_user(self):
        self.click_element(MsgLoc.msg_more_user,"点击用户")
    def msg_more_block(self):
        self.click_element(MsgLoc.msg_more_block,"屏蔽")
    def msg_more_translate(self):
        self.click_element(MsgLoc.msg_more_translate,"自动翻译")
    def msg_more_follow(self):
        self.click_element(MsgLoc.msg_more_follow,"关注")
    def msg_more_report(self):
        self.click_element(MsgLoc.msg_more_report,"举报")
    def msg_more_report_assert(self):
        return self.is_exist(MsgLoc.report_photo)
    def report_photo(self):
        self.click_element(MsgLoc.report_photo,"上传截图")
    def report_choose(self):
        self.click_element(MsgLoc.report_choose,"选择截图")
    def report_msg(self):
        self.click_element(MsgLoc.report_msg,"举报描述")
    def report_submit(self):
        self.click_element(MsgLoc.report_submit,"提交举报")
    def report_ok(self):
        self.click_element(MsgLoc.report_ok, "提交举报")

    '''帮助中心'''
    def CuteU_help(self):
        self.click_element(MsgLoc.CuteU_help,"点击客服中心按钮")
    def CuteU_help_assert(self):
        return self.is_exist(MsgLoc.help_name)

    '''更多'''
    def CuteU_more(self):
        self.click_element(MsgLoc.CuteU_more,"点击右上角更多按钮")
    def CuteU_more_assert(self):
        return self.is_exist(MsgLoc.more_allread)
    def read_all(self):
        self.click_element(MsgLoc.more_allread,"全部已读按钮")
    def more_clear(self):
        self.click_element(MsgLoc.more_clear,"清理聊天列表")
    def more_clear_assert(self):
        return self.is_exist(MsgLoc.more_cancel)
    def more_cancel(self):
        self.click_element(MsgLoc.more_cancel,"取消按钮")
    def more_save(self):
        self.click_element(MsgLoc.more_save,"确认清空按钮")


    '''非会员或钻石不足场景使用'''
    def close_vip(self):
        self.click_element(MsgLoc.close_vip,"关闭VIP弹窗")
    def close_vip_assert(self):
        return self.is_exist(MsgLoc.close_vip)
    def close_diamond_assert(self):
        return self.is_exist(MsgLoc.close_diamond)
    def gitf_close_diamond_assert(self):
        return self.is_exist(MsgLoc.gift_diamond_close)




