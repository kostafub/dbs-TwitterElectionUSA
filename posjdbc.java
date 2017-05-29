import java.sql.*;
import java.io.BufferedReader;
import java.io.FileReader;

class posjdbc {
	
	/**
	 * Establishes a connection with the “election” database
	 * and populates the tables present in it with the data 
	 * from the file american-election-tweets.csv
	 */
	public static void main(String[] args){
		Connection c = null;
		Statement stmt = null;
		try {
			Class.forName("org.postgresql.Driver");
			c = DriverManager.getConnection("jdbc:postgresql:election",
					"postgres", "postgres");
			c.setAutoCommit(false);
			System.out.println("Opened database successfully");
			stmt = c.createStatement();
			populateTables(stmt);
			stmt.close();
			c.commit();
			c.close();
		} catch (Exception e) {
			System.err.println( e.getClass().getName()+": "+ e.getMessage() );
			System.exit(0);
	    }
		System.out.println("Records created successfully");
	}
	
	/**
	 * Reads line by line the data present in the file american-election-tweets.csv,
	 * processes that data and inserts it into the "election" database
	 * @param stmt
	 */
	private static void populateTables(Statement stmt){
		//To read CSV file		
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ";"; // use ; as separator
		String sql = "";
		
		try {
			br = new BufferedReader(new FileReader("/home/kosta/Desktop/american-election-tweets.csv"));
		// placeholder for UID if neccessary
			
			while ((line = br.readLine()) != null) {
			String[] entry = line.split(cvsSplitBy);
	
			System.out.println("handle: " + entry[0] + 
								" , text: " + entry[1] +
								" , is_retweet: " + entry[2] +							
								" , originalauthor: " + entry[3] +
								" , timeTweeted: " + entry[4] +
								" , in_reply_to_screen_name: " + entry[5] +
								" , is_quote_status: " + entry[6] +
								" , retweetCount: " + entry[7] +
								" , favoriteCount: " + entry[8] +
								" , source_url: " + entry[9] +
								" , truncated: " + entry[10]);
			
			//Populate tweet table
			//Process date name
			String[] parts = entry[4].split("T");
			String part1 = parts[0]; // 2016-09-28
			String part2 = parts[1]; // 00:22:34
			
			//part1 = part1.substring(0, part1.length()-1); //Remove last space from part 1
			
			//insert values
			stmt.executeUpdate("INSERT INTO tweet (handle,timeTweeted,text,retweetCount,favoriteCount,originalAuthor) "
					+ "VALUES (entry[0],part1[0]+' '+part2[0],entry[1],entry[7],entry[8],entry[3])");
			stmt.executeUpdate(sql);
			
			//Populate hashtag table
      //Populate has table
			//selbes spiel wie oben
			
      
      
			//Increment UID placeholder
			}
		} catch (Exception e) {
			System.err.println( e.getClass().getName()+": "+ e.getMessage() );
			System.exit(0);
		  }
	}
}
