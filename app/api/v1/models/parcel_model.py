parcels = []


class Parcels:
    def __init__(self):
        self.db = parcels

    def save_parcel(self, name, phonenumber, idnumber, location, address, weight):
        new_order = {
            'order_id': len(self.db) + 1,
            'name': name,
            'phonenumber': int(phonenumber),
            'idnumber': idnumber,
            'location': location,
            'address': address,
            'weight': int(weight),
            'status':"intransit",
            'destination':"nairobi"
        }
        self.db.append(new_order)

    def get_all_parcels(self):

        return self.db

    def get_single_order(self, order_id):
        for order in self.db:
            if order['order_id'] == order_id:
                return order
    def cancel_order(self, order_id):
        for order in self.db:
            if order['order_id'] == order_id:
                order['status'] = "cancelled"

    # def change_destination(self, order_id):
    #     for order in self.db:
    #         if order['order_id'] == order_id and order['status'] == "intransit":
    #             order['destination'] = "mombasa"





janet = Parcels()
janet.save_parcel('book', '987654321', '345678', 'kisumu', '31156', '2')
janet.save_parcel('kitabu', '987654321', '345678', 'kitale', '31156', '3')
# print(janet.db)

# print(janet.get_single_order(2))
print(janet.cancel_order(2))
# print(janet.get_all_parcels())
# print(janet.change_destination(1))

