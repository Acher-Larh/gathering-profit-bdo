#SPH = Silver Per Hour
def calculateIncome():
    materialPrices = {
    "Red Meat" : 9900,
    "Caphras Stone" : 2450000,
    "Sharp Crystal Shard" : 1400000,
    "Hard Crystal Shard" : 1400000,
    "Ancient Spirit Dust" : 490000, 
    "Fairy's Powder" : 10000,
    "Black Gem Fragment" : 251000 
    }

    redMeat = int(input("Red Meat Gathered -> ")) or 0
    caphrasStones = int(input("Caphras Stone Gathered -> ")) or 0
    sharpShards = int(input("Sharp Crystal Shard Gathered -> ")) or 0
    hardShards = int(input("Hard Crystal Shard Gathered -> ")) or 0
    spiritDust = int(input("Ancient Spirit Dust Gathered -> ")) or 0
    fairyPowder = int(input("Fairy's Powder Gathered -> ")) or 0
    blackGemFrags = int(input("Black Gem Fragment Gathered -> ")) or 0

    redMeatSilver = materialPrices["Red Meat"] * redMeat
    caphrasStoneSilver = materialPrices["Caphras Stone"] * caphrasStones
    sharpShardSilver = materialPrices["Sharp Crystal Shard"] * sharpShards
    hardShardSilver = materialPrices["Hard Crystal Shard"] * hardShards
    spiritDustSilver = materialPrices["Ancient Spirit Dust"] * spiritDust
    fairyPowderSilver = materialPrices["Fairy's Powder"] * fairyPowder
    blackGemFragSilver = materialPrices["Black Gem Fragment"] * blackGemFrags

    print(redMeatSilver)
    print(caphrasStoneSilver)
    print(sharpShardSilver)
    print(hardShardSilver)
    print(spiritDustSilver)
    print(fairyPowderSilver)
    print(blackGemFragSilver)

    totalTaxedSilver = (redMeatSilver + caphrasStoneSilver + sharpShardSilver + hardShardSilver + spiritDustSilver + blackGemFragSilver)*0.845 + fairyPowderSilver


    totalTime = input("Input the time it took you to gather those materials -> ")
    print("##################################")
    print("total(taxed): ", totalTaxedSilver)
    print("Your income per hour is: ", getSilverPerHour(totalTaxedSilver, totalTime))

def getSilverPerHour(totalTaxedSilver, totalTime):
    return 60*int(totalTaxedSilver)/int(totalTime)

def main():
    calculateIncome()

if __name__ == "__main__":
    main()