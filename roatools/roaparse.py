import enum
import os


class ActionType(enum.Enum):

    INVALID = -1

    LEFT_PRESS = 0
    LEFT_RELEASE = 1
    LEFT_TAP = 2

    RIGHT_PRESS = 3
    RIGHT_RELEASE = 4
    RIGHT_TAP = 5

    UP_PRESS = 6
    UP_RELEASE = 7
    UP_TAP = 8

    DOWN_PRESS = 9
    DOWN_RELEASE = 10
    DOWN_TAP = 11

    ATTACK_PRESS = 12
    ATTACK_RELEASE = 13

    SPECIAL_PRESS = 14
    SPECIAL_RELEASE = 15

    JUMP_PRESS = 16
    JUMP_RELEASE = 17

    DODGE_PRESS = 18
    DODGE_RELEASE = 19

    STRONG_PRESS = 20
    STRONG_RELEASE = 21

    STRONG_LEFT_PRESS = 22
    STRONG_LEFT_RELEASE = 23

    STRONG_RIGHT_PRESS = 24
    STRONG_RIGHT_RELEASE = 25

    STRONG_UP_PRESS = 26
    STRONG_UP_RELEASE = 27

    STRONG_DOWN_PRESS = 28
    STRONG_DOWN_RELEASE = 29

    ANG_RIGHT = 30
    ANG_UP_RIGHT = 31
    ANG_UP = 32
    ANG_UP_LEFT = 33
    ANG_LEFT = 34
    ANG_DOWN_LEFT = 35
    ANG_DOWN = 36
    ANG_DOWN_RIGHT = 37

    ANG_TOGGLE_PRESS = 38
    ANG_TOGGLE_RELEASE = 39

    @staticmethod
    def get_action(action_character):
        return{
            'L': ActionType.LEFT_PRESS,
            'l': ActionType.LEFT_RELEASE,
            'E': ActionType.LEFT_TAP,
            'R': ActionType.RIGHT_PRESS,
            'r': ActionType.RIGHT_RELEASE,
            'I': ActionType.RIGHT_TAP,
            'U': ActionType.UP_PRESS,
            'u': ActionType.UP_RELEASE,
            'M': ActionType.UP_TAP,
            'D': ActionType.DOWN_PRESS,
            'd': ActionType.DOWN_RELEASE,
            'O': ActionType.DOWN_TAP,
            'A': ActionType.ATTACK_PRESS,
            'a': ActionType.ATTACK_RELEASE,
            'B': ActionType.SPECIAL_PRESS,
            'b': ActionType.SPECIAL_RELEASE,
            'J': ActionType.JUMP_PRESS,
            'j': ActionType.JUMP_RELEASE,
            'S': ActionType.DODGE_PRESS,
            's': ActionType.DODGE_RELEASE,
            'C': ActionType.STRONG_PRESS,
            'c': ActionType.STRONG_RELEASE,
            'F': ActionType.STRONG_LEFT_PRESS,
            'f': ActionType.STRONG_LEFT_RELEASE,
            'G': ActionType.STRONG_RIGHT_PRESS,
            'g': ActionType.STRONG_RIGHT_RELEASE,
            'X': ActionType.STRONG_UP_PRESS,
            'x': ActionType.STRONG_UP_RELEASE,
            'W': ActionType.STRONG_DOWN_PRESS,
            'w': ActionType.STRONG_DOWN_RELEASE,
            0: ActionType.ANG_RIGHT,
            45: ActionType.ANG_UP_RIGHT,
            90: ActionType.ANG_UP,
            135: ActionType.ANG_UP_LEFT,
            180: ActionType.ANG_LEFT,
            225: ActionType.ANG_DOWN_LEFT,
            270: ActionType.ANG_DOWN,
            315: ActionType.ANG_DOWN_RIGHT,
            'Z': ActionType.ANG_TOGGLE_PRESS,
            'z': ActionType.ANG_TOGGLE_RELEASE
        }.get(action_character, ActionType.INVALID)


class SimpleAction(enum.Enum):
    INVALID = -1

    LEFT = 0
    LEFT_TAP = 1

    RIGHT = 2
    RIGHT_TAP = 3

    UP = 4
    UP_TAP = 5

    DOWN = 6
    DOWN_TAP = 7

    ATTACK = 8
    SPECIAL = 9
    JUMP = 10
    DODGE = 11
    STRONG = 12

    STRONG_LEFT = 13
    STRONG_RIGHT = 14
    STRONG_UP = 15
    STRONG_DOWN = 16

    ANG_RIGHT = 17
    ANG_UP_RIGHT = 18
    ANG_UP = 19
    ANG_UP_LEFT = 20
    ANG_LEFT = 21
    ANG_DOWN_LEFT = 22
    ANG_DOWN = 23
    ANG_DOWN_RIGHT = 24

    ANG_TOGGLE = 25

    @staticmethod
    def cast_action(action):
        return{
            ActionType.LEFT_PRESS: SimpleAction.LEFT,
            ActionType.LEFT_RELEASE: SimpleAction.LEFT,
            ActionType.LEFT_TAP: SimpleAction.LEFT_TAP,
            ActionType.RIGHT_PRESS: SimpleAction.RIGHT,
            ActionType.RIGHT_RELEASE: SimpleAction.RIGHT,
            ActionType.RIGHT_TAP: SimpleAction.RIGHT_TAP,
            ActionType.UP_PRESS: SimpleAction.UP,
            ActionType.UP_RELEASE: SimpleAction.UP,
            ActionType.UP_TAP: SimpleAction.UP_TAP,
            ActionType.DOWN_PRESS: SimpleAction.DOWN,
            ActionType.DOWN_RELEASE: SimpleAction.DOWN,
            ActionType.DOWN_TAP: SimpleAction.DOWN_TAP,
            ActionType.ATTACK_PRESS: SimpleAction.ATTACK,
            ActionType.ATTACK_RELEASE: SimpleAction.ATTACK,
            ActionType.SPECIAL_PRESS: SimpleAction.SPECIAL,
            ActionType.SPECIAL_RELEASE: SimpleAction.SPECIAL,
            ActionType.JUMP_PRESS: SimpleAction.JUMP,
            ActionType.JUMP_RELEASE: SimpleAction.JUMP,
            ActionType.DODGE_PRESS: SimpleAction.DODGE,
            ActionType.DODGE_RELEASE: SimpleAction.DODGE,
            ActionType.STRONG_PRESS: SimpleAction.STRONG,
            ActionType.STRONG_RELEASE: SimpleAction.STRONG,
            ActionType.STRONG_LEFT_PRESS: SimpleAction.STRONG_LEFT,
            ActionType.STRONG_LEFT_RELEASE: SimpleAction.STRONG_LEFT,
            ActionType.STRONG_RIGHT_PRESS: SimpleAction.STRONG_RIGHT,
            ActionType.STRONG_RIGHT_RELEASE: SimpleAction.STRONG_RIGHT,
            ActionType.STRONG_UP_PRESS: SimpleAction.STRONG_UP,
            ActionType.STRONG_UP_RELEASE: SimpleAction.STRONG_UP,
            ActionType.STRONG_DOWN_PRESS: SimpleAction.STRONG_DOWN,
            ActionType.STRONG_DOWN_RELEASE: SimpleAction.STRONG_DOWN,
            ActionType.ANG_RIGHT: SimpleAction.ANG_RIGHT,
            ActionType.ANG_UP_RIGHT: SimpleAction.ANG_UP_RIGHT,
            ActionType.ANG_UP: SimpleAction.ANG_UP,
            ActionType.ANG_UP_LEFT: SimpleAction.ANG_UP_LEFT,
            ActionType.ANG_LEFT: SimpleAction.ANG_LEFT,
            ActionType.ANG_DOWN_LEFT: SimpleAction.ANG_DOWN_LEFT,
            ActionType.ANG_DOWN: SimpleAction.ANG_DOWN,
            ActionType.ANG_DOWN_RIGHT: SimpleAction.ANG_DOWN_RIGHT,
            ActionType.ANG_TOGGLE_PRESS: SimpleAction.ANG_TOGGLE,
            ActionType.ANG_TOGGLE_RELEASE: SimpleAction.ANG_TOGGLE
        }.get(action, SimpleAction.INVALID)

    @staticmethod
    def generate_matrix(action):
        base = numpy.zeros(26)
        if action is not SimpleAction.INVALID:
            base[action] = 1
        return base


class StageType(enum.Enum):
    INVALID = -1
    BASIC = 0
    AETHER = 1

    @staticmethod
    def get_stage_type(type_str):
        conv = int(type_str)
        if conv >= 0 and conv < 2:
            return StageType(conv)

        return StageType.INVALID


class Stage(enum.Enum):
    INVALID = -1
    NOTHING = 0
    TREETOP_LODGE = 1
    FIRE_CAPITOL = 2
    AIR_ARMADA = 3
    ROCK_WALL = 4
    MERCHANT_PORT = 5
    CRASH_GAME = 6
    BLAZING_HIDEOUT = 7
    TOWER_HEAVEN = 8
    TEMPEST_PEAK = 9
    FROZEN_FORTRESS = 10
    AETHERIAL_GATES = 11
    ENDLESS_ABYSS = 12
    UNAVAILABLE = 13
    CEO_RING = 14
    SPIRIT_TREE = 15
    STAGE_NAME = 16
    NEO_FIRE_CAPITAL = 17
    SWAMPY_ESTUARY = 18

    @staticmethod
    def get_stage(stage_str):
        conv = int(stage_str)
        if conv >= 0 and conv < 19:
            return Stage(conv)

        return Stage.INVALID


class Character(enum.Enum):
    INVALID = -1
    NONE = 0
    ERROR = 1
    ZETTERBURN = 2
    ORCANE = 3
    WRASTOR = 4
    KRAGG = 5
    FORSBURN = 6
    MAYPUL = 7
    ABSA = 8
    ETALUS = 9
    ORI = 10
    RANNO = 11
    CLAIREN = 12

    @staticmethod
    def get_character(char_str):
        conv = int(char_str)
        if conv >= 0 and conv < 13:
            return Character(conv)

        return Character.INVALID


class Replay:
    def __init__(self, roa_apath):

        if not roa_apath.endswith('.roa'):
            return

        self.f_name = os.path.basename(roa_apath)[:-4]


class MetaData:
    def __init__(self, meta_line):
        self.is_starred = bool(int(meta_line[0]))
        self.version = meta_line[1:8]
        self.date_time = meta_line[8:21]

    def format_meta_str(self):
        return str(self.is_starred) + "\t" + \
            self.version + "\t" + \
            self.date_time + "\n"


class RuleData:
    def __init__(self, rule_line):
        self.stage_type = StageType.get_stage_type(rule_line[0])
        self.stage_id = Stage.get_stage(rule_line[1:3])
        self.stock_count = rule_line[3:5]
        self.time = rule_line[5:7]
        self.team = bool(int(rule_line[7]))
        self.friendly_fire = bool(int(rule_line[8]))

    def format_rule_str(self):
        return str(self.stage_type) + "\t" + \
            str(self.stage_id) + "\t" + \
            str(self.stock_count) + "\t" + \
            str(self.time) + "\t" + \
            str(self.team) + "\t" + \
            str(self.friendly_fire) + "\n"


class Player:
    def __init__(self, ln_info, ln_actions):
        self.name = ln_info[1:33].rstrip()
        self.character = Character.get_character(ln_info[39:41])


class Action:
    def __init__(self, frame_index, action_str):
        self.fame_index = int(frame_index)
        self.action = ActionType.get_action(action_str)
        self.simple_action = SimpleAction.cast_action(self.action)
        self.matrix = SimpleAction.generate_matrix(self.simple_action)
