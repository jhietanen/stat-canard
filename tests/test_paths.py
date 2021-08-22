import unittest
from src import settings


class SettingsTestCase(unittest.TestCase):

    def setUp(self):
        self.project_dir = settings.PROJECT_DIR
        self.subdirs_dict = settings.SUB_DIRS
        self.data_paths = settings.DATA_PATHS
        self.report_paths = settings.REPORT_PATHS
        self.references_paths = settings.REFERENCES_PATHS

    def test_subdirectories(self):
        # Test that all configured subdirectories exist
        subdirectories = [x for x in self.project_dir.iterdir() if x.is_dir()]
        for i in list(self.subdirs_dict.values()):
            self.assertIn(i, subdirectories)

    def test_datapaths(self):
        # Test that all data paths are configured in settings
        data_subdirs = [x for x in self.subdirs_dict['DATA'].iterdir() if x.is_dir()]
        self.assertCountEqual(data_subdirs, list(self.data_paths.values()))

    def test_reportpaths(self):
        # Test that all report paths are configured in settings
        report_subdirs = [x for x in self.subdirs_dict['REPORTS'].iterdir() if x.is_dir()]
        self.assertCountEqual(report_subdirs, list(self.report_paths.values()))

    def test_referencepaths(self):
        # Test that all references paths are configured in settings
        references_subdirs = [x for x in self.subdirs_dict['REFERENCES'].iterdir() if x.is_dir()]
        self.assertCountEqual(references_subdirs, list(self.references_paths.values()))


if __name__ == '__main__':
    unittest.main()
