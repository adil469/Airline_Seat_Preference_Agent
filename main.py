
from agents import Agent, RunContextWrapper, Runner,trace
from pydantic import BaseModel
from connection import config
from dotenv import load_dotenv
import rich
import asyncio

load_dotenv()

#                     Exercise 3: Travel Planning Assistant (Intermediate-Advanced)
# Requirement: Build a dynamic instructions system for a travel planning agent that customizes recommendations based 
# on trip_type and traveler_profile.

# Adventure + Solo: Suggest exciting activities, focus on safety tips, recommend social hostels and group tours 
# for meeting people. 
# Cultural + Family: Focus on educational attractions, kid-friendly museums, interactive experiences, 
# family accommodations.
# Business + Executive: Emphasize efficiency, airport proximity, business centers, reliable
# wifi, premium lounges. medical_student/doctor


class Dynamic_Instr(BaseModel):
    name : str = "Adil"
    trip_type :str
    treveler_profile : str

def get_dynamic_func_instrction(type_of_trip:str):
    show_trip_type = type_of_trip.lower()

    if show_trip_type == "adventure":
        return Dynamic_Instr(trip_type = "adventure", treveler_profile = "solo")
    
    elif show_trip_type == "cultural":
        return Dynamic_Instr(trip_type = "cultural", treveler_profile = "family")
    
    elif show_trip_type == "bussiness":
        return Dynamic_Instr(trip_type = "bussiness", treveler_profile = "executive")


def travel_planning_assistant(ctx:RunContextWrapper[Dynamic_Instr], agent:Agent):
    trip_type = ctx.context.trip_type
    treveler_profile = ctx.context.treveler_profile

    if trip_type == "adventure" and treveler_profile == "solo":
        return """Suggest exciting activities, focus on safety tips, recommend social hostels and group tours
          for meeting people. """
    
    elif trip_type == "cultural" and treveler_profile == "family":
        return """ Focus on educational attractions, kid-friendly museums, interactive experiences, 
          family accommodations."""
    
    elif trip_type == "bussiness" and treveler_profile == "executive":
        return """ Emphasize efficiency, airport proximity, business centers, reliable
          wifi, premium lounges. medical_student/doctor"""
    
    else:
        return """Sorry, I didn’t recognize that trip type. Available options: adventure, cultural, business."""

triage_agent = Agent(
    name = "triage agent",
    instructions=travel_planning_assistant,
)

async def main():
    with trace("llm context work flow .."):
        user_input = input("Please confirm your trip type\n(adventure/cultural/bussiness): ")
        llm_context = get_dynamic_func_instrction(user_input)

        result = await Runner.run(
            triage_agent,
            input = user_input,
            run_config = config,
            context = llm_context
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
