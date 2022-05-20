package com.tjoeun.hadoop;

import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;

public class HiveConn 
{
   private static String driverName = "org.apache.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws Exception {
   
      // Register driver and create driver instance
      Class.forName(driverName);
      
      // get connection, �����ͺ��̽� �̸� : userdb
      // VMWare�� Ubuntu�� Hadoop, Hive�� ����ǰ�, ȣ��Ʈ ���� Eclipse���� �� Ŭ���� ����
      Connection con = DriverManager.getConnection("jdbc:hive2://192.168.184.128:10000/userdb", "hduser", "hduser");
      
      // create statement
      Statement stmt = con.createStatement();
      
      // execute statement.   default �����ͺ��̽��� employee ���̺� ���� �� �׽�Ʈ
      ResultSet res = stmt.executeQuery("SELECT * FROM employee WHERE salary>30000");
      
      System.out.println("Result:");
      System.out.println(" ID \t Name \t Salary \t Designation ");
      
      while (res.next()) {
         System.out.println(res.getInt(1) + " " + res.getString(2) + " " + res.getDouble(3) + " " + res.getString(4));
      }
      con.close();
   }
}