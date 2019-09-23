import java.util.*;
public class _133_CloneGraph {
	  public Node cloneGraph(Node node) {
	      if (node == null) return null;
	      Map<Node, Node> map = new HashMap<>();
	      helper(node, map);
	      return map.get(node);
	  }
	  void helper(Node node, Map<Node, Node> map) {
		  if(map.containsKey(node)) return ;
		  Node copy = new Node(node.val, node.neighbors);
		  map.put(node, copy);
		  for(Node nei: node.neighbors) {
			  helper(nei,map);
			  copy.neighbors.add(map.get(nei));
		  }
	  }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
