from mcp.server.fastmcp import FastMCP
from evapi.workflow import Workflow


def register(mcp: FastMCP):

    @mcp.tool()
    async def send_email(workflow: str, wsids: str, context: dict = {}) -> str:
        """
        Send an email using your Evolutivo Application functionality.
        You must set the workflow suffix and a comma-separated list of record IDs to merge field values with.
        The tool will send an individual email to each record ID provided.
        In the context dictionary, you can provide additional parameters such as
            - SendFromName (str): The sender's email name.
            - SendFromEmail (str): The sender's email address.
            - ReplyToEmail (str): The reply-to email address.
            - SendEmailTo (str): string representation of recipient email addresses. Is a string that can contain a comma separated list of emails and Evolutivo field references.
            - SendEmailCC (str): string representation of email addresses to CC. Is a string that can contain a comma separated list of emails and Evolutivo field references.
            - SendEmailBCC (str): string representation of email addresses to BCC. Is a string that can contain a comma separated list of emails and Evolutivo field references.
            - SendThisSubject (str): The subject of the email.
            - SendThisBody (str): The body content of the email.
            - SendThisMsgTemplate (str): The email template to use.
            - SendTheseAttachments (list): List of file paths or URLs to attach to the email.
            - MergeTemplateWith (str): Comma-separated list of other entities to use for merging template fields.

        Args:
            workflow (str): The workflow suffix name, they all start with "send email"
            wsids (str): Comma-separated list of record IDs.
            context (dict, optional): Additional context for the email. Defaults to {}.

        Returns:
            string: result of the email sending operation.
        """
        wf = Workflow()
        return wf.send_email(workflow, wsids, context)
