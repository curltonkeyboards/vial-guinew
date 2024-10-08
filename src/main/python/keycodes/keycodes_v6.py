class keycodes_v6:
    kc = {
        "QK_LAYER_TAP": 0x4000,
        "MOD_LCTL": 0x01,
        "MOD_LSFT": 0x02,
        "MOD_LALT": 0x04,
        "MOD_LGUI": 0x08,
        "MOD_RCTL": 0x11,
        "MOD_RSFT": 0x12,
        "MOD_RALT": 0x14,
        "MOD_RGUI": 0x18,
        "MOD_HYPR": 0xF,
        "MOD_MEH": 0x7,
        "QK_TO": 0x5200,
        "QK_MOMENTARY": 0x5220,
        "QK_DEF_LAYER": 0x5240,
        "QK_TOGGLE_LAYER": 0x5260,
        "QK_ONE_SHOT_LAYER": 0x5280,
        "QK_ONE_SHOT_MOD": 0x52A0,
        "QK_TAP_DANCE": 0x5700,
        "QK_LAYER_TAP_TOGGLE": 0x52C0,
        "QK_LAYER_MOD": 0x5000,
        "QK_MOD_TAP": 0x2000,
        "ON_PRESS": 1,
        "QK_LCTL": 0x0100,
        "QK_LSFT": 0x0200,
        "QK_LALT": 0x0400,
        "QK_LGUI": 0x0800,
        "QK_RCTL": 0x1100,
        "QK_RSFT": 0x1200,
        "QK_RALT": 0x1400,
        "QK_RGUI": 0x1800,
        "QK_MACRO": 0x7700,

        "ALL_T(kc)": 0x2f00,
        "C_S_T(kc)": 0x2300,
        "C_S(kc)": 0x300,
        "HYPR(kc)": 0xf00,
        "LALT_T(kc)": 0x2400,
        "LALT(kc)": 0x400,
        "LCA_T(kc)": 0x2500,
        "LCA(kc)": 0x500,
        "LCAG_T(kc)": 0x2d00,
        "LCAG(kc)": 0xd00,
        "LCG_T(kc)": 0x2900,
        "LCG(kc)": 0x900,
        "LCTL_T(kc)": 0x2100,
        "LCTL(kc)": 0x100,
        "LGUI_T(kc)": 0x2800,
        "LGUI(kc)": 0x800,
        "LSA_T(kc)": 0x2600,
        "LSA(kc)": 0x600,
        "LSFT_T(kc)": 0x2200,
        "LSFT(kc)": 0x200,
        "MEH_T(kc)": 0x2700,
        "MEH(kc)": 0x700,
        "RALT_T(kc)": 0x3400,
        "RALT(kc)": 0x1400,
        "RCAG_T(kc)": 0x3d00,
        "RCG_T(kc)": 0x3900,
        "RCG(kc)": 0x1900,
        "RCTL_T(kc)": 0x3100,
        "RCTL(kc)": 0x1100,
        "RGUI_T(kc)": 0x3800,
        "RGUI(kc)": 0x1800,
        "RSFT_T(kc)": 0x3200,
        "RSFT(kc)": 0x1200,
        "SGUI_T(kc)": 0x2a00,
        "SGUI(kc)": 0xa00,

        "OSM(MOD_LSFT)": 0x52A2,
        "OSM(MOD_LCTL)": 0x52A1,
        "OSM(MOD_LALT)": 0x52A4,
        "OSM(MOD_LGUI)": 0x52A8,
        "OSM(MOD_RSFT)": 0x52B2,
        "OSM(MOD_RCTL)": 0x52B1,
        "OSM(MOD_RALT)": 0x52B4,
        "OSM(MOD_RGUI)": 0x52B8,
        "OSM(MOD_LCTL|MOD_LSFT)": 0x52A3,
        "OSM(MOD_LCTL|MOD_LALT)": 0x52A5,
        "OSM(MOD_LCTL|MOD_LGUI)": 0x52A9,
        "OSM(MOD_LSFT|MOD_LALT)": 0x52A6,
        "OSM(MOD_LSFT|MOD_LGUI)": 0x52AA,
        "OSM(MOD_LALT|MOD_LGUI)": 0x52AC,
        "OSM(MOD_LCTL|MOD_LSFT|MOD_LGUI)": 0x52AB,
        "OSM(MOD_LCTL|MOD_LALT|MOD_LGUI)": 0x52AD,
        "OSM(MOD_LSFT|MOD_LALT|MOD_LGUI)": 0x52AE,
        "OSM(MOD_MEH)": 0x52A7,
        "OSM(MOD_HYPR)": 0x52AF,
        "OSM(MOD_RCTL|MOD_RSFT)": 0x52B3,
        "OSM(MOD_RCTL|MOD_RALT)": 0x52B5,
        "OSM(MOD_RCTL|MOD_RGUI)": 0x52B9,
        "OSM(MOD_RSFT|MOD_RALT)": 0x52B6,
        "OSM(MOD_RSFT|MOD_RGUI)": 0x52BA,
        "OSM(MOD_RALT|MOD_RGUI)": 0x52BC,
        "OSM(MOD_RCTL|MOD_RSFT|MOD_RGUI)": 0x52BB,
        "OSM(MOD_RCTL|MOD_RALT|MOD_RGUI)": 0x52BD,
        "OSM(MOD_RSFT|MOD_RALT|MOD_RGUI)": 0x52BE,
        "OSM(MOD_RCTL|MOD_RSFT|MOD_RALT)": 0x52B7,
        "OSM(MOD_RCTL|MOD_RSFT|MOD_RALT|MOD_RGUI)": 0x52BF,

        "KC_NO": 0x00,
        "KC_TRNS": 0x01,
        "KC_NUMLOCK": 0x53,
        "KC_KP_SLASH": 0x54,
        "KC_KP_ASTERISK": 0x55,
        "KC_KP_MINUS": 0x56,
        "KC_KP_PLUS": 0x57,
        "KC_KP_ENTER": 0x58,
        "KC_KP_1": 0x59,
        "KC_KP_2": 0x5A,
        "KC_KP_3": 0x5B,
        "KC_KP_4": 0x5C,
        "KC_KP_5": 0x5D,
        "KC_KP_6": 0x5E,
        "KC_KP_7": 0x5F,
        "KC_KP_8": 0x60,
        "KC_KP_9": 0x61,
        "KC_KP_0": 0x62,
        "KC_KP_DOT": 0x63,
        "KC_KP_EQUAL": 0x67,
        "KC_KP_COMMA": 0x85,
        "KC_PSCREEN": 0x46,
        "KC_SCROLLLOCK": 0x47,
        "KC_PAUSE": 0x48,
        "KC_INSERT": 0x49,
        "KC_HOME": 0x4A,
        "KC_PGUP": 0x4B,
        "KC_DELETE": 0x4C,
        "KC_END": 0x4D,
        "KC_PGDOWN": 0x4E,
        "KC_RIGHT": 0x4F,
        "KC_LEFT": 0x50,
        "KC_DOWN": 0x51,
        "KC_UP": 0x52,
        "KC_A": 0x04,
        "KC_B": 0x05,
        "KC_C": 0x06,
        "KC_D": 0x07,
        "KC_E": 0x08,
        "KC_F": 0x09,
        "KC_G": 0x0A,
        "KC_H": 0x0B,
        "KC_I": 0x0C,
        "KC_J": 0x0D,
        "KC_K": 0x0E,
        "KC_L": 0x0F,
        "KC_M": 0x10,
        "KC_N": 0x11,
        "KC_O": 0x12,
        "KC_P": 0x13,
        "KC_Q": 0x14,
        "KC_R": 0x15,
        "KC_S": 0x16,
        "KC_T": 0x17,
        "KC_U": 0x18,
        "KC_V": 0x19,
        "KC_W": 0x1A,
        "KC_X": 0x1B,
        "KC_Y": 0x1C,
        "KC_Z": 0x1D,
        "KC_1": 0x1E,
        "KC_2": 0x1F,
        "KC_3": 0x20,
        "KC_4": 0x21,
        "KC_5": 0x22,
        "KC_6": 0x23,
        "KC_7": 0x24,
        "KC_8": 0x25,
        "KC_9": 0x26,
        "KC_0": 0x27,
        "KC_ENTER": 0x28,
        "KC_ESCAPE": 0x29,
        "KC_BSPACE": 0x2A,
        "KC_TAB": 0x2B,
        "KC_SPACE": 0x2C,
        "KC_MINUS": 0x2D,
        "KC_EQUAL": 0x2E,
        "KC_LBRACKET": 0x2F,
        "KC_RBRACKET": 0x30,
        "KC_BSLASH": 0x31,
        "KC_SCOLON": 0x33,
        "KC_QUOTE": 0x34,
        "KC_GRAVE": 0x35,
        "KC_COMMA": 0x36,
        "KC_DOT": 0x37,
        "KC_SLASH": 0x38,
        "KC_CAPSLOCK": 0x39,
        "KC_F1": 0x3A,
        "KC_F2": 0x3B,
        "KC_F3": 0x3C,
        "KC_F4": 0x3D,
        "KC_F5": 0x3E,
        "KC_F6": 0x3F,
        "KC_F7": 0x40,
        "KC_F8": 0x41,
        "KC_F9": 0x42,
        "KC_F10": 0x43,
        "KC_F11": 0x44,
        "KC_F12": 0x45,
        "KC_APPLICATION": 0x65,
        "KC_LCTRL": 0xE0,
        "KC_LSHIFT": 0xE1,
        "KC_LALT": 0xE2,
        "KC_LGUI": 0xE3,
        "KC_RCTRL": 0xE4,
        "KC_RSHIFT": 0xE5,
        "KC_RALT": 0xE6,
        "KC_RGUI": 0xE7,
        "KC_TILD": 0x235,
        "KC_EXLM": 0x21E,
        "KC_AT": 0x21F,
        "KC_HASH": 0x220,
        "KC_DLR": 0x221,
        "KC_PERC": 0x222,
        "KC_CIRC": 0x223,
        "KC_AMPR": 0x224,
        "KC_ASTR": 0x225,
        "KC_LPRN": 0x226,
        "KC_RPRN": 0x227,
        "KC_UNDS": 0x22D,
        "KC_PLUS": 0x22E,
        "KC_LCBR": 0x22F,
        "KC_RCBR": 0x230,
        "KC_LT": 0x236,
        "KC_GT": 0x237,
        "KC_COLN": 0x233,
        "KC_PIPE": 0x231,
        "KC_QUES": 0x238,
        "KC_DQUO": 0x234,
        "KC_NONUS_HASH": 0x32,
        "KC_NONUS_BSLASH": 0x64,
        "KC_RO": 0x87,
        "KC_KANA": 0x88,
        "KC_JYEN": 0x89,
        "KC_HENK": 0x8A,
        "KC_MHEN": 0x8B,
        "KC_LANG1": 0x90,
        "KC_LANG2": 0x91,
        "KC_GESC": 0x7C16,
        "KC_LSPO": 0x7C1A,
        "KC_RSPC": 0x7C1B,
        "KC_LCPO": 0x7C18,
        "KC_RCPC": 0x7C19,
        "KC_LAPO": 0x7C1C,
        "KC_RAPC": 0x7C1D,
        "KC_SFTENT": 0x7C1E,
        "MAGIC_SWAP_CONTROL_CAPSLOCK": 0x7000,
        "MAGIC_UNSWAP_CONTROL_CAPSLOCK": 0x7001,
        "MAGIC_CAPSLOCK_TO_CONTROL": 0x7004,
        "MAGIC_UNCAPSLOCK_TO_CONTROL": 0x7003,
        "MAGIC_SWAP_LCTL_LGUI": 0x7017,
        "MAGIC_UNSWAP_LCTL_LGUI": 0x7018,
        "MAGIC_SWAP_RCTL_RGUI": 0x7019,
        "MAGIC_UNSWAP_RCTL_RGUI": 0x701A,
        "MAGIC_SWAP_CTL_GUI": 0x701B,
        "MAGIC_UNSWAP_CTL_GUI": 0x701C,
        "MAGIC_TOGGLE_CTL_GUI": 0x701D,
        "MAGIC_SWAP_LALT_LGUI": 0x7005,
        "MAGIC_UNSWAP_LALT_LGUI": 0x7006,
        "MAGIC_SWAP_RALT_RGUI": 0x7007,
        "MAGIC_UNSWAP_RALT_RGUI": 0x7008,
        "MAGIC_SWAP_ALT_GUI": 0x7014,
        "MAGIC_UNSWAP_ALT_GUI": 0x7015,
        "MAGIC_TOGGLE_ALT_GUI": 0x7016,
        "MAGIC_NO_GUI": 0x700A,
        "MAGIC_UNNO_GUI": 0x7009,
        "MAGIC_SWAP_GRAVE_ESC": 0x700C,
        "MAGIC_UNSWAP_GRAVE_ESC": 0x700D,
        "MAGIC_SWAP_BACKSLASH_BACKSPACE": 0x700E,
        "MAGIC_UNSWAP_BACKSLASH_BACKSPACE": 0x700F,
        "MAGIC_HOST_NKRO": 0x7011,
        "MAGIC_UNHOST_NKRO": 0x7012,
        "MAGIC_TOGGLE_NKRO": 0x7013,
        "MAGIC_EE_HANDS_LEFT": 0x701E,
        "MAGIC_EE_HANDS_RIGHT": 0x701F,
        "AU_ON": 0x7480,
        "AU_OFF": 0x7481,
        "AU_TOG": 0x7482,
        "CLICKY_TOGGLE": 0x748A,
        "CLICKY_UP": 0x748D,
        "CLICKY_DOWN": 0x748E,
        "CLICKY_RESET": 0x748F,
        "MU_ON": 0x7490,
        "MU_OFF": 0x7491,
        "MU_TOG": 0x7492,
        "MU_MOD": 0x7493,
        "HPT_ON": 0x7C40,
        "HPT_OFF": 0x7C41,
        "HPT_TOG": 0x7C42,
        "HPT_RST": 0x7C43,
        "HPT_FBK": 0x7C44,
        "HPT_BUZ": 0x7C45,
        "HPT_MODI": 0x7C46,
        "HPT_MODD": 0x7C47,
        "HPT_CONT": 0x7C48,
        "HPT_CONI": 0x7C49,
        "HPT_COND": 0x7C4A,
        "HPT_DWLI": 0x7C4B,
        "HPT_DWLD": 0x7C4C,
        "KC_ASDN": 0x7C10,
        "KC_ASUP": 0x7C11,
        "KC_ASRP": 0x7C12,
        "KC_ASON": 0x7C13,
        "KC_ASOFF": 0x7C14,
        "KC_ASTG": 0x7C15,
        "CMB_ON": 0x7C50,
        "CMB_OFF": 0x7C51,
        "CMB_TOG": 0x7C52,
        "BL_TOGG": 0x7802,
        "BL_STEP": 0x7805,
        "BL_BRTG": 0x7806,
        "BL_ON": 0x7800,
        "BL_OFF": 0x7801,
        "BL_INC": 0x7804,
        "BL_DEC": 0x7803,
        "RGB_TOG": 0x7820,
        "RGB_MOD": 0x7821,
        "RGB_RMOD": 0x7822,
        "RGB_HUI": 0x7823,
        "RGB_HUD": 0x7824,
        "RGB_SAI": 0x7825,
        "RGB_SAD": 0x7826,
        "RGB_VAI": 0x7827,
        "RGB_VAD": 0x7828,
        "RGB_SPI": 0x7829,
        "RGB_SPD": 0x782A,
        "RGB_M_P": 0x782B,
        "RGB_M_B": 0x782C,
        "RGB_M_R": 0x782D,
        "RGB_M_SW": 0x782E,
        "RGB_M_SN": 0x782F,
        "RGB_M_K": 0x7830,
        "RGB_M_X": 0x7831,
        "RGB_M_G": 0x7832,
        "RGB_M_T": 0x7833,
        "KC_F13": 104,
        "KC_F14": 105,
        "KC_F15": 106,
        "KC_F16": 107,
        "KC_F17": 108,
        "KC_F18": 109,
        "KC_F19": 110,
        "KC_F20": 111,
        "KC_F21": 112,
        "KC_F22": 113,
        "KC_F23": 114,
        "KC_F24": 115,
        "KC_PWR": 165,
        "KC_SLEP": 166,
        "KC_WAKE": 167,
        "KC_EXEC": 116,
        "KC_HELP": 117,
        "KC_SLCT": 119,
        "KC_STOP": 120,
        "KC_AGIN": 121,
        "KC_UNDO": 122,
        "KC_CUT": 123,
        "KC_COPY": 124,
        "KC_PSTE": 125,
        "KC_FIND": 126,
        "KC_CALC": 178,
        "KC_MAIL": 177,
        "KC_MSEL": 175,
        "KC_MYCM": 179,
        "KC_WSCH": 180,
        "KC_WHOM": 181,
        "KC_WBAK": 182,
        "KC_WFWD": 183,
        "KC_WSTP": 184,
        "KC_WREF": 185,
        "KC_WFAV": 186,
        "KC_BRIU": 189,
        "KC_BRID": 190,
        "KC_MPRV": 172,
        "KC_MNXT": 171,
        "KC_MUTE": 168,
        "KC_VOLD": 170,
        "KC_VOLU": 169,
        "KC__VOLDOWN": 129,
        "KC__VOLUP": 128,
        "KC_MSTP": 173,
        "KC_MPLY": 174,
        "KC_MRWD": 188,
        "KC_MFFD": 187,
        "KC_EJCT": 176,
        "KC_MS_U": 0xCD,
        "KC_MS_D": 0xCE,
        "KC_MS_L": 0xCF,
        "KC_MS_R": 0xD0,
        "KC_BTN1": 0xD1,
        "KC_BTN2": 0xD2,
        "KC_BTN3": 0xD3,
        "KC_BTN4": 0xD4,
        "KC_BTN5": 0xD5,
        "KC_WH_U": 0xD9,
        "KC_WH_D": 0xDA,
        "KC_WH_L": 0xDB,
        "KC_WH_R": 0xDC,
        "KC_ACL0": 0xDD,
        "KC_ACL1": 0xDE,
        "KC_ACL2": 0xDF,
        "KC_LCAP": 130,
        "KC_LNUM": 131,
        "KC_LSCR": 132,
        "DYN_REC_START1": 0x7C53,
        "DYN_REC_START2": 0x7C54,
        "DYN_REC_STOP": 0x7C55,
        "DYN_MACRO_PLAY1": 0x7C56,
        "DYN_MACRO_PLAY2": 0x7C57,
        "MI_C": 0x7103,
        "MI_Cs": 0x7104,
        "MI_D": 0x7105,
        "MI_Ds": 0x7106,
        "MI_E": 0x7107,
        "MI_F": 0x7108,
        "MI_Fs": 0x7109,
        "MI_G": 0x710A,
        "MI_Gs": 0x710B,
        "MI_A": 0x710C,
        "MI_As": 0x710D,
        "MI_B": 0x710E,
        "MI_C_1": 0x710F,
        "MI_Cs_1": 0x7110,
        "MI_D_1": 0x7111,
        "MI_Ds_1": 0x7112,
        "MI_E_1": 0x7113,
        "MI_F_1": 0x7114,
        "MI_Fs_1": 0x7115,
        "MI_G_1": 0x7116,
        "MI_Gs_1": 0x7117,
        "MI_A_1": 0x7118,
        "MI_As_1": 0x7119,
        "MI_B_1": 0x711A,
        "MI_C_2": 0x711B,
        "MI_Cs_2": 0x711C,
        "MI_D_2": 0x711D,
        "MI_Ds_2": 0x711E,
        "MI_E_2": 0x711F,
        "MI_F_2": 0x7120,
        "MI_Fs_2": 0x7121,
        "MI_G_2": 0x7122,
        "MI_Gs_2": 0x7123,
        "MI_A_2": 0x7124,
        "MI_As_2": 0x7125,
        "MI_B_2": 0x7126,
        "MI_C_3": 0x7127,
        "MI_Cs_3": 0x7128,
        "MI_D_3": 0x7129,
        "MI_Ds_3": 0x712A,
        "MI_E_3": 0x712B,
        "MI_F_3": 0x712C,
        "MI_Fs_3": 0x712D,
        "MI_G_3": 0x712E,
        "MI_Gs_3": 0x712F,
        "MI_A_3": 0x7130,
        "MI_As_3": 0x7131,
        "MI_B_3": 0x7132,
        "MI_C_4": 0x7133,
        "MI_Cs_4": 0x7134,
        "MI_D_4": 0x7135,
        "MI_Ds_4": 0x7136,
        "MI_E_4": 0x7137,
        "MI_F_4": 0x7138,
        "MI_Fs_4": 0x7139,
        "MI_G_4": 0x713A,
        "MI_Gs_4": 0x713B,
        "MI_A_4": 0x713C,
        "MI_As_4": 0x713D,
        "MI_B_4": 0x713E,
        "MI_C_5": 0x713F,
        "MI_Cs_5": 0x7140,
        "MI_D_5": 0x7141,
        "MI_Ds_5": 0x7142,
        "MI_E_5": 0x7143,
        "MI_F_5": 0x7144,
        "MI_Fs_5": 0x7145,
        "MI_G_5": 0x7146,
        "MI_Gs_5": 0x7147,
        "MI_A_5": 0x7148,
        "MI_As_5": 0x7149,
        "MI_B_5": 0x714A,
        "MI_ALLOFF": 0x7185,
        "MI_OCT_N2": 0x714B,
        "MI_OCT_N1": 0x714C,
        "MI_OCT_0": 0x714D,
        "MI_OCT_1": 0x714E,
        "MI_OCT_2": 0x714F,
        "MI_OCT_3": 0x7150,
        "MI_OCT_4": 0x7151,
        "MI_OCT_5": 0x7152,
        "MI_OCT_6": 0x7153,
        "MI_OCT_7": 0x7154,
        "MI_OCTD": 0x7155,
        "MI_OCTU": 0x7156,
        "MI_TRNS_N6": 0x7157,
        "MI_TRNS_N5": 0x7158,
        "MI_TRNS_N4": 0x7159,
        "MI_TRNS_N3": 0x715A,
        "MI_TRNS_N2": 0x715B,
        "MI_TRNS_N1": 0x715C,
        "MI_TRNS_0": 0x715D,
        "MI_TRNS_1": 0x715E,
        "MI_TRNS_2": 0x715F,
        "MI_TRNS_3": 0x7160,
        "MI_TRNS_4": 0x7161,
        "MI_TRNS_5": 0x7162,
        "MI_TRNS_6": 0x7163,
        "MI_TRNSD": 0x7164,
        "MI_TRNSU": 0x7165,
        "MI_VEL_1": 0x7167,
        "MI_VEL_2": 0x7168,
        "MI_VEL_3": 0x7169,
        "MI_VEL_4": 0x716A,
        "MI_VEL_5": 0x716B,
        "MI_VEL_6": 0x716C,
        "MI_VEL_7": 0x716D,
        "MI_VEL_8": 0x716E,
        "MI_VEL_9": 0x716F,
        "MI_VEL_10": 0x7170,
        "MI_VELD": 0x7171,
        "MI_VELU": 0x7172,
        "MI_CH1": 0x7173,
        "MI_CH2": 0x7174,
        "MI_CH3": 0x7175,
        "MI_CH4": 0x7176,
        "MI_CH5": 0x7177,
        "MI_CH6": 0x7178,
        "MI_CH7": 0x7179,
        "MI_CH8": 0x717A,
        "MI_CH9": 0x717B,
        "MI_CH10": 0x717C,
        "MI_CH11": 0x717D,
        "MI_CH12": 0x717E,
        "MI_CH13": 0x717F,
        "MI_CH14": 0x7180,
        "MI_CH15": 0x7181,
        "MI_CH16": 0x7182,
        "MI_CHD": 0x7183,
        "MI_CHU": 0x7184,
        "MI_SUS": 0x7186,
        "MI_PORT": 0x7187,
        "MI_SOST": 0x7188,
        "MI_SOFT": 0x7189,
        "MI_LEG": 0x718A,
        "MI_MOD": 0x718B,
        "MI_MODSD": 0x718C,
        "MI_MODSU": 0x718D,
        "MI_BENDD": 0x718E,
        "MI_BENDU": 0x718F,
        



        "RESET": 0x7C00,

        "FN_MO13": 0x7C77,
        "FN_MO23": 0x7C78,

        # "QK_KB": 0x7E00,
        "MI_CC_0_TOG": 0x8000,  # start value for new keycodes
        "MI_CC_0_UP": 0x8000 + 128,
        "MI_CC_0_DWN": 0x8000 + 128 * 2,
        "MI_CC_0_0": 0x8000 + 128 * 3,  # 128*128 keycodes for fixed CC values
        "MI_BANK_MSB_0": (0x8000 + 128 * 3) + 128 * 128,
        "MI_BANK_LSB_0": (0x8000 + 128 * 4) + 128 * 128,
        "MI_PROG_0": (0x8000 + 128 * 5) + 128 * 128,
        "MI_BANK_UP": (0x8000 + 128 * 6) + 128 * 128 + 1,
        "MI_BANK_DWN": (0x8000 + 128 * 6) + 128 * 128 + 2,
        "MI_PROG_UP": (0x8000 + 128 * 6) + 128 * 128 + 3,
        "MI_PROG_DWN": (0x8000 + 128 * 6) + 128 * 128 + 4,

        "MI_VELOCITY_0": (0x8000 + 128 * 6) + 128 * 128 + 5,
        
        
        "CC_STEPSIZE_1": (0x8000 + 128 * 7) + 128 * 128 + 5,
        "CC_STEPSIZE_2": (0x8000 + 128 * 7) + 128 * 128 + 6,
        "CC_STEPSIZE_3": (0x8000 + 128 * 7) + 128 * 128 + 7,
        "CC_STEPSIZE_4": (0x8000 + 128 * 7) + 128 * 128 + 8,
        "CC_STEPSIZE_5": (0x8000 + 128 * 7) + 128 * 128 + 9,
        "CC_STEPSIZE_6": (0x8000 + 128 * 7) + 128 * 128 + 10,
        "CC_STEPSIZE_7": (0x8000 + 128 * 7) + 128 * 128 + 11,
        "CC_STEPSIZE_8": (0x8000 + 128 * 7) + 128 * 128 + 12,
        "CC_STEPSIZE_9": (0x8000 + 128 * 7) + 128 * 128 + 13,
        "CC_STEPSIZE_10": (0x8000 + 128 * 7) + 128 * 128 + 14,
        "CC_STEPSIZE_11": (0x8000 + 128 * 7) + 128 * 128 + 15,
        "CC_STEPSIZE_12": (0x8000 + 128 * 7) + 128 * 128 + 16,
        "CC_STEPSIZE_13": (0x8000 + 128 * 7) + 128 * 128 + 17,
        "CC_STEPSIZE_14": (0x8000 + 128 * 7) + 128 * 128 + 18,
        "CC_STEPSIZE_15": (0x8000 + 128 * 7) + 128 * 128 + 19,
        "CC_STEPSIZE_16": (0x8000 + 128 * 7) + 128 * 128 + 20,
        
        
                # midi chords "MI_CHORD_1": (0x8000 + 128 * 7) + 128 * 128 + 5 + 17,
        "MI_CHORD_0": 0xC396,
        "MI_CHORD_1": 0xC397,
        "MI_CHORD_2": 0xC398,
        "MI_CHORD_128": 0xC399,
        "MI_CHORD_3": 0xC39A,
        "MI_CHORD_4": 0xC39B,
        "MI_CHORD_5": 0xC39C,
        "MI_CHORD_6": 0xC39D,
        "MI_CHORD_7": 0xC39E,
        "MI_CHORD_8": 0xC39F,
        "MI_CHORD_9": 0xC3A0,
        "MI_CHORD_10": 0xC3A1,
        "MI_CHORD_11": 0xC3A2,
        "MI_CHORD_12": 0xC3A3,
        "MI_CHORD_13": 0xC3A4,
        "MI_CHORD_14": 0xC3A5,
        "MI_CHORD_15": 0xC3A6,
        "MI_CHORD_16": 0xC3A7,
        "MI_CHORD_17": 0xC3A8,
        "MI_CHORD_18": 0xC3A9,
        "MI_CHORD_19": 0xC3AA,
        "MI_CHORD_20": 0xC3AB,
        "MI_CHORD_21": 0xC3AC,
        "MI_CHORD_22": 0xC3AD,
        "MI_CHORD_23": 0xC3AE,
        "MI_CHORD_24": 0xC3AF,
        "MI_CHORD_25": 0xC3B0,
        "MI_CHORD_26": 0xC3B1,
        "MI_CHORD_27": 0xC3B2,
        "MI_CHORD_28": 0xC3B3,
        "MI_CHORD_29": 0xC3B4,
        "MI_CHORD_30": 0xC3B5,
        "MI_CHORD_31": 0xC3B6,
        "MI_CHORD_32": 0xC3B7,
        "MI_CHORD_33": 0xC3B8,
        "MI_CHORD_34": 0xC3B9,
        "MI_CHORD_35": 0xC3BA,
        "MI_CHORD_36": 0xC3BB,
        "MI_CHORD_37": 0xC3BC,
        "MI_CHORD_38": 0xC3BD,
        "MI_CHORD_39": 0xC3BE,
        "MI_CHORD_40": 0xC3BF,
        "MI_CHORD_41": 0xC3C0,
        "MI_CHORD_42": 0xC3C1,
        "MI_CHORD_43": 0xC3C2,
        "MI_CHORD_44": 0xC3C3,
        "MI_CHORD_45": 0xC3C4,
        "MI_CHORD_46": 0xC3C5,
        "MI_CHORD_47": 0xC3C6,
        "MI_CHORD_48": 0xC3C7,
        "MI_CHORD_49": 0xC3C8,
        "MI_CHORD_50": 0xC3C9,
        "MI_CHORD_51": 0xC3CA,
        "MI_CHORD_52": 0xC3CB,
        "MI_CHORD_53": 0xC3CC,
        "MI_CHORD_54": 0xC3CD,
        "MI_CHORD_55": 0xC3CE,
        "MI_CHORD_56": 0xC3CF,
        "MI_CHORD_57": 0xC3D0,
        "MI_CHORD_58": 0xC3D1,
        "MI_CHORD_59": 0xC3D2,
        "MI_CHORD_60": 0xC3D3,
        "MI_CHORD_61": 0xC3D4,
        "MI_CHORD_62": 0xC3D5,
        "MI_CHORD_63": 0xC3D6,
        "MI_CHORD_64": 0xC3D7,
        "MI_CHORD_65": 0xC3D8,
        "MI_CHORD_66": 0xC3D9,
        "MI_CHORD_67": 0xC3DA,
        "MI_CHORD_68": 0xC3DB,
        "MI_CHORD_69": 0xC3DC,
        "MI_CHORD_70": 0xC3DD,
        "MI_CHORD_71": 0xC3DE,
        "MI_CHORD_72": 0xC3DF,
        "MI_CHORD_73": 0xC3E0,
        "MI_CHORD_74": 0xC3E1,
        "MI_CHORD_75": 0xC3E2,
        "MI_CHORD_76": 0xC3E3,
        "MI_CHORD_77": 0xC3E4,
        "MI_CHORD_78": 0xC3E5,
        "MI_CHORD_79": 0xC3E6,
        "MI_CHORD_80": 0xC3E7,
        "MI_CHORD_81": 0xC3E8,
        "MI_CHORD_82": 0xC3E9,
        "MI_CHORD_83": 0xC3EA,
        "MI_CHORD_84": 0xC3EB,
        "MI_CHORD_85": 0xC3EC,
        "MI_CHORD_86": 0xC3ED,
        "MI_CHORD_87": 0xC3EE,
        "MI_CHORD_88": 0xC3EF,
        "MI_CHORD_89": 0xC3F0,
        "MI_CHORD_90": 0xC3F1,
        "MI_CHORD_91": 0xC3F2,
        "MI_CHORD_92": 0xC3F3,
        "MI_CHORD_93": 0xC3F4,
        "MI_CHORD_94": 0xC3F5,
        "MI_CHORD_95": 0xC3F6,
        "MI_CHORD_96": 0xC3F7,
        "MI_CHORD_97": 0xC3F8,
        "MI_CHORD_98": 0xC3F9,
        "MI_CHORD_99": 0xC3FA,
        "MI_CHORD_100": 0xC3FB,
        "MI_CHORD_101": 0xC3FC,
        "MI_CHORD_102": 0xC3FD,
        "MI_CHORD_103": 0xC3FE,
        "MI_CHORD_104": 0xC3FF,
        "MI_CHORD_105": 0xC400,
        "MI_CHORD_106": 0xC401,
        "MI_CHORD_107": 0xC402,
        "MI_CHORD_108": 0xC403,
        "MI_CHORD_109": 0xC404,
        "MI_CHORD_110": 0xC405,
        "MI_CHORD_111": 0xC406,
        "MI_CHORD_112": 0xC407,
        "MI_CHORD_113": 0xC408,
        "MI_CHORD_114": 0xC409,
        "MI_CHORD_115": 0xC40A,
        "MI_CHORD_116": 0xC40B,
        "MI_CHORD_117": 0xC40C,
        "MI_CHORD_118": 0xC40D,
        "MI_CHORD_119": 0xC40E,
        "MI_CHORD_120": 0xC40F,
        "MI_CHORD_121": 0xC410,
        "MI_CHORD_122": 0xC411,
        "MI_CHORD_123": 0xC412,
        "MI_CHORD_124": 0xC413,
        "MI_CHORD_125": 0xC414,
        "MI_CHORD_126": 0xC415,
        "MI_CHORD_127": 0xC416,
        
        #midi inversion (0x8000 + 128 * 7) + 128 * 128 + 5 + 25 + 130,         
        "MI_INVERSION_DEF" : 0xC420,
        "MI_INVERSION_1" : 0xC421,
        "MI_INVERSION_2" : 0xC422,
        "MI_INVERSION_3" : 0xC423,
        "MI_INVERSION_4" : 0xC424,
        "MI_INVERSION_5" : 0xC425,
        "MI_INVERSION_6" : 0xC426,
        "MI_INVERSION_7" : 0xC427,
        "MI_INVERSION_8" : 0xC428,
        
        "MI_SMARTCHORD_PRESS" : 0xC429,
        "MI_SMARTCHORD_UP" : 0xC42A,
        "MI_SMARTCHORD_DOWN" : 0xC42B,
        
        "MI_VELOCITY_STEPSIZE_1": 0xC42C,
        "MI_VELOCITY_STEPSIZE_2": 0xC42D,
        "MI_VELOCITY_STEPSIZE_3": 0xC42E,
        "MI_VELOCITY_STEPSIZE_4": 0xC42F,
        "MI_VELOCITY_STEPSIZE_5": 0xC430,
        "MI_VELOCITY_STEPSIZE_6": 0xC431,
        "MI_VELOCITY_STEPSIZE_7": 0xC432,
        "MI_VELOCITY_STEPSIZE_8": 0xC433,
        "MI_VELOCITY_STEPSIZE_9": 0xC434,
        "MI_VELOCITY_STEPSIZE_10": 0xC435,
        
        "MI_VELOCITY_UP": 0xC436,
        "MI_VELOCITY_DOWN": 0xC437,
        
        "MI_CHANNEL_OS_1": 0xC438,
        "MI_CHANNEL_OS_2": 0xC439,
        "MI_CHANNEL_OS_3": 0xC43A,
        "MI_CHANNEL_OS_4": 0xC43B,
        "MI_CHANNEL_OS_5": 0xC43C,
        "MI_CHANNEL_OS_6": 0xC43D,
        "MI_CHANNEL_OS_7": 0xC43E,
        "MI_CHANNEL_OS_8": 0xC43F,
        "MI_CHANNEL_OS_9": 0xC440,
        "MI_CHANNEL_OS_10": 0xC441,
        "MI_CHANNEL_OS_11": 0xC442,
        "MI_CHANNEL_OS_12": 0xC443,
        "MI_CHANNEL_OS_13": 0xC444,
        "MI_CHANNEL_OS_14": 0xC445,
        "MI_CHANNEL_OS_15": 0xC446,
        "MI_CHANNEL_OS_16": 0xC447,

        "MI_CHANNEL_HOLD_1": 0xC448,
        "MI_CHANNEL_HOLD_2": 0xC449,
        "MI_CHANNEL_HOLD_3": 0xC44A,
        "MI_CHANNEL_HOLD_4": 0xC44B,
        "MI_CHANNEL_HOLD_5": 0xC44C,
        "MI_CHANNEL_HOLD_6": 0xC44D,
        "MI_CHANNEL_HOLD_7": 0xC44E,
        "MI_CHANNEL_HOLD_8": 0xC44F,
        "MI_CHANNEL_HOLD_9": 0xC450,
        "MI_CHANNEL_HOLD_10": 0xC451,
        "MI_CHANNEL_HOLD_11": 0xC452,
        "MI_CHANNEL_HOLD_12": 0xC453,
        "MI_CHANNEL_HOLD_13": 0xC454,
        "MI_CHANNEL_HOLD_14": 0xC455,
        "MI_CHANNEL_HOLD_15": 0xC456,
        "MI_CHANNEL_HOLD_16": 0xC457,    
        
        "OLED_1": 0xC458,
        "OLED_2": 0xC459,
        "OLED_3": 0xC45A,
        "OLED_4": 0xC45B,
        "OLED_5": 0xC45C,
        "OLED_6": 0xC45D,        

        "RGB_KC_1": 0xC460,
        "RGB_KC_2": 0xC461,
        "RGB_KC_3": 0xC462,
        "RGB_KC_4": 0xC463,
        "RGB_KC_5": 0xC464,
        "RGB_KC_6": 0xC465,
        "RGB_KC_7": 0xC466,
        "RGB_KC_8": 0xC467,
        "RGB_KC_9": 0xC468,
        "RGB_KC_10": 0xC469,
        "RGB_KC_11": 0xC46A,
        "RGB_KC_12": 0xC46B,
        "RGB_KC_13": 0xC46C,
        "RGB_KC_14": 0xC46D,
        "RGB_KC_15": 0xC46E,
        "RGB_KC_16": 0xC46F,
        "RGB_KC_17": 0xC470,
        "RGB_KC_18": 0xC471,
        "RGB_KC_19": 0xC472,
        "RGB_KC_20": 0xC473,
        "RGB_KC_21": 0xC474,
        "RGB_KC_22": 0xC475,
        "RGB_KC_23": 0xC476,
        "RGB_KC_24": 0xC477,
        "RGB_KC_25": 0xC478,
        "RGB_KC_26": 0xC479,
        "RGB_KC_27": 0xC47A,
        "RGB_KC_28": 0xC47B,
        "RGB_KC_29": 0xC47C,
        "RGB_KC_30": 0xC47D,
        "RGB_KC_31": 0xC47E,
        "RGB_KC_32": 0xC47F,
        "RGB_KC_33": 0xC480,
        "RGB_KC_34": 0xC481,
        "RGB_KC_35": 0xC482,
        "RGB_KC_36": 0xC483,
        "RGB_KC_37": 0xC484,
        "RGB_KC_38": 0xC485,
        "RGB_KC_39": 0xC486,
        "RGB_KC_40": 0xC487,
        "RGB_KC_41": 0xC488,
        "RGB_KC_42": 0xC489,
        "RGB_KC_43": 0xC48A,
        "RGB_KC_44": 0xC48B,
        "RGB_KC_45": 0xC48C,
        
        "RGB_KC_COLOR_1": 0xC48D,
        "RGB_KC_COLOR_2": 0xC48E,
        "RGB_KC_COLOR_3": 0xC48F,
        "RGB_KC_COLOR_4": 0xC490,
        "RGB_KC_COLOR_5": 0xC491,
        "RGB_KC_COLOR_6": 0xC492,
        "RGB_KC_COLOR_7": 0xC493,
        "RGB_KC_COLOR_8": 0xC494,
        "RGB_KC_COLOR_9": 0xC495,
        "RGB_KC_COLOR_10": 0xC496,
        "RGB_KC_COLOR_11": 0xC497,
        "RGB_KC_COLOR_12": 0xC498,
        "RGB_KC_COLOR_13": 0xC499,
        "RGB_KC_COLOR_14": 0xC49A,
        "RGB_KC_COLOR_15": 0xC49B,
        "RGB_KC_COLOR_16": 0xC49C,
        "RGB_KC_COLOR_17": 0xC49D,
        "RGB_KC_COLOR_18": 0xC49E,
        "RGB_KC_COLOR_19": 0xC49F,  
        
        "SMARTCHORD_DOWN": 0xC4A0,
        "SMARTCHORD_UP": 0xC4A1,
        "COLORBLIND_TOGGLE": 0xC4A2,
        "SMARTCHORDCOLOR_TOGGLE": 0xC4A3,

        "QK_KB":0xC600,  # custom keycodes safe range
        
       

    }

    masked = set()


for x in range(128):
    keycodes_v6.kc["MI_CC_{}_TOG".format(x)] = keycodes_v6.kc["MI_CC_0_TOG"] + x
    keycodes_v6.kc["MI_CC_{}_UP".format(x)] = keycodes_v6.kc["MI_CC_0_UP"] + x
    keycodes_v6.kc["MI_CC_{}_DWN".format(x)] = keycodes_v6.kc["MI_CC_0_DWN"] + x
    keycodes_v6.kc["MI_BANK_MSB_{}".format(x)] = keycodes_v6.kc["MI_BANK_MSB_0"] + x
    keycodes_v6.kc["MI_BANK_LSB_{}".format(x)] = keycodes_v6.kc["MI_BANK_LSB_0"] + x
    keycodes_v6.kc["MI_PROG_{}".format(x)] = keycodes_v6.kc["MI_PROG_0"] + x
    keycodes_v6.kc["MI_VELOCITY_{}".format(x)] = keycodes_v6.kc["MI_VELOCITY_0"] + x

for x in range(128):
    for y in range(128):
        keycodes_v6.kc["MI_CC_{}_{}".format(x, y)] = keycodes_v6.kc["MI_CC_0_0"] + (x * 128) + y



for x in range(256):
    keycodes_v6.kc["M{}".format(x)] = keycodes_v6.kc["QK_MACRO"] + x
    keycodes_v6.kc["TD({})".format(x)] = keycodes_v6.kc["QK_TAP_DANCE"] + x


for x in range(32):
    keycodes_v6.kc["MO({})".format(x)] = keycodes_v6.kc["QK_MOMENTARY"] + x
    keycodes_v6.kc["DF({})".format(x)] = keycodes_v6.kc["QK_DEF_LAYER"] + x
    keycodes_v6.kc["TG({})".format(x)] = keycodes_v6.kc["QK_TOGGLE_LAYER"] + x
    keycodes_v6.kc["TT({})".format(x)] = keycodes_v6.kc["QK_LAYER_TAP_TOGGLE"] + x
    keycodes_v6.kc["OSL({})".format(x)] = keycodes_v6.kc["QK_ONE_SHOT_LAYER"] + x
    keycodes_v6.kc["TO({})".format(x)] = keycodes_v6.kc["QK_TO"] + x

for x in range(16):
    keycodes_v6.kc["LT{}(kc)".format(x)] = keycodes_v6.kc["QK_LAYER_TAP"] | (((x) & 0xF) << 8)

for x in range(32):
   keycodes_v6.kc["USER{:02}".format(x)] = keycodes_v6.kc["QK_KB"] + x

for name, val in keycodes_v6.kc.items():
    if name.endswith("(kc)"):
        keycodes_v6.masked.add(val)
