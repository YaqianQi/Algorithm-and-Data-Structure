package graph;
import java.util.*;
public class _207_CourseSchedule {
	public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        int res = numCourses;
        
        for(int[] pair: prerequisites){
            indegree[pair[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < indegree.length; i++){
            if(indegree[i] == 0){
                queue.offer(i);
            }
        }
        
        while(!queue.isEmpty()){
            int pre = queue.poll();
            res--;
            for(int[] pair: prerequisites){
                if (pair[1] == pre){
                    indegree[pair[0]] -- ;
                    if(indegree[pair[0]] == 0){
                        queue.offer(pair[0]);
                    }
                }
            }
        }
        return res == 0;
    }
	
	public static void main(String[] args) {
		int courseNum = 2;
		int[][] course = {{1,0},{0,1}};
		_207_CourseSchedule cs = new _207_CourseSchedule();
		System.out.println(cs.canFinish(courseNum, course));
	}

}
