import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.safari.*;
public class WritePost {
public static void main(String[]args) 
{
post_on_blog();	
}
public static void post_on_blog() 
{
try {
Authentication ST = new Authentication();
ST.LogIn("", "");
}
catch(Exception e) 
{
System.out.println(e.getMessage());
}
}
}

