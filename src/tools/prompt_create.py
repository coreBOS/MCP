from mcp.server.fastmcp import FastMCP
# from fastmcp.prompts import PromptMessage
# from mcp.types import TextContent

def register(mcp: FastMCP):

    @mcp.prompt()
    def create_procedure(entity: str) -> list[str]:
        """
        Defines the steps to create a record.
        """
        return [
            f"Use get_fields metainformation to get a list of fields for the {entity} entity",
            f"Loop over all the mandatory fields asking the user for values. Use the metainformation about field types to show possible values for each field",
            f"Ask if the user wants to set any optional fields. If yes, loop over all the optional fields asking the user for values. Use the metainformation about field types to show possible values for each field",
            f"Validate each field with it's type",
            f"Create a new {entity} record with the provided values using the create tool",
            f"Return the ID of the newly created record or an error message if the creation failed",
        ]

    @mcp.prompt()
    def create_inventory_procedure(entity: str) -> list[str]:
        """
        Defines the steps to create an Invoice, SalesOrder, Quotes or PurchaseOrder record.
        """
        return [
            f"Use get_fields metainformation to get a list of fields for the {entity} entity",
            f"Loop over all the mandatory fields asking the user for values. Use the metainformation about field types to show possible values for each field",
            f"Ask if the user wants to set any optional fields. If yes, loop over all the optional fields asking the user for values. Use the metainformation about field types to show possible values for each field",
            f"Validate each field with it's type",
            f"Ask the user for the inventory lines details by doing a loop that asks for:"
            f"Product or Service ID"
            f"Ask for the Quantity of the inventory line"
            f"Use the product or service ID to retrieve the price"
            f"Ask if they want to modify the Price"
            f"Ask if there is any Discount to apply to the inventory line"
            f"Create a new {entity} record with the provided values using the create tool with the special pdoInformation array",
            f"Return the ID of the newly created record or an error message if the creation failed",
        ]
