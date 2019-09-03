package graph;
import java.util.*;
public class _210_CourseScheduleII {
	/*
	 difference, 
	 return a list of courses
     construct indegree array 
     indegree == 0 put it into queue
     if pre == queue.poll  res[k++] = pair[0]
     pair[0], later course, pair[1]: pre
     
     */
	 public int[] findOrder(int numCourses, int[][] prerequisites) {
	        int[] indegree = new int[numCourses];
	        int[] res = new int[numCourses];
	        int k = 0 ;
	        for(int[] pair: prerequisites){
	            indegree[pair[0]] ++ ;
	        }
	        
	        Queue<Integer> queue = new LinkedList<>();
	        for(int i = 0; i < indegree.length;i++){
	            if(indegree[i] == 0){
	                queue.offer(i);
	                res[k++] = i;
	            }
	        }
	        while(!queue.isEmpty()){
	            int pre = queue.poll();
	            for(int[] pair : prerequisites){
	                if(pair[1] == pre){
	                    queue.offer(pair[0]);
	                    res[k++] = pair[0];
	                }
	            }
	        }
	        return (k == numCourses)? res: new int[0];
	    }
	 
	 public static void main(String[] args) {
			int numCourse = 2;
			int[][] prerequisites = {{0,1}};
			_210_CourseScheduleII cs2 = new _210_CourseScheduleII();
			int[] res = cs2.findOrder(numCourse,prerequisites);
		
			System.out.println(Arrays.toString(res));
	 }
	}


