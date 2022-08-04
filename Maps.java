package HashMaps;
import java.util.*;

public class Maps
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		Map<String, String> students = new HashMap<>();
		String get = "";
		for(int i = 0; i < 3; i++)
		{
			System.out.print("Enter student number " + (i+1) + ": ");
			String snum = scan.nextLine();
			System.out.print("Enter first name " + (i+1) + ": ");
			String sname = scan.nextLine();
			students.put(snum,sname);
			get = snum;
		}
		
			students.remove(get);
		

		System.out.println("Student List:");
		for(Map.Entry e : students.entrySet())
		{
			System.out.println("" + e.getKey() + " " + e.getValue());
		}
		
	}
}