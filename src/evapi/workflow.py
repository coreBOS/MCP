from evapi.connect import EVConnect
from helper.mcplogger import logger
import json


class Workflow:
    def __init__(self):
        self.evconn = EVConnect()
        self.ws = self.evconn.get_connection()

    def do_workflow(self, workflow: str, wsids: str, context: dict = {}) -> str:
        try:
            ids_list = wsids.split(",")
            info = self.ws.do_invoke(
                'ExecuteWorkflowWithContext',
                {
                    "workflow": workflow,
                    "entities": json.dumps(ids_list),
                    "context": json.dumps(context),
                }
            )
            return "Success" if info else "Failed"
        except (AttributeError, TypeError, ValueError) as e:
            logger.error("Error in execute workflow '%s' '%s': %s", workflow, wsids, e)
            return "Failed"

    def send_email(self, workflow: str, wsids: str, context: dict = {}) -> str:
        try:
            return self.do_workflow('send email ' + workflow.lower(), wsids, context)
        except (AttributeError, TypeError, ValueError) as e:
            logger.error("Error in send email workflow %s %s %s: %s", workflow, wsids, context, e)
            return "Failed"
