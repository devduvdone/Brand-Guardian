import operator
from typing import Annotated, List, Dict, Optional, TypedDict, Any


# defines schema for single compliance result
# error report
class ComplianceIssue(TypedDict):
    category: str
    description: str
    severity: str
    timestamp: Optional[str]

# defines the global graph state
# this defines the state that get passsed around in agentic workflow
class VideoAuditState(TypedDict):
    '''
    defines the data schema for langgraph execution content
    Main container: holds all the information about the audit right from the initial url to final report
    '''

    # input parameters
    video_url: str
    video_id: str

    # ingestion and extraction data
    local_file_path: Optional[str]  
    video_metadata: Dict[str,Any]
    transcript: Optional[str]
    ocr_text: List[str]


    # stores the list of all violations found by AI
    compliance_results: Annotated[List[ComplianceIssue],operator.add]


    # final deliverables
    final_status: str # PASS | FAIL 
    final_report: str


    # errors: API timeout , system level errors
    # list of system level errors
    errors: Annotated[List[str], operator.add]