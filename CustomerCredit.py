class CustCredit:
    def __init__(self,accNum,begBal,totalItem,totalCred,credLim):
        self.accNum = accNum
        self.begBal = begBal
        self.totalItem = totalItem
        self.totalCred = totalCred
        self.credLim = credLim
    def exceedOrNot(self):
        newBal = self.begBal + self.totalItem - self.totalCred
        
        if newBal > self.credLim:
            print(f'Account Number :{self.accNum}\nCredit Limit :{self.credLim}\nNew Balance :{newBal}/nCredit limit exceeded.')

tom = CustCredit(249056045,0,100,1500,1)

tom.exceedOrNot()        