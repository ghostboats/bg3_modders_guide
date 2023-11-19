# If a dict has a _ before its name, its correspoding file started w/
# numbers which is not a valid variable name so _ was added.
 # All other underscores in variable names indicate a filename with hyphens,
# which can't be used in variable names hence the replacement _.
meta = {
    '1': {'id': 'Author', 'type': 'LSString', 'value': ''},
    '2': {'id': 'CharacterCreationLevelName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'Description', 'type': 'LSString', 'value': ''},
    '4': {'id': 'Folder', 'type': 'LSString', 'value': ''},
    '5': {'id': 'LobbyLevelName', 'type': 'FixedString', 'value': ''},
    '6': {'id': 'MD5', 'type': 'LSString', 'value': ''},
    '7': {'id': 'MainMenuBackgroundVideo', 'type': 'FixedString', 'value': ''},
    '8': {'id': 'MenuLevelName', 'type': 'FixedString', 'value': ''},
    '9': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '10': {'id': 'NumPlayers', 'type': 'uint8', 'value': ''},
    '11': {'id': 'PhotoBooth', 'type': 'FixedString', 'value': ''},
    '12': {'id': 'StartupLevelName', 'type': 'FixedString', 'value': ''},
    '13': {'id': 'Tags', 'type': 'LSString', 'value': ''},
    '14': {'id': 'Type', 'type': 'FixedString', 'value': ''},
    '15': {'id': 'UUID', 'type': 'FixedString', 'value': ''},
    '16': {'id': 'Version64', 'type': 'int64', 'value': ''},
}

CustomDice = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'IsDefault', 'type': 'bool', 'value': ''},
    '4': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

DLC = {
    '1': {'id': 'CustomDice', 'type': 'guid', 'value': ''},
    '2': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '3': {'id': 'PS5APICode', 'type': 'uint32', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'XLiveAPICode', 'type': 'uint32', 'value': ''},
}

SystemConfig = {
    '1': {'id': 'HoldTimeAfterEvent', 'type': 'float', 'value': ''},
    '2': {'id': 'IsEnabled', 'type': 'bool', 'value': ''},
    '3': {'id': 'MaxSequenceTime', 'type': 'float', 'value': ''},
    '4': {'id': 'MinAngleDegreesDifferenceToChangeCamera', 'type': 'float', 'value': ''},
    '5': {'id': 'MinChangeCameraTime', 'type': 'float', 'value': ''},
    '6': {'id': 'ObstructionBufferTime', 'type': 'float', 'value': ''},
    '7': {'id': 'ObstructionCheckRadius', 'type': 'float', 'value': ''},
    '8': {'id': 'CycleSpeed', 'type': 'float', 'value': ''},
    '9': {'id': 'CycleSpeedDeviation', 'type': 'float', 'value': ''},
    '10': {'id': 'StartOffset', 'type': 'float', 'value': ''},
    '11': {'id': 'StartOffsetDeviation', 'type': 'float', 'value': ''},
    '12': {'id': 'Bone', 'type': 'FixedString', 'value': ''},
    '13': {'id': 'EyeLookAtBone', 'type': 'FixedString', 'value': ''},
    '14': {'id': 'HeadSafeZoneAngle', 'type': 'float', 'value': ''},
    '15': {'id': 'HeadTurnSpeedMultiplier', 'type': 'float', 'value': ''},
    '16': {'id': 'IsEyeLookAtEnabled', 'type': 'bool', 'value': ''},
    '17': {'id': 'SafeZoneAngle', 'type': 'float', 'value': ''},
    '18': {'id': 'TurnSpeedMultiplier', 'type': 'float', 'value': ''},
    '19': {'id': 'Weight', 'type': 'float', 'value': ''},
}

_0055e802_a9e0_473c_9848_1b1d7fc998a2 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_009e083e_c857_42e9_9e5c_9f6c242fb912 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_00f72954_fa37_4818_8f35_d28c2344cc06 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_02722555_c17c_4f59_9765_8dc75df36b40 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_03c7841e_3a05_469a_bef7_ae99e294fc15 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_04f70c98_e2ef_48d9_b78a_8d7de6c4ccb9 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_06e19378_2ff1_402a_a000_218a58694104 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_07a7c5e4_44c6_4973_bbb6_0f7c53b8c750 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_094057b3_d0ee_460e_a172_b4bd3aef588b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_09965f67_f0af_4b8e_93bf_76a04f1bdab4 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0996709e_67e6_47aa_a84c_198e3c7c58fa = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_09cf2fa7_79c1_4c0a_b04f_ff788020809b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0a012927_140b_4482_a16d_ab5ca19b19ea = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0a8d6d61_f5f1_489f_92f3_b7edfa2a216a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0af0e5d6_99a3_45b5_a8e5_c78ef39f612f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_0c887127_b520_4df7_83a7_b1f4ff8c7fed = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0c968d12_bbc1_49ae_9ab3_9375c8c05a34 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0d6adc67_26ec_4bbc_86c7_faec3ab994d2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0d9943ab_75e2_4ff2_a0c4_e03704fd7094 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0dd3f247_8465_4ab3_8db8_54841892f9b1 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0df195fa_5363_4a8e_a184_7cf2c61d82ab = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_0ff25ce5_0768_4452_a72c_1972eaf9992e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_106604cf_c76b_4c23_a8ae_dd3d434459fe = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1548df3e_b856_4aa0_8315_0b94ef7c019d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_156a2490_d796_402c_b7fc_e00c032042c1 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_15a9c7b9_b86f_4195_a8d3_b7d7a456d159 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_15c8962d_a83f_40c4_b0a2_90225deff67f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_15cc7de0_a7a4_4a81_a0c1_9f59d1206b2c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_160ba7e8_ae33_4adf_bac2_8632732a31df = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_161b48f3_641a_49ec_886a_df7a7630b65a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_164f210c_dd88_4e3d_8976_79201048aaa1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_16642e50_a21b_4274_b547_e867e1a5e775 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_16a61952_fe6b_4204_be23_664e992e31d8 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_16afef95_b968_49dd_bba1_8b3477202d42 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_16e37a6a_2e82_42c2_893f_0374ff845632 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1738e376_3a0e_4d31_bd01_74d5ce77ffb3 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_176b39d6_371e_429e_95af_fb97819cc922 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1818b43b_400e_44f8_abb9_db73c5a9356c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_182393d9_70d9_4136_92d4_c7bd109516d4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_18686725_73b2_4a70_9bce_4fc20ba2f102 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_18f8b145_0529_46e4_a383_463bfc101e93 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1914ad85_40aa_4822_bd92_04860a6f6f17 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_19846634_17c5_41a8_b6b9_7c88e8e70434 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1a79641d_8ee6_49e4_a4b6_e12bf94198f6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1a872cc3_cedd_436b_bb41_0cd820aad44d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1a89dfc4_e61b_4ea6_ad10_69aadfe638e7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1adafdc9_31c0_4208_befa_80fd1a29bc84 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1b00d1d1_985b_4985_b8b6_a1b1464347ba = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1bd1cd79_9ccb_403c_b9fa_a33b41936e94 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1bdd7187_f4cd_4a66_8648_4bdbae3a32bc = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1c4b376e_e888_4100_88c0_e761a35593fe = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1ca9196b_170b_4c2b_af59_50f1d678fe58 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1d13efe0_fd39_4e85_ade8_e19660dcd2c7 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1d6a6108_c75b_49fe_8112_5a738ef34098 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_1dbf9242_c368_4f15_8f3a_7ae85ebc955c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1f58ec84_7297_4b15_a0c1_fd759aaba7a9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_1f7cf255_434c_4da0_910d_620e473e9fff = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_1fca62a2_8c30_4570_9286_f08f01e8c45b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_207c1f68_48fc_48b6_a6b3_f67ed9cda6ad = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_20e93816_f46c_4123_a9f2_f4d7a8c384d9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_211d0b56_fcc4_434f_95ea_4848368b2b85 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_213cf510_ddf3_4d80_9b9f_6a1950d42dda = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_21a5bf9d_f97d_4e38_ba2f_35e88e6f4d78 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_21b9ece2_54be_4e93_8183_8750f9387580 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_21e33db1_4ae1_4362_bfa9_266f1b93a1b8 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_22587d39_6d18_4100_8b3d_a2c02e931518 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_22bad855_e195_4d5b_91e8_f7f974acea63 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_230a6679_1d00_42aa_b091_693db335527e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2384e5cd_6f73_4545_a078_1609902516c2 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_248573ea_c3af_4cce_b202_8857d2413afb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_249acc14_fbfc_4aee_bb73_e4c807b4facc = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_24d5a248_d52a_48b1_9398_d893625a2e72 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_24f150c2_4c5c_446f_8381_b5e1b237467e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2500cb17_eeb9_41c9_b02b_ed03ee6ac0e7 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_266cc4cb_d076_44ec_82af_afbd0832c1b0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_26fc760a_30ad_4a0a_8334_e307618a1f6a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_27b29de6_c915_447c_a20d_14b78a78f6dd = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_27e1c191_832e_4408_ad32_dbb0f27b9a1a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2848558e_434e_4ebe_9b4a_55b25faff6c9 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_28a8de3e_51cd_4311_b551_b4d8c1c81345 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2926ebbe_cf02_4c71_a9a6_a8259fcb1499 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_29fc4f59_b85c_45b5_a805_8ba7f996a06c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_29fec304_ab9e_428b_a65f_e681325e6a70 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2a199dc4_5223_4ba0_8235_fc652be0946d = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2aa406af_6f5f_451e_86e1_89e513245774 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2ad160e3_0c1d_46e2_bb1e_9cade2383103 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2b2b7c12_3f6e_4f6b_82f9_c49e0725d017 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2b86f332_fc54_4731_a77a_7388ce0d2798 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2bb3eefc_d0a6_44f4_9d42_28d7ed045500 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2c1a0701_26bb_4223_9ea6_d6b86486dc88 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2c5dab21_ec5b_4899_8847_c00968a642b2 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
}

_2ca3f400_1d2a_43ce_96c9_bfaa752f8054 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2d432f06_5935_40ba_ae90_3381c9bc83fb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2e0d40e1_1c9f_41b2_87f1_82a841544255 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2e2c61ba_0e6f_4f8f_966c_8d5e432799f5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2e5e79d5_8243_4cec_9c1e_3740cabf0c18 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2e657aaa_1980_4247_a9d6_9ec4fdfe8c64 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2e959c71_3465_4a1d_8ad4_4617722673a7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2ec2bca0_829a_4d9b_b5b1_a5769b2cf6ac = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2ee7bef6_edf5_4b9b_bddb_6ab4dee08209 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_2ff020f6_9361_4016_9f85_2b4e54d3b4a4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_30bd251c_4f79_4b03_a86d_7f8f1039a838 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3151fd06_270d_4788_bc1b_54dc6376b3b5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

_31c5d1e9_5b2f_4c60_9f84_b1c11521f8fa = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_325d5bb2_d6cb_49b8_a5c8_89c5f7f5a9dd = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_32964912_b291_4d2a_9dc6_5d5c164390c7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_32a7ff9f_58ef_4fcc_a37c_5421eac6383e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_33797b29_f989_4569_8a2a_2a01289ec661 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_338ff3e6_479c_4f0e_aaae_7e5b912c6c2e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_33c11f33_9a7e_4813_8563_5d0f3768bf66 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_33d8632e_4e26_4663_bdf9_dc15fe78e75a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_33e77fab_6ad6_485d_9d4b_0615aebe1bc0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_34a05e2a_e15c_4f46_acff_993360d60230 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_34ebac36_cf0f_42f6_a579_3308d9ac2c07 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_35ae9557_a807_40ef_9ccb_dd80f89c8b4a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_36a29e5d_8061_420d_a4b2_828ba65c3de2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_38c198dd_51c3_4fe6_8662_94e5c230205a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_39a99ca7_d32f_4016_baf3_671583f7fed7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3a2b2f90_e9bb_4c8e_98e8_9970e151ff38 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3a8c5103_3921_40fe_805d_e6f9f49e1e76 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3acd5d6d_db96_41db_97cd_dd43921149b0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3b131620_d960_4d17_88b9_5ea0c380049e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3b1a2d2d_c730_42b2_91c7_a22d26d58362 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3b88e092_6af8_4f12_95b7_c058f47aac23 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3b8add11_f889_48fe_8407_873e7165bc8d = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3c4b5ad9_fce1_4e5e_9476_b8c32e0c9309 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3c6496f3_2d1c_4998_b651_f6cec44f703e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3d2c3974_88fd_4370_9c05_4f011ca370c5 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3d75ca2e_bbd2_4b81_b72f_7f6c5b1c505b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3e3d2300_6ce3_475e_af3f_6e8de2c5bad9 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

_3f54f995_7c86_4f59_b0b0_2541412351e9 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_3f640f19_d5b0_405d_9e16_9f0520f6817b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_3f75a3a9_3e17_4e8d_a04e_a6c0af0c3cc0 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4057e0e4_f9f7_490a_82da_0b07951910ac = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_408be61a_fcc6_4925_be28_f32c1a0546bf = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_428b6831_c9e5_4fb3_82b5_cc8038433d00 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4303661d_083a_48b8_b480_cb35b984d8a6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4308c2de_bc31_4d2e_b1ad_0bc6b6d96cb6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_439acdba_5289_431b_9e52_8e4cae18bf09 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_43c3fee2_4130_48cc_9c63_e9d68084a7b3 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_44d9d50d_16e2_4089_b584_e6777a2d4179 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_464b1139_6810_4822_b837_2ac408764733 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_46b0086b_f650_4e70_8b4f_d1669afa8249 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_470ff3b0_5767_4f5d_be79_c9968bb9e37e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_478acb62_e59d_4811_9fb2_43ef09e0d037 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_47dac6de_d9d1_4431_be75_e36c0074bb33 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_480b3d82_53ea_453f_bba4_3b0a70f46b01 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_481ce0d9_cab0_46d7_8d32_b78fe5e7540c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_48778334_20b9_4e6f_b0ff_663f5e9e4019 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4906aefa_f5ba_4468_b018_947eb347afa5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_49afd25c_67a4_44c3_b83a_7074ff66fb1c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4a1161e1_c64d_41e6_bdb4_d7073aaa3934 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4a47a29e_2a45_4361_8556_5af12ae72d26 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4a4dbeb1_ed82_4352_81c8_8b90bd0fe848 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4ae5f1e2_a873_42fa_8487_c816773e65be = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4aff0111_1386_4ab2_8d52_e1e533886dc3 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4b5841fc_b963_4a31_b557_3c87a5c4d696 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4b85284f_6f3c_4963_8091_6cf12e9c94b1 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_4bb0bdcb_5fff_45b3_b3ca_cd317e910fd7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4cd01a5d_696c_411a_a82d_872829fe09bb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4d3b023c_05d3_4fc2_8021_343e6b2c1cbf = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4d5522bc_d131_4f42_a57c_f0abcfaf85d1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4e1eb4a4_d178_4668_9883_0096273d0967 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4e90685f_56b6_40c1_94e2_e81177c130ae = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4eb958f8_ac74_4b3f_b3dc_e7f78a0ee773 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4f9949e5_cc06_441b_809f_3d582f8eeec8 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_4ff25b7b_e761_44f6_88d3_90b3ddd94a12 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_50125653_dcbf_4313_8c4d_20bd2a2dd346 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_50b921f3_756f_45df_8313_67c06882b78a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_50eef273_dbd5_4fd1_a3c0_c60c1f4e6962 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_50ffc45d_bc77_4138_a51e_211d317d73f7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5100f96e_76b5_47ad_aecd_6160c776a5ab = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5199148a_78bb_4e87_8517_5181d97a19a7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5278c90f_dd04_42f2_a1f3_63629e29afdd = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_52c04312_0ac5_4399_991c_0de1beb4b52a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_52f16b65_61c2_4994_83cf_715c5f4b4cc9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5326da5a_7c4d_44da_be05_f66b76bc8426 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5343c220_d6e2_4dde_aca8_f932a7ca4da2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_54ed37b8_75d7_40d2_bd5c_9956de04bf9f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_54f81732_27d9_492c_b2a3_006ce71c6f17 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_578c117b_1e06_4797_be84_bad2c56ea106 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_57a860d1_6d8d_4039_865b_d5f94380ad31 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_58394bff_1d3b_4f7b_a2fb_30586d139337 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

_587ec6fe_cc0f_4bd5_ba02_5aa714aa0d7b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_58da5ddc_d630_464e_b912_dbced5ef707e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_59f2cb64_be4b_4330_86e1_7231b145d794 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5a1ecf04_c11d_415f_b670_88d396a9eb52 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5b714143_b2a5_4943_89dd_0e2b8644c0d4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5b833809_4e9b_48c8_a501_3bc8472ea304 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5b991999_435e_444e_ae1a_3118fc52348f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5bce1cce_15cd_47ae_8c37_7ee837f483ff = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5be9b6cb_7840_4d6e_baa8_5116abe4f4d4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5c14ae91_4819_44f8_acc3_126f7a9a9e31 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5c5f9d9f_8f43_42a6_905a_537a31063d02 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5cbe1ab9_f2f7_4ea8_8284_e737a4ce40f4 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5d00b5cb_aeba_4f39_b24d_440ea3e192b0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5d2498e6_8027_4ac9_a1f4_dbe9d4a030b1 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5d2d3a0c_16fe_4494_ae72_fba8d5f475de = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5d2ed9f6_8d95_49f7_8fcf_5dd37324b6c9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5d5f8697_196c_4651_a589_2fb0872ce5ae = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5db9a6b0_c7f0_4910_9fe0_e7f870776626 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5e126e50_9ddb_4720_872d_eb99053c7381 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5f38fabe_82a2_42ac_abb9_29fc540ea40c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5f9d30b8_de02_4b75_aa17_81821f5a9b4c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_5ff6f203_f161_434a_a4bb_268382502f07 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_60c933f3_ad99_41ed_83a6_b317d139d6c6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_60e3471b_9950_479d_9903_8d9d8e2ae352 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_60e992e3_d694_4d3f_80cf_55500699cb02 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_615daa8c_f17d_49c6_a864_ac3b5d977d31 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_616fdb0d_7aa2_4600_8335_269cc6f1e5be = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_618d71ce_6228_4ba7_98c9_9c90099e123c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_625075ae_bc15_4252_8117_0b3b60281bdc = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_62989fc6_77d5_4df7_b49e_3fda35c48d6a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_62a922a2_f920_4aef_8aed_97e8df383eb9 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6308d469_0200_4227_bb6c_c1a31f83ba79 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_631e7672_9066_4051_a331_46f2865bca42 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6357248c_f20a_43ec_8c59_851f803d5a53 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_63d00bac_7eb1_4722_99a6_1d5432a597cc = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_647215be_e021_4cb1_927d_4a96ebbfd16f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

_6655b2b4_d20e_4a51_9043_ee0c2b59bfae = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_669d157b_a0a4_4719_8ad0_7df7a8ecc010 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_66c65fdf_e902_40ed_804b_bc6212bb7f0a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_67807075_26af_48f7_bf5d_3c535fe25027 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_682944a7_3e1f_480d_8691_b6b209cb0681 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_685e0234_1a84_4601_9f8e_624dc39b33f1 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_6863f760_55a6_45f1_abd6_0871b3903dc1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_690a42d4_5d0a_43d5_98a5_38c3de57408a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6959abfc_4ec7_4fb6_a58a_eaf05d2cb0eb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6961e6cd_ba72_4178_b6fa_fb1548b1e2f7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_69dc3731_0f8f_4bfe_9d91_8038b336425b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6a6f1ac0_1fb1_49fe_bd6a_248f1ce68050 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6ace09fc_91f2_47c5_a094_f76f422b6dcd = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6bef167b_949e_4add_b492_8d8b2143d59b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6beff6e3_084d_4a6c_b2c9_e534261be310 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6c58fe30_4730_4882_9a73_9c27cc060bbd = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6d17a9ab_2433_469a_ac6e_6da269ee1696 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6df71344_53ef_4765_bd05_32ad4b0149fb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_6fe0a55b_c9d0_47d8_8bc3_1667fffda051 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

_7071cf2c_a006_42f9_9121_40c6983711e9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7162fe59_4865_4cb8_afb1_8d2bc8df5a6e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7261ef7b_44d6_4269_b12e_42899264b841 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_73f7dd7a_fde3_45a6_b2ea_f28450fa527d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_749a21e9_fb0f_4b57_8459_541dbcb8e458 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_752196fa_00d6_4714_a030_3e5861042229 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_75d5abc2_6761_4150_a591_3121b707e239 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_765bf096_0daf_4e8b_9b17_3f45d1a0ddd6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_768ba586_1d99_4bca_ac23_9caea7e26c15 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_76b4835b_72ad_44c4_92d2_fd7d067d4988 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_775a8373_cb38_4d0f_a6a5_673907c1a3a0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_776ca4a1_43d7_4ed7_936a_fa573138c8dc = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_779e9f32_e282_4df1_a640_f318c1cb81cb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7882c73d_821a_424b_a61b_1963fa9d919c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_78f0ff4c_6b80_4dbf_91f5_ea5a766e1a24 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7939cd78_af5d_4799_be79_fb5825034e14 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7b5be5e8_3f20_4434_a92e_435242a64a2b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7b7db777_94ed_4e21_9bf2_4d9237560a22 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7c1103dc_adac_4af2_9601_506894e8f476 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7c38ab2b_bec8_41e0_85d7_3e8058c5ff84 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7c4e31f4_2f30_4975_80d0_d55e3ec68557 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7c838ef6_535c_4ac9_b6ee_2c4dd7debfcf = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7cdf7fd5_ce1a_4b0c_940a_a2304b285624 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7d007906_81f8_4253_bcca_c71942fff61b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7d7e28b3_5593_41a7_ac77_5a887e0095b2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7de0cd96_8727_4494_b4b3_ba9bda8f88ed = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7ec889b3_9865_492f_b80f_2c66fab51da1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7ed95f1d_5d81_49cb_88fe_aba90d343791 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_7ef35665_d137_48a5_96c2_670ee2ee867a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_7f906e90_9937_4d62_9a8c_19b516f6258c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8114c737_0469_4eab_bf4d_db14a0486a4d = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_813b0a29_fb35_4b7a_ba20_97977f5f3d32 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_82776faa_0c8d_4d05_881a_f13f8822aa67 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8285a86a_c98b_49ac_a995_a1982bc29d74 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_83b1ce97_ff89_4444_a3cf_b68734d881a4 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_83c005e4_325a_4612_a662_7a2563196e8e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_851878e4_5e36_44d1_8326_131196b3a3b6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_854702e8_a892_4ac6_9bf1_df52c841257d = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_86060142_40ed_48a3_97d1_39d37ac13607 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_863414f5_98bc_48a0_a440_403e7d48db24 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_864d9854_2e06_4b23_89f9_e7d89294d800 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_865cb373_da6e_4785_8f14_7277c13a7bd0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8697463a_a8b7_45b1_8768_4c24105c0327 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_88602a6e_06a8_4319_a688_b261143c11ba = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_88b018dc_3c01_4648_85f0_c0deb13b64c9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_88db3a14_5824_4919_878a_b7442e92eb75 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_89926e5b_d449_44fa_a202_e5f17b1b001a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_89ebc16d_e7e9_4bc8_aafa_80fb74f86954 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8a5b0d9e_166f_4950_99b0_cac12a615155 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8c04baed_d85e_47b7_85f1_cc7643af91ba = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8c0681e7_0eff_4375_a697_dd7fbefde665 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8c983099_573c_4e3c_85f8_21c4b03c5e1a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8dd752a8_a0d6_4b17_bd73_990e99db5f21 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8e3e8cd3_f401_4fd8_abd7_0db72dfb2dcb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8e59e31f_86f7_429c_b07a_df748a3dec17 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8e8f81d4_3fd3_426e_a442_9346f1c04497 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8f830416_fb34_4500_8f62_7110f3a5858f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_8fd1fa59_aaeb_40b3_856f_7714d9afc9b5 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_914159e5_95e8_43d9_b8a6_6edd780ecedf = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9214055c_5e47_434c_afe3_df51e4aaca85 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_92d6ddf9_76a1_4e39_86f4_804705dc759f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_92fe7eb3_5780_407f_b346_f34916e0a162 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_93e2495b_cceb_49dd_9119_f7328b2b5d18 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_94593029_08eb_42d6_899b_96269040a8dc = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_955bfd54_4dab_43b6_a58a_a70d234b53a6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_95d3cead_413a_4283_afba_ef46c4e9c0ba = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_95e3efd5_0357_4028_8dff_e3b3de3cd994 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_967141f9_b26f_401b_8fc4_f79b2bd6aa04 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_970af73f_2136_4edb_b5f3_db7308f246a9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_972970dd_93f9_4f63_bb77_2df8e72cebf1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_976fb330_4613_40e3_b428_b6a726909e23 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9783a9dc_0785_458a_9d21_7a371080eed4 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_98047166_ecda_4af8_8b29_9631a06e4dc8 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
}

_9859cf79_436b_4216_87ba_8ec7cfb005a3 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_986837de_11a0_4e03_b7a7_21580d622fd3 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9898e0c8_d6df_4105_8a89_593ac0119b75 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_996b6aa2_596f_428b_8a08_5b844f360ae1 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9b30ea12_d3b3_4fd7_9e05_78cfae647c9f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9c02c339_5345_4c74_87d2_33ba0673f4a1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9caf0fad_81da_4469_9e61_2c1e17393d18 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9d327d8b_14b3_4ef4_9ba1_77cd183f787e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9d90987e_feba_443e_bb65_97eb3867abe0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9d934ff4_30b7_4a16_9ff6_8cdbb3dee83e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

_9e9bb27f_8ed8_44f1_9229_679562bc45b5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

_9f54e010_7594_4ed2_b055_f06f0216e647 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a004557f_973e_488a_b258_9c4f1014ccb4 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a008a9e4_8936_45b9_8a65_ec06e852dd1c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a0e24940_d5b4_43ee_ac1f_d2c37cc1b71a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a0e94996_662a_46a4_b2d6_5c3d33be4681 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a130f872_e0d0_4fb0_b7e2_0a34df9a38b2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a1d0e31d_bcdc_4758_880f_1677401c9f46 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a228ec26_764e_40ac_adc6_d66f613f18b2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a295ab14_9ab4_4cde_ba79_fee45d7c3f63 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a2c59e1c_0618_431e_9fe7_534db7fecd86 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a2d4003a_ef01_42f1_87f8_c29446ffb18b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a41ed421_4139_49e1_b79f_9c258e1a8ca2 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a44a38cb_b36c_4254_8429_df0cb078f50a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a48c02b3_7eaa_4ef2_9403_1019d016fdba = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a4cd5e52_0804_40a6_b7a1_c4398d8cba61 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a59a6954_9e2c_4b93_b184_fec06ed47cb8 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a64baf64_3126_41bd_a78d_0547c7a1fc88 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

a7276f2d_ea48_4c73_ab32_b3dcbbe0ba9a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

a7a4859b_796c_4a4a_afbe_6666fdc6b638 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a812f87a_8fd2_46b3_9cf0_b96f71a5196b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a8bb358e_4666_4097_8ccc_de7104e9e2e7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a912ed0c_9a5b_4d9b_9336_9dccaa858b87 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a913ffb6_56ca_442a_9cfb_455ea1a38f5a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a94be0d9_677b_4ba0_887f_d7ed2b63d033 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

a98699d7_e90a_47be_98bb_15c0535fca5d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

aa0c98a1_6b1f_42ef_baf1_e0ca373a11a0 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

aace0fac_0f15_45b4_9c6e_09cc41b0b2bd = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ab1b2f30_d550_453d_b0ac_03e85fa1998b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

abd97d52_7639_46ce_a701_a0222e96a2e9 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ac8c3cfe_4aea_4d15_baa2_e30337c70981 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ad203d59_cad0_4008_804a_945784432615 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ae0c1131_bec3_4d8c_b841_680abb04e2ff = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ae468371_011d_4e8b_9cfc_909d9b4622d6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ae685fa1_2c92_44ca_8f6f_ce0ee2c59b26 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

aec9d8a9_f7d3_40a6_b2da_8d7c1ae1c298 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

af2a30a4_8104_4f3e_a492_91bfb779d2c4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

af8897ec_82ae_45c8_9de4_ce04537a6d56 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b018fca2_5f2f_458e_9e7e_7231e73d7eec = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b020b3c9_0584_44d7_a25b_55a539598202 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b03badb1_4e6e_4602_a21a_bd8af0668678 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b0610dc3_c428_4e22_ac09_a1d54a28c36e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

b10c3ae3_ee92_4402_8f8f_2c1d9f1fad43 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b18763fe_6ab2_480d_9bf6_6d70d2f716b0 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b1ab75ec_1c8d_48d1_bb8a_10e3224dead5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b249850e_c7dd_48da_b069_eadd679c2a21 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b25cac4d_4bec_48cc_af67_12d2212dcc17 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b28437a8_4fc3_4025_b7ca_e92765d6378c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b2d1c53d_6136_43e7_9ea6_039be681f34b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b3002661_00da_4dec_ba42_0494d38fadf2 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b3d05d69_0903_40cf_b1e5_aae2dad68c7f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b41aac27_8b58_42fa_b941_89041b5c7085 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b47044ff_c9c5_4406_bb6a_05f21d2bc6eb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b593c509_93f5_4153_a41b_94e76ff59398 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b6890a53_47a8_43ae_8300_f212a7d22188 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b7ad35eb_4e69_4f0e_96ad_b18ec4630440 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b87d2d16_9689_4e49_93f6_7a1affedd464 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b889c54a_8d5f_4c69_abdc_c7a2377d3ae2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

b8919781_689d_45d0_bdbb_4d8b17738917 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ba70f492_c045_42be_998c_c5e2b30b66c7 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bb2136be_3b9d_45c8_919f_544d39f2c9e3 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

bb3c5505_055b_4951_a696_65e18e96011d = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bb52552d_2728_4222_9a2e_f808a381e290 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bb7a205a_f654_468f_a03a_f85088a1bd01 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bbb28ced_820c_48d7_a1bb_34a94e075784 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bcb30050_76a7_418b_98a8_8129b7041f04 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bcdefeae_5be5_464b_ab40_88cff2c821e5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bd1d8c40_db57_4a65_b5eb_18cde5fcb18e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bd2f9b76_5a20_463a_b843_122d168f3ba6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bd5d2a03_4d5d_4606_8aa0_d6c13657cf8d = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bd9cf283_2341_42ec_85cf_7fdf118f5007 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bddca7bb_9ee5_4356_b9f3_ea785ec72bef = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

be11c2cc_2bfc_4770_82ee_82bde1d76cc9 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

be4be2f9_acd0_464d_b5d7_6a22a6e380f6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
}

bea00caf_8194_4787_89f0_a58f67c39193 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bef4f929_fca2_4528_a38b_c33e51a43aa0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bf4f2b73_b795_4a8b_a90d_df81879abb29 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bf5800d5_fb0d_442a_8d68_2043eb4fbbb6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bf7b70fb_2871_4cba_b014_73d6487c2caf = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bfc7c69c_d11f_4f82_873a_95bf9507ce0e = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bfe56659_c29e_4dd9_ba28_a7044505369a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

bfe65ea5_fd0e_4fb0_94ae_fce2588681af = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c05882d1_32d0_4a4a_8b35_415c59f796cf = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c09b5651_dae9_437c_b64c_322d7862240a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

c10f0b9c_ac63_47f4_8855_1aa9fe8d4885 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c2480eac_e01a_4f89_a350_ad31efa8309b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c25b5d29_90e9_4ff1_ab28_3dab202fbc4b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c2b8bab0_6fa5_49a7_b6ca_2970c37fc4eb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c2d87dd9_db0c_47db_a113_45319c2cc97f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c40ded84_39af_4650_b528_111296bbd03b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c4635383_1153_4c73_9eab_c59d2d0fa7f0 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '4': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

c497b32d_dc02_425f_9341_94a8e99c7319 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c528237a_1720_4d17_8eef_70fc446a9286 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c5db3600_5b00_413f_a972_e9d691ff04a6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c5e8b30f_bd06_4bfe_800d_12e25d076efa = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c69957fb_3e72_4c58_adcf_718387f2c8fa = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c73c5636_521c_4032_85da_3f4ffffa6b3a = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c7ce70de_8282_4710_b01e_87ea0421d583 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c8508b18_fba0_4e76_82bb_3da00fb9c8b3 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c8b10f9d_9f70_479c_b535_70c7a608cf09 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

c9b1b825_38eb_46cf_a65f_69c74f123972 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
}

cb1d0c72_698e_486b_aa80_6d032af59055 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cb88a12e_0a04_4b0b_a217_d2c3a994f906 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cbbd535e_fcc8_4c0c_9a2a_8b41078d6154 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cc276919_b9de_442c_8111_59a53f69d762 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cc47c58c_b419_4d18_84ab_61ef6fcb413c = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cc6c1766_57b6_418a_9374_38ddcaf34be3 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ccb42651_ba9f_41e8_a483_1686730db2a0 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cd89a79f_0532_44b7_a50f_e53784d34cc2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ced4e75b_0fe1_457f_9c29_ec0d852a0dfb = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ced9256f_08d2_46ea_b193_063babf0cd21 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

cf662a06_bed9_4d32_88f3_944c769df814 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d02146aa_7d05_4f8a_b83f_13e59988e712 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d076a11e_2f99_4084_b9fc_1bf7da11d269 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d0f09b1f_4a5d_49e5_8b9d_66ca610607a2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d193aa62_b9af_4b82_8c29_7e344d117f32 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

d1a744fb_5a64_4845_9665_a6f8f4d64e0f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d1f80f0e_1bad_4d90_95b4_ab3ff0c060af = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d2990165_3d6a_449e_8c39_a73c4d2357c1 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d2c26fb8_51cf_4ab7_a098_101149c193f2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d2dd36bc_041d_4993_a464_5538054ca183 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d46dada0_962b_41b5_83f0_fcd764c2229f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d4fc694d_7785_487b_bebf_c170b3f6f9ea = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

d51b142a_a56d_4092_aa31_c6a12e922f96 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d533f540_b73b_423f_996d_9f6f812c1fae = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d575489a_504d_409c_97fc_d38f5c63d272 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d5ce9389_2889_420e_b3c2_fa2dc2cc19ac = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d7409dd3_4728_403c_bd03_118c0c27ea3f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d7f5802f_a661_4944_845a_df035cdba6f0 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d80ba532_0b52_4ca0_8599_ac389df5f810 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d9045d3b_5d2f_40de_88a7_0f2d4b019616 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

d9531715_c8bd_4a5d_b85b_dd52fdca9d75 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

da227f82_4291_4a19_9651_bd15f3d0dc0f = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

dbab134a_8597_4748_95e6_2f9bceb9dddc = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

dbf5ed37_7535_4ace_a14e_14a0dbfb7ea7 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

dd6ad13c_aaa0_4c1f_9f0c_6ed42d75a91d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

dd95a51c_c1e4_48d8_b547_8e538abf86f5 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

dd9ead42_a3da_4178_af65_c43ffa649477 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ddcf2d6e_0d4d_4b63_a4dd_89d8d3a92fb8 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ddf7fc5d_59d9_4482_ba07_dcc942c46ceb = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

de32ce63_9e8b_49fd_bc56_35b9971ef9de = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

de47de92_70c9_49a7_b0f8_265726105e2d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

deca2392_7156_40bf_9cbd_b486070a56ca = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

df000782_6d77_4714_bfd2_9f62ea14e8eb = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

df1c3326_6618_4898_9318_b245c88d8aea = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

df5b3c1f_81af_451b_9ca4_e23e5e882070 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

dfb4d8af_2cde_4ee5_90bf_b356acb04e63 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

dfb55e92_24cf_4ba5_8afd_ff13729abae4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e083f3b1_0e40_4b03_9074_d90e78221f3b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e1ae7d11_0d48_47a3_a392_5a71e63835a4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e1aff032_c8bd_4445_b3f6_525e41616b8c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e2576842_bf16_4676_a714_c4a347da6887 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e27bea2e_aea2_4522_92e6_25e7b8fa7752 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e37b7d03_be6e_491a_aa74_3775f45747a2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e4509f90_82a3_449a_b2df_f80ddcc11140 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e4e61380_fa28_4197_8763_e5bd3531dfb8 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e55e4cd7_c0bd_4fa3_a473_c9458647c565 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e6796409_907a_48d2_9f70_c89bff4f796a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e693e29d_27a9_4af2_ad42_17d4fdb58996 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e6bf18dd_9b1e_4770_ad8d_f3bb68b3ca58 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '5': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e6df2779_a1a6_4a3f_a993_12d8a903f76b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e75ece92_2a5f_43c6_99df_54f9b76584da = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e85ee57d_0b8c_4aac_b3eb_cb6371a63e7b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e88b96f9_2562_44f3_a234_3ccbc6b19a5b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e97db474_e27e_4afd_a060_b41e62c0cc31 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e9928948_c2c0_4a37_ae98_9755ad1b5504 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

e9e233ae_0d86_4439_9ca3_2f940897a8ea = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ea42242a_95ce_4c55_8c97_2fc3ef89ce4b = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

eab21377_e75f_4d9c_b734_270ee7336d36 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

eb29ac15_5483_4b13_842e_b691db34449d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ebcf0119_9efe_4565_b94a_97bb0455f3ae = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

eced1df3_8618_4cc0_8a53_920303982c3e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ed43252a_8dbe_497b_9ed0_cf309a731c33 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ed748b31_d6c8_44fd_b80a_a7276284d875 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ee4fb2e2_551f_418e_b9e6_145a15afba78 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ee542e81_6e5d_4156_b450_0c4650136197 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

eef9edb2_0176_43e9_bca1_45d701919cad = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

efbf58d1_dbba_4cff_9f14_c31e45c5a6f4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f13741f0_0ba7_4eb3_98b7_b33277edd67b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f16b4ce6_f300_47cd_9aeb_0ef1046949ed = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f16c7187_d1f6_45ac_9aef_b5ce521c9704 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f1bcf7d0_b77a_448b_a4ec_78d58d380f18 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f281ed2c_96b2_4269_a1ce_c7990311dc08 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f29c1dd6_232d_46c0_834a_33968654c55d = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f2aa8ffa_4a74_4c35_bbb0_639923801a55 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
}

f37710b4_8e6d_4bcf_95c9_56a7f0debf7f = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f37c269f_5363_40a9_baa9_726f70e61ab6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f4f9bc47_7fc5_4ff9_a431_b5514286045a = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f5359242_e9dd_418b_9c6b_583625229f45 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f54dbdd3_03e7_4872_a770_fd00842cb478 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f5ac527e_6393_49d7_b9a2_9044766922b7 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f64b7447_3c6d_4e59_bf61_6e9cd3c2dd0e = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f6b0fc3a_e1fd_4d32_9fd5_aa0a2dae31b6 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f831d840_d123_47ed_b1ae_c0552e96c161 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f982823f_831b_4d9e_8e01_998722e3d9cd = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f98dec27_9753_41a9_8fcc_600981cf4cf6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f99198e7_6d1c_489b_aa35_001384e06274 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

f999635a_ce6e_4ca2_bac6_486bc98dfa70 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

faa67d93_d928_45e9_ade7_aa549de411e5 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

faad6692_8514_40bd_823d_a4ea8367a937 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fae76904_b702_409c_931e_1b3bab9ef56c = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fafc0127_3fef_4855_884f_d618048b18ab = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fb14fd13_9ed3_4c23_a704_90f260274b0b = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fbb179dc_5739_493c_8d13_d6dc91a6bb33 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fc444634_5870_4ca2_b0da_00b182127657 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fc7f90de_1510_4f90_b20c_97182d6ceb54 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'SlotIndex', 'type': 'int32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fce6cea4_14ac_4981_8f4d_e59cb34552d6 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fd2b8b51_cd00_474d_b4a3_f92c841dcdd4 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fd997694_70fe_4aab_9d04_d10a4146d605 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fdaa0c48_6167_487c_9527_38b4dcaffbad = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

fe07624c_890f_4bc5_9a32_21e6af5ba5df = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ff5a0fb8_5488_454e_b4e9_aecd27653c82 = {
    '1': {'id': 'Key', 'type': 'guid', 'value': ''},
    '2': {'id': 'MaterialApplyFlags', 'type': 'uint32', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

ffac54be_9ce6_4783_b070_b37c6d0401a2 = {
    '1': {'id': 'ForceEnabled', 'type': 'bool', 'value': ''},
    '2': {'id': 'Key', 'type': 'guid', 'value': ''},
    '3': {'id': 'VisualResourceID', 'type': 'guid', 'value': ''},
}

Hints = {
    '1': {'id': 'Controller', 'type': 'bool', 'value': ''},
    '2': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'HintKey', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'Internal', 'type': 'bool', 'value': ''},
    '5': {'id': 'Keyboard', 'type': 'bool', 'value': ''},
    '6': {'id': 'WikiPage', 'type': 'LSString', 'value': ''},
}

TutorialInputEvents = {
    '1': {'id': 'InputEvent', 'type': '22', 'value': ''},
    '2': {'id': 'MapKey', 'type': '22', 'value': ''},
}

DialogVariables = {
    '1': {'id': 'DefaultValue', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Description', 'type': 'LSString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'name', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'type', 'type': 'LSString', 'value': ''},
}

ScriptFlags = {
    '1': {'id': 'Description', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Script', 'type': 'LSString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'name', 'type': 'FixedString', 'value': ''},
}

AnimationSetPriorities = {
    '1': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Priority', 'type': 'int32', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'ReferenceId', 'type': 'guid', 'value': ''},
}

_13a88c36_e4e1_484d_b031_b53ad6e79f21 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_13f608e6_61ea_46d5_946b_f2fd1e2fccfe = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_1bf9cd73_a064_4efe_b8a9_6bbaa6e1063c = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_1c934688_64ff_4917_81de_4b9e4d4818f9 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_3a087064_38e1_4e0a_9b3a_8cbac9fa289e = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_3f5d948f_8378_499a_baa2_51fd0aa6cb1a = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_4153b2f7_6830_412a_b121_dfcd05000903 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_53a1f46f_d675_486b_8b66_88274b9b1b1c = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_5c1383ac_4ac5_42f8_b538_0c4b498429a1 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_6246b38a_c2d8_4a2b_be2a_2f96fb1f4ac6 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_6a15d9a0_a98b_4219_aee8_589551e00e70 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_6b14fa73_5d92_4cf8_a3fd_eebc6c279d38 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_85636852_d0da_44f2_a1d6_ced79ad505fc = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_8a4a3a56_5463_4585_a8e1_aa01eeb5c709 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_952cdac8_a85c_4c50_baa9_f3d7d18d6666 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_95433d1e_c817_4b18_b110_7860b4022bf4 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

a28e8995_27a3_4e86_a99c_2d5597a0e1ec = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

a52602f6_61ec_413b_a6c3_991d2e451a13 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

a5bccc37_58be_4c3b_9087_7701c7a02acf = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

a7091f0a_dfb6_48a8_8a39_e1c7731eb4cd = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

a9ee4176_dd4f_4601_a209_fe799c9783a9 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

af4d899a_2d66_417c_b8ac_f08c795de3f1 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

bc5c0870_a336_47a0_a5fd_603e1597c601 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

bcfd1907_09e0_49c1_9de1_59f786d10c20 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

bfcf75eb_223f_468a_ac63_1d7bcfbf90a2 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

c2edcc1d_0d04_40e6_8d1d_248468e20425 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

c4bee4ce_6006_42ac_a92b_c19978d9f163 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

c9644ed9_830d_4234_abf2_8ca972f51240 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

d041432f_d3b5_4440_a5cb_0664dbebcdf2 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

d5a5fba6_94f4_405c_8e40_4e4297cf2d2d = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

dd7a4159_179a_4f95_9387_128a9fba3777 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

e917d542_64aa_4628_b11d_ed4fa46f6531 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

f0382315_4024_4392_bf62_d2ca1280e54b = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

f07c5c36_708e_4514_b486_65ea3bc49d9f = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

f9886c84_736f_466d_ac06_9f220722008c = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

f9c06dd6_4e80_46a7_ba05_c2744323357e = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

fe172e0f_58e2_4331_b3c0_ade9f15343bf = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

fe273bf5_0d66_4fa9_9d08_5954eedcbc20 = {
    '1': {'id': 'Scope', 'type': 'uint8', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

BackgroundGoals = {
    '1': {'id': 'BackgroundUUID', 'type': 'guid', 'value': ''},
    '2': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'ExperienceReward', 'type': 'guid', 'value': ''},
    '4': {'id': 'InspirationPoints', 'type': 'uint32', 'value': ''},
    '5': {'id': 'RewardLevel', 'type': 'uint32', 'value': ''},
    '6': {'id': 'Title', 'type': 'TranslatedString', 'value': ''},
    '7': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

CompanionPresets = {
    '1': {'id': 'BodyShape', 'type': 'uint8', 'value': ''},
    '2': {'id': 'BodyType', 'type': 'uint8', 'value': ''},
    '3': {'id': 'CloseUpA', 'type': 'LSString', 'value': ''},
    '4': {'id': 'CloseUpB', 'type': 'LSString', 'value': ''},
    '5': {'id': 'Overview', 'type': 'LSString', 'value': ''},
    '6': {'id': 'RaceUUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'RootTemplate', 'type': 'guid', 'value': ''},
    '8': {'id': 'SubRaceUUID', 'type': 'guid', 'value': ''},
    '9': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '10': {'id': 'VOLinesTableUUID', 'type': 'guid', 'value': ''},
    '11': {'id': 'VoiceTableUUID', 'type': 'guid', 'value': ''},
}

Factions = {
    '1': {'id': 'Faction', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'ParentGuid', 'type': 'guid', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Gossips = {
    '1': {'id': 'DialogUUID', 'type': 'guid', 'value': ''},
    '2': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'Priority', 'type': 'int32', 'value': ''},
    '4': {'id': 'Type', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

AreaLevelOverrides = {
    '1': {'id': 'EntityLevel', 'type': 'int32', 'value': ''},
    '2': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '3': {'id': 'ParentUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'TreasureLevel', 'type': 'int32', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

ExperienceRewards = {
    '1': {'id': 'Level1', 'type': 'uint32', 'value': ''},
    '2': {'id': 'Level10', 'type': 'uint32', 'value': ''},
    '3': {'id': 'Level2', 'type': 'uint32', 'value': ''},
    '4': {'id': 'Level3', 'type': 'uint32', 'value': ''},
    '5': {'id': 'Level4', 'type': 'uint32', 'value': ''},
    '6': {'id': 'Level5', 'type': 'uint32', 'value': ''},
    '7': {'id': 'Level6', 'type': 'uint32', 'value': ''},
    '8': {'id': 'Level7', 'type': 'uint32', 'value': ''},
    '9': {'id': 'Level8', 'type': 'uint32', 'value': ''},
    '10': {'id': 'Level9', 'type': 'uint32', 'value': ''},
    '11': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '12': {'id': 'RewardType', 'type': 'uint8', 'value': ''},
    '13': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '14': {'id': 'LevelSource', 'type': 'uint8', 'value': ''},
}

Origins = {
    '1': {'id': 'AppearanceLocked', 'type': 'bool', 'value': ''},
    '2': {'id': 'AvailableInCharacterCreation', 'type': 'uint8', 'value': ''},
    '3': {'id': 'BodyShape', 'type': 'uint8', 'value': ''},
    '4': {'id': 'BodyType', 'type': 'uint8', 'value': ''},
    '5': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '6': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '7': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '8': {'id': 'Passives', 'type': 'LSString', 'value': ''},
    '9': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '10': {'id': 'VoiceTableUUID', 'type': 'guid', 'value': ''},
}

ProgressionDescriptions = {
    '1': {'id': 'ExactMatch', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'Hidden', 'type': 'bool', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '5': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '6': {'id': 'Type', 'type': 'FixedString', 'value': ''},
    '7': {'id': 'PassivePrototype', 'type': 'FixedString', 'value': ''},
    '8': {'id': 'ParamMatch', 'type': 'FixedString', 'value': ''},
    '9': {'id': 'ProgressionId', 'type': 'guid', 'value': ''},
    '10': {'id': 'SelectorId', 'type': 'FixedString', 'value': ''},
    '11': {'id': 'ProgressionTableId', 'type': 'guid', 'value': ''},
}

Progressions = {
    '1': {'id': 'Boosts', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Level', 'type': 'uint8', 'value': ''},
    '3': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '4': {'id': 'PassivesAdded', 'type': 'LSString', 'value': ''},
    '5': {'id': 'ProgressionType', 'type': 'uint8', 'value': ''},
    '6': {'id': 'Selectors', 'type': 'LSString', 'value': ''},
    '7': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '8': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '9': {'id': 'AllowImprovement', 'type': 'bool', 'value': ''},
    '10': {'id': 'PassivesRemoved', 'type': 'LSString', 'value': ''},
}

ScriptMaterialOverrideParameters = {
    '1': {'id': 'ParameterName', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'ParameterType', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'ParameterValue', 'type': 'LSString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

ScriptMaterialOverridePresets = {
    '1': {'id': 'PresetName', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Rulebook = {
    '1': {'id': 'FootstepsType', 'type': 'bool', 'value': ''},
    '2': {'id': 'RuleName', 'type': 'LSString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'ApplyTagsFromTemplate', 'type': 'bool', 'value': ''},
    '5': {'id': 'ApplyVisual', 'type': 'bool', 'value': ''},
    '6': {'id': 'ChangeBodyType', 'type': 'bool', 'value': ''},
    '7': {'id': 'ChangeIcon', 'type': 'bool', 'value': ''},
    '8': {'id': 'ChangeRace', 'type': 'bool', 'value': ''},
    '9': {'id': 'IgnoreCustomLooks', 'type': 'bool', 'value': ''},
    '10': {'id': 'RemoveOldTags', 'type': 'bool', 'value': ''},
    '11': {'id': 'RetainDisplayName', 'type': 'bool', 'value': ''},
    '12': {'id': 'UseShapeshiftIdentity', 'type': 'bool', 'value': ''},
    '13': {'id': 'ApplySpellsFromTemplate', 'type': 'bool', 'value': ''},
    '14': {'id': 'ChangeAi', 'type': 'bool', 'value': ''},
    '15': {'id': 'DisableEquipmentSlots', 'type': 'bool', 'value': ''},
    '16': {'id': 'MuteEquipmentSound', 'type': 'bool', 'value': ''},
    '17': {'id': 'RemovePrevSpells', 'type': 'bool', 'value': ''},
    '18': {'id': 'UnarmedAbilityFromTemplate', 'type': 'bool', 'value': ''},
    '19': {'id': 'WildShapeHotBar', 'type': 'bool', 'value': ''},
    '20': {'id': 'BaseACOverride', 'type': 'bool', 'value': ''},
    '21': {'id': 'UseTemplateEquipmentSet', 'type': 'bool', 'value': ''},
    '22': {'id': 'KillEntityAtZeroHP', 'type': 'bool', 'value': ''},
    '23': {'id': 'ChangeScript', 'type': 'LSString', 'value': ''},
    '24': {'id': 'SpellsAdd', 'type': 'LSString', 'value': ''},
    '25': {'id': 'SpellsRemove', 'type': 'LSString', 'value': ''},
    '26': {'id': 'BlockLevelUp', 'type': 'bool', 'value': ''},
}

Crimes = {
    '1': {'id': 'Audible', 'type': 'uint8', 'value': ''},
    '2': {'id': 'AudibleRange', 'type': 'float', 'value': ''},
    '3': {'id': 'Continuous', 'type': 'uint8', 'value': ''},
    '4': {'id': 'CreatesCrimescene', 'type': 'uint8', 'value': ''},
    '5': {'id': 'CrimeType', 'type': 'LSString', 'value': ''},
    '6': {'id': 'DetectionRange', 'type': 'float', 'value': ''},
    '7': {'id': 'InterrogateDialog', 'type': 'LSString', 'value': ''},
    '8': {'id': 'Lifetime', 'type': 'float', 'value': ''},
    '9': {'id': 'MaxInvestigators', 'type': 'int32', 'value': ''},
    '10': {'id': 'TensionWeight', 'type': 'int32', 'value': ''},
    '11': {'id': 'Parent', 'type': 'FixedString', 'value': ''},
    '12': {'id': 'CanMergeConfrontation', 'type': 'uint8', 'value': ''},
    '13': {'id': 'MergeConditions', 'type': 'uint8', 'value': ''},
    '14': {'id': 'ContinuousDelayTimer', 'type': 'float', 'value': ''},
}

Voices = {
    '1': {'id': 'BodyType', 'type': 'uint8', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'SpeakerUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

EquipmentRaces = {
    '1': {'id': 'Name', 'type': '22', 'value': ''},
    '2': {'id': 'Guid', 'type': '31', 'value': ''},
    '3': {'id': 'CharacterVisual', 'type': '31', 'value': ''},
    '4': {'id': 'DefaultParent', 'type': '31', 'value': ''},
}

_029ff53f_e6fd_e27c_42f5_b12da4409435 = {
    '1': {'id': 'Object', 'type': 'guid', 'value': ''},
}

_2d8a968f_03f4_969d_ea0c_1b14a07001c6 = {
    '1': {'id': 'Object', 'type': 'guid', 'value': ''},
}

_69e20fca_d5f8_e307_940d_ee0e312d1240 = {
    '1': {'id': 'Object', 'type': 'guid', 'value': ''},
}

_816b0ade_18bf_4c4d_5d7b_c0798f1ce81e = {
    '1': {'id': 'Object', 'type': 'guid', 'value': ''},
}

_61ce9ba3_72f8_8f5b_21e5_54b59af5c8e9 = {
    '1': {'id': 'Object', 'type': 'guid', 'value': ''},
}

c93abaaf_7120_8279_c6e1_324b597410aa = {
    '1': {'id': 'Object', 'type': 'guid', 'value': ''},
}

ActionResourceDefinitions = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Error', 'type': 'TranslatedString', 'value': ''},
    '4': {'id': 'MaxLevel', 'type': 'uint32', 'value': ''},
    '5': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '6': {'id': 'ReplenishType', 'type': 'FixedString', 'value': ''},
    '7': {'id': 'ShowOnActionResourcePanel', 'type': 'bool', 'value': ''},
    '8': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '9': {'id': 'IsSpellResource', 'type': 'bool', 'value': ''},
    '10': {'id': 'UpdatesSpellPowerLevel', 'type': 'bool', 'value': ''},
    '11': {'id': 'DiceType', 'type': 'uint32', 'value': ''},
    '12': {'id': 'MaxValue', 'type': 'uint32', 'value': ''},
    '13': {'id': 'PartyActionResource', 'type': 'bool', 'value': ''},
    '14': {'id': 'IsHidden', 'type': 'bool', 'value': ''},
}

ActionResourceGroupDefinitions = {
    '1': {'id': 'ActionResourceDefinitions', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Backgrounds = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Passives', 'type': 'LSString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

DayRanges = {
    '1': {'id': 'DisplayCommonName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'End', 'type': 'uint32', 'value': ''},
    '4': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'Start', 'type': 'uint32', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'LeapYearEnd', 'type': 'uint32', 'value': ''},
    '8': {'id': 'LeapYearStart', 'type': 'uint32', 'value': ''},
}

CharacterCreationAccessorySets = {
    '1': {'id': 'CharacterCreationSet', 'type': 'bool', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'SlotName', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'RaceUUID', 'type': 'guid', 'value': ''},
}

CharacterCreationAppearanceMaterials = {
    '1': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'FemaleCameraName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'FemaleRootTemplate', 'type': 'guid', 'value': ''},
    '4': {'id': 'MaleCameraName', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'MaleRootTemplate', 'type': 'guid', 'value': ''},
    '6': {'id': 'MaterialPresetUUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'MaterialType', 'type': 'FixedString', 'value': ''},
    '8': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '9': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '10': {'id': 'DragonbornFemaleRootTemplate', 'type': 'guid', 'value': ''},
    '11': {'id': 'DragonbornMaleRootTemplate', 'type': 'guid', 'value': ''},
    '12': {'id': 'UIColor', 'type': 'LSString', 'value': ''},
}

CharacterCreationAppearanceVisuals = {
    '1': {'id': 'DefaultSkinColor', 'type': 'guid', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'RootTemplate', 'type': 'guid', 'value': ''},
    '4': {'id': 'SlotName', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '6': {'id': 'VisualResource', 'type': 'guid', 'value': ''},
    '7': {'id': 'BodyShape', 'type': 'uint8', 'value': ''},
    '8': {'id': 'BodyType', 'type': 'uint8', 'value': ''},
    '9': {'id': 'RaceUUID', 'type': 'guid', 'value': ''},
    '10': {'id': 'IconIdOverride', 'type': 'FixedString', 'value': ''},
}

CharacterCreationEquipmentIcons = {
    '1': {'id': 'EquipmentTemplate', 'type': 'guid', 'value': ''},
    '2': {'id': 'RootTemplate', 'type': 'guid', 'value': ''},
    '3': {'id': 'SlotName', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'MeshIsTwoSided', 'type': 'bool', 'value': ''},
    '6': {'id': 'AnimationUUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'IconGenerationTrigger', 'type': 'FixedString', 'value': ''},
}

CharacterCreationIconSettings = {
    '1': {'id': 'BodyShape', 'type': 'uint8', 'value': ''},
    '2': {'id': 'RootTemplate', 'type': 'guid', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'HeadAppearanceUUID', 'type': 'guid', 'value': ''},
}

CharacterCreationPassiveAppearances = {
    '1': {'id': 'Passive', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'RaceUUID', 'type': 'guid', 'value': ''},
}

CharacterCreationSharedVisuals = {
    '1': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'SlotName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'VisualResource', 'type': 'guid', 'value': ''},
    '5': {'id': 'BoneName', 'type': 'FixedString', 'value': ''},
}

CharacterCreationVOLines = {
    '1': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'VoiceLine', 'type': 'FixedString', 'value': ''},
}

VisualLocatorAttachments = {
    '1': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'LocatorName', 'type': 'FixedString', 'value': ''},
}

AbilityDistributionPresets = {
    '1': {'id': 'Charisma', 'type': 'int32', 'value': ''},
    '2': {'id': 'ClassUUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'Constitution', 'type': 'int32', 'value': ''},
    '4': {'id': 'Dexterity', 'type': 'int32', 'value': ''},
    '5': {'id': 'Intelligence', 'type': 'int32', 'value': ''},
    '6': {'id': 'Strength', 'type': 'int32', 'value': ''},
    '7': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '8': {'id': 'Wisdom', 'type': 'int32', 'value': ''},
}

CharacterCreationEyeColors = {
    '1': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'MaterialPresetUUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UIColor', 'type': 'LSString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

CharacterCreationHairColors = {
    '1': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'MaterialPresetUUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UIColor', 'type': 'LSString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

CharacterCreationPresets = {
    '1': {'id': 'BodyShape', 'type': 'uint8', 'value': ''},
    '2': {'id': 'BodyType', 'type': 'uint8', 'value': ''},
    '3': {'id': 'CloseUpA', 'type': 'LSString', 'value': ''},
    '4': {'id': 'CloseUpB', 'type': 'LSString', 'value': ''},
    '5': {'id': 'Overview', 'type': 'LSString', 'value': ''},
    '6': {'id': 'RaceUUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'RootTemplate', 'type': 'guid', 'value': ''},
    '8': {'id': 'SubRaceUUID', 'type': 'guid', 'value': ''},
    '9': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '10': {'id': 'VOLinesTableUUID', 'type': 'guid', 'value': ''},
}

CharacterCreationSkinColors = {
    '1': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'MaterialPresetUUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UIColor', 'type': 'LSString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

CinematicArenaFrequencyGroups = {
    '1': {'id': 'MaxFrequency', 'type': 'double', 'value': ''},
    '2': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'PercentageChance', 'type': 'int32', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

ClassDescriptions = {
    '1': {'id': 'BaseHp', 'type': 'int32', 'value': ''},
    '2': {'id': 'CharacterCreationPose', 'type': 'guid', 'value': ''},
    '3': {'id': 'ClassEquipment', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'ClassHotbarColumns', 'type': 'int32', 'value': ''},
    '5': {'id': 'CommonHotbarColumns', 'type': 'int32', 'value': ''},
    '6': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '7': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '8': {'id': 'HpPerLevel', 'type': 'int32', 'value': ''},
    '9': {'id': 'ItemsHotbarColumns', 'type': 'int32', 'value': ''},
    '10': {'id': 'LearningStrategy', 'type': 'uint8', 'value': ''},
    '11': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '12': {'id': 'PrimaryAbility', 'type': 'uint8', 'value': ''},
    '13': {'id': 'ProgressionTableUUID', 'type': 'guid', 'value': ''},
    '14': {'id': 'SoundClassType', 'type': 'FixedString', 'value': ''},
    '15': {'id': 'SpellCastingAbility', 'type': 'uint8', 'value': ''},
    '16': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '17': {'id': 'ParentGuid', 'type': 'guid', 'value': ''},
    '18': {'id': 'IsSomaticWithInstrument', 'type': 'bool', 'value': ''},
    '19': {'id': 'MulticlassSpellcasterModifier', 'type': 'double', 'value': ''},
    '20': {'id': 'SpellList', 'type': 'guid', 'value': ''},
    '21': {'id': 'HasGod', 'type': 'bool', 'value': ''},
    '22': {'id': 'MustPrepareSpells', 'type': 'bool', 'value': ''},
    '23': {'id': 'SubclassTitle', 'type': 'TranslatedString', 'value': ''},
    '24': {'id': 'ShortName', 'type': 'TranslatedString', 'value': ''},
    '25': {'id': 'CanLearnSpells', 'type': 'bool', 'value': ''},
    '26': {'id': 'IsDefaultForUseSpellAction', 'type': 'bool', 'value': ''},
}

CombatCameraGroups = {
    '1': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Abilities = {
    '1': {'id': 'Add', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Level', 'type': 'int32', 'value': ''},
    '3': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Equipments = {
    '1': {'id': 'Add', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Level', 'type': 'int32', 'value': ''},
    '3': {'id': 'SelectorId', 'type': 'LSString', 'value': ''},
    '4': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Passives = {
    '1': {'id': 'CastEffect', 'type': 'guid', 'value': ''},
    '2': {'id': 'PassiveName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'PrepareEffect', 'type': 'guid', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

PreparedSpells = {
    '1': {'id': 'Level', 'type': 'int32', 'value': ''},
    '2': {'id': 'Prepare', 'type': 'LSString', 'value': ''},
    '3': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'OriginUUID', 'type': 'guid', 'value': ''},
}

Skills = {
    '1': {'id': 'Add', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Level', 'type': 'int32', 'value': ''},
    '3': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'RaceUUID', 'type': 'guid', 'value': ''},
    '6': {'id': 'SelectorId', 'type': 'LSString', 'value': ''},
}

Spells = {
    '1': {'id': 'Add', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Level', 'type': 'int32', 'value': ''},
    '3': {'id': 'TableUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'SelectorId', 'type': 'LSString', 'value': ''},
    '6': {'id': 'OriginUUID', 'type': 'guid', 'value': ''},
}

DifficultyClasses = {
    '1': {'id': 'Difficulties', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

DisturbanceProperties = {
    '1': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Types = {
    '1': {'id': 'Status', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

EquipmentTypes = {
    '1': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '3': {'id': 'WeaponType_OneHanded', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'WeaponType_TwoHanded', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'BoneMainSheathed', 'type': 'FixedString', 'value': ''},
    '6': {'id': 'BoneMainUnsheathed', 'type': 'FixedString', 'value': ''},
    '7': {'id': 'BoneOffHandSheathed', 'type': 'FixedString', 'value': ''},
    '8': {'id': 'BoneOffHandUnsheathed', 'type': 'FixedString', 'value': ''},
    '9': {'id': 'SoundAttackType', 'type': 'FixedString', 'value': ''},
    '10': {'id': 'SoundEquipmentType', 'type': 'FixedString', 'value': ''},
    '11': {'id': 'BoneVersatileSheathed', 'type': 'FixedString', 'value': ''},
    '12': {'id': 'BoneVersatileUnsheathed', 'type': 'FixedString', 'value': ''},
    '13': {'id': 'SourceBoneAlternativeUnsheathed', 'type': 'FixedString', 'value': ''},
    '14': {'id': 'SourceBoneSheathed', 'type': 'FixedString', 'value': ''},
    '15': {'id': 'SourceBoneVersatileSheathed', 'type': 'FixedString', 'value': ''},
    '16': {'id': 'SourceBoneVersatileUnsheathed', 'type': 'FixedString', 'value': ''},
}

ConditionErrors = {
    '1': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'ErrorDescriptionType', 'type': 'uint8', 'value': ''},
    '3': {'id': 'Identifier', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'Hidden', 'type': 'bool', 'value': ''},
}

FeatDescriptions = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'ExactMatch', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'FeatId', 'type': 'guid', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

FixedHotBarSlots = {
    '1': {'id': 'HotBarController', 'type': 'uint8', 'value': ''},
    '2': {'id': 'HotBarType', 'type': 'uint8', 'value': ''},
    '3': {'id': 'SlotIndex', 'type': 'uint32', 'value': ''},
    '4': {'id': 'SpellId', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Gods = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Characters_Portraits = {
    '1': {'id': 'Height', 'type': 'int32', 'value': ''},
    '2': {'id': 'Width', 'type': 'int32', 'value': ''},
    '3': {'id': 'Path', 'type': 'string', 'value': ''},
    '4': {'id': 'UUID', 'type': 'FixedString', 'value': ''},
}

Creatures_Portraits = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

Icons_Items = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

Icons_Items_2 = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

Icons_Items_3 = {
    '1': {'id': 'Height', 'type': 'int32', 'value': ''},
    '2': {'id': 'Width', 'type': 'int32', 'value': ''},
    '3': {'id': 'Path', 'type': 'string', 'value': ''},
    '4': {'id': 'UUID', 'type': 'FixedString', 'value': ''},
}

Icons_Items_4 = {
    '1': {'id': 'Height', 'type': 'int32', 'value': ''},
    '2': {'id': 'Width', 'type': 'int32', 'value': ''},
    '3': {'id': 'Path', 'type': 'string', 'value': ''},
    '4': {'id': 'UUID', 'type': 'FixedString', 'value': ''},
}

Icons_Items_5 = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

Icons_Items_6 = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

Icons_Skills = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

New_EquipmentIcons = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

Player_Portraits = {
    '1': {'id': 'Height', 'type': 'int32', 'value': ''},
    '2': {'id': 'Width', 'type': 'int32', 'value': ''},
    '3': {'id': 'Path', 'type': 'string', 'value': ''},
    '4': {'id': 'UUID', 'type': 'FixedString', 'value': ''},
}

Portraits_Gustav = {
    '1': {'id': 'MapKey', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'U1', 'type': 'float', 'value': ''},
    '3': {'id': 'U2', 'type': 'float', 'value': ''},
    '4': {'id': 'V1', 'type': 'float', 'value': ''},
    '5': {'id': 'V2', 'type': 'float', 'value': ''},
}

ItemThrowParams = {
    '1': {'id': 'Conditions', 'type': 'LSString', 'value': ''},
    '2': {'id': 'MaxDistForOneRotation', 'type': 'int32', 'value': ''},
    '3': {'id': 'MaxDistForTwoRotations', 'type': 'int32', 'value': ''},
    '4': {'id': 'MaxDistForZeroRotations', 'type': 'int32', 'value': ''},
    '5': {'id': 'Priority', 'type': 'int32', 'value': ''},
    '6': {'id': 'RotationAxis', 'type': 'FixedString', 'value': ''},
    '7': {'id': 'StartAngleY', 'type': 'int32', 'value': ''},
    '8': {'id': 'StartAngleZ', 'type': 'int32', 'value': ''},
    '9': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

GoldValues = {
    '1': {'id': 'Level1', 'type': 'uint32', 'value': ''},
    '2': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'ParentScale', 'type': 'double', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'Level10', 'type': 'uint32', 'value': ''},
    '6': {'id': 'Level2', 'type': 'uint32', 'value': ''},
    '7': {'id': 'Level3', 'type': 'uint32', 'value': ''},
    '8': {'id': 'Level4', 'type': 'uint32', 'value': ''},
    '9': {'id': 'Level5', 'type': 'uint32', 'value': ''},
    '10': {'id': 'Level6', 'type': 'uint32', 'value': ''},
    '11': {'id': 'Level7', 'type': 'uint32', 'value': ''},
    '12': {'id': 'Level8', 'type': 'uint32', 'value': ''},
    '13': {'id': 'Level9', 'type': 'uint32', 'value': ''},
    '14': {'id': 'Level11', 'type': 'uint32', 'value': ''},
    '15': {'id': 'Level12', 'type': 'uint32', 'value': ''},
    '16': {'id': 'ParentUUID', 'type': 'guid', 'value': ''},
}

LevelMapValues = {
    '1': {'id': 'Level1', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Level10', 'type': 'LSString', 'value': ''},
    '3': {'id': 'Level2', 'type': 'LSString', 'value': ''},
    '4': {'id': 'Level3', 'type': 'LSString', 'value': ''},
    '5': {'id': 'Level4', 'type': 'LSString', 'value': ''},
    '6': {'id': 'Level5', 'type': 'LSString', 'value': ''},
    '7': {'id': 'Level6', 'type': 'LSString', 'value': ''},
    '8': {'id': 'Level7', 'type': 'LSString', 'value': ''},
    '9': {'id': 'Level8', 'type': 'LSString', 'value': ''},
    '10': {'id': 'Level9', 'type': 'LSString', 'value': ''},
    '11': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '12': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '13': {'id': 'PreferredClassUUID', 'type': 'guid', 'value': ''},
    '14': {'id': 'FallbackValue', 'type': 'LSString', 'value': ''},
}

LongRestCosts = {
    '1': {'id': 'CampGrowthDifficulty', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'CampQuality', 'type': 'int32', 'value': ''},
    '3': {'id': 'RequiredSupplies', 'type': 'int32', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

LimbsMapping = {
    '1': {'id': 'BackLeft', 'type': 'LSString', 'value': ''},
    '2': {'id': 'BackRight', 'type': 'LSString', 'value': ''},
    '3': {'id': 'FrontLeft', 'type': 'LSString', 'value': ''},
    '4': {'id': 'FrontRight', 'type': 'LSString', 'value': ''},
    '5': {'id': 'RootTemplate', 'type': 'guid', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

AbilityLists = {
    '1': {'id': 'Abilities', 'type': 'LSString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

CampChestTemplates = {
    '1': {'id': 'TemplateId', 'type': 'guid', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

ColorDefinitions = {
    '1': {'id': 'Color', 'type': 'LSString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

EquipmentLists = {
    '1': {'id': 'Items', 'type': 'LSString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

PassiveLists = {
    '1': {'id': 'Passives', 'type': 'LSString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

SkillLists = {
    '1': {'id': 'Skills', 'type': 'LSString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

SpellLists = {
    '1': {'id': 'Comment', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Spells', 'type': 'LSString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

_41de42e1_56d0_4336_8b44_99fc38281525 = {
    '1': {'id': 'BindSourceTo', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'BindTargetTo', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'DamageType', 'type': 'uint32', 'value': ''},
    '4': {'id': 'DetachSource', 'type': 'bool', 'value': ''},
    '5': {'id': 'DetachTarget', 'type': 'bool', 'value': ''},
    '6': {'id': 'EffectResourceGuid', 'type': 'guid', 'value': ''},
    '7': {'id': 'Enabled', 'type': 'bool', 'value': ''},
    '8': {'id': 'KeepRotation', 'type': 'bool', 'value': ''},
    '9': {'id': 'KeepScale', 'type': 'bool', 'value': ''},
    '10': {'id': 'MainHand', 'type': 'bool', 'value': ''},
    '11': {'id': 'MaxDistance', 'type': 'float', 'value': ''},
    '12': {'id': 'MinDistance', 'type': 'float', 'value': ''},
    '13': {'id': 'OffHand', 'type': 'bool', 'value': ''},
    '14': {'id': 'Pivot', 'type': 'FixedString', 'value': ''},
    '15': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '16': {'id': 'UseDistance', 'type': 'bool', 'value': ''},
    '17': {'id': 'UseOrientDirection', 'type': 'bool', 'value': ''},
    '18': {'id': 'UseScaleOverride', 'type': 'bool', 'value': ''},
    '19': {'id': 'VerbalIntent', 'type': 'uint32', 'value': ''},
}

ProjectileDefaults = {
    '1': {'id': 'ProjectileDefaultType', 'type': 'uint8', 'value': ''},
    '2': {'id': 'ProjectileTemplateId', 'type': 'guid', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Races = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'DisplayTypeUUID', 'type': 'guid', 'value': ''},
    '6': {'id': 'ParentGuid', 'type': 'guid', 'value': ''},
    '7': {'id': 'ProgressionTableUUID', 'type': 'guid', 'value': ''},
    '8': {'id': 'RaceEquipment', 'type': 'FixedString', 'value': ''},
    '9': {'id': 'RaceSoundSwitch', 'type': 'FixedString', 'value': ''},
}

Outcomes = {
    '1': {'id': 'GroupName', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'Level', 'type': 'uint32', 'value': ''},
    '3': {'id': 'Spell', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'ClassLevel', 'type': 'uint32', 'value': ''},
    '6': {'id': 'ClassUUID', 'type': 'guid', 'value': ''},
}

RulesetModifierOptions = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Modifier', 'type': 'guid', 'value': ''},
    '4': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '6': {'id': 'Value', 'type': 'LSString', 'value': ''},
}

RulesetModifiers = {
    '1': {'id': 'Default', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '4': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '5': {'id': 'RulesetModifierType', 'type': 'uint8', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'Max', 'type': 'float', 'value': ''},
    '8': {'id': 'Min', 'type': 'float', 'value': ''},
    '9': {'id': 'Step', 'type': 'float', 'value': ''},
}

Rulesets = {
    '1': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '4': {'id': 'Type', 'type': 'uint8', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

RulesetSelectionPresets = {
    '1': {'id': 'Asset', 'type': 'LSString', 'value': ''},
    '2': {'id': 'Description', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'DisplayName', 'type': 'TranslatedString', 'value': ''},
    '4': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '5': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

RulesetValues = {
    '1': {'id': 'Modifier', 'type': 'guid', 'value': ''},
    '2': {'id': 'Ruleset', 'type': 'guid', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'Value', 'type': 'LSString', 'value': ''},
}

FlagSoundStates = {
    '1': {'id': 'DefaultSwitch', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'FlagName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'FlagUUID', 'type': 'guid', 'value': ''},
    '4': {'id': 'OverrideSwitch', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'OverrideSwitchGroup', 'type': 'FixedString', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

TagSoundStates = {
    '1': {'id': 'DefaultSwitch', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'OverrideSwitch', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'OverrideSwitchGroup', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'TagName', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'TagUUID', 'type': 'guid', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

MetaConditions = {
    '1': {'id': 'AdditionalConditions', 'type': 'LSString', 'value': ''},
    '2': {'id': 'ConditionType', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'Filter', 'type': 'LSString', 'value': ''},
    '4': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '5': {'id': 'OverrideOriginalCondition', 'type': 'bool', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

StatusSoundStates = {
    '1': {'id': 'CombatVocalOverrideSwitch', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'SoundStateName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'SpellOverrideSwitchClearState', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'SpellOverrideSwitchGroup', 'type': 'FixedString', 'value': ''},
    '5': {'id': 'SpellOverrideSwitchState', 'type': 'FixedString', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '7': {'id': 'BlockVocals', 'type': 'bool', 'value': ''},
}

bnz_standing_Px1_EALaunch = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px1_EA_Goblin = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px1_EA_Hyena = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px2_EALaunch = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px2_EA_Goblin = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px3_EALaunch = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px3_Shipping_GroupDiscussion = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

bnz_standing_Px4_EALaunch = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_Px1_crimeFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_Px1_goblinFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_Px1_ogreFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_Px1_ratFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_Px2_goblinFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

default_PxRD_final = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

SwD_Default = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_CURSED = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_DARK = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_FLD = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_FLD_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_GREEN = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_GREEN_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_LAVA = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_LAVA_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_LIGHT = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_LIGHT_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_MGC = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_MIND = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_NTRL = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_NTRL_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_SHAR = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_SHAR_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_UND = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_UND_Px1_mediumAnimalFinal = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_DGN_VALIDATE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_BRAIN = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_CURSED = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_DWN = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NIGHT = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_CAVE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_CRASH = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_FIRE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_FOREST = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_OCST = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_OCSTEVIL = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_OCSTEVILHOUSE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_OCSTGOB = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_SWAMP = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_SWAMPHOUSE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_VALIDATE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_NOON_WYRM = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_PLANE = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_EXT_SUNST = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_TUT = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

_Base_TUT_EXT = {
    '1': {'id': 'Object', 'type': 'FixedString', 'value': ''},
}

TooltipExtraTexts = {
    '1': {'id': 'Text', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

TooltipUpcastDescriptions = {
    '1': {'id': 'Name', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'Text', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

Jump = {
    '1': {'id': 'HeightMax', 'type': 'float', 'value': ''},
    '2': {'id': 'HeightMin', 'type': 'float', 'value': ''},
    '3': {'id': 'LengthMax', 'type': 'float', 'value': ''},
    '4': {'id': 'LengthMin', 'type': 'float', 'value': ''},
    '5': {'id': 'Priority', 'type': 'int32', 'value': ''},
    '6': {'id': 'Template', 'type': 'FixedString', 'value': ''},
    '7': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

SpellSoundTrajectoryRules = {
    '1': {'id': 'CurveUUID', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'DistancePastListener', 'type': 'float', 'value': ''},
    '3': {'id': 'RuleName', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

ModalTutorials = {
    '1': {'id': 'ControllerDescription', 'type': 'TranslatedString', 'value': ''},
    '2': {'id': 'DisplayTitle', 'type': 'TranslatedString', 'value': ''},
    '3': {'id': 'KeyboardDescription', 'type': 'TranslatedString', 'value': ''},
    '4': {'id': 'ModalType', 'type': 'uint8', 'value': ''},
    '5': {'id': 'Section', 'type': 'uint8', 'value': ''},
    '6': {'id': 'TutorialID', 'type': 'int32', 'value': ''},
    '7': {'id': 'TutorialName', 'type': 'FixedString', 'value': ''},
    '8': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '9': {'id': 'WaitForEndDialog', 'type': 'bool', 'value': ''},
}

TutorialEvents = {
    '1': {'id': 'ActionResource', 'type': 'guid', 'value': ''},
    '2': {'id': 'EventType', 'type': 'uint8', 'value': ''},
    '3': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '5': {'id': 'UserAction', 'type': 'uint8', 'value': ''},
}

DeathEffects = {
    '1': {'id': 'Acid', 'type': 'guid', 'value': ''},
    '2': {'id': 'Chasm', 'type': 'guid', 'value': ''},
    '3': {'id': 'CinematicDeath', 'type': 'guid', 'value': ''},
    '4': {'id': 'Cold', 'type': 'guid', 'value': ''},
    '5': {'id': 'Disintegrate', 'type': 'guid', 'value': ''},
    '6': {'id': 'DoT', 'type': 'guid', 'value': ''},
    '7': {'id': 'Electrocution', 'type': 'guid', 'value': ''},
    '8': {'id': 'Explode', 'type': 'guid', 'value': ''},
    '9': {'id': 'Fallback', 'type': 'guid', 'value': ''},
    '10': {'id': 'Falling', 'type': 'guid', 'value': ''},
    '11': {'id': 'Incinerate', 'type': 'guid', 'value': ''},
    '12': {'id': 'KnockedDown', 'type': 'guid', 'value': ''},
    '13': {'id': 'Lifetime', 'type': 'guid', 'value': ''},
    '14': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '15': {'id': 'Necrotic', 'type': 'guid', 'value': ''},
    '16': {'id': 'Physical', 'type': 'guid', 'value': ''},
    '17': {'id': 'Psychic', 'type': 'guid', 'value': ''},
    '18': {'id': 'Radiant', 'type': 'guid', 'value': ''},
    '19': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

ManagedStatusVFX = {
    '1': {'id': 'Group', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'MixedEffect', 'type': 'guid', 'value': ''},
    '3': {'id': 'Name', 'type': 'LSString', 'value': ''},
    '4': {'id': 'NegativeEffect', 'type': 'guid', 'value': ''},
    '5': {'id': 'PositiveEffect', 'type': 'guid', 'value': ''},
    '6': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

VFX = {
    '1': {'id': 'UUID', 'type': 'guid', 'value': ''},
    '2': {'id': 'VFXEffectName', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'VFXGameplayName', 'type': 'FixedString', 'value': ''},
}

WeaponAnimationSetData = {
    '1': {'id': 'AnimationSetUUID', 'type': 'FixedString', 'value': ''},
    '2': {'id': 'MainHand', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'OffHand', 'type': 'FixedString', 'value': ''},
    '4': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

WeightCategories = {
    '1': {'id': 'MaxWeight', 'type': 'int32', 'value': ''},
    '2': {'id': 'ObjectSize', 'type': 'FixedString', 'value': ''},
    '3': {'id': 'UUID', 'type': 'guid', 'value': ''},
}

