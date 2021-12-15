import json
from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from typing import List
from math import *
import pandas as pd
import csv
from ast import literal_eval
import time

start_time = time.time()
#Connect Ethereum node 
# ganache_url = "http://127.0.0.1:8545"
# web3 = Web3(Web3.HTTPProvider(ganache_url)) 
infuraKey = 'e4736089aa4c4c40a260e06af316a7a9'
infura = "https://mainnet.infura.io/v3/"+infuraKey
# ethrpc = "wss://speedy-nodes-nyc.moralis.io/01143cdca68914e18b964873/eth/mainnet/archive/ws"
# bscrpc = "wss://speedy-nodes-nyc.moralis.io/01143cdca68914e18b964873/bsc/mainnet/ws"
bscrpc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bscrpc))  
# web3 = Web3(Web3.WebsocketProvider(bscrpc))
 
# web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.functionx.io"))
print(web3.isConnected())
print(web3.eth.blockNumber)
latestBlk = web3.eth.blockNumber

# Load PURSE Smart Contract

purseAbi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"_averageInterval","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_getRewardEndTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_getRewardStartTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_lastRewardStartTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_monthlyDistributePr","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_numOfDaysPerMth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_percentageDistribute","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"accAmount","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"accReward","type":"uint256"},{"internalType":"uint256","name":"lastUpdateTime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_rewardStartTime","type":"uint256"},{"internalType":"uint256","name":"_rewardEndTime","type":"uint256"},{"internalType":"uint256","name":"_monthlyDisPr","type":"uint256"},{"internalType":"uint256","name":"_numOfDays","type":"uint256"},{"internalType":"uint256","name":"_percentage","type":"uint256"}],"name":"activateClaimMonthly","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"addAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"admins","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"burnPercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimDistributionPurse","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"disPercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"disPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"address","name":"_lPool","type":"address"},{"internalType":"uint256","name":"_burnPercent","type":"uint256"},{"internalType":"uint256","name":"_liqPercent","type":"uint256"},{"internalType":"uint256","name":"_disPercent","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isWhitelistedFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isWhitelistedTo","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liqPercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liqPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minimumSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"removeAdmin","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newWhitelist","type":"address"}],"name":"removeWhitelistedFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newWhitelist","type":"address"}],"name":"removeWhitelistedTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newWhitelist","type":"address"}],"name":"setWhitelistedFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newWhitelist","type":"address"}],"name":"setWhitelistedTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"transferERCToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newDPool","type":"address"}],"name":"updateDPoolAdd","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newLPool","type":"address"}],"name":"updateLPoolAdd","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minimumSupply","type":"uint256"}],"name":"updateMinimumSupply","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newDisPercent","type":"uint256"},{"internalType":"uint256","name":"_newLiqPercent","type":"uint256"},{"internalType":"uint256","name":"_newBurnPercent","type":"uint256"}],"name":"updatePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"}]')
purseAddress = '0x29a63F4B209C29B4DC47f06FFA896F32667DAD2C'
proxyContract = web3.eth.contract(address=purseAddress, abi=purseAbi)

print(proxyContract)
totalSupply = proxyContract.functions.totalSupply().call(block_identifier= 'latest')
print(web3.fromWei(totalSupply, 'ether'))
print(proxyContract.functions.name().call())
print("......")

# ##########################################################################################################
# Query ERC20 transfer event
# ##########################################################################################################
def queryEvent(_fromBlock, _toBlock, i):
# receipt = web3.eth.get_transaction_receipt("0x59c4f19ea4a6af4876f617419b812248bae8c5d915db5b6cc67ded5ede7ff593")   # or use tx_hash deifined on above command line
# event = proxyContract.events.Transfer().processReceipt(receipt, errors= DISCARD)
    if _toBlock == "latest":
        _toBlock = web3.eth.blockNumber
        print(_toBlock)
    numOfBlk = _toBlock - _fromBlock
    iterationBlk = 500
    queryIteration = numOfBlk // iterationBlk
    z = {}
    toBlkIteration = _fromBlock -1
    print(toBlkIteration)
    for index in range(queryIteration):
        fromBlkIteration = _fromBlock + iterationBlk*(index)
        print(fromBlkIteration)
        toBlkIteration = _fromBlock + iterationBlk*(index+1) -1
        print(toBlkIteration)
        eventfilter = proxyContract.events.Burn.createFilter(fromBlock= fromBlkIteration , toBlock= toBlkIteration)
        eventlist = eventfilter.get_all_entries()
        for event in eventlist:
            # print(event)
            y = json.loads(Web3.toJSON(event))
            y = {'event'+str(i): y}
            i += 1
            print(y)
            with open("purseEvent.json", 'r+') as event_file:
                event_file_data = json.load(event_file)
                event_file_data.update(y)
                event_file.seek(0)
                json.dump((event_file_data), event_file, indent=4)
            event_file.close()

    lastfromBlk = toBlkIteration + 1
    eventfilter = proxyContract.events.Burn.createFilter(fromBlock= lastfromBlk , toBlock= _toBlock)
    eventlist = eventfilter.get_all_entries()

    for event in eventlist:
        # print(event)
        y = json.loads(Web3.toJSON(event))
        y = {'event'+str(i): y}
        i += 1
    
        with open("purseEvent.json", 'r+') as event_file:
            event_file_data = json.load(event_file)
            event_file_data.update(y)
            event_file.seek(0)
            json.dump((event_file_data), event_file, indent=4)
        event_file.close()
    # with open("purseEvent.json", 'r+') as event_file:
    #     json.dump((z), event_file, indent=4)
    # event_file.close()
    print("Done Query Events")


# ###########################################################################################################
# Extract token holder list and balance
# ###########################################################################################################

def extractBurnAmount():
    with open("purseEvent.json", 'r') as event_file:
        # returns JSON object as a dictionary
        data = json.load(event_file)
        # latestBlock = web3.eth.blockNumber
        # account = {latestBlock: {}}
        blkNumber = {}
        account = {'blockNumber': blkNumber}
        i = 0
        for event in data:
            amount = data[event]["args"]["_value"]
            blockNumber = data[event]["blockNumber"]
            # y = {addressFrom:0}
            z = {i:{blockNumber:amount}}
            account['blockNumber'].update(z)
            i += 1

        with open("burnAmount.json", 'w') as balance_file:
            json.dump((account), balance_file, indent=4)
        balance_file.close()

def calcSum():
    with open("burnAmount.json", 'r') as event_file:
        data = json.load(event_file)
        data2 = data["blockNumber"]
        y=0
        i=0
        for event in data2:
            data3 = data["blockNumber"][event]
            for event2 in data3:
                print(event2)
                z= data["blockNumber"][event][event2]
                print(z)
                y= y+z
                i+=1

    with open("totalburnAmount.json", 'w') as balance_file:
        totalBurnAmount = {"totalBurnAmount":y}
        json.dump((totalBurnAmount), balance_file, indent=4)

# #############################################################################################################
# Check Holder Balance at history block 
# #############################################################################################################
def checkBalance(checkBlkNum, revertEndblk ,blockGap, iterations):
    
    if checkBlkNum < revertEndblk:
        print("target block is out of the range")
        return
    i = 0

    with open("burnAmount.json", 'r') as event_file:
        data = json.load(event_file)
        data2 = data["blockNumber"]
        y=0
        z = {}
        for event in reversed(data2):
            data3 = data["blockNumber"][event]
            for event2 in data3:
                if checkBlkNum-blockGap*iterations < int(event2):
                    targetBlk = event
                    targetBalance = data["blockNumber"][event]
                    y = {targetBlk: targetBalance}
                    z.update(y)
                else: 
                    break

        with open("targetBurnAmount.json", 'w') as event_file:
            json.dump((z), event_file, indent=4)
        event_file.close()

    print("Done extract target balance")

# #############################################################################################################
# Calculate average Holder Balance for a priod
# #############################################################################################################
# fromBlock, toBlock, intervalBlk
def calSum30Balance():

    with open("targetBurnAmount.json", 'r') as target_file:
        data = json.load(target_file)
        print(len(data))
        y = 0
        for event in data:
            data3 = data[event]
            for event2 in data3:
                z= data[event][event2]
                print(z)
                y= y+z

    with open("sum30BurnAmount.json", 'w') as balance_file:
        sum30BurnAmount = {"sum30BurnAmount":y}
        json.dump((sum30BurnAmount), balance_file, indent=4)







# #############################################################################################################
# Main code
# #############################################################################################################
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run((extractHolder()))
# print("--- %s seconds ---" % (time.time() - start_time))

# async def main():
def main():
    #11732360 57 days 18 hrs ago (Oct-13-2021 09:01:59 AM +UTC) Purse contract created time

    purseInitializeBlk = 13384157     

    queryEvent(purseInitializeBlk, "latest", 2130 )
    extractBurnAmount()
    calcSum()
    checkBalance(purseInitializeBlk, 0 ,28000, 30)
    calSum30Balance()
#     getFinalHolderBalanceList()
#     getFinalHolderBalancekey_value()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":     # __name__ is a built-in variable in Python which evaluates to the name of the current module.
    main()
