from roatools import ActionType, SimpleAction, StageType, Stage, StageType
from roatools import Character, Replay, MetaData, RuleData, Player, Action

import pytest


class TestActionEnums:

    def test_comp_init(self):
        act = ActionType(17)
        assert act is ActionType.JUMP_RELEASE

    def test_simp_init(self):
        act = SimpleAction(10)
        assert act is SimpleAction.JUMP

    def test_get_action(self):
        act = ActionType.get_action('j')
        assert act is ActionType.JUMP_RELEASE

    def test_get_action_OOB(self):
        act = ActionType.get_action('[')
        assert act is ActionType.INVALID

    def test_cast_action(self):
        act = ActionType.JUMP_PRESS
        simp = SimpleAction.cast_action(act)
        assert simp is SimpleAction.JUMP


class TestStageEnums:
    def test_stage_init(self):
        stage = Stage(3)
        assert stage is Stage.AIR_ARMADA

    def test_type_init(self):
        stage_type = StageType(0)
        assert stage_type is StageType.BASIC

    def test_get_stage(self):
        stage = Stage.get_stage('3')
        assert stage is Stage.AIR_ARMADA

    def test_get_stage_OOB(self):
        stage = Stage.get_stage('8989348')
        assert stage is Stage.INVALID

    def test_get_stage_type(self):
        stage_type = StageType.get_stage_type('1')
        assert stage_type is StageType.AETHER

    def test_get_stage_type_OOB(self):
        stage_type = StageType.get_stage_type('8989348')
        assert stage_type is StageType.INVALID


class TestCharacterEnum:
    def test_char_init(self):
        char = Character(3)
        assert char is Character.ORCANE

    def test_get_character(self):
        char = Character.get_character('03')
        assert char is Character.ORCANE

    def test_get_character_OOB(self):
        char = Character.get_character('328493479')
        assert char is Character.INVALID


@pytest.fixture
def replay_obj():
    return Replay("../samples/2017-10-21-214825120337.roa")


class TestReplayBase:
    def test_replay_init(self):
        Replay("../samples/2017-10-21-214825120337.roa")

    def test_replay_name(self):
        assert replay_obj().f_name == "2017-10-21-214825120337"
