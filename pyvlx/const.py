"""Module for enum and consts."""

from enum import Enum


class Command(Enum):
    """Enum class for GW Command bytes."""

    # pylint: disable=invalid-name

    GW_ERROR_NTF = 0x0000
    GW_REBOOT_REQ = 0x0001
    GW_REBOOT_CFM = 0x0002

    GW_SET_FACTORY_DEFAULT_REQ = 0x0003
    GW_SET_FACTORY_DEFAULT_CFM = 0x0004

    GW_GET_VERSION_REQ = 0x0008
    GW_GET_VERSION_CFM = 0x0009

    GW_GET_PROTOCOL_VERSION_REQ = 0x000A
    GW_GET_PROTOCOL_VERSION_CFM = 0x000B

    GW_GET_STATE_REQ = 0x000C
    GW_GET_STATE_CFM = 0x000D

    GW_LEAVE_LEARN_STATE_REQ = 0x000E
    GW_LEAVE_LEARN_STATE_CFM = 0x000F

    GW_GET_NETWORK_SETUP_REQ = 0x00E0
    GW_GET_NETWORK_SETUP_CFM = 0x00E1
    GW_SET_NETWORK_SETUP_REQ = 0x00E2
    GW_SET_NETWORK_SETUP_CFM = 0x00E3

    GW_CS_GET_SYSTEMTABLE_DATA_REQ = 0x0100
    GW_CS_GET_SYSTEMTABLE_DATA_CFM = 0x0101
    GW_CS_GET_SYSTEMTABLE_DATA_NTF = 0x0102

    GW_CS_DISCOVER_NODES_REQ = 0x0103
    GW_CS_DISCOVER_NODES_CFM = 0x0104
    GW_CS_DISCOVER_NODES_NTF = 0x0105

    GW_CS_REMOVE_NODES_REQ = 0x0106
    GW_CS_REMOVE_NODES_CFM = 0x0107

    GW_CS_VIRGIN_STATE_REQ = 0x0108
    GW_CS_VIRGIN_STATE_CFM = 0x0109

    GW_CS_CONTROLLER_COPY_REQ = 0x010A
    GW_CS_CONTROLLER_COPY_CFM = 0x010B
    GW_CS_CONTROLLER_COPY_NTF = 0x010C
    GW_CS_CONTROLLER_COPY_CANCEL_NTF = 0x010D

    GW_CS_RECEIVE_KEY_REQ = 0x010E
    GW_CS_RECEIVE_KEY_CFM = 0x010F
    GW_CS_RECEIVE_KEY_NTF = 0x0110

    GW_CS_PGC_JOB_NTF = 0x0111
    GW_CS_SYSTEM_TABLE_UPDATE_NTF = 0x0112
    GW_CS_GENERATE_NEW_KEY_REQ = 0x0113
    GW_CS_GENERATE_NEW_KEY_CFM = 0x0114
    GW_CS_GENERATE_NEW_KEY_NTF = 0x0115

    GW_CS_REPAIR_KEY_REQ = 0x0116
    GW_CS_REPAIR_KEY_CFM = 0x0117
    GW_CS_REPAID_KEY_NTF = 0x0118

    GW_CS_ACTIVATE_CONFIGURATION_MODE_REQ = 0x0119
    GW_CS_ACTIVATE_CONFIGURATION_MODE_CFM = 0x011A

    GW_GET_NODE_INFORMATION_REQ = 0x0200
    GW_GET_NODE_INFORMATION_CFM = 0x0201
    GW_GET_NODE_INFORMATION_NTF = 0x0210

    GW_GET_ALL_NODES_INFORMATION_REQ = 0x0202
    GW_GET_ALL_NODES_INFORMATION_CFM = 0x0203
    GW_GET_ALL_NODES_INFORMATION_NTF = 0x0204
    GW_GET_ALL_NODES_INFORMATION_FINISHED_NTF = 0x0205

    GW_SET_NODE_VARIATION_REQ = 0x0206
    GW_SET_NODE_VARIATION_CFM = 0x0207

    GW_SET_NODE_NAME_REQ = 0x0208
    GW_SET_NODE_NAME_CFM = 0x0209

    GW_SET_NODE_VELOCITY_REQ = 0x020A
    GW_SET_NODE_VELOCITY_CFM = 0x020B

    GW_NODE_INFORMATION_CHANGED_NTF = 0x020C

    GW_NODE_STATE_POSITION_CHANGED_NTF = 0x0211

    GW_SET_NODE_ORDER_AND_PLACEMENT_REQ = 0x020D
    GW_SET_NODE_ORDER_AND_PLACEMENT_CFM = 0x020E

    GW_GET_GROUP_INFORMATION_REQ = 0x0220
    GW_GET_GROUP_INFORMATION_CFM = 0x0221
    GW_GET_GROUP_INFORMATION_NTF = 0x0230

    GW_SET_GROUP_INFORMATION_REQ = 0x0222
    GW_SET_GROUP_INFORMATION_CFM = 0x0223

    GW_GROUP_INFORMATION_CHANGED_NTF = 0x0224

    GW_DELETE_GROUP_REQ = 0x0225
    GW_DELETE_GROUP_CFM = 0x0226

    GW_NEW_GROUP_REQ = 0x0227
    GW_NEW_GROUP_CFM = 0x0228

    GW_GET_ALL_GROUPS_INFORMATION_REQ = 0x0229
    GW_GET_ALL_GROUPS_INFORMATION_CFM = 0x022A
    GW_GET_ALL_GROUPS_INFORMATION_NTF = 0x022B

    GW_GET_ALL_GROUPS_INFORMATION_FINISHED_NTF = 0x022C

    GW_GROUP_DELETED_NTF = 0x022D

    GW_HOUSE_STATUS_MONITOR_ENABLE_REQ = 0x0240
    GW_HOUSE_STATUS_MONITOR_ENABLE_CFM = 0x0241

    GW_HOUSE_STATUS_MONITOR_DISABLE_REQ = 0x0242
    GW_HOUSE_STATUS_MONITOR_DISABLE_CFM = 0x0243

    GW_COMMAND_SEND_REQ = 0x0300
    GW_COMMAND_SEND_CFM = 0x0301
    GW_COMMAND_RUN_STATUS_NTF = 0x0302
    GW_COMMAND_REMAINING_TIME_NTF = 0x0303
    GW_SESSION_FINISHED_NTF = 0x0304

    GW_STATUS_REQUEST_REQ = 0x0305
    GW_STATUS_REQUEST_CFM = 0x0306
    GW_STATUS_REQUEST_NTF = 0x0307

    GW_WINK_SEND_REQ = 0x0308
    GW_WINK_SEND_CFM = 0x0309
    GW_WINK_SEND_NTF = 0x030A

    GW_SET_LIMITATION_REQ = 0x0310
    GW_SET_LIMITATION_CFM = 0x0311
    GW_GET_LIMITATION_STATUS_REQ = 0x0312
    GW_GET_LIMITATION_STATUS_CFM = 0x0313
    GW_LIMITATION_STATUS_NTF = 0x0314

    GW_MODE_SEND_REQ = 0x0320
    GW_MODE_SEND_CFM = 0x0321
    GW_MODE_SEND_NTF = 0x0322

    GW_INITIALIZE_SCENE_REQ = 0x0400
    GW_INITIALIZE_SCENE_CFM = 0x0401
    GW_INITIALIZE_SCENE_NTF = 0x0402
    GW_INITIALIZE_SCENE_CANCEL_REQ = 0x0403
    GW_INITIALIZE_SCENE_CANCEL_CFM = 0x0404
    GW_RECORD_SCENE_REQ = 0x0405
    GW_RECORD_SCENE_CFM = 0x0406
    GW_RECORD_SCENE_NTF = 0x0407

    GW_DELETE_SCENE_REQ = 0x0408
    GW_DELETE_SCENE_CFM = 0x0409

    GW_RENAME_SCENE_REQ = 0x040A
    GW_RENAME_SCENE_CFM = 0x040B

    GW_GET_SCENE_LIST_REQ = 0x040C
    GW_GET_SCENE_LIST_CFM = 0x040D
    GW_GET_SCENE_LIST_NTF = 0x040E

    GW_GET_SCENE_INFORMATION_REQ = 0x040F
    GW_GET_SCENE_INFORMATION_CFM = 0x0410
    GW_GET_SCENE_INFORMATION_NTF = 0x0411

    GW_ACTIVATE_SCENE_REQ = 0x0412
    GW_ACTIVATE_SCENE_CFM = 0x0413

    GW_STOP_SCENE_REQ = 0x0415
    GW_STOP_SCENE_CFM = 0x0416

    GW_SCENE_INFORMATION_CHANGED_NTF = 0x0419

    GW_ACTIVATE_PRODUCTGROUP_REQ = 0x0447
    GW_ACTIVATE_PRODUCTGROUP_CFM = 0x0448
    GW_ACTIVATE_PRODUCTGROUP_NTF = 0x0449

    GW_GET_CONTACT_INPUT_LINK_LIST_REQ = 0x0460
    GW_GET_CONTACT_INPUT_LINK_LIST_CFM = 0x0461

    GW_SET_CONTACT_INPUT_LINK_REQ = 0x0462
    GW_SET_CONTACT_INPUT_LINK_CFM = 0x0463

    GW_REMOVE_CONTACT_INPUT_LINK_REQ = 0x0464
    GW_REMOVE_CONTACT_INPUT_LINK_CFM = 0x0465

    GW_GET_ACTIVATION_LOG_HEADER_REQ = 0x0500
    GW_GET_ACTIVATION_LOG_HEADER_CFM = 0x0501

    GW_CLEAR_ACTIVATION_LOG_REQ = 0x0502
    GW_CLEAR_ACTIVATION_LOG_CFM = 0x0503

    GW_GET_ACTIVATION_LOG_LINE_REQ = 0x0504
    GW_GET_ACTIVATION_LOG_LINE_CFM = 0x0505

    GW_ACTIVATION_LOG_UPDATED_NTF = 0x0506

    GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_REQ = 0x0507
    GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_NTF = 0x0508
    GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_CFN = 0x0509

    GW_SET_UTC_REQ = 0x2000
    GW_SET_UTC_CFM = 0x2001

    GW_RTC_SET_TIME_ZONE_REQ = 0x2002
    GW_RTC_SET_TIME_ZONE_CFM = 0x2003

    GW_GET_LOCAL_TIME_REQ = 0x2004
    GW_GET_LOCAL_TIME_CFM = 0x2005

    GW_PASSWORD_ENTER_REQ = 0x3000
    GW_PASSWORD_ENTER_CFM = 0x3001

    GW_PASSWORD_CHANGE_REQ = 0x3002
    GW_PASSWORD_CHANGE_CFM = 0x3003
    GW_PASSWORD_CHANGE_NTF = 0x3004


class Originator(Enum):
    """Enum class for originator."""

    USER = 1
    RAIN = 2
    TIMER = 3
    UPS = 5  # UPC unit
    SAAC = 8  # Stand Alone Automatic Controls
    WIND = 9
    LOAD_SHEDDING = 11
    LOCAL_LIGHT = 12
    UNSPECIFIC_ENVIRONMENT_SENSOR = 13
    EMERGENCY = 255


class Priority(Enum):
    """Enum class for priority."""

    PROTECTION_HUMAN = 0
    PROTECTION_ENVIRONMENT = 1
    USER_LEVEL_1 = 2
    USER_LEVEL_2 = 3
    COMFORT_LEVEL_1 = 4
    COMFORT_LEVEL_2 = 5
    COMFORT_LEVEL_3 = 6
    COMFORT_LEVEL_4 = 7

class DiscoverStatus(Enum):
    """Enum class for DiscoverStatus."""

    OK = 0
    FAILED_CS_NOT_READY = 5
    OK_NOT_ADDED = 6
    CS_BUSY = 7

class Velocity(Enum):
    """Enum class for velocity."""

    DEFAULT = 0
    SILENT = 1
    FAST = 2
    NOT_AVAILABLE = 255


class NodeTypeWithSubtype(Enum):
    """Enum class for node type plus sub type combined values."""

    # pylint: disable=invalid-name
    NO_TYPE = 0
    INTERIOR_VENETIAN_BLIND = 0x0040
    ROLLER_SHUTTER = 0x0080
    ADJUSTABLE_SLUTS_ROLLING_SHUTTER = 0x0081
    ADJUSTABLE_SLUTS_ROLLING_SHUTTER_WITH_PROJECTION = 0x0082
    VERTICAL_EXTERIOR_AWNING = 0x00C0
    WINDOW_OPENER = 0x0100
    WINDOW_OPENER_WITH_RAIN_SENSOR = 0x0101
    GARAGE_DOOR_OPENER = 0x0140
    LINAR_ANGULAR_POSITION_OF_GARAGE_DOOR = 0x017A
    LIGHT = 0x0180
    LIGHT_ON_OFF = 0x01BA
    GATE_OPENER = 0x01C0
    GATE_OPENER_ANGULAR_POSITION = 0x01FA
    DOOR_LOCK = 0x0240
    WINDOW_LOCK = 0x0241
    VERTICAL_INTERIOR_BLINDS = 0x0280
    DUAL_ROLLER_SHUTTER = 0x0340
    ON_OFF_SWITCH = 0x03C0
    HORIZONTAL_AWNING = 0x0400
    EXTERIOR_VENETIAN_BLIND = 0x0440
    LOUVER_BLIND = 0x0480
    CURTAIN_TRACK = 0x04C0
    VENTILATION_POINT = 0x0500
    VENTILATION_POINT_AIR_INLET = 0x0502
    VENTILATION_POINT_AIR_TRANSFER = 0x0503
    VENTILATION_POINT_AIR_OUTLET = 0x0503
    EXTERIOR_HEATING = 0x0540
    SWINGING_SHUTTERS = 0x0600
    SWINGING_SHUTTER_WITH_INDEPENDENT_LEAVES = 0x0601
    BLADE_OPENER = 0x0740


class NodeType(Enum):
    """Enum class for node types."""

    NO_TYPE = 0
    VENETIAN_BLIND = 1
    ROLLER_SHUTTER = 2
    AWNING = 3
    WINDOW_OPENER = 4
    GARAGE_OPENER = 5
    LIGHT = 6
    GATE_OPENER = 7
    ROLLING_DOOR_OPENER = 8
    LOCK = 9
    BLIND = 10
    SECURE_CONFIGURATION_DEVICE = 11
    BEACON = 12
    DUAL_SHUTTER = 13
    HEATING_TEMPERATURE_INTERFACE = 14
    ON_OFF_SWITCH = 15
    HORIZONTAL_AWNING = 16
    EXTERNAL_VENETIAN_BLIND = 17
    LOUVRE_BLINT = 18
    CURTAIN_TRACK = 19
    VENTILATION_POINT = 20
    EXTERIOR_HEATING = 21
    HEAT_PUMP = 22
    INTRUSION_ALARM = 23
    SWINGING_SHUTTER = 24


class NodeVariation(Enum):
    """Enum class for node variations."""

    NOT_SET = 0
    TOPHUNG = 1
    KIP = 2
    FLAT_ROOT = 3
    SKY_LIGHT = 3

class NodePowerMode(Enum):
    """Enum Class for Node Power Mode"""

    ALWAYS_ALIVE = 0
    LOW_POWER_MODE = 1

class NodeRfSupport(Enum):
    """Enum Class for Node RF Support"""

    NO_RF_SUPPORT = 0
    RF_SUPPORT = 1

class ActuatorTurnaroundTime(Enum):
    """Enum Class for Actuator Turnaround Time"""

    MS_05 = 0
    MS_10 = 1
    MS_20 = 2
    MS_40 = 3

class IoManufacturerId(Enum):
    """Enum Class for Manufacturer IDs"""

    UNDEFINED = 0
    VELUX = 1
    SOMFY = 2
    HONEYWELL = 3
    HOERMANN = 4
    ASSA_ABLOY = 5
    NIKO = 6
    WINDOW_MASTER = 7
    RENSON = 8
    CIAT = 9
    SECUYOU = 10
    OVERKIZ = 11
    ATLANTIC_GROUP = 12
    MF_RESERVED_13 = 13
    MF_RESERVED_14 = 14
    MF_RESERVED_15 = 15
    MF_RESERVED_16 = 16
    MF_RESERVED_17 = 17
    MF_RESERVED_18 = 18
    MF_RESERVED_19 = 19
    MF_RESERVED_20 = 20
    MF_RESERVED_21 = 21
    MF_RESERVED_22 = 22
    MF_RESERVED_23 = 23
    MF_RESERVED_24 = 24
    MF_RESERVED_25 = 25
    MF_RESERVED_26 = 26
    MF_RESERVED_27 = 27
    MF_RESERVED_28 = 28
    MF_RESERVED_29 = 29
    MF_RESERVED_30 = 30
    MF_RESERVED_31 = 31
    MF_RESERVED_32 = 32
    MF_RESERVED_33 = 33
    MF_RESERVED_34 = 34
    MF_RESERVED_35 = 35
    MF_RESERVED_36 = 36
    MF_RESERVED_37 = 37
    MF_RESERVED_38 = 38
    MF_RESERVED_39 = 39
    MF_RESERVED_40 = 40
    MF_RESERVED_41 = 41
    MF_RESERVED_42 = 42
    MF_RESERVED_43 = 43
    MF_RESERVED_44 = 44
    MF_RESERVED_45 = 45
    MF_RESERVED_46 = 46
    MF_RESERVED_47 = 47
    MF_RESERVED_48 = 48
    MF_RESERVED_49 = 49
    MF_RESERVED_50 = 50
    MF_RESERVED_51 = 51
    MF_RESERVED_52 = 52
    MF_RESERVED_53 = 53
    MF_RESERVED_54 = 54
    MF_RESERVED_55 = 55
    MF_RESERVED_56 = 56
    MF_RESERVED_57 = 57
    MF_RESERVED_58 = 58
    MF_RESERVED_59 = 59
    MF_RESERVED_60 = 60
    MF_RESERVED_61 = 61
    MF_RESERVED_62 = 62
    MF_RESERVED_63 = 63
    MF_RESERVED_64 = 64
    MF_RESERVED_65 = 65
    MF_RESERVED_66 = 66
    MF_RESERVED_67 = 67
    MF_RESERVED_68 = 68
    MF_RESERVED_69 = 69
    MF_RESERVED_70 = 70
    MF_RESERVED_71 = 71
    MF_RESERVED_72 = 72
    MF_RESERVED_73 = 73
    MF_RESERVED_74 = 74
    MF_RESERVED_75 = 75
    MF_RESERVED_76 = 76
    MF_RESERVED_77 = 77
    MF_RESERVED_78 = 78
    MF_RESERVED_79 = 79
    MF_RESERVED_80 = 80
    MF_RESERVED_81 = 81
    MF_RESERVED_82 = 82
    MF_RESERVED_83 = 83
    MF_RESERVED_84 = 84
    MF_RESERVED_85 = 85
    MF_RESERVED_86 = 86
    MF_RESERVED_87 = 87
    MF_RESERVED_88 = 88
    MF_RESERVED_89 = 89
    MF_RESERVED_90 = 90
    MF_RESERVED_91 = 91
    MF_RESERVED_92 = 92
    MF_RESERVED_93 = 93
    MF_RESERVED_94 = 94
    MF_RESERVED_95 = 95
    MF_RESERVED_96 = 96
    MF_RESERVED_97 = 97
    MF_RESERVED_98 = 98
    MF_RESERVED_99 = 99
    MF_RESERVED_100 = 100
    MF_RESERVED_101 = 101
    MF_RESERVED_102 = 102
    MF_RESERVED_103 = 103
    MF_RESERVED_104 = 104
    MF_RESERVED_105 = 105
    MF_RESERVED_106 = 106
    MF_RESERVED_107 = 107
    MF_RESERVED_108 = 108
    MF_RESERVED_109 = 109
    MF_RESERVED_110 = 110
    MF_RESERVED_111 = 111
    MF_RESERVED_112 = 112
    MF_RESERVED_113 = 113
    MF_RESERVED_114 = 114
    MF_RESERVED_115 = 115
    MF_RESERVED_116 = 116
    MF_RESERVED_117 = 117
    MF_RESERVED_118 = 118
    MF_RESERVED_119 = 119
    MF_RESERVED_120 = 120
    MF_RESERVED_121 = 121
    MF_RESERVED_122 = 122
    MF_RESERVED_123 = 123
    MF_RESERVED_124 = 124
    MF_RESERVED_125 = 125
    MF_RESERVED_126 = 126
    MF_RESERVED_127 = 127
    MF_RESERVED_128 = 128
    MF_RESERVED_129 = 129
    MF_RESERVED_130 = 130
    MF_RESERVED_131 = 131
    MF_RESERVED_132 = 132
    MF_RESERVED_133 = 133
    MF_RESERVED_134 = 134
    MF_RESERVED_135 = 135
    MF_RESERVED_136 = 136
    MF_RESERVED_137 = 137
    MF_RESERVED_138 = 138
    MF_RESERVED_139 = 139
    MF_RESERVED_140 = 140
    MF_RESERVED_141 = 141
    MF_RESERVED_142 = 142
    MF_RESERVED_143 = 143
    MF_RESERVED_144 = 144
    MF_RESERVED_145 = 145
    MF_RESERVED_146 = 146
    MF_RESERVED_147 = 147
    MF_RESERVED_148 = 148
    MF_RESERVED_149 = 149
    MF_RESERVED_150 = 150
    MF_RESERVED_151 = 151
    MF_RESERVED_152 = 152
    MF_RESERVED_153 = 153
    MF_RESERVED_154 = 154
    MF_RESERVED_155 = 155
    MF_RESERVED_156 = 156
    MF_RESERVED_157 = 157
    MF_RESERVED_158 = 158
    MF_RESERVED_159 = 159
    MF_RESERVED_160 = 160
    MF_RESERVED_161 = 161
    MF_RESERVED_162 = 162
    MF_RESERVED_163 = 163
    MF_RESERVED_164 = 164
    MF_RESERVED_165 = 165
    MF_RESERVED_166 = 166
    MF_RESERVED_167 = 167
    MF_RESERVED_168 = 168
    MF_RESERVED_169 = 169
    MF_RESERVED_170 = 170
    MF_RESERVED_171 = 171
    MF_RESERVED_172 = 172
    MF_RESERVED_173 = 173
    MF_RESERVED_174 = 174
    MF_RESERVED_175 = 175
    MF_RESERVED_176 = 176
    MF_RESERVED_177 = 177
    MF_RESERVED_178 = 178
    MF_RESERVED_179 = 179
    MF_RESERVED_180 = 180
    MF_RESERVED_181 = 181
    MF_RESERVED_182 = 182
    MF_RESERVED_183 = 183
    MF_RESERVED_184 = 184
    MF_RESERVED_185 = 185
    MF_RESERVED_186 = 186
    MF_RESERVED_187 = 187
    MF_RESERVED_188 = 188
    MF_RESERVED_189 = 189
    MF_RESERVED_190 = 190
    MF_RESERVED_191 = 191
    MF_RESERVED_192 = 192
    MF_RESERVED_193 = 193
    MF_RESERVED_194 = 194
    MF_RESERVED_195 = 195
    MF_RESERVED_196 = 196
    MF_RESERVED_197 = 197
    MF_RESERVED_198 = 198
    MF_RESERVED_199 = 199
    MF_RESERVED_200 = 200
    MF_RESERVED_201 = 201
    MF_RESERVED_202 = 202
    MF_RESERVED_203 = 203
    MF_RESERVED_204 = 204
    MF_RESERVED_205 = 205
    MF_RESERVED_206 = 206
    MF_RESERVED_207 = 207
    MF_RESERVED_208 = 208
    MF_RESERVED_209 = 209
    MF_RESERVED_210 = 210
    MF_RESERVED_211 = 211
    MF_RESERVED_212 = 212
    MF_RESERVED_213 = 213
    MF_RESERVED_214 = 214
    MF_RESERVED_215 = 215
    MF_RESERVED_216 = 216
    MF_RESERVED_217 = 217
    MF_RESERVED_218 = 218
    MF_RESERVED_219 = 219
    MF_RESERVED_220 = 220
    MF_RESERVED_221 = 221
    MF_RESERVED_222 = 222
    MF_RESERVED_223 = 223
    MF_RESERVED_224 = 224
    MF_RESERVED_225 = 225
    MF_RESERVED_226 = 226
    MF_RESERVED_227 = 227
    MF_RESERVED_228 = 228
    MF_RESERVED_229 = 229
    MF_RESERVED_230 = 230
    MF_RESERVED_231 = 231
    MF_RESERVED_232 = 232
    MF_RESERVED_233 = 233
    MF_RESERVED_234 = 234
    MF_RESERVED_235 = 235
    MF_RESERVED_236 = 236
    MF_RESERVED_237 = 237
    MF_RESERVED_238 = 238
    MF_RESERVED_239 = 239
    MF_RESERVED_240 = 240
    MF_RESERVED_241 = 241
    MF_RESERVED_242 = 242
    MF_RESERVED_243 = 243
    MF_RESERVED_244 = 244
    MF_RESERVED_245 = 245
    MF_RESERVED_246 = 246
    MF_RESERVED_247 = 247
    MF_RESERVED_248 = 248
    MF_RESERVED_249 = 249
    MF_RESERVED_250 = 250
    MF_RESERVED_251 = 251
    MF_RESERVED_252 = 252
    MF_RESERVED_253 = 253
    MF_RESERVED_254 = 254
    MF_RESERVED_255 = 255
    