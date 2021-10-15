import json
from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from typing import List
from math import *
import asyncio

from aiohttp import ClientSession

#Connect Ethereum node 
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url)) 
infuraKey = '0866de87b4de4c7f843156d964c88c0a'
infura = "https://mainnet.infura.io/v3/"+infuraKey
web3 = Web3(Web3.HTTPProvider(infura))  
 
# web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.functionx.io"))
print(web3.isConnected())
print(web3.eth.blockNumber)
latestBlk = web3.eth.blockNumber

# Load ERC20 Smart Contract

xAbi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"transferAndCall","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenContractAddress","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferERCToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
xAddress = "0x4daA3c4c0a253C1E6c6FCb0705e5C64D21CF9c59"
proxyAbi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"address","name":"_admin","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"initialize","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"initialize","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"}]')
proxyAddress = "0x0FD10b9899882a6f2fcb5c371E17e70FdEe00C38"
proxyContract = web3.eth.contract(address=proxyAddress, abi=xAbi)
xContract = web3.eth.contract(address=xAddress, abi=xAbi)
print(proxyContract)
totalSupply = proxyContract.functions.totalSupply().call(block_identifier= 'latest')
print(web3.fromWei(totalSupply, 'ether'))
print(proxyContract.functions.name().call())
print("......")

# ##########################################################################################################
# Query ERC20 transfer event
# ##########################################################################################################
def queryEvent(_fromBlock, _toBlock):
# receipt = web3.eth.get_transaction_receipt("0x59c4f19ea4a6af4876f617419b812248bae8c5d915db5b6cc67ded5ede7ff593")   # or use tx_hash deifined on above command line
# event = proxyContract.events.Transfer().processReceipt(receipt, errors= DISCARD)
    if _toBlock == "latest":
        _toBlock = web3.eth.blockNumber
        print(_toBlock)
    numOfBlk = _toBlock - _fromBlock
    iterationBlk = 15000
    queryIteration = numOfBlk // iterationBlk
    i=0
    z = {}
    toBlkIteration = _fromBlock -1
    print(toBlkIteration)
    for index in range(queryIteration):
        fromBlkIteration = _fromBlock + iterationBlk*(index)
        print(fromBlkIteration)
        toBlkIteration = _fromBlock + iterationBlk*(index+1) -1
        print(toBlkIteration)
        eventfilter = proxyContract.events.Transfer.createFilter(fromBlock= fromBlkIteration , toBlock= toBlkIteration)
        eventlist = eventfilter.get_all_entries()
        for event in eventlist:
            y = json.loads(Web3.toJSON(event))
            y = {'event'+str(i): y}
            z.update(y)
            i += 1
    
    lastfromBlk = toBlkIteration + 1
    eventfilter = proxyContract.events.Transfer.createFilter(fromBlock= lastfromBlk , toBlock= _toBlock)
    eventlist = eventfilter.get_all_entries()

    for event in eventlist:
        # print(event)
        y = json.loads(Web3.toJSON(event))
        y = {'event'+str(i): y}
        z.update(y)
        i += 1
    
    # print(z)
    with open("event.json", 'w') as event_file:
        json.dump((z), event_file, indent=4)
    event_file.close()
    print("Done Query Events")


# ###########################################################################################################
# Extract token holder list and balance
# ###########################################################################################################
def extractHolder():
# with open("events.json", 'r') as balance_file:
#     # returns JSON object as a dictionary
#     data = json.load(balance_file)
#     data = json.loads(data)
#     print(data["args"]["from"])
# balance_file.close()

    with open("event.json", 'r') as event_file:
        # returns JSON object as a dictionary
        data = json.load(event_file)
        print(len(data))
        latestBlock = web3.eth.blockNumber
        # account = {latestBlock: {}}        
        blkNumber = {latestBlock: {}}
        account = {'latestBalanceBlock' : latestBlock, 'blockNumber': blkNumber}
        iterations =0
        for event in data:
            addressFrom = data[event]["args"]["from"]
            addressTo = data[event]["args"]["to"]
            # y = {addressFrom:proxyContract.functions.balanceOf(addressFrom).call() }
            # z = {addressTo:proxyContract.functions.balanceOf(addressTo).call() }
            y = {addressFrom:0}
            z = {addressTo:0}
            account['blockNumber'][latestBlock].update(y)
            account['blockNumber'][latestBlock].update(z)
        for add in account['blockNumber'][latestBlock]:
            # print(add)
            # y = proxyContract.functions.balanceOf("0x5C45526BF984d1D76E2eE03C4cb70fc4919CcBbA").call()
            # print(y)
            y = proxyContract.functions.balanceOf(add).call()
            # print(y)
            account['blockNumber'][latestBlock][add] = y
            # print(account['blockNumber'][latestBlock][add])
            print(iterations)
            iterations +=1

        with open("balance.json", 'w') as balance_file:
            json.dump((account), balance_file, indent=4)
        balance_file.close()
        with open("balanceNew.json", 'w') as balance_file:
            json.dump((account), balance_file, indent=4)
        balance_file.close()
    event_file.close()
    print("Done Extract Holder Balance")


# #############################################################################################################
# Revert transaction history
# #############################################################################################################
def revertTransaction():
    with open("balanceNew.json", 'r') as balance_file:
        dataBalance = json.load(balance_file)
        lastEventBlock = dataBalance["latestBalanceBlock"]
        print(lastEventBlock)
    balance_file.close()    
    with open("event.json", 'r') as event_file:
        data = json.load(event_file)
        i = len(data)
        for index in range(len(data)):
            print(i)
            addressFrom = data[f"event{i-1}"]["args"]["from"]
            addressTo = data[f"event{i-1}"]["args"]["to"]
            value = data[f"event{i-1}"]["args"]["value"]
            latestblocknumber = data[f"event{i-1}"]["blockNumber"]
            with open("balanceNew.json", 'r') as balance_file:
                dataBalance = json.load(balance_file)
                newBlkNumber = {latestblocknumber: dataBalance['blockNumber'][f"{lastEventBlock}"]}
                dataBalance['blockNumber'].update(newBlkNumber)
            balance_file.close()

            print("....")

            with open("balanceNew.json", 'w') as balancefile:
                json.dump(dataBalance, balancefile, indent=4)
            balancefile.close()

            with open("balanceNew.json", 'r') as balance_file:
                dataBalance = json.load(balance_file)
            dataBalance['blockNumber'][f"{latestblocknumber}"][addressTo] -= value
            dataBalance['blockNumber'][f"{latestblocknumber}"][addressFrom] += value

            with open("balanceNew.json", 'w') as balance_file:
                json.dump(dataBalance, balance_file, indent=4)
            
            lastEventBlock = data[f"event{i-1}"]["blockNumber"]
            print(lastEventBlock)    
            i -= 1

    event_file.close()

    with open("targetbalance.json", 'w') as targetbalance_file:
        json.dump({}, targetbalance_file, indent=4)
    targetbalance_file.close()
    print("Done Revert Holder Balance")


# #############################################################################################################
# Check Holder Balance at history block 
# #############################################################################################################
def checkBalance(checkBlkNum):
    with open("balanceNew.json", 'r') as balance_file:
        dataBalance = json.load(balance_file)
        datablkNumber = dataBalance["blockNumber"]
        blkList = []
        for item in datablkNumber:
            x = item
            blkList.insert(0,int(x))
        print(blkList)
        for blk in blkList:
            if checkBlkNum >= blk:
                targetBlk = blk
            else:
                break
        print(targetBlk)
        targetBalance = dataBalance["blockNumber"][str(targetBlk)]
        print(targetBalance)     
        
    balance_file.close()

    with open("targetbalance.json", 'r') as targetbalance_file:
        targetBalanceJson = json.load(targetbalance_file)  
        newTargetBalanceJson = {targetBlk: {}}
        targetBalanceJson.update(newTargetBalanceJson)
        targetBalanceJson[targetBlk].update(targetBalance)
    targetbalance_file.close()

    with open("targetbalance.json", 'w') as targetbalance_file:
        json.dump((targetBalanceJson), targetbalance_file, indent=4)
    targetbalance_file.close()


# #############################################################################################################
# Calculate average Holder Balance for a priod
# #############################################################################################################
# fromBlock, toBlock, intervalBlk
def calAvgBalance():
    with open("targetbalance.json", 'r') as targetbalance_file:
        targetBalanceJson = json.load(targetbalance_file)
        blkList = []
        for item in targetBalanceJson:
            y = item
            blkList.append(int(y))
        dataAddress = targetBalanceJson[str(blkList[0])]
        addList = dataAddress.keys()
        keys = []
        for add in addList:
            keys.append(add)
        i=0 
        dataAddresses = {} 
        for blk in blkList:
            dataAddresses[i] = targetBalanceJson[str(blkList[i])]
            i+=1
        avgBalance = {}
        for key in keys:
            avgBalance[key] = 0
            for index in range(i):
                avgBalance[key] += dataAddresses[index][key]
                print(avgBalance[key])
            avgBalance[key] /= i
        print(avgBalance)
    targetbalance_file.close()
    with open("avgbalance.json", 'w') as avgbalance_file:
        json.dump((avgBalance), avgbalance_file, indent=4)
    avgbalance_file.close()

# #############################################################################################################
# Main code
# #############################################################################################################


xInitializeBlk = 11995660     #147 days 21 hrs ago (Mar-08-2021 04:21:39 +UTC)
blk = web3.eth.blockNumber - 1000
toBlock = xInitializeBlk +170500
latestblk = web3.eth.blockNumber
startblk = latestblk -300
# queryEvent(startblk, "latest" )
# extractHolder()
revertTransaction()
# checkBalance(12949488)
# checkBalance(12949488)
# checkBalance(12949560)
# calAvgBalance()