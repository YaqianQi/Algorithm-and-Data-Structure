package greedySearch;

public class _122_BestTimetoBuyandSellStockII {
	public int maxProfit(int[] prices) {
		int res = 0;
		for(int i = 0; i < prices.length-1; i++) {
			if(prices[i+1] > prices[i]) {
				res += prices[i+1] - prices[i];
			}
		}
		return res;
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] prices = {7,1,5,3,6,4};
		_122_BestTimetoBuyandSellStockII bt = new _122_BestTimetoBuyandSellStockII();
		System.out.println(bt.maxProfit(prices));		
	}

}
