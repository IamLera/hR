class customerBody():

    def __init__(self, profile, addresses, wallets, club_membership):

        self.profile = profile
        self.addresses = addresses
        self.wallets = wallets
        self.club_membership = club_membership

class customerProfileBody():

    def __init__(self, first_name, last_name, account_group, email, phone_number, preferred_primary_location_id=None,
                 customer_source_id=None, email_opt_in=True, sms_opt_in=True, pos_notes="", system_notes="",
                 date_of_birth=None):
        self.first_name = first_name
        self.last_name = last_name
        self.account_group = account_group
        self.email = email
        self.phone_number = phone_number
        self.customer_source_id = customer_source_id
        self.preferred_primary_location_id = preferred_primary_location_id
        self.email_opt_in = email_opt_in
        self.sms_opt_in = sms_opt_in
        self.pos_notes = pos_notes
        self.system_notes = system_notes
        self.date_of_birth = date_of_birth

class customerAddressBody():

    def __init__(self, address_name="", first_name="", last_name="", country="USA", state="", city="", business="",
                 street_address_one="", street_address_two="", zip_code=None, is_same_as_shipping_address=False,
                 is_default=False):
        self.address_name = address_name
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.state = state
        self.city = city
        self.business = business
        self.street_address_one = street_address_one
        self.street_address_two = street_address_two
        self.zip_code = zip_code
        self.is_same_as_shipping_address = is_same_as_shipping_address
        self.is_default = is_default

class customerWalletBody():

    def __init__(self, card_name, card_number, expiration_date, cvv, name_on_card, first_name, last_name, country, state,
                 city, business, street_address_one, street_address_two, zip_code, is_same_as_shipping_address, is_default, address_name):
        self.card_name = card_name
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.name_on_card = name_on_card
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.state = state
        self.city = city
        self.business = business
        self.street_address_one = street_address_one
        self.street_address_two = street_address_two
        self.zip_code = zip_code
        self.is_same_as_shipping_address = is_same_as_shipping_address
        self.is_default = is_default
        self.address_name = address_name


class customerNoClubMembershipBody():
    def __init__(self,  tier=None, add_on=None, shipment=None, pickup=None):
        self.tier = tier
        self.add_on = add_on
        self.shipment = shipment
        self.pickup = pickup

class customerClubMembershipBody():
    def __init__(self,  tier, add_on=None, shipment=None, hasShipment=True, pickup=None):
        self.tier = tier
        self.add_on = add_on
        self.hasShipment = hasShipment
        self.shipment = shipment
        self.pickup = pickup