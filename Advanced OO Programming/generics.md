### Generics 泛型
---
#### Generics 泛型

A  facility that enables types (classes and interfaces) to be parameters when defining classes, interfaces and methods.

#### Type Parameters 类型参数
 Type parameters ==provide a way for you to reuse the same code with different inputs==, it is the main mechanism for implementing Generics   

**notation**: ++angle brackets++ ==<>== (e.g: Vector <Integer>)
* **Formal Type Parameter 形式类型参数**: the "placeholds" in the declarations of classes and methods    
    e.g. E in <E> is a formal type parameter type here
    

    public class Vector<E> {
        public Vector() {
        E[] elementData = ...;   
        } 
 
        public E elementAt(int i) {
            E theElement = elementData[i];     
            ...   
        }  
        ...  
    }
    
* **Actual Type Parameter 实际类型参数**: the specific implementation of a formal type parameter   

    **different from normal actual parameters**: normal actual parameters are values, while the actual type parameters are types

    e.g. BandCard in <BandCard> is an actual type parameter, it replaces the formal parameter E (the  replacement continues even within the method bodies)

    
    public class Vector<BandCard> {
        public Vector() {
            BandCard [] elementData = ...;   
        } 
 
        public BandCard elementAt(int i) {
            BandCard theElement = elementData[i];
            ...   
        }   
        ...  
    } 
    
**notes**:
* The ++constructor++ ==does not== take a type parameter when it is declared:
    *  in class Vector, public Vector() {...} 
* The ++constructor++ ==does== take an actual type parameter when it is called: 
    *  using class Vector, Vector<BandCard> hand = new Vector<BandCard>() 

#### Extends 关键词（边界符）
The keyword "extends" can be used to give a restriction to type parameters

e.g.1: In this case, any actual parameter must be a subclass of **java.awt.Component**. 

    public class IconView<C extends Component> extends JPanel {
        private C[] components;    
        public void setComponents(C[] comps) {      
            components = comps;
            ...      
            add(components[i]); 
        }  
    } 
    
e.g.2: In this case, any actual parameter must a class that implements **Runnable**.

    public class RunnablePool<A extends Runnable>{
        ...  
    } 
    
    RunnablePool<Consumer> consumerPool = new RunnablePool<Consumer>(…);
    RunnablePool<EchoHandler> echoPool = new RunnablePool<EchoHandler>(…);
    
用边界符将类型变量的范围限制起来之后，可以确保这些类型的实例共有某些变量/方法,方便代码的编写

#### Generic Interfaces 泛型接口
除了泛型类，接口也可以用类型参数实现泛型接口

e.g. Generic AVLTrees

    public class AVLTree<A implements Comparable<A>>  {
        public boolean isIn(A v) {
            if (v.equals(value)) {
                return true;   } else if (v < value) {    ... }  } 
            ...  
    }