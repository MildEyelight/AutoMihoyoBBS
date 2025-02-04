# 米游社的Salt
mihoyobbs_salt = "TsmyHpZg8gFAVKTtlPaL6YwMldzxZJxQ"
mihoyobbs_salt_x4 = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"
mihoyobbs_salt_x6 = "t0qEgfub6cvueAPgR5m9aQWWVciEer7v"
mihoyobbs_salt_web = "osgT0DljLarYxgebPPHJFjdaxPfoiHGt"
# 米游社的版本
mihoyobbs_version = "2.41.2"  # Salt和Version相互对应
# 米游社的客户端类型
mihoyobbs_Client_type = "2"  # 1为ios 2为安卓
mihoyobbs_Client_type_web = "5"  # 4为pc web 5为mobile web
# 云原神版本
cloudgenshin_Version = "3.0.0"

# 米游社的分区列表
mihoyobbs_List = [{
    "id": "1",
    "forumId": "1",
    "name": "崩坏3",
    "url": "https://bbs.mihoyo.com/bh3/"
}, {
    "id": "2",
    "forumId": "26",
    "name": "原神",
    "url": "https://bbs.mihoyo.com/ys/"
}, {
    "id": "3",
    "forumId": "30",
    "name": "崩坏2",
    "url": "https://bbs.mihoyo.com/bh2/"
}, {
    "id": "4",
    "forumId": "37",
    "name": "未定事件簿",
    "url": "https://bbs.mihoyo.com/wd/"
}, {
    "id": "5",
    "forumId": "34",
    "name": "大别野",
    "url": "https://bbs.mihoyo.com/dby/"
}, {
    "id": "6",
    "forumId": "52",
    "name": "崩坏：星穹铁道",
    "url": "https://bbs.mihoyo.com/sr/"
}, {
    "id": "8",
    "forumId": "57",
    "name": "绝区零",
    "url": "https://bbs.mihoyo.com/zzz/"
}]

game_id2name = {
    "bh2_cn": "崩坏2",
    "bh3_cn": "崩坏3",
    "nxx_cn": "未定事件簿",
    "hk4e_cn": "原神",
    "hkrpg_cn": "崩铁",
}

game_id2config = {
    "bh2_cn": "hokai2",
    "bh3_cn": "honkai3rd",
    "nxx_cn": "tears_of_themis",
    "hk4e_cn": "genshin",
    "hkrpg_cn": "honkaiStarRail",
}

# Config Load之后run里面进行列表的选择
mihoyobbs_List_Use = []

# 游戏签到的请求头
headers = {
    'Accept': 'application/json, text/plain, */*',
    'DS': "",
    "x-rpc-channel": "miyousheluodi",
    'Origin': 'https://webstatic.mihoyo.com',
    'x-rpc-app_version': mihoyobbs_version,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) '
                  f'Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 miHoYoBBS/{mihoyobbs_version}',
    'x-rpc-client_type': mihoyobbs_Client_type_web,
    'Referer': '',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'X-Requested-With': 'com.mihoyo.hyperion',
    "Cookie": "",
    'x-rpc-device_id': ""
}

# 通用设置
bbs_api = "https://bbs-api.mihoyo.com"
web_api = "https://api-takumi.mihoyo.com"
account_Info_url = web_api + "/binding/api/getUserGameRolesByCookie?game_biz="

# 米游社的API列表
bbs_cookie_url = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
bbs_cookie_url2 = web_api + "/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
bbs_tasks_list = bbs_api + "/apihub/sapi/getUserMissionsState"  # 获取任务列表
bbs_sign_url = bbs_api + "/apihub/app/api/signIn"  # post
bbs_post_list_url = bbs_api + "/post/api/getForumPostList?forum_id={}&is_good=false&is_hot=false&page_size=20&sort_type=1"
bbs_detail_url = bbs_api + "/post/api/getPostFull?post_id={}"
bbs_share_url = bbs_api + "/apihub/api/getShareConf?entity_id={}&entity_type=1"
bbs_like_url = bbs_api + "/apihub/sapi/upvotePost"  # post json
bbs_get_captcha = bbs_api + "/misc/api/createVerification?is_high=true"
bbs_captcha_verify = bbs_api + "/misc/api/verifyVerification"

# 崩坏2自动签到相关的相关设置
honkai2_Act_id = "e202203291431091"
honkai2_checkin_rewards = f'{web_api}/event/luna/home?lang=zh-cn&act_id={honkai2_Act_id}'
honkai2_Is_signurl = web_api + "/event/luna/info?lang=zh-cn&act_id={}&region={}&uid={}"
honkai2_Sign_url = web_api + "/event/luna/sign"

# 崩坏3自动签到相关的设置
honkai3rd_Act_id = "e202207181446311"
honkai3rd_checkin_rewards = f'{web_api}/event/luna/home?lang=zh-cn&act_id={honkai3rd_Act_id}'
honkai3rd_Is_signurl = web_api + "/event/luna/info?lang=zh-cn&act_id={}&region={}&uid={}"
honkai3rd_Sign_url = web_api + "/event/luna/sign"

# 未定事件簿自动签到相关设置
tearsofthemis_Act_id = "e202202251749321"
tearsofthemis_checkin_rewards = f'{web_api}/event/luna/home?lang=zh-cn&act_id={tearsofthemis_Act_id}'
tearsofthemis_Is_signurl = honkai2_Is_signurl
tearsofthemis_Sign_url = honkai2_Sign_url  # 和二崩完全一致

# 原神自动签到相关的设置
genshin_Act_id = "e202009291139501"
genshin_checkin_rewards = f'{web_api}/event/bbs_sign_reward/home?act_id={genshin_Act_id}'
genshin_Is_signurl = web_api + "/event/bbs_sign_reward/info?act_id={}&region={}&uid={}"
genshin_Signurl = web_api + "/event/bbs_sign_reward/sign"

#崩铁的相关设置
honkaiStarRail_Act_id = "e202304121516551"
honkaiStarRail_checkin_rewards = f'{web_api}/event/luna/home?lang=zh-cn&act_id={honkaiStarRail_Act_id}'
honkaiStarRail_Is_signurl = web_api + "/event/luna/info?lang=zh-cn&act_id={}&region={}&uid={}"
honkaiStarRail_Signurl = web_api + "/event/luna/sign"
#还有一个/event/signin/hkrpg 不知道是干什么的

# 云原神相关api
cloud_genshin_Api = "https://api-cloudgame.mihoyo.com"
cloud_genshin_sgin = cloud_genshin_Api + "/hk4e_cg_cn/wallet/wallet/get"
