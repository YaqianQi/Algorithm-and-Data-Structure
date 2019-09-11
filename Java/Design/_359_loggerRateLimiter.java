package design;
import java.util.*;
public class _359_loggerRateLimiter {
	int limiter = 10;
	 public _359_loggerRateLimiter () {
	        
	    }
	 
	    
	    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
	If this method returns false, the message will not be printed.
	The timestamp is in seconds granularity. */
	 private HashMap<String, Integer> map = new HashMap<>();
	public boolean shouldPrintMessage(int timestamp, String message) {
	  if(!map.containsKey(message)) {
		  map.put(message, timestamp);
		  return true;
	  }else {
		  if(timestamp-map.get(message) >= limiter) {
			  map.put(message, timestamp);
			  return true;
		  }
	  }
	  return false;
	}
	 
	 public static void main(String[] args) {
		 _359_loggerRateLimiter lrl = new _359_loggerRateLimiter();
		 lrl.shouldPrintMessage(1, "bite");
		 lrl.shouldPrintMessage(1, "me");
		 lrl.shouldPrintMessage(1, "if");
		 lrl.shouldPrintMessage(11, "you");
		 lrl.shouldPrintMessage(1, "can");
		 System.out.println(lrl.shouldPrintMessage(12, "bite"));
	 }
}

