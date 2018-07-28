# -*- coding: utf-8 -*-

US_VISITOR = 'VISITOR'
US_ADMIN = 'BUSINESS'
US_SUPERUSER = 'SUPERUSER'
US_OTHER = 'OTHER'

USER_TYPES = (
    (US_VISITOR, 'Visitor'),
    (US_ADMIN, 'Admin'),
    (US_SUPERUSER, 'Superuser'),
    (US_OTHER, 'Other'),
)

# avatars
USER_AVATARS = [
    'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/avatar_01.png',
    'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/avatar_02.png',
    'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/avatar_03.png',
    'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/avatar_04.png',
    'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/avatar_05.png',
    'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/avatar_06.png',
]

# 发送code的邮件头和内容
EMAIL_CODE_SUBJECT = 'Code info from Markone'
EMAIL_CODE_CONTENT = 'Code of this request is:'

# 发送重置密码邮件头和内容
EMAIL_PASSWORD_SUBJECT = 'Reset your password request'
EMAIL_PASSWORD_CONTENT = 'Your new password is:'


# 账号中心-questions
QUESTIONS = [
    {
        'title': 'Install the plugin',
        'answer': 'Install on chrome extensions center chrome://extensions/ or install it by local download',
    },
    {
        'title': 'Format my notes',
        'answer': 'Add note by first, and then edit it.',
    },
    {
        'title': 'Share my notes with my friends',
        'answer': 'Follow your friends, and you will see their notes.',
    },
    {
        'title': 'Mark my favorite',
        'answer': 'Just click the favorite button.',
    },
]

# 账户中心-feedback
FEEDBACK_IMAGE = 'http://www.baidu.com'
FEEDBACK_CONTACT = [
    {
        'title': 'email',
        'url': 'mailto:Markonenote@163.com',
        'info': 'mail',
    },
    {
        'title': 'QQ',
        'url': 'qq',
        'info': '123456',
    },
    {
        'title': 'Wechat',
        'url': 'Wechat',
        'info': 'Wechat',
    },
    {
        'title': 'Facebook',
        'url': 'Facebook',
        'info': 'Facebook',
    },
    {
        'title': 'Twitter',
        'url': 'Twitter',
        'info': 'Twitter',
    },
]

# 账户中心-about us
ABOUT_US_DESC = 'Hello, there! We are a group of students from School of Design, PolyU, ' \
                'medium celebrates diversity in people, backgrounds, and life experiences. ' \
                'For instance, our founder co-created two of the most transformative tools ' \
                'for sharing ideas online, Blogger and Twitter.'

ABOUT_US_MEBS = [
    {
        'name': 'Fancy',
        'title': 'Project Manager',
        'image': 'http://www.baidu.com'
    },
    {
        'name': 'Sharnk',
        'title': 'Project Designer',
        'image': 'http://www.baidu.com'
    },
    {
        'name': 'Joy',
        'title': 'Operation',
        'image': 'http://www.baidu.com'
    },
    {
        'name': 'Wendy',
        'title': 'UI Designer',
        'image': 'http://www.baidu.com'
    },
    {
        'name': 'Phil',
        'title': 'Marketing',
        'image': 'http://www.baidu.com'
    }
]

# 默认notes
DEFAULT_NOTES_TITLE = 'Markone user guide'
DEFAULT_SITE = 'http://www.markonenote.com/'

# 默认sections

SECTION_ONE = 'Welcome to Mark One! We are building this tool to help you record information more efficiently while watching online videos. With Mark One, you can record subtitles, capture screenshots and input your insights without leaving the web page. And all of these will automatically appear here, in the notes page.'
SECTION_TWO = '歡迎來到馬一記！我們想通過這個工具來幫助您提升在觀看在線視頻時的效率。在馬一記Chrome擴展程序中，您可以記錄字幕、截圖、輸入筆記，而所有的這些內容，均可通過點擊頭像進入筆記頁面查看和導出。'
SECTION_THERE = 'https://audionetwork.oss-cn-beijing.aliyuncs.com/markone/section_deault3.png'
SECTION_FOUR = 'If you haven’t installed our Chrome extension, please click here, or search for “Mark One” in the Chrome Web Store. If you have any problems or suggestions when using our extension, please contact us through markone_support@163.com, Facebook or Twitter @Mark One馬一記.'
SECTION_FIVE = '如果您還沒有安裝拓展程序，請點擊這裡，或者在Chrome應用商店搜索“Mark One”。如果中國大陸的用戶在安装中遇到问题，請在幫助中心查看如何科學安裝，也歡迎微博微信搜索“Mark One馬一記”關注我們，了解科學學習方法，獲取更多新奇學習資料。'
SECTION_SIX = 'Let us begin your new learning journey!'

DEFAULT_SECTION_LIST = [SECTION_ONE, SECTION_TWO, SECTION_THERE, SECTION_FOUR, SECTION_FIVE, SECTION_SIX]

