import os

class ReplayFile:
    '''Interface for a replay file'''
    def __init__(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError
        self.path = path
        self.fname = os.path.basename(path)
        self.id = os.path.splitext(self.fname)[0]
        self.dname = os.path.basename(os.path.dirname(path))

    def get_version(self, pretty=False):
        with open(self.path, 'r') as fin:
            ln = fin.readline()
            x = str(ln[1:3])
            y = str(ln[3:5])
            z = str(ln[5:7])
            version = '{}_{}_{}'.format(x, y, z)
            if pretty:
                version = '.'.join([
                    str(int(ch)) for ch in version.split('_') if ch.isdigit()
                    ])
            return version
        return None


class ReplayFolder:
    '''Interface for the folder where the game stores replay files'''
    def __init__(self, path):
        if not os.path.isdir(path):
            raise FileNotFoundError
        self.__path = path
        self.__replays = [
            ReplayFile(os.path.join(self.__path, dirent))
            for dirent in os.listdir(self.__path) if dirent.endswith('.roa')
        ]
        self.__replays_by_version = {}
        for replay in self.__replays:
            v = replay.get_version()
            if not v:
                continue
            if not self.__replays_by_version.get(v):
                self.__replays_by_version[v] = []
            self.__replays_by_version[v].append(replay)

    def get_available_versions(self):
        return list(self.__replays_by_version.keys())

    def get_replays_by_version(self, version):
        return self.__replays_by_version.get(version)


class ReplayManager:
    def __init__(self, replays_folder_path, version):
        if not os.path.isdir(replays_folder_path):
            raise FileNotFoundError
        self.__replay_folder = ReplayFolder(replays_folder_path)
        self.__replays = self.__replay_folder.get_replays_by_version(version)
        self.__datastore = ROADatastore(replays_folder_path)

    def get_all_unvisited(self):
        return (
            replay for replay in self.__replays
            if not self.__datastore.is_captured(replay)
            )

    def move_replay_to_replays_folder(self, replay):
        pass

class ROADatastore:
    '''Interface for a directory structure containing raw frames and replays'''
    def __init__(self, path):
        if not os.path.isdir(path):
            raise FileNotFoundError
        self.path = path
        self.frames_path = os.path.join(path, 'frames')
        self.labels_path = os.path.join(path, 'labels')

    def is_captured(self, replay):
        return os.path.isdir(os.path.join(self.frames_path, replay.id))

    def add_captured(self, replay):
        pass

    def cull_low_contrast(self):
        pass
