
public class _322_CoinChange {
	// trainsition function: 
	// min = min(min, dp[i - coin] + 1) 
	
    public int coinChange(int[] coins, int amount) {
    	if(amount == 0) return 0;
    	if (coins== null || coins.length == 0) return -1;
        int[] dp = new int[amount+1];
    	
        for (int i = 1; i <= amount; i++) {
        	
        	//Arrays.fill(dp,	 Integer.MAX_VALUE);
        	int min = Integer.MAX_VALUE;
        	for (int coin: coins) {
        		if (i >= coin && dp[i- coin]!= -1) {
        			min = Math.min(min, dp[i-coin] + 1);
        		}
        		dp[i] = min == Integer.MAX_VALUE ? -1: min;
        	}
        }
    	return dp[amount];
    	
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] coins = {1,2,5};
		int amount = 11;
		int[] coins2 = {2};
		_322_CoinChange cc = new _322_CoinChange();
		System.out.println(cc.coinChange(coins, amount));
		System.out.println(cc.coinChange(coins2, 3));
	}

}
