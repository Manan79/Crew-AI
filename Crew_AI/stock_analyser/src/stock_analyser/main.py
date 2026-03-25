#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
from datetime import datetime

from stock_analyser.crew import StockAnalyser

load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'company': 'Tata Consultancy Services',
    }
    # crew = StockAnalyser()
    # result = crew.run(inputs=inputs)
    # print(f"Crew finished with result: {result}")
    results = StockAnalyser().crew().kickoff(inputs=inputs)
    print(f"Crew finished with results: {results.raw}")

if __name__ == "__main__":
    run()