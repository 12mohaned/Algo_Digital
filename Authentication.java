import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.safari.*;;
public class Authentication{
private static WebDriver Safari_Driver;
public static void main(String[]args) 
{

}
	/*
	Testing the Sign-up Function in the Website
	*/	
public static void SignUp(String Username, String FirstName,String LastName, String Email,
		String Password){
try {
Safari_Driver = new SafariDriver(); 
Safari_Driver.get("http://127.0.0.1:8000/Algorthims/SignUp");
Safari_Driver.findElement(By.name("username")).sendKeys(Username);
Safari_Driver.findElement(By.name("first_name")).sendKeys(FirstName);
Safari_Driver.findElement(By.name("last_name")).sendKeys(LastName);
Safari_Driver.findElement(By.name("email")).sendKeys(Email);
Safari_Driver.findElement(By.name("password1")).sendKeys(Password);
Safari_Driver.findElement(By.name("password2")).sendKeys(Password);
Safari_Driver.findElement(By.cssSelector("button[type='submit']")).click();
}
catch (Exception e) 
{
System.out.println(e.getMessage());	
}
}
	/*
	Testing the LogIn Function in the Website
	*/
public static void LogIn(String Username, String Password){
try {
WebDriver Safari_Driver = new SafariDriver(); 
Safari_Driver.get("http://127.0.0.1:8000/Login.html");
Safari_Driver.findElement(By.name("username")).sendKeys(Username);
Safari_Driver.findElement(By.name("password")).sendKeys(Password);
Safari_Driver.findElement(By.cssSelector("button[type='submit']")).click();
}
catch (Exception e) 
{
System.out.println(e.getMessage());	
}
}
public static WebDriver getSafari_Driver() {
	return Safari_Driver;
}
}
