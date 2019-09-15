import java.util.*;


public class _120_Triangle {
	// 这一题并不是找，每层最小的值，而是找最小的值组成的路径
	// 一个数只和她下面两个数相连接
    public int minimumTotal(List<List<Integer>> triangle) {
        // 把数字从最小的一次放进去
    	// 寻找路径
    	int[] total = new int[triangle.size()];
        int l = triangle.size()-1;
    	for(int i = 0; i < triangle.get(l).size() ; i++) {
    		total[i] = triangle.get(l).get(i);
    	}
    	
    	for(int i = triangle.size()-2; i>=0; i --) {
    		// 取下层的进行标
    		for(int j = 0; j < triangle.get(i+1).size()-1; j++) {
    			total[j] = triangle.get(i).get(j) + Math.min(total[j], total[j+1]);
    		}
    	}
    	return total[0];
    }
   
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer[][] triangle = {{2},
						   {3,4},
						  {6,5,7},
					     {4,1,8,3}};
		_120_Triangle t = new _120_Triangle();
		
		List<List<Integer>> lists = new ArrayList<>();
		for (Integer[] ints : triangle) {
		    lists.add(Arrays.asList(ints));
		}
		
		System.out.println(t.minimumTotal(lists));
		
	}

}
