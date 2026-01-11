import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool
)





@CrewBase
class MarketingContentStudioLeadGenerationConversionAutomationCrew:
    """MarketingContentStudioLeadGenerationConversionAutomation crew"""

    
    @agent
    def marketing_trend_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["marketing_trend_research_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def marketing_content_strategist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["marketing_content_strategist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def research_marketing_opportunities(self) -> Task:
        return Task(
            config=self.tasks_config["research_marketing_opportunities"],
            markdown=False,
            
            
        )
    
    @task
    def create_high_converting_marketing_content(self) -> Task:
        return Task(
            config=self.tasks_config["create_high_converting_marketing_content"],
            markdown=False,
            
            
        )
    
    @task
    def finalize_marketing_campaign_package(self) -> Task:
        return Task(
            config=self.tasks_config["finalize_marketing_campaign_package"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingContentStudioLeadGenerationConversionAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
