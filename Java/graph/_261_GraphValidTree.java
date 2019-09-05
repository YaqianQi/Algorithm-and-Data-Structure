package graph;
import java.util.*;
public class _261_GraphValidTree {
	/*Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
	 *  write a function to check whether these edges make up a valid tree.
	 *  Solution  
	 *  1.dfs
	 *  2.union find : index : mapping_val index: 连接的图的val
	 *  time O(V*E)
	 *  */
	public boolean validTree(int n, int[][] edges) {
	    HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
	    for(int i=0; i < n; i++){
	        ArrayList<Integer> list = new ArrayList<Integer>();
	        map.put(i, list);
	    }
	 
	    for(int[] edge: edges){
	        map.get(edge[0]).add(edge[1]);
	        map.get(edge[1]).add(edge[0]);
	    }
	 
	    boolean[] visited = new boolean[n];
	 
	    if(!helper(0, -1, map, visited))
	        return false;
	 
	    for(boolean b: visited){
	        if(!b)
	            return false;
	    }
	 
	    return true;
	}
	 
	public boolean helper(int curr, int parent, HashMap<Integer, ArrayList<Integer>> map, boolean[] visited){
	    if(visited[curr])
	        return false;
	 
	    visited[curr] = true;
	 
	    for(int i: map.get(curr)){
	        if(i!=parent && !helper(i, curr, map, visited)){
	            return false;
	        }
	    }   
	 
	    return true;
	}
	public boolean validTreeUnionFound(int n, int[][] edges) {
		if (n == 1 || edges.length == 0) return true;
		if(n < 1|| edges == null || edges.length != n- 1) return false;
		int[] root = new int[n];
		for(int i = 0; i < n ; i++) {
			root[i] = -1;
		}
		
		for(int[] pair: edges) {
			int x = find(root, pair[0]);
			int y = find(root, pair[1]);
			if (x == y) return false;
			root[x] = y;
		}
		return true;
	}
	
	private int find(int[] root, int i) {
		while(root[i]!= -1) {
			i = root[i];
		}
		return i;
	}
	
	
	
	public static void main (String[] args) {
		int[][] edges = {{0,1},{0,2},{0,3},{1,4}};
		int n = 5;
		_261_GraphValidTree gvt = new _261_GraphValidTree();
		System.out.println(gvt.validTree(n, edges));
		System.out.println(gvt.validTreeUnionFound(n, edges));
		
	}
}
