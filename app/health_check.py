import asyncio
import random


async def check_component_health(component_id):
    await asyncio.sleep(1)

    status = random.choice(["HEALTHY", "UNHEALTHY"])

    return {
        "component": component_id,
        "status": status
    }


async def check_all_components(components):
    tasks = [
        check_component_health(component.id)
        for component in components
    ]

    return await asyncio.gather(*tasks)