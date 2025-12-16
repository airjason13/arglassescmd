''' CMD @20250919 '''
CMD_Version_PN = "ARGLASSES_CMD"
CMD_Version_Year = '2025'
CMD_Version_Month = '12'
CMD_Version_Date = '03'
CMD_Version_Major = "01"
CMD_Version_Minor = "00"
CMD_Version_Patch = "00"

CMD_Version = CMD_Version_PN + "_" + \
          CMD_Version_Year + \
          CMD_Version_Month + \
          CMD_Version_Date + "_" + \
          CMD_Version_Major + \
          CMD_Version_Minor + \
          CMD_Version_Patch


''' ============== Start of SPEC CMD ============== '''

# SPEC_CMD
MSG_SPEC_HELLO="msg_spec_hello"
# SPEC_CMD_SYS_Reboot
SYS_SPEC_GOING_TO_REBOOT="msg_spec_going_to_reboot"

# SPEC_CMD_LE
LE_SPEC_TEMP_PROTECTION="le_spec_temp_protection"
LE_SPEC_NOTIFY_ERROR="le_spec_notify_error"

# SPEC_CMD_DEMO
DEMO_SPEC_MEDIAENGINE_CMD_ERROR_REPORT="demo_spec_mediaengine_cmd_error_report"
DEMO_SPEC_MEDIAENGINE_STATUS_REPORT="demo_spec_mediaengine_status_report"

''' ============== End of SPEC CMD ============== '''

''' ============== Start of GET CMD ============== '''

# GET_CMD_VERSION
MSG_GET_SW_VERSION="msg_get_sw_version"
LE_GET_SW_VERSION="le_get_sw_version"
DEMO_GET_SW_VERSION="demo_get_sw_version"
SYS_GET_SW_VERSION="sys_get_sw_version"

# GET_CMD_DEMO_File_List
DEMO_GET_MEDIAFILE_FILE_LIST="demo_get_mediafile_file_list"
DEMO_GET_SNAPSHOTS_FILE_LIST= "demo_get_snapshots_file_list"
DEMO_GET_RECORDINGS_FILE_LIST="demo_get_recordings_file_list"
DEMO_GET_MEDIA_FILE_LIST="demo_get_media_file_list"
DEMO_GET_THUMBNAILS_FILE_LIST="demo_get_thumbnails_file_list"

# GET_CMD_DEMO_MEDIAENGINE_STATUS
DEMO_GET_MEDIAENGINE_STATUS="demo_get_mediaengine_status"
DEMO_GET_MEDIAENGINE_STILL_IMAGE_PERIOD="demo_get_mediaengine_still_image_period"
DEMO_GET_MEDIAENGINE_FILE_URI="demo_get_mediaengine_file_uri"


# GET_CMD_SYS_Wifi
SYS_GET_WIFI_UAP0_SSID="sys_get_wifi_uap0_ssid"
SYS_GET_WIFI_UAP0_PWD="sys_get_wifi_uap0_pwd"
SYS_GET_WIFI_UAP0_SSID_PWD="sys_get_wifi_uap0_ssid_pwd"
SYS_GET_WIFI_UAP0_HW_MODE="sys_get_wifi_uap0_hw_mode"

# GET_CMD_LE
LE_GET_BRIGHTNESS="le_get_brightness"
LE_GET_CURRENT="le_get_current"
LE_GET_TEMPERATURE="le_get_temperature"
LE_GET_MIRROR="le_get_mirror"
LE_GET_FLIP="le_get_flip"
LE_GET_OFFSET="le_get_offset"

# GET_CMD_PLAYLIST
DEMO_GET_PLAYLIST_GET_ALL          = "demo_get_playlist_get_all"            # 取得所有播放清單
DEMO_GET_PLAYLIST_GET_LIST         = "demo_get_playlist_get_list"           # 查詢當前清單內容
DEMO_GET_PLAYLIST_GET_CURRENT_FILE = "demo_get_playlist_get_current_file"   # 查詢當前播放

# GET_CMD_SPEAKER
CMD_GET_MEDIA_VOLUME  = "demo_get_media_volume" #取得多媒體音量

''' ============== End of GET CMD ================ '''

''' ============== Start of SET CMD ============== '''

# SET_CMD
DEMO_SET_PLAY_MEDIA="demo_set_play_media"
SYS_SET_WIFI_SSID="sys_set_wifi_ssid"

# SET_CMD_DEMO_MEDIAENGINE
DEMO_SET_MEDIAENGINE_STILL_IMAGE_PERIOD="demo_set_mediaengine_still_image_period"
DEMO_SET_MEDIAENGINE_PLAY_SINGLE_FILE="demo_set_mediaengine_play_single_file"
DEMO_SET_MEDIAENGINE_PAUSE="demo_set_mediaengine_pause"
DEMO_SET_MEDIAENGINE_STOP="demo_set_mediaengine_stop"
DEMO_SET_MEDIAENGINE_RESUME_PLAYING="demo_set_mediaengine_resume_playing"
DEMO_SET_MEDIAENGINE_RENDER_SUBTITLE="demo_set_mediaengine_render_subtitle"
DEMO_SET_MEDIAENGINE_SUBTITLE_COLOR="demo_set_mediaengine_subtitle_color"
DEMO_SET_MEDIAENGINE_SUBTITLE_REPEAT="demo_set_mediaengine_subtitle_repeat"
DEMO_SET_MEDIAENGINE_SUBTITLE_COLOR_LINES="demo_set_mediaengine_subtitle_color_lines"

# SET_CMD_LE
LE_SET_BRIGHTNESS="le_set_brightness"
LE_SET_CURRENT="le_set_current"
LE_SET_MIRROR="le_set_mirror"
LE_SET_FLIP="le_set_flip"
LE_SET_OFFSET="le_set_offset"

# SET_CMD TEST
DEMO_SET_TEST="demo_set_test"
SYS_SET_TEST="sys_set_test"
LE_SET_TEST="le_set_test"

# SET_CMD_SYS_Wifi
SYS_SET_WIFI_UAP0_SSID="sys_set_wifi_uap0_ssid"
SYS_SET_WIFI_UAP0_PWD="sys_set_wifi_uap0_pwd"
SYS_SET_WIFI_UAP0_SSID_PWD="sys_set_wifi_uap0_ssid_pwd"
SYS_SET_WIFI_UAP0_HW_MODE="sys_set_wifi_uap0_hw_mode"
SYS_SET_WIFI_UAP0_RESTART="sys_set_wifi_uap0_restart"

# SET_CMD_PLAYLIST
DEMO_SET_PLAYLIST_CREATE                  = "demo_set_playlist_create"                 # 建立播放清單
DEMO_SET_PLAYLIST_SELECT                  = "demo_set_playlist_select"                 # 選擇播放清單
DEMO_SET_PLAYLIST_ADD_ITEM                = "demo_set_playlist_add_item"               # 加入影片
DEMO_SET_PLAYLIST_REMOVE_ITEM             = "demo_set_playlist_remove_item"            # 移除影片
DEMO_SET_PLAYLIST_PLAY                    = "demo_set_playlist_play"                   # 播放目前清單
DEMO_SET_PLAYLIST_STOP                    = "demo_set_playlist_stop"                   # 停止播放
DEMO_SET_PLAYLIST_REMOVE_PLAYLIST         = "demo_set_playlist_remove_playlist"        # 移除播放清單
DEMO_SET_PLAYLIST_NEXT_ITEM               = "demo_set_playlist_next_item"              # 切換下一部
DEMO_SET_PLAYLIST_PREV_ITEM               = "demo_set_playlist_prev_item"              # 切換上一部
DEMO_SET_PLAYLIST_BATCH_ADD               = "demo_set_playlist_batch_add"              # 批次加入影片
DEMO_SET_PLAYLIST_BATCH_REMOVE_BY_NAME    = "demo_set_playlist_batch_remove_by_name"   # 批次移除影片(路徑名稱)
DEMO_SET_PLAYLIST_BATCH_REMOVE_BY_INDEX   = "demo_set_playlist_batch_remove_by_index"   # 批次移除影片(內容索引)
DEMO_GET_PLAYLIST_EXPAND_ALL              = "demo_get_playlist_expand_all"             # 展開全部清單內容

# SET_CMD_SPEAKER
CMD_SET_MEDIA_VOLUME  = "demo_set_media_volume" # 寫入多媒體音量
''' ============== End of SET CMD ============== '''
