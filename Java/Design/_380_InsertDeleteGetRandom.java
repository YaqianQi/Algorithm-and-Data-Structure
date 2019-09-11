package design;
import java.util.*;
public class _380_InsertDeleteGetRandom {
	private List<Integer> lst; 
	private HashMap<Integer, Integer> map; 
	Random rand;
	 /** Initialize your data structure here. */
    public _380_InsertDeleteGetRandom() {
    	lst = new ArrayList<>();
    	map = new HashMap<Integer, Integer>();
    	rand = new Random();
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val)) {
        	return false;
        }else {
        	map.put(val, map.size()-1);
        	lst.add(val);
        }
        return true;
   
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (map.containsKey(val)) {
        	return false;
        }
        swap(lst, map.get(val), lst.size() - 1, map);
        lst.remove(lst.size()-1);
        return true;
        
        
    }
    
    private void swap(List<Integer> list, int i, int j, Map<Integer, Integer> map) {
    	int tmp = lst.get(i);
    	lst.set(i,lst.get(j));
    	lst.set(j, tmp);
    	map.put(lst.get(i),	i);
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
    	int idx = rand.nextInt(lst.size());
        return lst.get(idx);
    }
    
    public static void main(String[] args) {
    	_380_InsertDeleteGetRandom idr = new _380_InsertDeleteGetRandom();
    	idr.insert(3);
    	idr.insert(4);
    	idr.insert(5);
    	idr.insert(6);
    	System.out.println(idr.remove(3));
    	System.out.println(idr.getRandom());
    }
}
