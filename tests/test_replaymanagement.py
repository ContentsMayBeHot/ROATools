from test_common import roatools
from roatools import ReplayFile, ReplayFolder, ReplayManager, ROADatastore

import pytest
import os

@pytest.fixture
def samples_path():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'samples')

@pytest.fixture
def samples_01_02_01():
    return [
        '2017-10-21-214825120337.roa', '2017-10-21-215302397203.roa',
        '2017-10-21-215752688136.roa', '2017-10-21-215929784285.roa',
        '2017-10-21-220031846478.roa', '2017-10-21-220201936686.roa',
        '2017-10-21-220325020940.roa', '2017-10-21-220442097729.roa',
        '2017-10-21-220540155252.roa', '2017-10-21-220710245259.roa',
        '2017-10-21-220912367715.roa']

@pytest.fixture
def replay_path(samples_path):
    return os.path.join(samples_path, '2017-10-21-214825120337.roa')

@pytest.fixture
def replay(replay_path):
    return ReplayFile(replay_path)

@pytest.fixture
def replay_folder(samples_path):
    return ReplayFolder(samples_path)

@pytest.fixture
def replay_manager(samples_path):
    return ReplayManager(samples_path, '01_02_01')

@pytest.fixture
def datastore(samples_path):
    return ROADatastore(samples_path)

class TestReplayFile:
    def test_init(self, replay_path):
        ReplayFile(replay_path)

    def test_init_exception(self):
        with pytest.raises(FileNotFoundError):
            ReplayFile('')

    def test_attributes(self, replay, replay_path):
        assert replay.path == replay_path
        assert replay.id == '2017-10-21-214825120337'
        assert replay.fname == '2017-10-21-214825120337.roa'
        assert replay.dname == 'samples'

    def test_get_version(self, replay):
        assert replay.get_version() == '01_02_01'

    def test_get_version_pretty(self, replay):
        assert replay.get_version(pretty=True) == '1.2.1'

class TestReplayFolder():
    def test_init(self, samples_path):
        ReplayFolder(samples_path)

    def test_init_exception(self):
        with pytest.raises(FileNotFoundError):
            ReplayFolder('')

    def test_get_available_versions(self, replay_folder):
        expected = ['01_02_01']
        assert replay_folder.get_available_versions() == expected

    def test_get_replays_by_version(self, replay_folder, samples_01_02_01):
        assert replay_folder.get_replays_by_version('01_02_01')

    def test_get_replays_by_nonexistent_version(self, replay_folder):
        assert replay_folder.get_replays_by_version('') == None

class TestReplayManager():
    def test_init(self, samples_path):
        ReplayManager(samples_path, '01_02_01')

    def test_init_exception(self):
        with pytest.raises(FileNotFoundError):
            ReplayManager('', '01_02_01')

    def test_get_all_unvisited(self, replay_manager, samples_01_02_01):
        assert len(samples_01_02_01) == 11
        for replay in replay_manager.get_all_unvisited():
            assert replay.fname in samples_01_02_01
            samples_01_02_01.remove(replay.fname)
        assert samples_01_02_01 == []

class TestROADatastore:
    def test_init(self, samples_path):
        ROADatastore(samples_path)

    def test_init_exception(self):
        with pytest.raises(FileNotFoundError):
            ROADatastore('')

    def test_attributes(self, samples_path, datastore):
        assert datastore.path == samples_path
        assert datastore.frames_path == os.path.join(samples_path, 'frames')
        assert datastore.labels_path == os.path.join(samples_path, 'labels')
