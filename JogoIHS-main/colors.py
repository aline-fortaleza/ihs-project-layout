class Colors:
    dark_grey=(26,31,40)
    green=(47,230,23)
    red=(232,18,18)
    yellow=(237,234,4)
    purple=(178,102,255)
    cyan=(21,204,209)
    blue=(13,64,216)
    dark_blue = (44,44,127)
    white = (255, 255, 255)
    light_blue = (59, 85, 162)
    pink =(153,0,153)
    light_purple =(51,0,102)
    orange=(255,128,0)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey,cls.green,cls.red,cls.orange,cls.yellow,cls.purple,cls.cyan,cls.blue]
