from app.bfs import bfs_traversal


def test_bfs():
    graph = {
        "Step1": ["Step2"],
        "Step2": ["Step3", "Step4"],
        "Step3": ["Step5", "Step7"],
        "Step4": ["Step9"],
        "Step5": ["Step6"],
        "Step7": ["Step8"],
        "Step6": ["Step10"],
        "Step8": ["Step10"],
        "Step9": ["Step10"],
        "Step10": ["Step11"],
        "Step11": []
    }

    result = bfs_traversal(graph, "Step1")

    assert result[0] == "Step1"
    assert "Step11" in result