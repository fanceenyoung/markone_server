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

# 发送code的邮件头和内容
EMAIL_CODE_SUBJECT = 'code info from Markone'
EMAIL_CODE_CONTENT = 'code of this request is:'


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
