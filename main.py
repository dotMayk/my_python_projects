import art
import os

bids = {}

noMoreBids = False


def HighestBidder(bidRecord):
    highestBid = 0
    winner = ""
    for bidder in bidRecord:
        bidAmount = bidRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    os.system('clear')
    print(art.logo)
    print("")
    print(f"The winner is {winner} with a bid of ${highestBid}.")


while not noMoreBids:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    toContinue = input("Are there any other bidders? (Y/N): ").lower()
    if toContinue == 'n':
        noMoreBids = True
        HighestBidder(bids)
    else:
        art.logo
        os.system('clear')
