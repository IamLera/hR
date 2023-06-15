from src.api.services.data.customer_body import customerBody as cusB, customerAddressBody as cusA, customerProfileBody \
    as cusP, customerWalletBody as cusW, customerNoClubMembershipBody as cusNoC, customerClubMembershipBody as cusC
from src.api.services.data.tier_body import tierBody as tierB
from src.api.services.requests.cutomer_req import CustomerReq
from src.helpers.value_generators import Generators
from src.api.storage.stored_data import StoreData as sD


class TestCustomers:

    def testCreateRegisteredCustomer(self, api_login):
        fName = Generators.stringGenerator()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()

        profile = cusP(fName, lName, accGroup, email, phone)

        address = cusA()
        addresses = [address]

        wallets = []

        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

    def testCreateEmployeeCustomer(self, api_login):
        fName = Generators.stringGenerator()
        lName = Generators.lastNameGenerator()
        accGroup = "employee"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()

        profile = cusP(fName, lName, accGroup, email, phone)

        address = cusA()
        addresses = [address]

        wallets = []

        id = "a0038b2a-82f2-440d-a53d-9f48efc10b62"
        tier = tierB(id)
        membership = cusC(tier)

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

    def testCreateFriendsAndFamilyCustomer(self, api_login):
        fName = Generators.stringGenerator()
        lName = Generators.lastNameGenerator()
        accGroup = "friends_and_family"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()

        profile = cusP(fName, lName, accGroup, email, phone)

        address = cusA()
        addresses = [address]

        wallets = []

        id = "fd50837c-79ff-4df1-a760-801735a2010a"
        tier = tierB(id)
        membership = cusC(tier)

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

    def testCreateWineClubMemberCustomer(self, api_login):
        fName = Generators.stringGenerator()
        lName = Generators.lastNameGenerator()
        accGroup = "wine_club_member"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()

        profile = cusP(fName, lName, accGroup, email, phone)

        address = cusA()
        addresses = [address]

        wallets = []

        tId = "b67a8623-bd3d-41b8-b584-2e14d4cac2cd"
        tType = "reds"
        qnt = 6
        tier = tierB(tId, tType, qnt)
        pickup = {"location_id": "dba8714f-6dc2-497e-a85b-b039ace787ce"}
        membership = cusC(tier, pickup=pickup)

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)
