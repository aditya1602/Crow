class LandOwner:
    def __init__(self, landOwnerID=0, landOwnerName="", acres=0, amount=0):
        self.landOwnerID = landOwnerID
        self.landOwnerName = landOwnerName
        self.acres = acres
        self.amount = amount

    @setLandOwnerID.setter
    def setLandOwnerID(self, landOwnerID):
        self.landOwnerID = landOwnerID

    @property
    def getLandOwnerID(self):
        return self.landOwnerID

    def setLandOwnerName(self, landOwnerName):
        self.landOwnerName = landOwnerName

    def getLandOwnerName(self):
        return self.landOwnerName

    def setAcres(self, acres):
        self.acres = acres

    def getAcres(self):
        return self.acres

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def printDetails(self):
        print("Land Owner ID: ", self.landOwnerID)
        print("Land Owner Name: ", self.landOwnerName)
        print("Acres: ", self.acres)
        print("Amount: ", self.amount)

    def sellLand(self, landQty, pricePerAcre, LandOwner):
        if self.acres < landQty:
            print("Not enough land to sell!")
            return
        if LandOwner.amount < (landQty * pricePerAcre):
            print("Buyer doesnt have enough money!")
            return
        self.acres = self.acres - landQty
        LandOwner.acres = LandOwner.acres + landQty
        self.amount = self.amount + (landQty * pricePerAcre)
        LandOwner.amount = LandOwner.amount - (landQty * pricePerAcre)


# Driver
L1 = LandOwner(1, "Aditya", 100, 1000)
# L1.setLandOwnerID = 2323
L1.setLandOwnerID = 2323
L2 = LandOwner(3, "Meet", 200, 2000)
L1.sellLand(100, 2, L2)
L3 = LandOwner()
L1.printDetails()
L2.printDetails()

