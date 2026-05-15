import os
import logging
from azure.monitor.opentelemetry import configure_azure_monitor

logger = logging.getLogger("brand-guardian.-telemetry")

def setup_telemetry():
    """
    Initializes Azure Monitor OpenTelemetry,
    it tracks: http requests, database queries, errors, performance metrics.
    sends this data to azure monitor
    
    it auto captures every api requests,
    no need to log every endpoint manually
    """

    connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")

    if not connection_string:
        logger.warning("No instrument key found, Telemetry is DISABLED")
        return
    
    try:
        configure_azure_monitor(
            connection_string = connection_string,
            logger_name = "brand-guardian-tracer"
        )
        logger.info("Azure monitor tracking is enabled and connected")
    except Exception as e:
        logger.error(f"Failed to initialise Azure monitor: {e}")


"""
why do we use telemetry?

without it:
API is slow -> we have no idea that which part,
How many user today ? No visibility

with telemetry:
'/audit' endpoint averages 4.5 s (Indexer takes 3.8 s)
Error logs show: 12% of audit failed due to Youtube video download error
Metrics show : 450 API calls today , 89% success rate. 
"""