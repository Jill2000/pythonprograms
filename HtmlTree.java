package htmltree;

import javax.swing.*;
import javax.swing.JFrame;
import javax.swing.JTree;
import javax.swing.tree.DefaultMutableTreeNode;
import java.util.Collections;
import java.util.*;

public class HtmlTree extends JFrame{
	JTree tree;
	
	static DefaultMutableTreeNode root = new DefaultMutableTreeNode("html");
	static DefaultMutableTreeNode root2 = new DefaultMutableTreeNode("head");
	static DefaultMutableTreeNode root3 = new DefaultMutableTreeNode("body");
	static DefaultMutableTreeNode n1 = new DefaultMutableTreeNode("meta");
	static DefaultMutableTreeNode n2 = new DefaultMutableTreeNode("title");
	static DefaultMutableTreeNode root4 = new DefaultMutableTreeNode("ul");
	static DefaultMutableTreeNode root5 = new DefaultMutableTreeNode("h2");
	static DefaultMutableTreeNode n4 = new DefaultMutableTreeNode("li");
	static DefaultMutableTreeNode n5 = new DefaultMutableTreeNode("li");
	static DefaultMutableTreeNode n6 = new DefaultMutableTreeNode("a");
	
	public HtmlTree()
	{
		
		root.add(root2);
		root.add(root3);
		root2.add(n1);
		root2.add(n2);
		root3.add(root4);
		root3.add(root5);
		root4.add(n4);
		root4.add(n5);
		root5.add(n6);
		tree = new JTree(root);
		add(tree);
		this.setTitle("JTree Example");
		this.setSize(300,300);
		this.setVisible(true);
	}
	public static void main(String[] args)
	{
		new HtmlTree();
		List breadth = Collections.list(root.breadthFirstEnumeration());
		List pre = Collections.list(root.preorderEnumeration());
		List post = Collections.list(root.postorderEnumeration());
		
		System.out.println("The root node is: " + root.getRoot());
		System.out.println("The parent nodes are: " +root2.getParent()+ "," +n1.getParent()+ ","+ root4.getParent()+ "," +n4.getParent()+","+n6.getParent());
		System.out.println("The Siblings are: " + Collections.list(root.children()) + "," + Collections.list(root2.children()) + "," + Collections.list(root3.children()) + "," + Collections.list(root4.children()) + "," + Collections.list(root5.children()) + "\n" );
		System.out.println("The one-level subtrees are: " + "\n" + root2.getParent()+" => "+root3.getPreviousSibling()+" and "+root2.getNextSibling()+"\n"
			+n1.getParent()+" => "+n2.getPreviousSibling()+" and "+n1.getNextSibling()+"\n"
			+root4.getParent()+" => "+root5.getPreviousSibling()+" and "+root4.getNextSibling()+"\n"
			+n4.getParent()+" => "+n5.getPreviousSibling()+" and "+n4.getNextSibling()+"\n"
			+n6.getParent()+" => "+n6 + "\n" );
		System.out.println("Nodes per level are: " + "\n" + "Level "+root.getLevel()+" - "+root+"\n"+"Level "+root2.getLevel()+" - "+root2+", "+root3+"\n"+
			"Level "+n1.getLevel()+" - "+n1+", "+n2+", "+root4+", "+root5+"\n"+"Level "+n4.getLevel()+" - "+n4+", "+n5+", "+"a" + "\n");
		System.out.println("Depth: " +root.getDepth()+" - "+n4+", "+n5+", "+n6);
		System.out.println("The Degree of each one level subtree are:" + "\n" +root+" - "+root.getChildCount()+"\n"+root2+" - "+root2.getChildCount()+
			"\n"+root3+" - "+root3.getChildCount()+"\n"+root4+" - "+root4.getChildCount()+"\n"+root5+" - "+root5.getChildCount() + "\n");
		System.out.println("List of nodes based on breadth-first, preorder, and postorder: "+ "\n" + "Breadth-first: "+breadth+
			"\n"+"Preorder: "+pre+"\n"+"Postorder: "+post);
	}
	
		
	
}
