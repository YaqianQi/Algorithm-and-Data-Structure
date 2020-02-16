import java.util.*;
public class _5341_ProductoftheLastKNumbers {
		List<Integer> lst ; 
	    public _5341_ProductoftheLastKNumbers () {
	        lst = new ArrayList<>();
	        lst.add(1);
	    }
	    
	    public void add(int num) {
	    	
	    	if (num == 0) {
	    		lst.clear();
	    		lst.add(1);
	    	}else {
	    		lst.add(lst.get(lst.size() -1) * num);
	    	}
	    }
    
	    
	    public int getProduct(int k) {
	    	//System.out.println(lst);
	        if (k < lst.size()) {
	        	return lst.get(lst.size()-1)/ lst.get(lst.size() - 1 - k);
	        }
	        return -1;
	    }
	    
	    
	    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_5341_ProductoftheLastKNumbers pl = new _5341_ProductoftheLastKNumbers();
		pl.add(3);
		pl.add(0);
		pl.add(2);
		pl.add(5);
		pl.add(4);
		System.out.println(pl.getProduct(2));
		//System.out.println(pl.getProduct(3));
	}

}
