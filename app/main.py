from fastapi import FastAPI
import logging

from app.models import SystemGraph
from app.health_check import check_all_components
from app.bfs import bfs_traversal
from app.utils import build_graph

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="System Health Check API"
)


@app.get("/")
def home():
    return {
        "message": "System Health Check API is running"
    }


@app.post("/health-check")
async def health_check(system: SystemGraph):

    logger.info("Health check request received")

    graph = build_graph(system.components)

    start_node = None

    for component in system.components:
        if not component.dependencies:
            start_node = component.id
            break

    bfs_order = bfs_traversal(graph, start_node)

    logger.info(f"BFS Traversal Order: {bfs_order}")

    results = await check_all_components(
        system.components
    )
    table_data = []

    for item in results:
        table_data.append(
            f"{item['component']:<20} | {item['status']}"
        )
    
    logger.info("Health check completed")

    return {
    "bfs_order": bfs_order,
    "total_components": len(system.components),
    "health_table": [
        "Component            | Status",
        "---------------------|----------",
        *table_data
    ],
    "results": results
    }