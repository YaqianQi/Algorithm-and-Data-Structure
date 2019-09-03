package graph;
import java.util.*;

class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

public class _133_CloneGraph {
	HashMap<Node, Node> map = new HashMap<>();
    public Node cloneGraphdfs(Node node) {
        map.put(node, new Node(node.val, new ArrayList<>()));
        for(Node neighbor : node.neighbors){
            if(map.containsKey(neighbor)){
                map.get(node).neighbors.add(map.get(neighbor));
            }
            else{
                map.get(node).neighbors.add(cloneGraphdfs(neighbor));
            }
        }
        return map.get(node);
    }
    
	HashMap<Node, Node> map2 = new HashMap<>();
    public Node cloneGraphbfs(Node node) {
        Map<Node,Node> map = new HashMap<>();
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(node);
        map.put(node, new Node(node.val,new ArrayList<>()));
        while(!queue.isEmpty()) {
        	Node h = queue.poll();
        	for(Node neighbor: h.neighbors) {
        		if(!map.containsKey(neighbor)) {
        			map.put(neighbor, new Node(neighbor.val, new ArrayList<>()));
        			queue.offer(neighbor);
        		}
        		map.get(h).neighbors.add(map.get(neighbor));
        	}
        }
        return map.get(node);
    }


}
