import json
from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from typing import List
from math import *
import asyncio
import pandas as pd
import csv
from ast import literal_eval
import asyncio
import time
import requests
import math

import  aiohttp

start_time = time.time()
#Connect Ethereum node 
# ganache_url = "http://127.0.0.1:8545"
# web3 = Web3(Web3.HTTPProvider(ganache_url)) 
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
import os
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
headers = {'Content-type': 'application/json'}


async def extractHolder():
    async with aiohttp.ClientSession() as session:
        with open("event.json", 'r') as event_file:
            # returns JSON object as a dictionary
            data = json.load(event_file)
            print(len(data))
            latestBlock = web3.eth.blockNumber
            # account = {latestBlock: {}}        
            blkNumber = {latestBlock: {'blockNumber' : latestBlock}}
            account = {'latestBalanceBlock' : latestBlock, 'blockNumber': blkNumber}
            iterations = 0
            for event in data:
                addressFrom = data[event]["args"]["from"]
                addressTo = data[event]["args"]["to"]
                y = {addressFrom:0}
                z = {addressTo:0}
                account['blockNumber'][latestBlock].update(y)
                account['blockNumber'][latestBlock].update(z)
            # for add in account['blockNumber'][latestBlock]:
            #     if add == "blockNumber":
            #         continue
            # z =[session.post("https://mainnet.infura.io/v3/0866de87b4de4c7f843156d964c88c0a", json=payload_call, headers=headers) for add in account]
            # responses = await asyncio.gather(*z)
            # results =[]
            # for response in responses:
            #     results.append(await response.json())
            # print(results)
            #     task1 = asyncio.create_task(getBalance(account, add, latestBlock))
            # await(task1)      
            #     tasks.append(asyncio.create_task(getBalance(account, add, latestBlock)))
            # await asyncio.gather(*tasks)  
            results = []
            tasks = getBalance(account,latestBlock,session)  
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(await response.json())
                results.append(await response.json())
            print("append_done")
            for result in results:
                print(literal_eval(result['result']))
            i = 0
            for add in account['blockNumber'][latestBlock]:
                if add == "blockNumber":
                    continue
                account['blockNumber'][latestBlock][add] = literal_eval(results[i]['result'])
                i+=1


            with open("balance.json", 'w') as balance_file:
                json.dump((account), balance_file, indent=4)
            balance_file.close()
            with open("balanceNew.json", 'w') as balance_file:
                json.dump((account), balance_file, indent=4)
            balance_file.close()
        event_file.close()
        print("Done Extract Holder Balance")

def getBalance(account, latestBlock, session):
    tasks = []
    # y = proxyContract.functions.balanceOf(add).call()
    # await asyncio.sleep(5)
    for add in account['blockNumber'][latestBlock]:
        print(add)
        add = add.replace('0x', '')
        # print(add.replace('0x', ''))
        params_call = [{"to":"0x0fd10b9899882a6f2fcb5c371e17e70fdee00c38","from":"0x6b175474e89094c44da98b954eedeac495271d0f","data":f"0x70a08231000000000000000000000000{add}"},"latest"]
        payload_call= {"jsonrpc":"2.0",
           "method":"eth_call",
           "params":params_call,
           "id":1}
        if add == "blockNumber":
            continue
        tasks.append(session.post("https://mainnet.infura.io/v3/0866de87b4de4c7f843156d964c88c0a", json=payload_call, headers=headers))
    # print(tasks)
    return tasks
    # account['blockNumber'][latestBlock][add] = y



# #############################################################################################################
# Revert transaction history
# #############################################################################################################
def revertTransaction(targetRevertBlk):
    with open("balance.json", 'r') as balance_file:
        oridataBalance = json.load(balance_file)
        lastEventBlock = oridataBalance["latestBalanceBlock"]
        print(lastEventBlock)
    
    balance_file.close()
    if targetRevertBlk > lastEventBlock:
        print("target revert block bigger than latest balance block in transfer event database")
        return

    addList = oridataBalance["blockNumber"][str(lastEventBlock)]

    with open("event_transfer_balance.csv", 'w', newline='') as csv_balancefile:
        # writer = csv.writer(data_balancefile)
        # items = dataBalance["blockNumber"][str(lastEventBlock)].items()
        # writer.writerow([key for key, value in items])
        # writer.writerow([value for key, value in items])

        addData = [oridataBalance["blockNumber"][str(lastEventBlock)]]
        csv_writer = csv.DictWriter(csv_balancefile, fieldnames=addList)
        csv_writer.writeheader()
        for add in addData:
            # print(add)
            csv_writer.writerow(add)         

    csv_balancefile.close()

    with open("balanceNew.json", 'w') as balance_file:
        json.dump(oridataBalance, balance_file, indent=4)

    # with open("targetbalance.json", 'w') as targetbalance_file:
    #     json.dump({}, targetbalance_file, indent=4)
    # targetbalance_file.close()
    # print("Done Revert Holder Balance")

    with open("target_balance.csv", 'w', newline='') as csv_balancefile:

        csv_writer = csv.DictWriter(csv_balancefile, fieldnames=addList)
        csv_writer.writeheader()        

    csv_balancefile.close()

    with open("avg_balance.csv", 'w', newline='') as csv_balancefile:

        csv_writer = csv.DictWriter(csv_balancefile, fieldnames=addList)
        csv_writer.writeheader()        

    csv_balancefile.close()


    with open("event.json", 'r') as event_file:
        data = json.load(event_file)
        i = len(data)
        print(i)
        ## Get event data from latest to oldest
        for index in range(len(data)):
            addressFrom = data[f"event{i-1}"]["args"]["from"]
            addressTo = data[f"event{i-1}"]["args"]["to"]
            value = data[f"event{i-1}"]["args"]["value"]
            eventblocknumber = data[f"event{i-1}"]["blockNumber"]

            if targetRevertBlk > eventblocknumber:
                break

            with open("balanceNew.json", 'r') as balance_file:
                dataBalance = json.load(balance_file)
                latestBlock = dataBalance['latestBalanceBlock']
                newBlkNumber = {eventblocknumber: dataBalance['blockNumber'][f"{lastEventBlock}"]}
                dataBalance = {'latestBalanceBlock' : latestBlock, 'blockNumber': newBlkNumber}
            balance_file.close()

            # print("....")

            with open("balanceNew.json", 'w') as balancefile:
                json.dump(dataBalance, balancefile, indent=4)
            balancefile.close()

            with open("balanceNew.json", 'r') as balance_file:
                dataBalance = json.load(balance_file)
            dataBalance['blockNumber'][f"{eventblocknumber}"]["blockNumber"] = eventblocknumber   
            dataBalance['blockNumber'][f"{eventblocknumber}"][addressTo] -= value
            dataBalance['blockNumber'][f"{eventblocknumber}"][addressFrom] += value

            with open("balanceNew.json", 'w') as balance_file:
                json.dump(dataBalance, balance_file, indent=4)

            addList = dataBalance["blockNumber"][str(eventblocknumber)]
            with open("event_transfer_balance.csv", 'a', newline='') as csv_balancefile:
                # writer = csv.writer(data_balancefile)
                # items = dataBalance["blockNumber"][str(lastEventBlock)].items()
                # writer.writerow([key for key, value in items])
                # writer.writerow([value for key, value in items])

                addData = [dataBalance["blockNumber"][str(eventblocknumber)]]
                csv_writer = csv.DictWriter(csv_balancefile, fieldnames=addList)
                # csv_writer.writeheader()
                for add in addData:
                    # print(add)
                    csv_writer.writerow(add)        

            csv_balancefile.close()
            
            lastEventBlock = data[f"event{i-1}"]["blockNumber"]
            print(lastEventBlock)
            i -= 1

    event_file.close()

    print("Done Revert transaction Holder Balance")

# #############################################################################################################
# Check Holder Balance at history block 
# #############################################################################################################
def checkBalance(checkBlkNum, revertEndblk ,blockGap, iterations):
    
    if checkBlkNum < revertEndblk:
        print("target block is out of the range")
        return
    i = 0
    with open("event_transfer_balance.csv", 'r', newline='') as csv_balancefile:
        csv_reader = csv.DictReader(csv_balancefile)        

        print(checkBlkNum)
        for rows in csv_reader:
            block = rows["blockNumber"]
            print(block)
            if checkBlkNum < int(block):
                continue
            else:
                targetBlk = block
                targetBalance = rows

                with open("target_balance.csv", 'a', newline='') as csv_balancefile:
                    csv_writer = csv.DictWriter(csv_balancefile, fieldnames=targetBalance)
                    csv_writer.writerow(targetBalance)
                csv_balancefile.close()

                checkBlkNum -= blockGap
                i+=1
                if i >= iterations:
                    break
                continue
        print(targetBlk)  

    
    # for i in range(iterations):
    #     print(i)
    #     if checkBlkNum < revertEndblk:
    #         print("target block is out of the range")
    #         return

    #     with open("event_transfer_balance.csv", 'r', newline='') as csv_balancefile:
    #         csv_reader = csv.DictReader(csv_balancefile)        
 
    #         print(checkBlkNum)
    #         for rows in csv_reader:
    #             block = rows["blockNumber"]
    #             print(block)
    #             if checkBlkNum < int(block):
    #                 continue
    #             else:
    #                 targetBlk = block
    #                 targetBalance = rows
    #                 break
    #         print(targetBlk)  

    #     with open("target_balance.csv", 'a', newline='') as csv_balancefile:
    #         csv_writer = csv.DictWriter(csv_balancefile, fieldnames=targetBalance)
    #         csv_writer.writerow(targetBalance)
    #     csv_balancefile.close()
    #     print("xxx")
    #     checkBlkNum -= blockGap


    # for i in range(iterations):
    #     print(i)

    print("Done extract target balance")


# #############################################################################################################
# Calculate average Holder Balance for a priod
# #############################################################################################################
# fromBlock, toBlock, intervalBlk
def calAvgBalance():

    with open("target_balance.csv", 'r', newline='') as csv_balancefile:
        balanceList = []
        blkList = []
        csv_reader = csv.DictReader(csv_balancefile)  
        addList = csv_reader.fieldnames
        # print(addList)
        for balances in csv_reader:
            balanceList.append(balances)
        print(len(balanceList))

    avgbalance = {}
    with open("avg_balance.csv", 'a', newline='') as avg_balancefile:
        csv_writer = csv.DictWriter(avg_balancefile, addList)
        print("...")
        for add in addList:
            # print(add)
            balanceAdd = 0
            for balances in balanceList:                
                balanceAdd += int(balances[add])               
            balanceAdd //= len(balanceList)
            print(balanceAdd)
            z = {add:balanceAdd}
            avgbalance.update(z)
        csv_writer.writerow(avgbalance)
    
    with open("avgbalance.json", 'w') as avgbalance_file:
        json.dump((avgbalance), avgbalance_file, indent=4)

    print("Done calc avg balance")


    # with open("targetbalance.json", 'r') as targetbalance_file:
    #     targetBalanceJson = json.load(targetbalance_file)
    #     blkList = []
    #     for item in targetBalanceJson:
    #         y = item
    #         blkList.append(int(y))
    #     dataAddress = targetBalanceJson[str(blkList[0])]
    #     addList = dataAddress.keys()
    #     keys = []
    #     for add in addList:
    #         keys.append(add)
    #     i=0 
    #     dataAddresses = {} 
    #     for blk in blkList:
    #         dataAddresses[i] = targetBalanceJson[str(blkList[i])]
    #         i+=1
    #     avgBalance = {}
    #     for key in keys:
    #         avgBalance[key] = 0
    #         for index in range(i):
    #             avgBalance[key] += dataAddresses[index][key]
    #             print(avgBalance[key])
    #         avgBalance[key] /= i
    #     print(avgBalance)
    # targetbalance_file.close()
    # with open("avgbalance.json", 'w') as avgbalance_file:
    #     json.dump((avgBalance), avgbalance_file, indent=4)
    # avgbalance_file.close()

pd.options.display.float_format = '{:.4f}'.format
# #############################################################################################################
# Calculate final average Holder list exclude 0 value for a priod
# #############################################################################################################         
def getFinalHolderBalanceList():
    with open("target_balance.csv", 'r', newline='') as csv_balancefile:
        balanceList = []
        csv_reader = csv.DictReader(csv_balancefile)  
        addList = csv_reader.fieldnames

    avgbalance = {}
    with open("avgbalance.json", 'r') as avgbalance_file:
        avgBalanceJson = json.load(avgbalance_file)
        for add in addList:
            balance = avgBalanceJson[add]
            if balance != 0:
                
                balance = balance * 8.93061
                # print(balance)
                balance = f"{math.trunc(balance)}"
                print((balance))

                z = {add:balance}
                avgbalance.update(z)

    with open("avgfinalbalance.json", 'w') as avgbalance_file:
        json.dump((avgbalance), avgbalance_file, indent=4)



    print("Done calc avg final balance")

# #############################################################################################################
# get final average Holder list for keys and value in array
# #############################################################################################################  
def getFinalHolderBalancekey_value():
    with open("avgfinalbalance.json", 'r') as avgfinalbalance_file:
        avgfinalBalanceJson = json.load(avgfinalbalance_file)
        keys = list(avgfinalBalanceJson.keys())
        values = list(avgfinalBalanceJson.values())
        # print(keys)
    with open("avgfinalbalancekey.json", 'w') as avgbalance_file:
        json.dump((keys), avgbalance_file, indent=4)
    with open("avgfinalbalancevalue.json", 'w') as avgbalance_file:
        json.dump((values), avgbalance_file, indent=4)

# #############################################################################################################
# Main code
# #############################################################################################################
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run((extractHolder()))
# print("--- %s seconds ---" % (time.time() - start_time))

# async def main():
def main():
    xInitializeBlk = 11995475     #(Apr-04-2021 08:59:52 PM +UTC) contract created time
    revertStartblk = 12678020       # (Jun-21-2021 02:00:09 PM +UTC)
    revertEndblk = 12678020  
    revertTargetStartblk = 13410485   # (Oct-13-2021 02:21:14 PM +UTC) Before PundiX chain go live
#     # blk = web3.eth.blockNumber - 1000
#     # toBlock = xInitializeBlk +170500
#     # latestblk = web3.eth.blockNumber
    # queryEvent(xInitializeBlk, "latest" )
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # asyncio.run((extractHolder()))
#     # task1 = asyncio.create_task(extractHolder())
#     # await task1
    # revertTransaction(revertStartblk)
    checkBalance(revertTargetStartblk, revertEndblk ,5760, 116)
    calAvgBalance()
    getFinalHolderBalanceList()
    getFinalHolderBalancekey_value()


if __name__ == "__main__":     # __name__ is a built-in variable in Python which evaluates to the name of the current module.
    main()

# if __name__ == '__main__':
#     try:
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(main())
#         # d1, d2 = loop.run_until_complete(main())     #d1 is result object, not result
#         # print(d1.result())
#         print("--- %s seconds ---" % (time.time() - start_time))
#     except Exception as e:
#         pass
#     finally:
#         loop.close()