from mcp.server.fastmcp import FastMCP
from evapi.create import Create

def register(mcp: FastMCP):
    @mcp.tool()
    async def create_record(entity: str, fields: dict):
        """
        Create a new record in the specified entity with the given fields in your Evolutivo Application.
        When creating an Invoice, SalesOrder, Quotes, or PurchaseOrder there is a special field value for the inventory lines
        'pdoInformation': [
            [
                "productid": 'product/service ID',
                "comment": 'some comment',
                "qty": 1, // number of units to be sold
                "listprice": 10,
                'discount': 0,  // 0 no discount, 1 discount
                "discount_type": 0,  //  amount/percentage
                "discount_percentage": 0,  // not needed nor used if type is amount
                "discount_amount": 0,  // not needed nor used if type is percentage
            ],
        ]

        Args:
            entity (str): entity where the new record will be created
            fields (dict): dictionary with field names and their values for the new record
        Returns:
            string: entity identifier of the newly created record or an error message
        """
        conn = Create()
        return conn.do_create(entity, fields)
