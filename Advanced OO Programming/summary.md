### Abstract data types (ADT)

* ##### Abstract class
    ++abstract class:++ a class that contains at least one abstract method
    * abstract method: a method declaration with no body
        * if a class contain an abstract method, it must declare itself and the method abstract
    * can't create an instance of an abstract class

* ##### Inner class
* ##### Field scope and modifiers: public, private, protected, default, static, final
* ##### Operations on LinkedList and Node, e.g., add(), insert(), remove(), etc 
* ##### Interfaces, e.g., implement methods in an interface 

---
### Class invariant 

* ##### What is class invariant? 
    ++class invariant++: some property that is always true for all instances of the class when a program is executed
    
    form: [class invariant X] for [class A]
* ##### How to check or ensure class invariant?
    1. check every constructors, make sure that class invariant is true for evrey new instances of this class
    2. check all public methods, make sure they perserve the class invariant
    * ==not necessary to be maintained by protected or private==
* ##### Generics and erasure 
    ++Generics++: a facility that enable types (classes and interfaces) to be parameters when defining classes interface and methods. (Introduced in Java 1.5)
    * main implementation mechanism: type parameters
    * benefits:
        * help to write re-usable code
        * help to create homogeneous collections

    ++Erasure++: before compile, compiler deletes all generic types
    * reason: the introduction of Generic didn't make any change to Java Interpreter, it just updated compiler some functions in parsing and type-checking
    * implementations
        * for generic classes:
            1. delete the generic type in class name
            2. delete the generic type in its extends clause
            3. do erasure for all generic method in this class
            4. change all generic type in class body to type "Object"
        * for generic interfaces:
            1. delete the generic type in interface name
            2. do erasure for all generic methods in this interface
        * for generic methods:
            * in the declartion of methods
                1. delete the <> before its return type (which indicates the generic types used in this method)
                2. change its generic return type to type "Object"
                3. do erasure for other generic methods called in this method body
                3. change all generic type in method body to type "Object
            * in the method calling   
                * must cast before the method 
    
* ##### Method call stack, e.g., know ==how to describe the call stack==
    ++Method Call Stack++: a stack which stores all the nested methods call
    * purpose: help Java interpreter to keep track of the point to which each active subroutine should return control when it finishes executing
    * notes:
        * first method on this stack is main method
        * parameters to a method are always evaluated before that method is actually called
        * once a method is fully evaluated, it is removed from the stack
* ##### ==Operations on trees, e.g., isIn(), find(), insert() and height()==

---
### Exceptions 

* ##### ==BoundedQueue and BoundedStack; the exceptions related to their implementation==

* ##### Checked and unchecked exceptions
    ++Unchecked Exceptions++: RuntimeException and its subclass
    * generally arise from: semantic coding errors (bugs)
    * checking: 
        * not checked during compiling time
        * shown afterwards
    * recovering: 
        * can be fixed by better programing
        * best recovering way - put a try-catch block at the top level (close to main method) with a general error message
            * do not need to be advertised   
    
    ++Checked Exceptions++: subclass of Exceptions but not subclass of RunTimeException
    * generally arise from: resource errors
        * e.g. disk errors, unexcepted user input
        * programmer cannot ignore them
    * checking: 
        * checked during compiling time: compiler will check whether each potential checked exception was catched or advertised
    * recovering:    
    for every method which might throw a checked exception, 2 options
        1. handle: 
            * use try-catch block
            * catch exceptions in its method body
        2. advertise: 
            * use throws keyword
            * advertise the fact that the method might throw xx exceptions
        
    
* ##### Handle and advertise checked exceptions
    * Handle
        ```
        //top->down: specific to general
        //superclass should be below of the subclass
        try {   
            int i = Integer.parseInt(s);
        } catch (NumberFormatException nfe) {
            System.err.println("not a valid integer");
        } catch (NullPointerException npe) {
            System.err.println("s not instantiated");
        } catch (RunTimeException re) {   
            System.err.println("something else...");
        } finally {
            //at most one finally block
            //default action
        }
        ```
    
    * Advertise
        ```
        //use keyword "throws" 
        //to declare that what kinds of exceptions might be thrown from this methods
        public int readInt(BufferedInputStream b) throws IOException  {      
            return b.read();
        }
        ```

* ##### Write checked exceptions
    * define a class extended from class Exception
        ```
        public class myException extends Exception {
            //step1: write a construtor with a String parameter
            public myException(String s){
                //content is call superclass's constructor with its own parameter
                super(s);
            }
            
            //step2: rewrite the method getMessage()
            @override
            public String getMessage() {
                //write a new error message for this class
                return "My error: "+super.getMessage();
            }
        ```
    
    * throw & catch the exception designed by you
        ```
        public static void main(String[] args) {
            try {
                myMethod();
            } catch (myException me) {
                System.out.println(me.getMessage())
            }
        }
        
        public void myMethod() {
            if(...){
                //...
            } else {
                //positivly throw a exception
                throw new myException("hahahahahaha")
            }
        }
* #####  ==Use exceptions to write more robust codes==

* ##### ==Know under which circumstances what exceptions might be throw==

---
### Multithreading 

* ##### Time-slicing and how it works 
* ##### Different states of threads 

* ##### Shared resource 
* ##### Interference and know how to analyse the possibility of interference, e.g., give some examples to describe the possibility 
    ++Interference++: data-corruption that occurs when two or more threads share some common resources   
    ==how to analyse the possibility?==
    
    
* ##### How to solve the interference problem? How to change the codes to avoid the problem? 
* ##### Deadlock and the solutions for it 
* ##### Threads in GUI, e.g., initial thread and eventdispatch thread 

---
### I/O streams and networking

* ##### I/O, e.g., System.in, I/O streams related to socket programming, BufferedReader and PrintWriter 
* ##### Programs client and server interaction 
* ##### Exceptions in server socket programming, trycatch, finally, close I/O streams and sockets 
* ##### How server can handle multiple clients concurrently? 
* ##### Adding statistical data to multi-threaded server 
* ##### Difference between piped I/O and byte oriented I/O 

---
### Generic functions 

* ##### Generic interface, generic class and generic methods

    * Generic Class   
    
        ```
        //define a generic class
        public class Generic<T>{ 
            private T key;

            //in the definetion of constructor
            //no generic type in <> between method name and parameters
            public Generic(T key) { 
                this.key = key;
            }

            public T getKey(){ 
                return key;
            }
        }
        ```
        
        ```
        /**
        create a new instance of generic class
        when call the constructor
        must have generic type in <> between method name and parameters
        and the parameters have to be the same type as the type parameters
        **/
        
        Generic<Integer> generic = new Generic<Integer>(12345)
        ```
        
    * Generic Interface
        ```
        public interface Comparable<T> {
            public int compareTo(T o); 
        } 
    * Generic Method
        ```
        /** 
        in the definition of generic method
        generic method must have type parameters in angle brackets before return value type
        it denotes that formal type parameters will be used in this method
        **/
        
        static <A,B> B eqTest(Pair<A,A> p, B b) {   
            B returnVal = null;    
            if (p.getFirst() == p.getSecond()) {
                returnVal = b;    
            }    
            return returnVal;   
        } 
        ```
        
        ```
        public static void main(String[] args) {
            Integer i = new Integer(9);
            Pair<Integer,Integer> p = duplicate(i);
            //when call a generic method
            //do not need write its type parameters 
            //compiler can works out the type of actual parameters
            String s = eqTest(p,"Ha!");     
            System.out.println(s);
            } 
        } 
        ```
        
* ##### ==Generic methods that return generic functions as a type== 
* ##### Write anonymous class
* ##### Know how to analyse generic codes 
