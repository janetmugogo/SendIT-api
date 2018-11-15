parcels = []


class Parcels:
    def __init__(self):
        self.db = parcels

    # the user creates an order and it is saved/stored in the dictionary

    def save_parcel(self, name, phonenumber, idnumber, location, address, weight, price, user_id):
        new_order = {
            'order_id': len(self.db) + 1,
            'name': name,
            'phonenumber': int(phonenumber),
            'idnumber': int(idnumber),
            'location': location,
            'address': int(address),
            'weight': int(weight),
            'status': "in-transit",
            'destination': "destination",
            'price': int(price),
            'user_id': user_id
        }

        self.db.append(new_order)


    # user can get all the orders they have created

    def get_all_parcels(self):

        return self.db

    # user can fetch for a specific order using an order_id

    def get_single_order(self, order_id):
        print(order_id)
        try:
            order_id=int(order_id)
        except ValueError:
            return {"message":"invalid id"}
        for order in self.db:
            if order['order_id'] == order_id:
                return order

    # user can cancel a specific order, and when the status of the order is in-transit

    def cancel_order(self, order_id):
        print(order_id)
        try:
            order_id = int(order_id)
        except ValueError:
            return {"message": "invalid order_id"}
        for order in self.db:
            if order['order_id'] == order_id:
                if order["status"] in ("undelivered", "in-transit"):
                    order['status'] = "cancelled"
                    message = {"message": "The order has been cancelled"}
                else:
                    message = {"message": "Already cancelled, cannot cancel twice"}
                return message

     #fetch all parcel delivery orders by a specific user

    def specific_user_order(self, user_id):
        orders = []
        for order in self.db:
            if order['user_id'] == user_id:
                orders.append(order)
        if not orders:
            return "Order not found"
        return orders







