### Some General Issue about AI
#### 两种关于AI的基本观念 (philosophies)：
* **weak:**
    * the digital computer is a useful ==**tool**== for studying intelligence and developing useful technology   
    数字计算机的实质是一种学习智能和开发有用技术的有用**工具**

    * program on it at most a ==**simulation**== of cognitive process   
    其上的程序实质上（最多）是对认知过程的一个**模拟**
* **strong:**
    * a digital computer can in principle be programmed to ==**actually be a mind**==   
    数字计算机从原则上来说是可以被编程为本质类似于**思维**的事物
    
    * exhibit cognitive states normally ascribed to human beings   
    能展示出通常意义上被认为是属于人类的认知状态

#### AI研究的四个视角(perspectives): 
* 像人类一样行动的AI (Turing test)
* 像人类一样思考的AI (cognitive science)
* 理性思考的AI (logical approaches)
* 理性行动的AI (the intelligent agent approach)
* humanly -> 类人地；==rationally -> 理性地==   

**像人类一样地行动 Acting Humanly**
* emphasis on how to tell that a machine is intelligent
* not emphasis on how to make it intelligent   
更强调的是如何辨别一个机器是否是智能的而不是让它变得智能
* 最有名的代表: Turing test, Turing Imitation Game

**理性地行动 Acting Rationally**
* Rational Behavior 理性行为：做==正确==的事
* the right thing: what is expected to ==maximize goal achievement==, given the available information   
正确的事：使用给定的可利用信息所做出的能**最大化达成目标**的事
* rational behavior does not necessarily involve thinking, but thinking should be **in the service of** rational action   
理性行为并不一定要包含思考，但是思考应该**服务于**理性行动

#### 关于AI目标(goal)的两个观点：
* AI is about duplicating what the (human) brain **DOES**   
AI 要做的是复制==人类大脑会做的事情==
* AI is about duplicating what the (human) brain **SHOULD DO** (RATIONALITY)   
AI要做的是复制人类大脑==应该做的事情==（**即理性地**）

#### AI系统的组件(components)：
3 typical components:
* Perception 认知
* Action 行动
* Reasoning 推理
---
### 智能体 Agent
> An **agent** is anything that can be viewd as **perceiving** its **environment**  through **sensors** and **acting** upon that environment through **actuators** (or effectors) to maximize progress towards its **goals**.   
> 智能体：一切可以被视为通过自身的传感器感知环境，并通过执行器给予环境行动反馈以及最大化完成其目标进度的事物

**定义**：an agent is an entity that perceives and acts   
智能体是进行感知并行动的实体   

**更抽象的理解**：  
an agent is a function from percept histories to actions      
智能体是一个由感知到的历史到行动的一个方程   
==***f：P\* -> A***==   
computational limitations make perfect rationality unachievable   
计算上的限制使得完美的理性是无法达到的

**Agent Function**：maps from percept histories to actions   
智能体方程：由感知到的历史到行动的映射

**Agent Program**：runs on the physical architecture to produce f   
智能体程序：在实体架构上运行的，用来产生智能体方程f的程序 

==**agent = architecture + program**==

---
#### 理性智能体 Rational Agents (Intelligent Agents)
**定义**：perceives its environment via ++sensors++ and acts ***rationally*** upon that envrionment with its ++actuators++   

理性智能体应该努力做“the right things”   
* based on what it can preceive and the actions it can perform   
基于它可以感知到的事物和它可以做出的行动
* right action: the action will cause the maximum grogress towrads its goal   
正确的行动：可以令智能体在其完成目标的路上产生最大进展的行动   

**Performance Measure**：an ==objective== criterion for success of an agent's behavior  
**效绩衡量**：一个评判智能体行为的成功程度的==客观==标准   

> **一些关于智能体的理性的东西**
> * rationality is distinct from **omniscience**  
> 理性不同于**全知全能**
> * agents can perform actions likes information gathering and exploration   
> 智能体可以类似于聚集和探索信息那样执行行动
> * an agent is **autonomous** if its behavior is determined by its own experience   
> 如果一个智能体的行为是由它自己的经验决定的，那么它就是**自治的**
>     * with ability to learn and adapt   
>     包括学习和接受的能力
>     * system guided by its desginer according to a priori decisons -> not autonomous   
>     系统由设计者预先设置好的决策所引导 -> 非自治的
> * 为了生存，智能体必须具备的
>     * enough built-in knowledge to survive   
>     预先嵌入的足够的生存的知识
>     * the ability to learn   
>     学习的能力

#### 智能体的理性取决于：
* **==P==erformance measure** - defines the criterion of success   
效绩衡量 - 定义成功程度的标准
* **==E==nvironment** - prior knowledge of the environment   
环境 - 关于环境的预置知识
* **==A==ctuators** - the actions that agent can peform   
执行器 - 智能体可以执行的动作
* **==S==ensors** - the agent's percept sequence to date   
传感器 - 迄今为止智能体所感知到的事物的序列   

==**PEAS**== - can be called as ==Task Environment==

#### 环境类型 Environment Types：
* **==Fully observable 完全可观察的== (vs. partially obervable 部分可观察的)**：   
An agent's sensors give it access to the ++complete++ state of the environment at ++each point in the time++.   
++任何时候++，智能体的传感器都可以访问到环境的++完整++状态

* **==Deterministic 确定性的== (vs. stochatsic 猜测的)**：  
The next state of the environment is completely determined by the current state and the action executed by the agent.   
环境的下一个状态完全由当前状态和智能体已执行的行动所决定
    * 环境的下一个状态由当前状态、智能体已执行的行动和++其他++智能体执行的行动所决定 - **策略性的 strategic**

* **==Episodic 片段式的== (vs. sequential 顺序的)**：   
The agent's experience is divided into ++atomic++ "episodes" and the choice of action in each episode depends only on the episode itself.   
智能体的经验被分成++不可分割++的“片段”，每个片段中的行动选择都只由此片段自己决定
    * 每个“片段”：包含智能体的感知与那之后的单独一次行动

* **==Static 静态的== (vs. dynamic 动态的)**：   
The environment is unchanged while an agent is ++deliberating++.   
环境在一个智能体++谨慎思考++时是不会改变的
    * The environment is semidynamic if the environment itself does not change with the passage of time but the agent's performancce socre does.   
    半动态的环境：环境本身随着时间不会变但智能体的效绩得分是会变的

* **==Discrete 离散的== (vs. continuous 连续的)**：   
A limited number of distinct, clearly defined percepts and actions.
环境中的感知和行动是清楚定义的、不同的、有限的

* **==Single agent 单智能体的== (vs. multiagent 多智能体的)**：  
An agent operating by itself in an environment.
