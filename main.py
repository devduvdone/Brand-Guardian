"""
Main execution entry point for the compliance QA Pipeline.
This file is the control center:
1, sets up the audit request
2, runs the ai workflow
3, display the final compliance report
"""

import uuid
import json
import logging
from pprint import pprint

from dotenv import load_dotenv
load_dotenv(override=True)

from backend.src.graph.workflow import app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("brand-guardian-runner")

def run_cli_simulation():
    """
    simulates the video compliance audit request
    """

    #generate the session id
    session_id = str(uuid.uuid4())
    logger.info(f"starting audit session: {session_id}")

    #define the initial state
    initial_inputs = {
        "video_url":"https://youtu.be/dT7S75eYhcQ",
        "video_id":f"vid_{session_id[:8]}",
        "compliance_results":[],
        "errors":[]
    }

    print("n-----------Initialising workflow..............")
    print(f"Input Payload :{json.dumps(initial_inputs,indent=2)}")

    try:
        final_state = app.invoke(initial_inputs)
        print("\n----------workflow execution is complete-----------")
        print("\n compliance  Audit Report == ")
        print(f"Video_ID: {final_state.get("video_id")}")
        print(f"Status: {final_state.get("final_status")}")
        print("\n [VIOLATION DETECTED]")
        results = final_state.get("compliance_results",[])
        if results:
            for issue in results:
                print(f"- [{issue.get('severity')}][{issue.get('category')}]:{issue.get('description')}")
        else:
            print("No violations detected..............")
        print("\n [FINAL SUMMARY]")
        print(final_state.get('final_report'))
    except Exception as e:
        logger.error(f"Workflow execution failed: {str(e)}")
        raise e


if __name__ == "__main__":
    run_cli_simulation()
