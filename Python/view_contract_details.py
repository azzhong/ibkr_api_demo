from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.contract import ContractDetails

import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print(f'Error, reqId = {reqId}, errorCode = {errorCode}, errorString = {errorString}')

    def contractDetails(self, reqId:int, contractDetails:ContractDetails):
        print(f'reqId = {reqId}, contractDetails = {contractDetails}')


app = TradingApp()
app.connect('127.0.0.1',  7497, clientId=2)


contract = Contract()
contract.symbol = 'AAPL'
contract.secType = 'STK'
contract.currency = 'USD'
contract.exchange = 'SMART'


def websocketConnect():
    app.run()

connThread = threading.Thread(target=websocketConnect, daemon=True)
connThread.start()
print('waiting connection...')
time.sleep(1)

app.reqContractDetails(10, contract)
print('waiting contract details...')
time.sleep(5)
app.disconnect()
print('app disconnected')
connThread.join()
print('done')



