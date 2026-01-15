import json
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def notebook_data():
    notebook_path = Path("exercises/questions_9_12_review.ipynb")
    return json.loads(notebook_path.read_text(encoding="utf-8"))


def _cell_text(cell):
    return "".join(cell.get("source", []))


def test_notebook_file_exists():
    assert Path("exercises/questions_9_12_review.ipynb").exists()


def test_notebook_metadata_basic(notebook_data):
    assert notebook_data["nbformat"] == 4
    assert notebook_data["nbformat_minor"] == 4
    kernelspec = notebook_data["metadata"]["kernelspec"]
    assert kernelspec["name"] == "python3"


def test_notebook_has_minimum_cells(notebook_data):
    assert len(notebook_data["cells"]) >= 30


def test_notebook_starts_with_title_markdown(notebook_data):
    first_cell = notebook_data["cells"][0]
    assert first_cell["cell_type"] == "markdown"
    assert "統計検定 模擬問題解説" in _cell_text(first_cell)


def test_notebook_contains_core_sections(notebook_data):
    markdown_text = "\n".join(
        _cell_text(cell) for cell in notebook_data["cells"] if cell["cell_type"] == "markdown"
    )
    for section in [
        "問9：χ²検定・連関係数・対応分析",
        "問10：正則化回帰",
        "問11：因子分析",
        "問12：時系列解析",
    ]:
        assert section in markdown_text


def test_notebook_includes_chi_square_code(notebook_data):
    code_text = "\n".join(
        _cell_text(cell) for cell in notebook_data["cells"] if cell["cell_type"] == "code"
    )
    assert "chi2_contingency" in code_text
    assert "Cramér" in code_text


def test_notebook_includes_elastic_net_demo(notebook_data):
    code_text = "\n".join(
        _cell_text(cell) for cell in notebook_data["cells"] if cell["cell_type"] == "code"
    )
    assert "enet_path" in code_text
    assert "Elastic Net" in code_text


def test_notebook_includes_time_series_decompose(notebook_data):
    code_text = "\n".join(
        _cell_text(cell) for cell in notebook_data["cells"] if cell["cell_type"] == "code"
    )
    assert "seasonal_decompose" in code_text
    assert "plot_acf" in code_text
