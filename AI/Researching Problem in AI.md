## 搜索问题的系统阐述 Formulating a search problem
#### 关于抽象 Abstraction
> **定义**：**移除无关细节**并对事物创建一个抽象表示的过程   
==process of **removing irrelevant** details to create an abstract representation==  
> 
> 抽象对于自动化的问题解决来说是具有==决定性的(critical)==    
> * 现实世界对于建立具体模型来说**太过于复杂**  
>  real-world is **too detailed** to model exactly   
> * 好的抽象应该保留**所有重要细节**   
good abstractions: retain **all important detais**   
> 
> 真实世界的复杂程度是**荒谬的(absurdly)**   
> * 所以解决问题过程中的状态空间必须要进行抽象   
> state space must be abstracted for problem solving   
> * 抽象一定要比原问题**更简单**   
> abstraction must be **"easier"** than the original problem   
> 
> 掌握正确的抽象级别很重要
---

#### 状态空间图 The State-space Graph：
**定义**：   
状态空间图实质上是对一些问题的抽象表示，很多问题都能归结为在某一状态图中寻找一个目标或者路径的问题   

**图中元素**：nodes, arcs, directed arcs, paths   

问题的状态空间表示（状态图表示）
状态空间的三元组（S，O，G）
* S：状态集合
* O：操作集合；
* G：目标状态集合


---
#### 基于树结构的搜索 Tree-based Search 

> **搜索问题 Search Problem**：
> 已知智能体的初始状态和目标状态，求解一个行动序列使得智能体能从初始状态转移到目标状态。如果所求序列可以使总耗散最低，则问题称为**最优搜索问题**。
> 组成：
>* 初始状态：智能体所处的初始状态
>* 后继函数：输入给定状态，可以输出合法行动和相应的后继状态
>* 目标函数： 用来确定给定的状态是否为目标状态
>* 路径耗散函数：在两个给定状态之间进行状态转移所需要的代价   
>
>**一般伪代码**：
>
>     //pseudocode of general search algorithm
>     agenda = initial state;
>     while agenda not empty do 
>         pick node from agenda;
>         new nodes = apply operations to state;
>         if goal state in new nodes then 
>             return solution;
>         else add new nodes to agenda;

**搜索图 Search Graphs**：   

使用状态空间图来解决搜索问题
* **节点**代表**状态**   
==states== are ==nodes==
* **有向弧线**代表**操作符**   
==operators== are ==directed arcs==
* **解**是一条始于起点终于目标地G的**路线**   
==solution== is a ==path== from start S to goal G
* **状态的扩充**：状态空间的探索是靠在已探索的状态的基础上生成新的后继状态   
**expanding states**: exploration of state space by generating sucessors of already- explored states   

* **目标测试**：每个状态都会被评估：这是一个目标状态吗？   
every state is evaluated: is it a goal state?   


**基于树结构的搜索的缺点**：
* 树搜索可能会结束于反复去访问相同的一些节点   
tree search can end up repeatedly visiting the same nodes   

* 除非搜索过程中跟踪所有访问过的节点，但这样可能会占用过量的内存   
unless it keeps track of all nodes visited, but this could take vast amounts of memory   

==图搜索比基于树结构的搜索更加普遍适用==

**示例**：  

    // pseudo codes of general Tree Search
    function Tree-Search(problem, strategy) returns a solution, or failure
        initialize the search tree using the initial state of problem
        loop do
            if there are no condidates for expansion then return failure
            choose a leaf node for expansion according to strategy //different search algorithms
            if the node contains a goal state then return the corresponding solution
            else expand the node and add the resulting nodes to the search tree
    
#### 状态与节点的比较 States vs Nodes：   
* **一个状态**：一个实体构型的表示   
**A state**：a represenation of a physical configuration   
*   **一个节点**：一个构成搜索树的数据结构   
**A node**：a data structure constituting part of a search tree   

节点包含如下信息：state 状态、parent node 父节点、action 动作、path cost g(x) 路径耗散、depth 深度
 
**扩展方程**创建新节点，填满各种各样的字段并使用问题的**后继函数**来创建对应的状态   
 the **expand function** creates new nodes, filling in the various fields and using the **SuccessorFn** of the problem to create the corresponding states   


#### 状态空间与搜索树的比较 State Space vs Search Trees：
* **状态空间 State Space**：
    * set of valid states for a problem   
    一个问题的有效状态的集合
    * linked by operators   
    由操作符连接
* **搜索树 search tree**：
    * 根节点来表示初始状态    
    root node = initial state   
    * 子节点-可以经由父节点访问的状态   
    child nodes - states that can be visited from parent   
    *  一颗树的的深度可以是==无限的== （例：经由重复的状态）   
    depth of the tree can be ==infinite== (e.g via repeated states)   
    * 局部搜索树 partial search tree:
        * 到目前为止已经被扩展张到的部分   
        portion of tree that has been expanded so far   
        
    * 边缘 frine：
        * 局部搜索树的叶节点，待扩展节点序列   
        leaves of partial search tree, candidates for expansion   
           

**二者的关系**：  
==search trees = data structure to search state-space==

---
### 搜索策略 Search Strategies
**定义**：搜索策略就是在搜索问题的求解过程中挑选扩展节点的顺序   
picking the order of node expansion    

**评估标准**：
* **完备性**：当问题有解时，是否总是能找到至少一个解？   
**completeness**: always find a solution if one exist? 
* **最优性**：是否总能找到一个最优解？   
**optimality**: always find a least-cost solution? 
* **时间复杂度**：生成的节点的数量（找解要花的时间）   
**time complexity**: number of nodes generated
* **空间复杂度**：（执行搜索过程中）要存储在内存中的节点的最大数目   
**space complexity**: maximum number of nodes in memory

> **测量时间与空间复杂度时用的一些参数**
> * 搜索树的最大++分支因子++   
> **b**: maximum ++branching factor++ of the search tree     
> 分支因子：智能体可选择行动的数量
> * 最优解的深度   
> **d**: depth of the least-cost solution   
> * 状态空间的最大深度（可能为无限大）   
> **m**: maximum depth of the state space (maybe infinite)   

#### 搜索策略的分类：
* **无信息（Uninformed）的搜索策略**：无法知道当前状态离目标状态的“远近”或者不利用类似的先验信息来进行搜索的策略（也被称为**盲目搜索 Blind Search**）
    * 广度优先搜索 (BFS, breadth-first search)
    * 代价一致搜索 (UCS, uniform-cost search)
    * 深度优先搜索 (DFS, depth-first search)
    * 深度有限搜索 (DLS, depth-limited search)
    * 迭代深入搜索 (IDS, iterative deepening search)
* **有信息的（Informed）搜索策略**：利用启发式信息来进行搜索的策略 (也叫**启发式搜索 Heuristic Search**)
    * 贪婪最佳优先搜索 (greedy best first search) 
    * A* 搜索 (A* search)
---
### 无信息的搜索策略 Uninformed Search Strategies

#### 广度优先搜索 Breadth First Search 
**基本思想**：
* 从初始状态开始扩展 - 扩展树至深度1（根节点深度为0）   
start by expanding initial state - give tree of depth 1   
* 有多个待扩展的节点时，==优先对先访问节点==（先加入待扩展节点序列的节点）==进行扩展==（FIFO数据结构存储待扩展节点的序列）
* 当深度n上的所有节点全部被扩展后才能开始扩展深度n+1上的节点（每次扩展深度**最浅**的节点）   
expand nodes at all depth n before levell n+1   


**一般伪代码**：

    //the general pseudocode of BFS
    agenda = initial state; //agenda is the sequence of nodes waiting for be expanded
    while agenda not empty do
        pick node from front of agenda;
        new nodes = apply operations to state;
        if goal state in new nodes then
            return solution;
        else APPEND new nodes to END of agenda; //First In First Out
    
**特性**：
* **优点**：
    * ++***完备性 completeness***++
    * ++***最优性 optimality***++
        * 依据求解时所++应用的操作的数量++来找到一个最优解   
        find the shortest (cheapest) solution in terms of ++the number of operations applied++ to reach a solution   
    
* **缺点 disadvantage**：
    * ++***高复杂度 high complexity***++   
        
    * **时间**：**组合爆炸**（在某些问题中应该要被避免）   
    **time**: ==combinatorial explosion== (should be avoided in any problem)   
         * 如果解出现在深度d，那么我们就要在达到解决方法前经过 ***1+ b+ b^2 + ... + b ^d*** 个节点-**呈指数上升**   
         if solution occurs at depth d, then we will look at ***1+ b+ b^2 + ... + b^d*** nodes before reaching solution - ==exponential==    

    * **空间**：需要的内存大小是 **b的d次方**   
    **space**: the memory requirement is **b^d**


#### 代价一致搜索 Uniform-Cost Search
在处理搜索最短路径类的问题中常被使用到的一种搜索策略
> **搜索最短路径问题 Minimum Cost Path Search Problem**
> * 赋予每个操作符（每条链接）++权重++或者++耗散++   
> adds ++weights++ or ++costs++ to operators (links)
> * 搜索树的扩展应该由当前已建立（局部）路径的整体耗散来驱动   
> expansion of the search tree should be driven by the cost of the current (partially) built path

**基本思想**：
* 从初始状态开始扩展 - 扩展树至深度1（根节点深度为0）   
start by expanding initial state - give tree of depth 1   
* 扩展节点时，在待扩展节点序列中**挑选出累计路径耗散最低**的节点进行扩展   
expand the leaf node ==with the minimum cost== first
* 扩展节点时，如果有多个待扩展节点同时具有最低累计路径耗散，优先扩展先访问的待扩展节点
* 当每条链接的路径耗散都相同时，UCS等价于BFS   

**一般伪代码**：

    //the general pseudocode of UCS
    agenda = initial state;
    while agenda not empty do
        take node from agenda such that
            g(node) = min{g(n)|n in agenda}; //path cost function
        if node is goal state then
            return solution;
        new nodes = apply operations to node;
        add new nodes to the agenda;

**特性**：
* ++***完备性 completeness***++
* ++***最优性 optimality***++（有限制条件）   
如果累计路径耗散是**单调递增**的话（即所有路径耗散都为正），UCS保证能找到最优解   
UCS guaranteed to find cheapest solution assuming path costs ==grow monotonically==
    * 当累计路径耗散不是单调变化时需用用到穷举搜索   
    exhaustive search is required if not monotonically

**UCS与BFS的比较**：
* BFS：沿着等长度路径（等深度节点）断层进行扩展
* UCS：沿着等代价路径断层进行扩展

#### 深度优先搜索 Depth First Search
**基本思想**：
* 从初始状态开始扩展 - 树从深度1开始   
start by expanding initial state - give tree of depth 1   
* 有多个待扩展的节点时，==优先对后访问节点==（后加入待扩展节点序列的节点）==进行扩展==（FILO数据结构存储待扩展节点的序列）
* 总是**沿着**搜索树的**一个分支**扩展到**最深**的节点   
always expand the ==deepest== node ==follow one "branch"== of search tree   

**一般伪代码**：
    
    //the general pseudocode of DFS
    agenda = initial state;
    while agenda not empty do
        pick node from front of agenda;
        new nodes = apply operations to state;
        if goal state in new nodes then
            return solution;
        else APPEND new nodes to FRONT of agenda; //First In Last Out

**特性**：
* 时间/空间 ++***复杂度***++ 比BFS ++***少***++ 非常多   
time/space complexity much less than BFS   
* ++***不完备性 incompleteness***++
* ++***不具有最优性 no optimality***++   


#### 深度有限搜索 Depth Limited Search
深度限制搜索是**在给定的步数之后会结束搜索路径**的DFS   
DFS but ==terminate any search path after a given number of steps==

**基本思想**：在要被扩展的分支上引入一个**深度限制**，在此深度以下不对分支进行扩展   
introduce a **depth limit** on branches to be expanded, don't expand a branch below this depth

**一般伪代码**：

    // the general pseudocode of depth limited search
    depth limit = max depth to search to;
    agenda = initial state;
    if initial state is goal state then
        return solution
    else
        while agenda not empty do
            take node from front of agenda;
            if depth(node) < depth limit then
            {
                new nodes = apply operations to node;
                add new nodes to front of agenda;
                if goal state in new nodes then
                    return solution;
            }

**特性**：
* 总是会终结，消除了DFS可能会永远循环的风险   
always terminate, remove risk of looping forever   
* ++***完备性 completeness***++（有限制条件）   
如果在**深度限制内**存在解的话，总是能找到一个解   
always find solution if there is one ==in the depth bound==
* 依然 ++***不具备最优性 no optimality***++

> 关于深度限制
> * 如果太小：会错过解 misses solutions
> * 如果太大：可能在存在更优解的时候找到很差的解   
> may find a poor solutions when there are better ones

#### 迭代深入搜索 Iterative Deepening Search
IDS是一种在DLS基础上延伸的搜索算法，用来寻找合适的深度限制的

它用来解决的那些**搜索空间可能会非常大**和**解决方案的最大深度未知**的问题   
solve the problem of ==possible very large search space== and the ==unknown maximum depth of the solution==   

**基本思想**：
* do DLS for depth n = 0; if solution found, return it;
* otherwise do DLS for depth n = n+1; if solution found, return it, et.al;

*++即深度从零开始递增，在每个深度上都做一次以此深度为深度限制的DLS直到找到解++*   
++*repeat DLS for all depths until solution found*++

一般伪代码：

    //the general pseudocode of Iterative Deepening 
    depth limit = 0;
    repeat
    {
        result = depth_limitd_search
        (
            max depth = depth limit;
            agenda = initial node;
        ); //call DLS as subroutine
        if result contains goal then return result;
        depth limit = depth limit + 1;
    }
    until false; 

**特性**：
* 当调用深度限制为n的DLS时，必须**重新生成**深度为n-1的树(每次调用)   
have to ==regenerate== the tree to depth d -1 when we  call on depth limited search for depth d (every-time)
* 舍弃时间换取空间   
trade off time for memory   
* IDS是 ++***完备***++ 而且 ++***最优***++ 的   
IDS is ==complete== and ==optiaml==

**DLS与IDS的比较**:

DLS扩张过程中经过的节点：
```math
1+b+b^2+b^3+...+b^{d-1}+b^d
```
IDS扩张过程中经过的节点：
```math
(d+1)1+(d)b+(d-1)b^2+(d-2)b^3+...+(2)b^{d-1}+(1)b^d
```

#### 各策略之间的对比

Criterion | BFS | UCS | DFS | DLS | IDS
---|---|---|---|---|---
Complete | Yes | Yes | No | Yes, if l>=d | Yes
Time | b^(d+1) | b^(C*/𝜀) | b^m | b^l | b^d
Space | b^(d+1) | b^(C*/𝜀) | bm | bl | bd
Optimal | Yes | Yes | No | No | Yes

---

### 有信息的搜索策略 Informed Search Strategies
> **最佳优先(Best First)搜索的通用思想**：   
> 用一个 **评价函数(evaluation function)** f(n)来对节点进行评价。在扩展节点的过程中，从待扩展节点中选择f(n)最小的节点来进行扩展。  
> 
> **此通用思想在各搜索策略中的体现**：   
> * BFS：f(n)表示节点深度
> * UCS：f(n)表示节点的累计路径耗散
> * DFS：f(n)表示节点深度的负值
> 
> 但很多时候盲目搜索中的f(n)不能真正度量节点好坏

#### 启发式函数 Heuristic Functions   
启发式函数是上述思想中的f(n)的一种具体实现   

**基本思想**：从节点n到目标节点的最低耗散路径的耗散**估计**值   
the ==estimated== value of the minimal path cost from node n to the goal node

**特性**： 
* **没有"通用"** 的启发式（对某领域的具体知识有需求）   
==no "general"== heuristic (require specific knowledge about the domain)
* 启发式是有信息的搜索方法的==核心==   
heuristics are at the ==heart== of informed search methods

#### 贪婪最佳优先搜索 Greedy Best-First Search

**基本思想**：  
* 估计每个节点到目标节点的最低扩展耗散
* 扩展节点的时候总是扩展 到目标节点的最低扩展耗散预计值最小的节点

**启发式函数 Heuristic Function**：   
==h ： Nodes -> R==   
估计每个节点到目标节点的最低扩展耗散，当h(n)=0时n是一个目标节点

**一般伪代码**：

    // the gereral pseudocode of Greedy Search
    agenda = initial state;
    while agenda not empty do
        take node from agenda such that
            h(node) = min{ h(n) | n in agenda} //just change the f(n) in the UCS to H(n)
        if node is goal state then
            return solution;
        new nodes = apply operations to node
        add new nodes to the agenda;
    
**特性**：
* ++***不完备性 incompleteness***++
* ++***不具有最优性 no optimality***++
* 易被错误的开始影响，一条路走到黑   
susceptible to false starts
* 只看当前的节点，忽略过去的节点   
only looking at current node, ignores past

#### A* 搜索 A* Search
为了弥补贪婪最佳优先搜索无法找到最优解的缺点，考虑在评价函数里加入累计路径耗散，由此形成A*搜索算法

**基本思想**：
* **结合**了UCS和贪婪搜索   
==combine== uniform cost search and
  greedy search
* 扩展节点的过程中，会关注当前累计的路径耗散和到目标的预计耗散   
look at the cost so far and the estimated cost to goal
* 目标是将全局范围内的耗散降至最小   
aims to minimise overall cost

**启发式函数 Heuristic Function**：   
==**f: f(n) = g(n) + h(n)**==   
* g(n)：节点n的累计路径耗散
* h(n)：从节点n到目标节点间最低耗散路径的耗散估计值
* f(n): 经过节点n到目标节点的总耗散估计值


**一般伪代码**：
    
    //the general pseudocode of A* Search
    agenda = initial state;
    while agenda not empty do
        take node from agenda such that
            f(node) = min{ f(n) | n in agenda} 
            where f(n) = g(n) + h(n) //combine UCS and Greedy Search
        if node is goal state then
            return solution;
        new nodes = apply operations to node
        add new nodes to the agenda;
        
**特性**：
* ++***完备性 completeness***++
* ++***最优性 optimality***++ （有限制条件）
    * 图中的每个节点都有有限个子节点   
    each node in the graph has a finite number of children
    * 所有路径耗散都要是正数   
    all arcs have a cost greater than some positive a
    * h(n)==是可采纳的(admissiable)==，即h(n)从不高估节点n到目标节点的最低耗散   
    h(n) is **admissiable** - for all nodes in the graph h(n) always underestimates the true distance to the goal   
    > 可采纳的：h(n) <= h True(n)
    
    > **有更多信息的搜索 More Informed Search**
    > * 有两个不同版本的A*，A*1和A\*2，分别用不同版本的h1和h2
    > * 而且对于所有非目标节点来说都有：h1(n) < h2(n)
    > * 那么A*2比A\*能提供更多信息
    > * 能提供更多信息的A*在找到最小路径耗散路径的过程中要经过的节点术越少
