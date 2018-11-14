#### Method-call stack 方法调用栈
method-call stack: a stack which stores all the nested methods call   

purpose: help Java interpreter to keeps track of where it is   

##### notes:
* first method on this stack is always main()
* parameters to a method are always evaluated before that method is actually called   
（如果在调用一个方法的时候使用其他方法作为参数：作为参数的方法将被放入调用栈中，在所有作为参数的方法返回完值并被移除调用栈之前，调用它们的那个原方法都不会被放入调用栈中）
* once a method is fully evaluated, it is removed from the call stack   
（方法的参数、局部变量等信息被存在方法对应的栈帧中，当方法的栈帧被移出栈的时候它的局部变量也会消失，这就是为什么局部变量的生命周期仅到方法结尾）

#### Error-Recovery 错误恢复
**Stack Trace**: Information appears on standard error output. It gives the state of the method-call stack at the point when the Exception was thrown.   
e.g:

    Exception in thread "main”
        java.lang.ArrayIndexOutOfBoundsException
    at Operators$3.toString(Operators.java:164)
    at Prop.toString(Prop.java:66)
    at Prop.toString(Prop.java:55)
    at Prop.main(Prop.java:90) 

**Robustness**: a program is robust if it recovers from unexpected errors ("fails gracefully")   
In a robust program, when things go wrong:
* catch any exceptions, and
* inform the user (if necessary)（没有专门去定制报错信息时，Java解释器会向stderr打印异常的类型和stack trace）, and
* carry on (if possible)   

**Catch Exceptions in Java**: use try-catch clauses   
    
    try {   
        // code that can raise an exception 
    } catch (Exception e) {
        // recovery code 
    } 
    
* Different types of Exceptions can be caught separately : several catch-blocks (just like else-if)
* When an exception is thrown, the Java interpreter looks through the list of catch-blocks, and ++executes the first one that applies to the particular exception++.
    * Therefore, superclasses should be ==below== subclasses.
* Default actions: in the ++finally++ block (not necessary) below all catch blocks, which will be excuted ==whether or not== an exception is thrown

e.g:
    
    try {   
        int i = Integer.parseInt(s);
    } catch (NumberFormatException nfe) {
        System.err.println("not a valid integer");
    } catch (NullPointerException npe) {
        System.err.println("s not instantiated");
    } catch (RunTimeException re) {   
        System.err.println("something else...");
    } finally {
        //default action
    }

#### Unchecked Exceptions and Checked Exceptions

##### *++Unchecked Exceptions:++*
subclass of RuntimeException

**RuntimeException**: a class for exceptions that occur "in the normal running of the Java Virtual Machine."   
* generally arise from ++semantic coding errors++ (programmers’ bugs -> unforeseeable 不可预见的)
* ++==do not need to be advertised==++ (they almost ++always++ arise through oversight or carelessness)
* ++best recovring way++: put a try-catch block at  the top level (e.g: in the main() method) with a general error message

e.g:
    
    public static void main(String[] args) {
    try {
        // all the code    
    } catch (RuntimeException re) {
        // report the error
        // exit gracefully
        }  
    }  
    
##### *++Checked Exceptions:++*
not a subclass of RuntimeException

*  They signal ++resource errors++ (e.g., disk errors, unexpected userinput) that the programmer ++cannot ignore++. 
*  Whenever it is possible that a method might throw one of these exceptions, the programmer must either ++catch++ them (in a trycatch block), ++or advertise++ the fact that the method might throw one of these exceptions.
*  The ++compiler will check++ that programmers either catch or advertise.

> **Example: catching or advertising**
>
> There is a method:
>   
>     public int read() throws IOException { 
>     ...
>     }
>     
> Any method that calls this method must:
> * either ++catch++ any IOExceptions,
> * or ++advertise++ that it may throw such exceptions.   
> 
>Catching:
>
>     public int readInt(BufferedInputStream b) {
>         try {     
>             return b.read();
>         } catch (IOException ioe) {
>             return -1;  
>         }  
>     } 
> 
> Advertising:
> 
>     public int readInt(BufferedInputStream b)   throws IOException  {      
>         return b.read();
>     }  

#### Which way we should choose when handling special cases?

1. Returning special values for special cases    
e.g: -1 can't be an index of an array, it is a speical value to indicate that element was not found in the array
    
    
    public int find(int elt, int[] vals) {   
        for (int i=0; i < vals.length; i++) {
            if (vals[i] == elt) return i;
        }  
        // if we’re here, elt not found   
        return -1;  
    } 
   
* danger: this is an ++implicit++ convention, one that any user of the find() method should be aware of    
* it should be clearly ++documented++
2. Using exceptions   

should consider about:
* **What kind of exception to throw?**  
except existed Exception classes, we can define our own exception class:  
    * inheriting exception functionality
    * overriding the method in class Exception   
    
    (the superclass Exception provides most of what we need such as throwing, catching, etc.)

e.g 
    
    public class ParseException extends Exception {   
        public ParseException(String s) {     
            super(s);   
        }   
        
        @overriden
        public String getMessage() {     
            return "Parse error:  " + super.getMessage();   
        }  
    } 

* **Where to throw such an exception?**  

Obtain and analyze the methods.   
note: Constructor and main() are also can throw exceptions.
*  **Where (if at all) to catch such exceptions?** 

It's better to catch exceptions at (or closer to) the top level.

We don't know where to print out the error message (command line or GUI), so it doesn't make sense to catch exceptions in a method which is very far from the main(). 

Two example problems
1. Inadequacy of representation

In Java, a data element will be represented by an instance of a class (e.g., Stack, Prop).

The representation is said to be ==adequate== if:
* every data element can be represented by some instance 
* every instance represents a data element

solutions: use exceptions, private constructors...
2. Operations in ADT   

 resource errors are common is in data structures, such as Stacks, Lists, Cardhands, etc., where we have operations to access elements of the data structure (or to add to/remove from data structures that have fixed capacity)
 
 ++In these situations, Exceptions are the best solution.++