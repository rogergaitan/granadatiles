class ItemDto():

    def __init__(self, item):
        self.id = item.id
        self.list_id = item.list_id
        self.name = item.name
        self.full_name = item.full_name
        self.is_active = item.is_active
        self.sublevel = item.sublevel
        self.sales_price = item.sales_price
        self.quantity_on_hand = item.quantity_on_hand
        self.average_cost = item.average_cost
        self.quantity_on_order = item.quantity_on_order
        self.quantity_on_sales_order = item.quantity_on_sales_order
        self.sales_desc = item.sales_desc
        self.purchase_desc = item.purchase_desc
        self.purchase_cost = item.purchase_cost
