
import java.util.*;

public class BirthMonth
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		Set group1 = new HashSet();
		Set group2 = new HashSet();
		Set self = new HashSet();
		
		for(int i = 0; i < 3; i++)
		{
			System.out.print("Enter birth month " + (i+1) + ": " );
			Collections.addAll(group1, scan.nextLine());
		}
		System.out.println("");
		for(int i = 0; i < 3; i++)
		{
			System.out.print("Enter birth month " + (i+1) + ": " );
			Collections.addAll(group2, scan.nextLine());
		}
		
		System.out.println(group1);
		System.out.println(group2);
		
		System.out.print("Enter your birth month: ");
		Collections.addAll(self, scan.nextLine());
		
		Set Union = new HashSet(group1);
		Set Intersection = new HashSet(group1);
		Set Difference = new HashSet(group1);
		
		Union.addAll(group2);
		Intersection.retainAll(group2);
		Difference.removeAll(group2);
		
		System.out.println("Union: " + Union);
		System.out.println("Intersection: " + Intersection);
		System.out.println("Difference: " + Difference);
		
		if(Union.containsAll(self))
		{
			System.out.println("You have the same birth month with one of your classmates");
		}
		
		
	}
}