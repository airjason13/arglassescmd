''' CMD @20250919 '''
CMD_Version_PN = "ARGLASSES_CMD"
CMD_Version_Year = '2025'
CMD_Version_Month = '10'
CMD_Version_Date = '17'
CMD_Version_Major = "02"
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

# SPEC_CMD_DEMO
DEMO_SPEC_NO_SUCH_FILE="demo_spec_no_such_file"

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

''' ============== End of SET CMD ============== '''
