import pytest
from services.file_manager import FileProcessingTool


def test_is_file_exists():
    res = FileProcessingTool.is_file_exists("none.txt")
    assert res == False
