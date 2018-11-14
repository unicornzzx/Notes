#### 关于知识 Knowlegde 
**定义**：   
知识是关于某些领域、学科或者如何做某事的信息   
knowledge is information about some domain or subject area, or about how to do something

> 抽象级别不同的几个概念：   
> Signal -> Data -> **Information -> Knowledge**
> 
> * 数据：大量的没有解释过的信号   
> * 信息：经过处理、解释过的有格式的数据
> * 知识：数据和信息结合的整体（知识和信息的区别是==依赖语境==的，提到知识是离不开它的==作用领域==的）
>     * 知识相对于信息新增的两个新特性：**目的感，再生（产生新信息的）能力**

**分类**：
* 事实：陈述性知识   
fact: declarative knowledge

* 规则：过程性知识   
rules: procedural knowledge
* 控制策略：元知识与超知识   
control strategy: meta, super knowlegde
    * 元知识 meta knowledge：关于知识的知识,是知识库中的高层知识，包括怎样使用规则、解释规则、校验规则、解释程序结构等知识

#### 知识表示 Knowledge Representation (KR)   

这个概念涉及到**认知科学 (cognitive science)** 和 **人工智能 (AI)** 两个学科
* 在认知科学中：KR关心人类如何存储和处理信息   
in cognitive science it is concerned with how people store and process information

* 在人工智能中，KR的原初目标是**存储知识以至于在程序中可以处理知识并完成对人类智能的拟真** (从认知学科中借来的理论)   
in AI, the primary aim is to ==store knowledge so that programs can process it and achieve the verisimilitude== of human intelligence (borrowed representation theories from cognitive science)

**理想的知识表示方法应有的特征**：   
* **表达的适用性 Representational Adequacy**：  

    *++能否正确、有效地将问题求解所需的各种知识表示出来？   
    Can all of the knowledge required for the problem be represented adequately?++*
    * 一个知识表示方法必须能将某一问题适用的知识具体表示出来   
    a KR scheme must be able to actually represent the knowledge appropriate to our problem

    * 在一些问题上，一些知识表示方法比另一些要好   
    some KR schemes are better at some sorts of knowledge than others
    
    * **不存在理想的**知识表示方法
    there is ==no== one ==ideal== KR scheme

* **推理的适用性 Inferential Adequacy**：  

    *++此种表达对必要的推理的产生是否提供支持？   
    Does the representation support the generation of necessary inferences?++*
        
    * 知识表示方法必须允许我们根据已有知识推导出新的结论   
    KR scheme must allow us to make new inferences from old knowledge
    
    * 推论应有的特性：
        * **彻底的 Sound**： 新的知识要完全由旧的知识推导出来（简单）
        * **完备的 Complete**：所有推论都应该是正确的（难）
        
    

* **推理的效率 Inferential Efficiency**：   

    *++这个系统能否对一个领域内的知识进行高效率的访问和处理？   
    Can the system access and process the domain knowledge efficiently?++*

    * 一个知识表示方法应是**易驾驭的** —— 将推理控制在合理的（多项式的）时间复杂度内   
    a KR scheme should be **tractable** — make inferences in reasonable (polynomial) time
    
    * 使用为某问题领域**定制**的知识表示方法 —— 这类方法通常没有那么普遍适用，但是更有效率   
    use KR schemes ==tailored== to problem domain — less general, but more efficient
        * 通常，**越普遍适用的知识表示方法越低效**   
        often, the ==more general a KR scheme is, the less efficient it is==
        
* **定义完好的语法&语义 Well-defined Syntax & Semantics**：
    * 定义完好的语法 Well Defined Syntax （简单）
        * 应该要能辨别任何造句是不是 **“语法上正确的”**   
        whether any construction is =="grammatically correct"==
        * 要知道能如何**没有歧义地**解读一个特定的造句   
        how to read any particular construction — ==no
	ambiguity==
    
    * 定义完好的语义 Well Defined Syntax （难）
        * 对于任何给定的造句，要能精确地判定它**确切的意思**   
        precisely determine, for any given construction, ==exactly what its meaning== is.
* **自然性 Naturalness**   

    ++*这个表示允许知识以一种 “自然的” 样式被输入与操作吗？  
    Does the representation allow the knowledge to be input and manipulated in a "natural" fashion?*++

    * 自然的：与人类思考、阅读和写作的方式贴近的
    * 通常，**越普遍适用的知识表示方法可读性和可理解性越少**
    often, ==more general a KR scheme is, less likely it is to be readable & understandable==

#### 规则 Rules

规则是最常用的知识表示类型，可以被定义成 **IF-THEN 结构**   
the most commonly used type of knowledge representation, can be defined as an ==IF-THEN structure== 
* **IF part**：前项 antecedent/ 前提 premise / 条件 condition
    * 允许多个前项（multiple antecedents）的存在：使用 ++AND++ 和 ++OR++ 操作符进行连接
* **THEN part**：结果 consequent / 行动 action

**规则可以表示的知识类型**：

* 关系 Relation
* 推荐 Recommendation
* 指令 Directive
* 策略 Strategy
* 启发 Heuristic

**规则作为知识表达的特性**：
* 对于某些类型的信息/环境具有 ++***表达适用性***++   
have ++***representational adequacy***++ for some types of information/envrionments

* 有 ++***推理适用性***++    
have ++***inferential adequacy***++ 
* 可能会 ++***推理低效***++ （主要做不受约束的搜索）   
can be ++***inferentially inefficient***++ (basically doing unconstrained search)   
* 可能有 ++***定义完好的语法***++ ，但 ++***缺乏定义完好的语义***++    
can have ++***a well-defined synatx***++ , but ++***lack a well-defined semantics***++ 
* 表达具有 ++***自然性***++    
this representation has ++***natrualness***++

**具有的问题**
* 不准确不完整的信息（难接触的环境）   
inaccurate or incomplete information (inaccessible environments)

* 含糊不清的推断 （不确定的环境）   
uncertain inference (non-deterministic environments)

* 非不相关的信息 （连续的环境）   
non-discrete information (continuous environments)


* 默认值 Default Value
    * 所有没有被陈述和被推导出的事物都是错的（封闭世界假设，但是真实世界中的绝大多数问题是开放世界假设）   
    anything that is not stated or derivable is false (closed world assumption, but most problems in real world is open)


---
#### 基于规则系统 Rule-based Systems
**基本思想**：   
* 知识被规定成一个关于规则的集合   
  knowledge is specified as a collection of rules  
* 每条规则的格式：   
  ==**condition -! action**== (读作：++if condition then action++)

    * 条件（前项）是一种模式   
    the condition (antecedent) is a pattern
    
    * 行动（结果）是一个在规则被触发时执行的操作   
    the action (consequent) is an operation to be performed if rule fires
* 知识应用于**事实** —— **被假定为正确的无条件陈述**   
knowledge is applied to ==facts—unconditional
	statements that are assumed to be correct== 

**规则库示例 Example Rule Base**

**基于规则系统的架构**：

* 一个规则的集合   
A collection of rules

* 一个事实的集合   
A collection of facts
* 如果一个事实与规则的条件相匹配，规则就会触发   
A rule fires if a fact matches the condition of the rule
    * **推理引擎**是触发规则的机制
    * mechanism that fires rules is ==inference engine==
    
**基于规则系统作为知识表示的优缺点**：   

**优点**：
* 这类系统非常有表达力   
these systems are very expressive

* 这些规则导致了一定程度上的模块化   
the rules lead to a degree of modularity

**缺点**：
* 这些规则缺乏语义性   
there is a lack of precise semantics for the rules

* 这类系统并不总是有效率的   
the systems are not always efficient

#### 专家系统 Expert System

**定义**：   

专家系统是一种能够**表达和推理某些知识领域**的计算系统   
an expert system is a computing system that is capable of ==expressing and reasoning about some domain of knowledge==

专家系统的目的是能够解决问题或在该领域提供建议   
the purpose of the expert system is to be able to solve problems or offer advice in that domain

**特别之处**：  

区别于传统程序  

* 传统程序 Conventional Program：   
算法 + 数据   
Program = algorithm + data  

* 专家系统 Expert System：   
推理机 + 知识库 + 数据   
==Expert system = inference engine + knowledge base + data==

> **产生式系统模型 Production System Model**   
>
> 上世纪七十年代产物，线代基于规则的专家系统的基石
>
>基础思想：人类通过将他们的知识(表示为生产式规则)应用到一个特定的问题来解决问题   
>humans solve problems by applying their knowledge (expressed as production rules) to a given problem represented by problem-specific information
>
>产生式规则被存储在**长期存储区**中   
>production rules are stored in the **long-term memory**   
>问题特定信息或者事实被存储在**短期存储区**中   
>problem-specific information or facts in the **short-term memory**
>
>三个基础组件：
>* **规则库 Rule Base (一种长期存储区域 Long-term Memory)**：   
>由一组被称为++产生式 production++、++产生式规则 production rule++ 或者++简单规则 simply rule++ 的"If LHS Then RHS" 的陈述构成   
>   * LHS->derermines when the rule may be applied   
>   * RHS-> defines the assoicated action
>
>* **工作内存 Working Memory （一种短期存储区域 Short-term Memory）**  
>存放++事实 facts++，包括++数据data++、++目标陈述 goal statement++ 和 ++中间结果intermediate (构成处理中问题的当前状态)++   
>* **推理机 Inference Engine**   
>决定何时应用何种规则

**专家系统的组成**：

* **知识库 Knowledge Base**   
*++对应产生式系统模型中的规则库、长期存储区域概念++*   
包含某领域中对解决问题很有用的知识   
知识被表示一组规则的集合   
==规则的**激活Fire**==：当一个知识的前提条件部分被满足时，规则会被激活，它的行动部分将被执行

* **数据库 Database**   
*++对应产生式系统模型中的工作内存、短期存储区域概念++*    
包含一组用于配对知识库中存储的规则的IF条件部分的事实

* **推理机 Inference Engine**   
*++对应产生式系统模型中的推理机概念++*   
专家系统中找到解的过程—— **推理(Reasoning)** 的执行者   
**连接**知识库给出的规则和数据库提供的事实

* **解释工具 Explanation Facilities**   
使用户可以询问专家系统一个具体的结论使如何达到的和为什么需要某个特定的事实   
enable the user to ask the expert system  ==how== a particular conclusion is reached and ==why== a specific fact is needed   
一个专家系统必须要能够对其做出的推理做出**解释**并且**证明**它做出的的建议、分析或者结论   
an expert system must be able to ==explain== its reasoning and ==justify== its advice, analysis or conclusion
* **用户接口 User Interface**   
用户和专家系统沟通的途径

---
#### 产生式系统模型中的控制方法 Control Schemes in Production System Model

> **产生式系统模型中**： 
>
> 推理机操作典型的 **"recognize-act"** 算法
> 1. **配对 Match**   
> 在规则库中找到LHS符合工作内存中存在的内容的规则   
>find the rules in the rule base whose LHSs are satisfied from the existing contents of the working memory
>
> 2. **冲突消解 Conflict Resolution**：   
> 通过一个或多个冲突消解策略，挑选出一个LHS符合要求的规则; 如果规则库中没有任何一个规则是可用的，停止   
> select one rule with a satisfied LHS by applying one or more conflict resolution strategies; if no rules are available in the rule base, stop
>
> 3. **行动 Act**
> 根据被挑选出规则的RHS对工作内存进行改动，可能是添加一个新的对象或者是删除一个   
> adapt the working memory according to the RHS of the selecte d rule, perhaps adding a new item or deleting an old one
> 4. 回到(1)，循环
>

#### 正向推理 Forward Chaining   
**过程**：   
1. 收集已配对的规则 Collect the Rules Matched
    * 使用控制 ++消解策略(Conflict Resolution Strategy)++ 对规则库中所有配对上的规则进行筛选，选出其中一个
2. 执行行动 Do Actions
    * 添加/删除工作内存中的事实

重复1,2，直到问题被解决/没有任何一个规则库中的知识被匹配

**特性**：
* 可能会没有效率(inefficient)
    * 导致虚假的规则激活 Spurious Rules Firing、不专注的解决问题 Unfocused Problem Solving (类似BFS)

* 所有可以被激活的规则都会去试图被激活   
all rules which can fire do fire
    * **冲突集 Conflict Set**：可以激活的规则的集合
    * **冲突消解 Conflict Resolution**：关于哪个规则要被激活的讨论

> 冲突消解策略 Conflict Resolution Strategy   

> **特性**：
> * **折射性 Refractoriness**：   
> 用同样的数据实例化某个规则时， 此规则不能被激活多次   
> a rule should not be allowed to fire more than once on the same set of data
> 实现该策略的简单方法：从工作内存中删除已经使用了一次的实例
>   * 这个特性可以阻止循环的发生(discourage looping)
>
>* **就近性 Recency**：   
>数据会被贴上时间标签，实例化规则的时候优先采用最新的数据   
>data is time-tagged(rules used more recent data are preferred
>   * 防止产生式系统再次返回查看旧数据（除非推理失败），类似DFS
>
>* **特殊性 Specificity**：   
> 具有更多条件数量（更难被满足）的规则更优先被实例化
>
>* **启发式控制 Heuristic Control**：
提供一些启发式函数来对规则的强度进行评估
>   * ==元知识 meta-knowledge==   
>   一种**关于知识的知识**，用作**指导搜索过程**    knowledge about knledge to guide search  
>
>       * 元知识推理是对已存在的冲突消解策略的加强   
>       Meta-Rules enhances an existing conflict resolution strategy
>       * 使用元规则将规则分类，在给定的某个点上选出一个超越其他类的类   
use Meta-Rules to divide rules into classes, choose one class over another at a given point
>
>
>
>


#### 逆向推理 Backward Chaining
从目标回到事实的推理，关注**搜索**的过程   
reasoning from goals back to facts, which focuses ==the search==

**过程**：   
为了证明目标 G
1. 如果G是初始事实(initial facts)，证明完成
2. 否则，找到一个可以推导出G的规则，并且尝试去证明那个规则的所有条件
3. 如果某一个假设条件不成立 (a hypothesis fails) 逆向推理回溯 (backtrack) 到另一条路径并尝试证明另一组假设 (sub-goals ——> goal)

**特性**：   

同样的规则/事实可能会被不同地执行   
same rules/facts may be processed differently

#### 二者的比较
详见克莱尔

---

#### 语义网络 Semantic Networks
一种将知识表达为图象的知识表达方式
* 节点 Nodes ——> 事实 Facts / 概念 Concepts (普遍被标记的 generally labeled)
* 弧线 Arcs ——> 概念之间的 关系 Relation / 联系 Association

**继承 Inheritance**：    不需要在每个地方都记录节点的完整信息

* 这种网络表示的强大：
    * 扩散式激活 Spreading Activation：   
    链接的定义，联系起来的推理规则   
    definitions of links and associated inference rules
    
    * 继承 Inheritance
