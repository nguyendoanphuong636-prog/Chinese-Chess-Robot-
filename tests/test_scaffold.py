from pathlib import Path
import unittest


class TestScaffold(unittest.TestCase):
    def test_expected_top_level_directories_exist(self) -> None:
        root = Path(__file__).resolve().parents[1]
        expected = [
            "docs",
            "hardware",
            "firmware",
            "software",
            "simulation",
            "datasets",
            "tests",
            "scripts",
        ]
        for directory in expected:
            self.assertTrue((root / directory).is_dir(), f"Missing directory: {directory}")

    def test_entrypoint_exists(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertTrue((root / "software" / "game_manager" / "main.py").is_file())
