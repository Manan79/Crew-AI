#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
from datetime import datetime

from stock_pricker.crew import StockPricker

load_dotenv()  # Load environment variables from .env file
print(load_dotenv())

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        "sector": "Financial sector in India",
    }
    # crew = StockAnalyser()
    # result = crew.run(inputs=inputs)
    # print(f"Crew finished with result: {result}")
    results = StockPricker().crew().kickoff(inputs=inputs)
    print(f"Crew finished with results: {results.raw}")

if __name__ == "__main__":
    run()