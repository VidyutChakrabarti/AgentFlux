from agents import Main_agents
from tasks import Main_Tasks
from crewai import Crew

main_agents = Main_agents()
main_tasks = Main_Tasks()

def promptrefinement(original_code):
    prompt_refiner = main_agents.prompt_refiner()
    prompt_refiner_task = main_tasks.refine_prompts(
        prompt_refiner
    )
    prompt_crew = Crew(
        agents=[prompt_refiner],
        tasks=[prompt_refiner_task],
        verbose=True,
        max_rpm=60,
        cache=True,
        full_output=True,
    )

    inputs = {"code": original_code}
    crew_result = prompt_crew.kickoff(inputs=inputs)
    refined_code = crew_result.raw
    refined_code = refined_code.replace("```python", "").replace("```", "")
    return refined_code

def rearchitect(original_code, allowedModels):
    graph_architect = main_agents.graph_architect()
    rearchitect_task = main_tasks.re_architect_graph(graph_architect)
    graph_crew = Crew(
        agents=[graph_architect],
        tasks=[rearchitect_task],
        verbose=True,
        max_rpm=60,
        cache=True,
        full_output=True,
    )

    inputs = {"code": original_code, "allowedModels": allowedModels}
    crew_output = graph_crew.kickoff(inputs=inputs)
    refined_code = crew_output.raw
    refined_code = refined_code.replace("```python", "").replace("```", "")
    return refined_code