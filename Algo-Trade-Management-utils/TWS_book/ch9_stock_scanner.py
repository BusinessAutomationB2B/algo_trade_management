from ibapi.client import EClient
from ibapi.contract import Contract
from ibapi.scanner import ScannerSubscription
from ibapi.tag_value import TagValue
from ibapi.wrapper import EWrapper
import time
from datetime import datetime
from ibapi.utils import iswrapper
from threading import Thread

class StockScanner(EWrapper, EClient):
    '''Serves as the client and the wrapper'''
    def __init__(self, addr, port, client_id):
        EWrapper.__init__(self)
        EClient. __init__(self, self)

        # Connect to TWS
        self.connect(addr, port, client_id)
        self.count = 0

        # Launch the client thread
        thread = Thread(target=self.run)
        thread.start()

    @iswrapper
    def scannerData(self, reqId, rank, details,distance, benchmark, projection, legsStr):
        # Print the symbols in the returned results
        print('{}: {}'.format(rank,details.contract.symbol))
        self.count += 1

    @iswrapper
    def scannerDataEnd(self, reqId):
        # Print the number of results
        print('Number of results:{}'.format(self.count))

    @iswrapper
    def error(self, reqId, code, msg):
        print('Error {}: {}'.format(code, msg))

def main():
    # Create the client and connect to TWS
    client = StockScanner('127.0.0.1', 7497, 0)
    time.sleep(0.5)# Create the ScannerSubscription object
    ss = ScannerSubscription()
    ss.instrument = 'STK'
    ss.locationCode = 'STK.US.MAJOR'
    ss.scanCode = 'HOT_BY_VOLUME'

    # Set additional filter criteria
    tagvalues = []
    tagvalues.append(TagValue('avgVolumeAbove','500000'))
    tagvalues.append(TagValue('marketCapAbove1e6','10'))

    # Request the scanner subscription
    client.reqScannerSubscription(0, ss, [],tagvalues)

    # Sleep while the request is processed
    time.sleep(5)
    client.disconnect()

if __name__ == '__main__':
    main()