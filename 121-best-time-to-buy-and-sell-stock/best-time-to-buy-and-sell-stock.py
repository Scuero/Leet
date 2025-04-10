class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        precioCompra = prices[0]
        for precio in prices:
            if precio < precioCompra:
                precioCompra = precio
            else:
                profit = max(profit, precio-precioCompra)
        return profit
        