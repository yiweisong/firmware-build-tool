from typing import List,Generic

class YMLElement:
    pass

class General(YMLElement):
    config_version: str = ''
    platform: str = ''

    def __init__(self):
        self.config_version = ''
        self.platform = ''

class RomConfiguration(YMLElement):
    file: str = ''
    name: str = ''
    begin_address: int = 0
    bootloader: bool = False

    def __init__(self):
        self.file = ''
        self.name = ''
        self.begin_address = 0
        self.bootloader = False

class RomWrapper(YMLElement):
    rom: RomConfiguration = RomConfiguration()

    def __init__(self):
        self.rom = RomConfiguration()

class RomList(list,YMLElement):
    item_type = RomWrapper

    def __init__(self):
        super(RomList,self).__init__()

class Region(YMLElement):
    address_type: str = ''
    rom_list: RomList = RomList()

    def __init__(self):
        self.address_type = ''
        self.rom_list = RomList()

class ConfigurationContext(YMLElement):
    general: General = General()
    main_region: Region = Region()

    def __init__(self):
        self.general = General()
        self.main_region = Region()
