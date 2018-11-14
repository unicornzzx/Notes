### OO and Information Hiding: 
---
#### Interfaces and Abstract Classes
> ***++抽象类++***（并非由abstract class翻译而来，或许这里的这个概念翻译成抽象体更好）：往往用来表征我们在对问题领域进行分析、设计中得出的抽象概念，是对一系列看上去不同，但是本质上相同的具体概念的抽象。   
>
> 正是因为抽象的概念在问题领域没有对应的具体概念，所以用以表征抽象概念的抽象类是不能够实例化的。
>
>==interface 和 abstract class 是两种在java中实现抽象类的途径==

##### Interface 接口
定义: java中的一个抽象类型，是抽象方法的集合

++接口的声明++

    //the declartion of interface
    
    [visibility] interface InterfaceName [extends name of other classes]{
        // the declartion of variables (final,static)
        // abstract methods
    }

* 接口是隐式抽象的，当声明一个接口的时候，不必使用 *abstract* 关键字
* 接口中每一个方法也是隐式抽象的，它们会被隐式指定为 **public abstract** (其他修饰符会导致编译错误)
* 接口中可以含有变量，但他们会被隐式指定为（且只能为） **public static final** 
* 接口中定义的方法都是**待实现**的（方法签名确定，但方法体为空），它们只能在实现对应接口的类中来实现
    * 方法签名 method signature：++***returnType methodName(parameters)***++



++接口的实现++   

    //the implementation of interface
    
    visibility class ClassName implements InterfaceName[,other InterfaceName,...]{
        // interface's variables (final & static)
        // the implementation of interface's methods
    }
    
* 实现接口的类必须实现此接口描述的**所有方法**，除非这个类是 abstract class
* 一个类可以同时实现多个接口（与继承不同，一个类只能继承一个类）
* 接口之间是可以相互继承的

++接口的继承++

    public interface InterfaceName extends SuperInterface_1, SuperInterface_2{
        
    }
* 接口允许多继承，这在类的继承中是不合法的
* 接口的多继承中 *extends* 关键词只需要用一次
* 继承与被继承的接口之间，被继承的多个接口之间，都有可能有相同的方法

---
##### Abstract Class
定义：是一种特殊的类，它其中没有包含足够的信息来描绘一个具体的对象，是java中用来实现抽象类的一种方式，拥有抽象方法，并有 *abstract* 关键词对类名进行修饰   

++abstract class的声明++

    visibility abstract class ClassName{
        //members
        //at least one abstract class
    }

* abstract class==不可以被直接实例化==，必须被向上转型成非抽象子类后进行处理
* abstract class必须有子类，使用extends继承，一个子类只能继承一个abstract class
* 子类（如果不是abstract class）必须覆写抽象类之中的全部抽象方法（如果子类没有实现父类的抽象方法，则必须将子类也定义为为abstract类）


++abstract method 抽象方法++

    public abstract returnType MethodName();
    //no method body, can end with ";"

* 抽象方法没有方法体，有 *abstract* 关键词作修饰
* 拥有没有被覆写的抽象方法的类就是abstract class
* abstract class至少有一个抽象方法
* 抽象方法必须为public或者protected（因为如果为private，则不能被子类继承，子类便无法实现该方法），缺省情况下默认为public

++abstract class的使用限制++
1. abstract class中有constructor吗?   
    由于abstract class中会存放一些属性，那么它其中==一定存在构造方法==，其存在目的是为了属性的初始化。并且子类对象实例化的时候，依然满足**先执行父类构造，再执行子类构造**的顺序
2. abstract class可以用 *final* 声明吗？   
    不能，因为它必须有子类，而 *final* 定义的类不能有子类；
3. abstract class可以用 *static* 声明吗？  
    外部抽象类不能用 *static* 声明，内部抽象类可以，且静态内部抽象类等同于外部抽象类， 继承的时候使用“外部类.内部类”的形式表示类名称
4. 可以直接调用abstract class中用 *static* 声明的方法吗？   
    任何时候，如果要执行类中的static方法的时候，都可以在没有对象的情况下直接调用，对于abstract class也一样
---
##### interface 和 abstract class之间的区别
1. 从语法定义层面   
    * abstract class可以有自己的数据成员（普通类能有的它都能有）
    * interface只可以有静态的不能被修改的数据成员，所有成员方法都是abstract的，而且它==没有constructor==
2. 从编程层面   
    * abstract class在Java中表示的是一种继承关系，一个类只能继承一个abstract class，而且方法可以被赋予默认行为（因为abstract class中是可以有普通方法的）
    * interface表示的是一种实现关系，一个类可以实现多个interfaces
3. 从设计理念层面   
    其实就是继承与实现的区别，继承abstract class 时是一种“is a”的关系；实现interface时是一种“like a”的关系，完成与inerface界定的契约就可以了
    