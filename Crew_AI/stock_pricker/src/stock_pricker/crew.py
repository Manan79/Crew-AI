from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from pydantic import BaseModel,Field
from crewai_tools import SerperDevTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


class Trending_company(BaseModel):
    """Model for a trending company in the stock market."""
    name: str = Field(..., description="Name of the company")
    stock_price: float = Field(..., description="Current stock price of the company")
    growth_percentage: float = Field(..., description="Growth percentage of the company's stock price over the last year")

class TrendingCompanyList(BaseModel):
    """Model for a list of trending companies in the stock market."""
    companies: list[Trending_company] = Field(..., description="List of trending companies with their stock price and growth percentage")

class TrendingCompanyResearch(BaseModel):

    """Model for researching trending companies in a specific sector."""

    name: str = Field(..., description="Name of the company")
    # stock_price: float = Field(..., description="Current stock price of the company")
    market_position: str = Field(..., description="Market position of the company")
    growth_potential: str = Field(..., description="Growth potential of the company based on current trends and market analysis")
    investment_potential: str = Field(..., description="Investment potential of the company based on its current performance and future outlook")

class TrendingCompanyResearchList(BaseModel):
    """Model for a list of researched trending companies in a specific sector."""
    companies: list[TrendingCompanyResearch] = Field(..., description="List of researched trending companies with their market position, growth potential, and investment potential")


@CrewBase
class StockPricker():
    """StockPricker crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(**self.agents_config['stock_finder_agent'], tools = [SerperDevTool(max_results=2)])
    
    @agent
    def financial_researcher_agent(self) -> Agent:
        return Agent(**self.agents_config['financial_researcher_agent'], tools = [SerperDevTool(max_results=2)])
    
    @agent
    def stock_picker_agent(self) -> Agent:
        return Agent(**self.agents_config['stock_picker_agent'])
    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config = self.tasks_config['find_trending_companies'],
            output_pydantic = TrendingCompanyList,
        )
    
    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config = self.tasks_config['research_trending_companies'],
            output_pydantic = TrendingCompanyResearchList,
        )
    
    @task
    def pick_stocks(self) -> Task:
        return Task(
            config = self.tasks_config['pick_stocks'],
            
        )
    
    @crew
    def crew(self) -> Crew:
        """Defines the crew and its workflow."""

        manager = Agent(**self.agents_config['manager_agent'],
                        allow_delegation = True)
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.hierarchical,
            verbose = True,
            manager_agent = manager
            )