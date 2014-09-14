computer_network_analyse
========================

computer network's resilience analyse after attack(remove some node).

计算机网络实际上可以看作一个无向图。在这个例子中，我以其中最大的连接体的大小来衡量一个网络的能力。以为网络受破坏时，那些小群体
基本就可以忽略了，而网络被破坏实际上就是把网络间隔开。

ugraph_compute 和 ugraph_compute2 是内含几个处理无向图的模块，包括从某个node找出相连的node，移除某个node诸如此类。

分析计算机网络时，我找来两个参照点，一个是ER文件里的，是一个根据概率产生Edge的图，图的分布是均匀的。另一个是UPA文件里的，Edge
集中在某些node上。

还有两种攻击方式，一种随即移除端点，另一种是从degree最大的node开始移除。

为了节省画图时间（常常要反复修改），我把生成的数据存放在文件中，画图时从中读取。因此文件中把读取，产生网络，攻击网络全部注释。
只留下了画图的部分。
