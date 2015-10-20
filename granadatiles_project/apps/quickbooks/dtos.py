class ItemDto():

    def __init__(self, item):
        self.id = item['$id']
        self.list_id = item['ListID']
        self.name = item['Name']
        self.full_name = item['FullName']
        self.is_active = item['IsActive']
        self.sublevel = item['SubLevel']
        self.sales_price = item['SalesPrice']
        self.quantity_on_hand = item['QuantityOnHand']
        self.average_cost = item['AverageCost']
        self.quantity_on_order = item['QuantityOnOrder']
        self.quantity_on_sales_order = item['QuantityOnSalesOrder']
        self.sales_desc = item['SalesDesc']
        self.purchase_desc = item['PurchaseDesc']
        self.purchase_cost = item['PurchaseCost']
