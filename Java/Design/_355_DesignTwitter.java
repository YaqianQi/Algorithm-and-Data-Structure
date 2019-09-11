package design;
import java.util.*;
public class _355_DesignTwitter {
	private static class Tweet{
		int tweetId;
		int timestamp;
		public Tweet(int id, int time) {
			tweetId = id;
			timestamp = time;
		}
	}
	
    private Map<Integer, Set<Integer>> followMap = new HashMap<Integer, Set<Integer>>();
    private Map<Integer, ArrayList<Tweet>> tweetMap = new HashMap<Integer, ArrayList<Tweet>>();
    private static int timestamp = 0;


	/** Initialize your data structure here. */
    public _355_DesignTwitter() {
        
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        Tweet newTweet = new Tweet(tweetId, timestamp++);
        if(!tweetMap.containsKey(userId)){
            tweetMap.put(userId, new ArrayList<Tweet>());
        }
       tweetMap.get(userId).add(newTweet);
    }
    /** Retrieve the 10 most recent tweet ids in the user's news feed. 
     * Each item in the news feed must be posted by users who the user 
     * followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new ArrayList<>();
        PriorityQueue<Tweet> pq = new PriorityQueue<>((t1, t2) -> t2.timestamp - t1.timestamp);
        follow(userId, userId);
        Set<Integer> followSet = followMap.get(userId);
        followSet.addAll(followMap.get(userId));
        for(Integer followee: followSet){
            if(tweetMap.containsKey(followee)){
                List<Tweet> tweetList = tweetMap.get(followee);
                int tweetListSize = tweetList.size();
                for(int i = 0; i < tweetListSize; i++){
                    pq.add(tweetList.get(i));
                }
            }
        }
        int size = pq.size();
        while(res.size() < 10 && size > 0){
            Tweet poll = pq.poll();
            res.add(poll.tweetId);
            size--;
        }
        return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if (!followMap.containsKey(followerId)) followMap.put(followerId, new HashSet<>());
        followMap.get(followerId).add(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
         Set<Integer> followSet = followMap.get(followerId);
	    if (followSet == null) {
		    followSet = new HashSet<Integer>();
		    followMap.put(followerId, followSet);
	    }
        followSet.remove(followeeId);
    }
	public static void main(String[] args) {
		_355_DesignTwitter dt = new _355_DesignTwitter();
		dt.postTweet(1, 5);
		dt.postTweet(1, 6);
		dt.postTweet(1, 7);
		dt.postTweet(1, 8);
		dt.postTweet(1, 9);
		System.out.println(dt.getNewsFeed(1));
	}

}
