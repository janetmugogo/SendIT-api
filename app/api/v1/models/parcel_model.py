import uuid
parcels = []


class Parcels:
    def __init__(self):
        self.db = parcels

    # the user creates an order and it is saved/stored in the dictionary

    def save_parcel(self, name, phonenumber, idnumber, location, address, weight, price):
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
            'user_id': str(uuid.uuid4())
        }

        self.db.append(new_order)


        # user can get all the orders they have created

    def get_all_parcels(self):

        return self.db

        # user can fetch for a specific order using an order_id

    def get_single_order(self, order_id):
        for order in self.db:
            if order['order_id'] == order_id:
                return order
        # user can cancel a specific order, and when the status of the order is in-transit

    def cancel_order(self, order_id):
        for order in self.db:
            if order['order_id'] == order_id:
                if order["status"] == "undelivered":
                    order['status'] = "cancelled"

        # user can change the  destination of a parcel when it is in-transit

    def change_destination(self, order_id, destination):
        for order in self.db:
            if order['order_id'] == order:
                if order["status"] == "undelivered":
                 order['destination'] = destination

    def specific_user_order(self, user_id):
        orders=[]
        for order in self.db:
            if order['user_id'] == (user_id):
                orders.append(order)
        payload = {
            "message": "success",
            "delivery_order": orders
        }
        return payload





