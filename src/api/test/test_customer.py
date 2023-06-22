from src.api.services.data.customer_body import customerBody as cusB, customerAddressBody as cusA, customerProfileBody \
    as cusP, customerWalletBody as cusW, customerNoClubMembershipBody as cusNoC, customerClubMembershipBody as cusC
from src.api.services.data.tier_body import tierBody as tierB
from src.api.services.requests.cutomer_req import CustomerReq
from src.helpers.value_generators import Generators
from src.api.storage.stored_data import StoreData as sD


class TestCustomers:

    def testGetProducts(self, api_login):
        cR = CustomerReq()
        cR.getCustomerList()

    def testCreateRegisteredCustomer(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

    def testCreateEmployeeCustomer(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "employee"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        tierId = "a0038b2a-82f2-440d-a53d-9f48efc10b62"
        tier = tierB(tierId)
        membership = cusC(tier)

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

    def testCreateWineClubMemberCustomer(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "wine_club_member"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        tId = "b67a8623-bd3d-41b8-b584-2e14d4cac2cd"
        tType = "reds"
        qnt = 6
        tier = tierB(tId, tType, qnt)
        pickup = {"location_id": "dba8714f-6dc2-497e-a85b-b039ace787ce"}
        membership = cusC(tier, pickup=pickup)

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

    def testDeleteCustomer(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)
        cR.deleteCustomer(sD.store['createCustomerResp']['id'])

    def testCreateCustomerWithAddress(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        aName=Generators.stringGeneratorMarked()
        state = "Texas"
        city = "Coldspring"
        address1 = "1 TX-150, Coldspring, TX 77331, USA"
        address2 = "second address"
        zipCode = "77331"
        address = cusA(aName, fName, lName, state, city, "Business", address1, address2, zipCode)
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

        addressResp = sD.store["createCustomerResp"]["addresses"][0]

        assert aName == addressResp["address_name"],  f'Wrong address_name - {addressResp["address_name"]}'
        assert fName == addressResp["first_name"], f'Wrong first_name - {addressResp["first_name"]}'
        assert lName == addressResp["last_name"], f'Wrong last_name - {addressResp["last_name"]}'
        assert city == addressResp["city"], f'Wrong city - {addressResp["city"]}'
        assert zipCode == addressResp["zip_code"], f'Wrong zip_code - {addressResp["zip_code"]}'
        assert address1 == addressResp["street_address_one"], f'Wrong street_address_one - {addressResp["street_address_one"]}'
        assert address2 == addressResp["street_address_two"], f'Wrong street_address_two - {addressResp["street_address_two"]}'
        assert addressResp["is_same_as_shipping_address"] is False, f'Wrong is_same_as_shipping_address - {addressResp["is_same_as_shipping_address"]}'

    def testCreateCustomerWithWallet(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "employee"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        cName = Generators.stringGeneratorMarked()
        cNumber = "4242 4242 4242 4242"
        expDate = "11 / 27"
        cvv=Generators.numberGenerator(3)
        nameOnCard = Generators.stringGeneratorMarked()
        state = "Texas"
        city = "Coldspring"
        bus = Generators.stringGeneratorMarked()
        address1 = "1 TX-150, Coldspring, TX 77331, USA"
        address2 = "second address"
        zipCode = "77331"
        aName = Generators.stringGeneratorMarked()
        wallet = cusW(cName, cNumber, expDate, cvv, nameOnCard, fName, lName, state, city, bus, address1, address2,
                      zipCode, aName)
        wallets = [wallet]

        # membership data
        tierId = "a0038b2a-82f2-440d-a53d-9f48efc10b62"
        tier = tierB(tierId)
        membership = cusC(tier)

        body = cusB(profile, addresses, wallets, membership)

        cR = CustomerReq()
        cR.createCustomer(body)

        walletsResp = sD.store["createCustomerResp"]["wallets"][0]

        assert fName == walletsResp["first_name"], f'Wrong first_name - {walletsResp["first_name"]}'
        assert lName == walletsResp["last_name"], f'Wrong last_name - {walletsResp["last_name"]}'
        assert city == walletsResp["city"], f'Wrong city - {walletsResp["city"]}'
        assert zipCode == walletsResp["zip_code"], f'Wrong zip_code - {walletsResp["zip_code"]}'
        assert address1 == walletsResp["street_address_one"], f'Wrong street_address_one - {walletsResp["street_address_one"]}'
        assert address2 == walletsResp["street_address_two"], f'Wrong street_address_two - {walletsResp["street_address_two"]}'
        assert cName == walletsResp["card_name"], f'Wrong is_same_as_shipping_address - {walletsResp["card_name"]}'
        assert nameOnCard == walletsResp["name_on_card"], f'Wrong is_same_as_shipping_address - {walletsResp["name_on_card"]}'

    def testEditCustomerProfile(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "employee"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        tierId = "a0038b2a-82f2-440d-a53d-9f48efc10b62"
        tier = tierB(tierId)
        membership = cusC(tier)

        body = cusB(profile, addresses, wallets, membership)

        # updated profile data
        newFName = Generators.stringGeneratorMarked()
        newLName = Generators.lastNameGenerator()
        newEmail = Generators.emailGenerator()
        newPhone = Generators.phoneGenerator()
        newPosNote = Generators.stringGenerator()
        newSysNote = Generators.stringGenerator()
        newBirthday = Generators.birthdayGenerator()
        newEmailOpt = False
        newSmsOpt = False
        newProfile = cusP(newFName, newLName, accGroup, newEmail, newPhone, email_opt_in=newEmailOpt,
                          sms_opt_in=newSmsOpt, pos_notes=newPosNote, system_notes=newSysNote, date_of_birth=newBirthday)

        cR = CustomerReq()
        cR.createCustomer(body)

        cusId = sD.store["createCustomerResp"]["id"]
        cR.editCustomerProfile(newProfile, cusId)

        profileResp = sD.store["editCustomerProfileResp"]["profile"]

        assert newFName == profileResp["first_name"], f'Wrong first_name - {profileResp["first_name"]}'
        assert newLName == profileResp["last_name"], f'Wrong last_name - {profileResp["last_name"]}'
        assert newEmail == profileResp["email"], f'Wrong email - {profileResp["email"]}'
        assert newPhone == profileResp["phone_number"], f'Wrong phone_number - {profileResp["phone_number"]}'
        assert newPosNote == profileResp["pos_notes"], f'Wrong pos_notes - {profileResp["pos_notes"]}'
        assert newSysNote == profileResp["system_notes"], f'Wrong system_notes - {profileResp["system_notes"]}'
        assert newBirthday == profileResp["date_of_birth"], f'Wrong date_of_birth - {profileResp["date_of_birth"]}'
        assert profileResp["email_opt_in"] is newEmailOpt, f'Wrong email_opt_in - {profileResp["email_opt_in"]}'
        assert profileResp["sms_opt_in"] is newSmsOpt, f'Wrong sms_opt_in - {profileResp["sms_opt_in"]}'

    def testEditCustomerAddress(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        # updated address data
        newAdName = Generators.stringGenerator()
        newAdFName = Generators.firstNameGenerator()
        newAdLName = Generators.lastNameGenerator()
        newState = "New York"
        newCity = "New York"
        newBus = Generators.stringGenerator()
        newAd1 = "156 William St, New York, NY 10038, USA"
        newAd2 = Generators.stringGenerator()
        newZip = "10038"
        newSameAsShipping = True
        newIsDefault = True
        newAddress = cusA(newAdName, newAdFName, newAdLName, newState, newCity, newBus, newAd1, newAd2, newZip,
                       newSameAsShipping, newIsDefault)

        cR = CustomerReq()
        cR.createCustomer(body)

        cusId = sD.store["createCustomerResp"]["id"]
        addressId = sD.store["createCustomerResp"]["addresses"][0]["id"]
        cR.editCustomerAddress(newAddress, cusId, addressId)

        profileResp = sD.store["editCustomerAddressResp"]
        assert newAdName == profileResp["address_name"], f'Wrong address_name - {profileResp["address_name"]}'
        assert newAdFName == profileResp["first_name"], f'Wrong first_name - {profileResp["first_name"]}'
        assert newAdLName == profileResp["last_name"], f'Wrong last_name - {profileResp["last_name"]}'
        assert newState == profileResp["state"], f'Wrong state - {profileResp["state"]}'
        assert newCity == profileResp["city"], f'Wrong city - {profileResp["city"]}'
        assert newBus == profileResp["business"], f'Wrong business - {profileResp["business"]}'
        assert newAd1 == profileResp["street_address_one"], f'Wrong street_address_one - {profileResp["street_address_one"]}'
        assert newAd2 == profileResp["street_address_two"], f'Wrong street_address_two - {profileResp["street_address_two"]}'
        assert newZip == profileResp["zip_code"], f'Wrong zip_code - {profileResp["zip_code"]}'
        assert profileResp["is_same_as_shipping_address"] is newSameAsShipping, f'Wrong is_same_as_shipping_address - {profileResp["is_same_as_shipping_address"]}'
        assert profileResp["is_default"] is newIsDefault, f'Wrong is_default - {profileResp["is_default"]}'

    def testAddCustomerAddress(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        # new address data
        adName = Generators.stringGenerator()
        adFName = Generators.firstNameGenerator()
        adLName = Generators.lastNameGenerator()
        state = "New York"
        city = "New York"
        bus = Generators.stringGenerator()
        ad1 = "156 William St, New York, NY 10038, USA"
        ad2 = Generators.stringGenerator()
        adZip = "10038"
        sameAsShippingBool = True
        isDefaultBool = True
        newAddress = cusA(adName, adFName, adLName, state, city, bus, ad1, ad2, adZip, sameAsShippingBool, isDefaultBool)

        cR = CustomerReq()
        cR.createCustomer(body)

        cusId = sD.store["createCustomerResp"]["id"]
        cR.addCustomerAddress(newAddress, cusId)

        profileResp = sD.store["addCustomerAddressResp"]
        assert adName == profileResp["address_name"], f'Wrong address_name - {profileResp["address_name"]}'
        assert adFName == profileResp["first_name"], f'Wrong first_name - {profileResp["first_name"]}'
        assert adLName == profileResp["last_name"], f'Wrong last_name - {profileResp["last_name"]}'
        assert state == profileResp["state"], f'Wrong state - {profileResp["state"]}'
        assert city == profileResp["city"], f'Wrong city - {profileResp["city"]}'
        assert bus == profileResp["business"], f'Wrong business - {profileResp["business"]}'
        assert ad1 == profileResp["street_address_one"], f'Wrong street_address_one - {profileResp["street_address_one"]}'
        assert ad2 == profileResp["street_address_two"], f'Wrong street_address_two - {profileResp["street_address_two"]}'
        assert adZip == profileResp["zip_code"], f'Wrong zip_code - {profileResp["zip_code"]}'
        assert profileResp["is_same_as_shipping_address"] is sameAsShippingBool, f'Wrong is_same_as_shipping_address - {profileResp["is_same_as_shipping_address"]}'
        assert profileResp["is_default"] is isDefaultBool, f'Wrong is_default - {profileResp["is_default"]}'

    def testAddCustomerWallet(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "registered_customer"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        membership = cusNoC()

        body = cusB(profile, addresses, wallets, membership)

        # new wallets data
        cName = Generators.stringGeneratorMarked()
        cNumber = "4242 4242 4242 4242"
        expDate = "11 / 27"
        cvv = Generators.numberGenerator(3)
        nameOnCard = Generators.stringGeneratorMarked()
        state = "Texas"
        city = "Coldspring"
        bus = Generators.stringGeneratorMarked()
        address1 = "1 TX-150, Coldspring, TX 77331, USA"
        address2 = "second address"
        zipCode = "77331"
        aName = Generators.stringGeneratorMarked()
        newWallet = cusW(cName, cNumber, expDate, cvv, nameOnCard, fName, lName, state, city, bus, address1, address2,
                      zipCode, aName)

        cR = CustomerReq()
        cR.createCustomer(body)

        cusId = sD.store["createCustomerResp"]["id"]
        cR.addCustomerWallet(newWallet, cusId)

        walletsResp = sD.store["addCustomerWalletResp"]

        assert fName == walletsResp["first_name"], f'Wrong first_name - {walletsResp["first_name"]}'
        assert lName == walletsResp["last_name"], f'Wrong last_name - {walletsResp["last_name"]}'
        assert city == walletsResp["city"], f'Wrong city - {walletsResp["city"]}'
        assert zipCode == walletsResp["zip_code"], f'Wrong zip_code - {walletsResp["zip_code"]}'
        assert address1 == walletsResp["street_address_one"], f'Wrong street_address_one - {walletsResp["street_address_one"]}'
        assert address2 == walletsResp["street_address_two"], f'Wrong street_address_two - {walletsResp["street_address_two"]}'
        assert cName == walletsResp["card_name"], f'Wrong is_same_as_shipping_address - {walletsResp["card_name"]}'
        assert nameOnCard == walletsResp["name_on_card"], f'Wrong is_same_as_shipping_address - {walletsResp["name_on_card"]}'

    def testEditCustomerClub(self, api_login):
        # profile data
        fName = Generators.stringGeneratorMarked()
        lName = Generators.lastNameGenerator()
        accGroup = "wine_club_member"
        email = Generators.emailGenerator()
        phone = Generators.phoneGenerator()
        profile = cusP(fName, lName, accGroup, email, phone)

        # address data
        address = cusA()
        addresses = [address]

        # wallets data
        wallets = []

        # membership data
        tierId = "b67a8623-bd3d-41b8-b584-2e14d4cac2cd"
        tType = "reds"
        qnt = 6
        tier = tierB(tierId, tType, qnt)
        pickup = {"location_id": "dba8714f-6dc2-497e-a85b-b039ace787ce"}
        membership = cusC(tier, pickup=pickup)

        body = cusB(profile, addresses, wallets, membership)

        # updated club data
        newtType = "mixed"
        newQnt = 12
        newPickup = {"location_id": "790fac1a-33bc-4236-bb96-d3a92ff49059"}  # Estrella
        newTier = tierB(tierId, newtType, newQnt)
        newMembership = cusC(newTier, pickup=newPickup)

        cR = CustomerReq()
        cR.createCustomer(body)

        cusId = sD.store["createCustomerResp"]["id"]
        clubId = sD.store["createCustomerResp"]["club_membership"]["id"]
        cR.editCustomerClub(newMembership, cusId, clubId)

        clubResp = sD.store["editCustomerClubResp"]
        assert newtType == clubResp["tier"]["wine_type"], f'Wrong wine_type - {clubResp["tier"]["wine_type"]}'
        assert newQnt == clubResp["tier"]["bottle_quantity"], f'Wrong bottle_quantity - {clubResp["tier"]["bottle_quantity"]}'
        assert newPickup["location_id"] == clubResp["pickup"]["location"]["id"], f'Wrong location id - {clubResp["pickup"]["location"]["id"]}'


