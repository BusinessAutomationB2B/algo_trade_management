from ibapi.client import EClient
from ibapi.contract import Contract
from ibapi.wrapper import EWrapper
import time
from datetime import datetime
from ibapi.utils import iswrapper
from threading import Thread


class MarketReader(EWrapper, EClient):
    '''Serves as the client and the wrapper'''

    def __init__(self, addr, port, client_id):
        EWrapper.__init__(self)
        EClient. __init__(self, self)

        # Connect to TWS
        self.connect(addr, port, client_id)

        # Launch the client thread
        thread = Thread(target=self.run)
        thread.start()

    @iswrapper
    def tickByTickMidPoint(self, reqId, tick_time,midpoint):
        '''Called in response to reqTickByTickData'''
        print('tickByTickMidPoint - Midpoint tick:{}'.format(midpoint))

    @iswrapper
    def tickPrice(self, reqId, field, price, attribs):
        '''Called in response to reqMktData'''
        print('tickPrice - field: {}, price:{}'.format(field,price))

    @iswrapper
    def tickSize(self, reqId, field, size):
        '''Called in response to reqMktData'''
        print('tickSize - field: {}, size:{}'.format(field,size))

    @iswrapper
    def realtimeBar(self, reqId, time, open, high,low,close, volume, WAP, count):
        '''Called in response to reqRealTimeBars'''
        print('realtimeBar - Opening price:{}'.format(open))

    @iswrapper
    def historicalData(self, reqId, bar):
        '''Called in response to reqHistoricalData'''
        print('historicalData - Close price: {}'.format(bar.close))

    @iswrapper
    def fundamentalData(self, reqId, data):
        '''Called in response to reqFundamentalData'''
        print('Fundamental data: ' + data)

    def error(self, reqId, code, msg):
        print('Error {}: {}'.format(code, msg))

def main():
    # Create the client and connect to TWS
    client = MarketReader('127.0.0.1', 7497, 0)

    # Request the current time
    con = Contract()
    con.symbol = 'GS' # IBM
    con.secType = 'STK'
    con.exchange = 'SMART'
    con.currency = 'USD'

    con1 = Contract()
    con1.symbol = 'VAS'
    con1.secType = 'STK'
    con1.exchange = 'SMART'
    con1.currency = 'AUD'

    # Request ten ticks containing midpoint data
    client.reqTickByTickData(0, con, 'MidPoint', 10,True)

    # Request market data
    client.reqMktData(1, con, ' ', False, False, [])

    # Request current bars
    client.reqRealTimeBars(2, con, 5, 'MIDPOINT',True, [])

    # Request historical bars
    now = datetime.now().strftime('%Y%m%d,%H:%M:%S')
    # client.reqHistoricalData(3, con, now, '2 w', '1day','MIDPOINT', False, 1, False, [])
    client.reqMarketDataType(4)
    client.reqMktData(1,con1,'',False,False,[])
    # Request fundamental data
    # client.reqFundamentalData(4, con,'ReportSnapshot', [])

    time.sleep(5)
    client.disconnect()

if __name__ == '__main__':
    main()