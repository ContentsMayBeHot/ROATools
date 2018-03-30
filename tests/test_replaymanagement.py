from test_common import roa
from roa import Replay

import pytest
import os

@pytest.fixture
def samples_path():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'samples')

@pytest.fixture
def replay_path(samples_path):
    return os.path.join(samples_path, '2017-10-21-214825120337.roa')

@pytest.fixture
def replay(replay_path):
    return Replay(replay_path)

def test_replay_init(replay_path):
    replay = Replay(replay_path)
    assert replay.path == replay_path
    assert replay.id == '2017-10-21-214825120337'
    assert replay.fname == '2017-10-21-214825120337.roa'
    assert replay.dname == 'samples'

def test_replay_init_exception():
    with pytest.raises(TypeError):
        replay = Replay()

def test_replay_get_version(replay):
    assert replay.get_version() == '01_02_01'

def test_replay_get_version_pretty(replay):
    assert replay.get_version(pretty=True) == '1.2.1'