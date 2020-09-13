from database_create import create_register, create_material, create_connection, show_database
from datetime import date

def calculateIncome():
    today = date.today()

    materialPrices = {
    "Red Meat" : 9900,
    "Caphras Stone" : 2450000,
    "Sharp Crystal Shard" : 1400000,
    "Hard Crystal Shard" : 1400000,
    "Ancient Spirit Dust" : 490000, 
    "Fairy's Powder" : 10000,
    "Black Gem Fragment" : 251000,
    "Courser Stuff" : 2490000,
    "Energy Pots" : 4500000
    }

    redMeat = int(input("Red Meat Gathered -> ")) or 0
    caphrasStones = int(input("Caphras Stone Gathered -> ")) or 0
    sharpShards = int(input("Sharp Crystal Shard Gathered -> ")) or 0
    hardShards = int(input("Hard Crystal Shard Gathered -> ")) or 0
    spiritDust = int(input("Ancient Spirit Dust Gathered -> ")) or 0
    fairyPowder = int(input("Fairy's Powder Gathered -> ")) or 0
    blackGemFrags = int(input("Black Gem Fragment Gathered -> ")) or 0
    courserStuff = int(input("Courser Stuff Gathered -> ")) or 0
    energyPots = int(input("Energy Pots Used -> ")) or 0

    redMeatSilver = materialPrices["Red Meat"] * redMeat
    caphrasStoneSilver = materialPrices["Caphras Stone"] * caphrasStones
    sharpShardSilver = materialPrices["Sharp Crystal Shard"] * sharpShards
    hardShardSilver = materialPrices["Hard Crystal Shard"] * hardShards
    spiritDustSilver = materialPrices["Ancient Spirit Dust"] * spiritDust
    fairyPowderSilver = materialPrices["Fairy's Powder"] * fairyPowder
    blackGemFragSilver = materialPrices["Black Gem Fragment"] * blackGemFrags
    courserStuffSilver = materialPrices["Courser Stuff"] * courserStuff
    energyPotsSilver = materialPrices["Energy Pots"] * energyPots

    # print(redMeatSilver)
    # print(caphrasStoneSilver)
    # print(sharpShardSilver)
    # print(hardShardSilver)
    # print(spiritDustSilver)
    # print(fairyPowderSilver)
    # print(blackGemFragSilver)

    totalTaxedSilver = (redMeatSilver + caphrasStoneSilver + sharpShardSilver + hardShardSilver + spiritDustSilver + blackGemFragSilver + courserStuffSilver) * 0.845 + fairyPowderSilver - energyPotsSilver

 
    totalTime = input("Input the time it took you to gather those materials -> ")
    silverPerHour = getSilverPerHour(totalTaxedSilver, totalTime)
    print("##################################")
    print("total(taxed): ", totalTaxedSilver)
    print("Your income per hour is: ", silverPerHour)

    conn = create_connection("database.db")
    register_1 = (str(totalTaxedSilver)+" Silver(Session)", str(silverPerHour)+" Silver(Per Hour)", today.strftime("%d/%m/%Y"), totalTime+" minutes")
    create_register(conn, register_1)

    show_database(conn)

def getSilverPerHour(totalTaxedSilver, totalTime):
    return 60*int(totalTaxedSilver)/int(totalTime)

def main():
    calculateIncome()

if __name__ == "__main__":
    main()