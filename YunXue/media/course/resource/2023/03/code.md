1.  一个递增有序的顺序表，向其中插入元素x，使其仍然递增有序

    ```
    int i;
    find{
       for(i=0 i<L.len i++) { 
         if x<i;  return i; 
       } 
    }  return i; // 遍历完整个顺序表都未找到大于x的数，表明x应插在末尾处
    inse return{
        int j,p;  p=find(L,x)  // p为x应该插入的位置
        for(j=len-1;j>=p;j--) { j+1=j }// 从后往前遍历
        p=x; len+=1;
    }
    ```
    
2.  从顺序表中删除给定值在s到t之间的所有元素

    ```
    delete{
       int i,k=0;
       for(i=0 i<L.len i++)
     	  if (i>=s && i<=t) k++; // i处的元素是否在s到t之间，同时下标往后移，符合条件的元素个数加1
          else i-k=i; // 用i-k表示需要覆盖的位置
       len-=k;
    }
    ```
    
3.    从有序表中删除所有值重复的元素

    ```
    delete{
    	int i=0,j=1;
    	for(j<len){
    		if (i!=j) L.data[++i]=L.data[j]; // 先对i+1，然后将j处的元素移到i+1处，要保证比较的元素是第二个和第三个，将不重复的值保留下来
    	} 
    	len=i+1; // 操作完成后，i值为表中最后一个元素的位置下标，所以表长为i+1
    }
    ```

4.    在数组A[m+n]中依次存放两个线性表(a1,a2...am),(b1,b2..bn)，将数组中两个顺序表的位置互换，将(b1,b2..bn)放在(a1,a2...am)的前面

    ```
    reverse(Sqlist &L int left int right){
    	int t;
    	for(i=left j=0 i<=(left+right)/2 i++ j++) // 最左边的元素下标0+最右边元素的下标(len-1)/2=中间位置下标
    		if(i!=right-j) // 若二者相等，表示同一个元素不用交换
    			t=i; i=right-j; right-j=t;  // 交换顺序表对称元素值
    }
    exchange(Sqlist &L int m int n){
    	if(m+n!=len || m<0 || n<0)  return false;
    	reverse(L,0,m-1);   // 交换前面部分
    	reverse(L,m,m+n-1); // 交换后面部分
    	reverse(L,0,m+n-1); // 交换整个顺序表
    }	
    ```
    
5.    顺序存储结构求子串

      ```
      void substring(char A[],long start,long count,char &B[]){ // char A[]原串,long start开始,long count子串长度,char B[]返回的子串
      	long i,j; long len=strlen(A);
      	 if(start<0||start>len||start+count-1>len) return -1;	//开始位置非法，或者子串长度非法
      	 else
              for(i=start-1,j=0;i<start+count-1;++i,++j) { B[j]=A[i]; }
              B[j]='/0';	//结束标志
      } 
      ```

6.     将两个有序顺序表合并成一个新的有序顺序表

      ```
      bool Merge(Sqlist A,Sqlist B,Sqlist &C){
      	if(A.len+B.len>C.maxSize)  return false;
          int i=0, j=0, k=0; //用i标记A中第一个元素，j标记B中第一个元素，k标记C中第一个元素
          while(i<A.length&&j<B.length){
           	if (i<j) C.[k++]=A.[i++];
              else C.[k++]=B.[j++];
          }
      	//若A中有剩余，将A中元素依次存入B中
          while(i<A.length) C.[k++]=A[i++];
          while(j<B.length) C.[k++]=B.[j++];
          C.length=k;
      }
      ```

7.     在带头结点的单链表L中，删除所有值为x的结点，并释放其空间，假设为x的结点不唯一

      ```
      Del_x(Linklist &L,int x){
      	LNode *p=L->next,*pre=L,*q;  // 删除操作需要前驱指针
          while(P!=NULL)
              if(p->data==x) q=p; p=p->next; pre->next=p; free(q); // 用p遍历整个链表找到x，用q标记要删除的元素然后删除q
              else pre=p; p=p->next; //此时p所指结点值不为x，pre和p都后移一位
      }
      ```

8.     查找链表C中是否存在一个值为x的结点，若存在，则删除该结点

      ```
      findAnddelete{
      	LNode *p,*q p=C;
      	while(p->next!=NULL){
      		if(p->next->data==x) break;  // 判断结点值是否为x，若是直接跳出循环
              p=p->next;
      	}
      	if(p->next==NULL)  return 0; // 若p指向NULL，则表示C链表遍历完毕未找到x
      	else q=p->next; p->next=p->next->next; free(q);  return 1;
      }
      ```

9.     实现单链表L中删除一个最小值节点的高效算法（假设最小值节点是唯一的）

      ```
      Del_min(Linklist &L){ // 用p遍历链表，用minp标记最小值，找到到最小值;找到后进行删除，所以不仅要标记最小值节点，还需要标记前驱指针pre和最小值前驱节点minpre
          LNode *pre=L,*p=L->next;
          Lnode *minpre=L，*minp=L->next;
          while(p!=NULL){
          	if(p->data<minp->data) {minp=p; minpre=pre;} // 如果当前结点小于最小值，将此结点设为最小值结点
          	else pre=p; p=p->next; // 否则pre,p同步后移
          }
      	minpre->next=minp->next;  free(minp);   return L;  // 最小值结点前驱指向最小值后继
      }
      ```

10.     编写算法将带头结点的单链表就地逆置

       ```
       Linklist Reverse_Linklist(Linklist *L){ // 头插法进行逆置，用p遍历标记结点，用r标记p的后续指针防止头插p结点后造成断链
       	LNode *p=L->next,*r; // r为p后继
       	L->next=NULL; //因为是头插法，要保证链表的表尾为空
       	while(p->next){
       	  r=p->next;  // 暂存p的后继
       	  p->next=L->next;  // p的后继指向L的后继
       	  L->next=p; p=r; // L的后继指向p，保留后继结点防止断链
           }
       }
       ```

11.     A和B是两个单链表，其中元素是递增有序的，将A,B归并成一个非递减有序的单链表C，C由A,B的结点组成

       ```
       merge(LNode *A,LNode *B,LNode *&C){ // 尾插法建立链表
       	LNode *p=A->next; LNode *q=B->next; // p用来跟踪A最小值结点，q跟踪B的最小值结点
           LNode *r; C=A; C->next=NULL; free(B); r=C; // r始终指向C的终端结点
       	while(p!=NULL&&q!=NULL){ // 当p和q都不空时，选取p,q所指结点中的较小者插入C的尾部
       		if(p->data<=q->data) r->next; p=p->next; r=r->next;
       		else r->next; q=q->next; r=r->next;
       	} r->next=NULL;
       	if(p!=NULL) r->next=p;
       	if(q!=NULL) r->next=q;
       }
       ```

12.     给定两个单链表，编写算法找出两个单链表的公共结点（公共结点之后的归并成一条链表）

       ```
       Search_Common(Linklist &L1,Linklist &L2){ // 暴力循环法，通过p,q指针分别遍历两个链表，然后一个动一个不动，寻找相同结点，直至两个指针都指向表尾
       	LNode *p=L1->next; LNode *q=L2->next;
       	while(p!=NULL){
       		while(q!=NULL){
       			if(p=q)  return p; //找到公共结点，返回
       			else q=q->next;//p不动，q向后移动
       		} 
       		p=p->next;	//p向后移动一位
           	q=L2->next;	//重置q，进行新一轮的扫描
       	}
       }
       ```

13.    将一个带头结点的单链表A分解为两个带头结点的单链表A和B，使得A表中含有原表中序号为奇数的元素，而B表中含有原表中序号为偶数的元素，且保持其相对顺序不变

       ```
       Linklist create(Linklist &A){ // 奇数插入A，偶数插入B，尾插法
       	int i=0; B=(Linklist *)malloc(sizeof(LNode)); B->next=NULL; // i用来记录遍历的位置下标来判断奇偶
       	LNode *p=A->next;  LNode *ra;  LNode *rb=B->next;  A->next=NULL; // 创建两个尾指针分别指向A,B头结点,p指向A第一个元素
       	while(p!=NULL){
       		if(i%2==0) rb->next=p; rb=p; ++i;
       		else  ra->next=p; ra=p; ++i; // ra的下一结点为p所指向的结点，ra指向p所指结点，p后移一位
       		p=p->next;
       	} 
       	ra->next=NULL;
       	rb->next=NULL; 
       	return B; }
       ```

14.     设C={a1,b1,a2,b2,…an,bn}为线性表，采用带头结点的hc单链表存放，设计一个就地算法，将其拆分为两个线性表，使得A={a1…an}，B={bn,bn-1…b1}

       ```
       Linklist create(Linklist &hc){
       	LNode *ra=hc; //尾插法的尾指针 
       	LNode *p=hc->next; //遍历指针
       	A=(LNode*)malloc(sizeof(LNode));  A->next=NULL;
       	B=(LNode*)malloc(sizeof(LNode));  B->next=NULL;
       	while(p!=NULL){  
       		ra->next=p; ra=p; p=p->next; //尾插法需要用ra标记尾结点
       		if(p->next!=NULL){ 
       			r=p->next; p->next=B->next; B->next=p; p=r; //头插法插入B链表 r指针用来防止断链
       		} 
       	}
       	ra->next=NULL; 
       	 return A;   return B;
       }
       ```

15.    在一个递增有序的线性表中，有数值相同的元素存在，若存储方式为单链表，设计算法去掉数值相同的元素，使表中不在有重复的元素

       ```
       Linklist Del_Same(Linklist &L){
       	LNode *p=L->next; LNode *q; //p是负责遍历的工作指针
       	while(p->next!=null){ // 当p指针的后继结点不空时才比较二者是否重复
       		q=p->next;
       		if(p->data==q->data) 
       			p->next=q->next; free(q); //找到相同结点,释放相同结点
       		else 
       			p=p->next; //如果结点不相同，p指针向后移动
       	}  return L;
       }
       ```

16.    已知一个带头结点的单链表，结点的结构为(data,next)，假设该链表只给出头指针head，在不改变链表的前提下，查找链表中倒数第k个位置上的结点（k为正整数）若查找成功，算法输出该结点data域的值，并返回1，否则返回0

       ```
       int getNode(LNode *head, int k){ // 当p走了k-1步后，p和q同时后移，当p走到表尾结点时，q所指即为倒数第k个结点
       	if(k<1 || head==NULL)  return 0; // k值不合法
       	LNode *p=head->next; LNode *q=head->next; 
       	for(int i=1;i<k;i++) p=p->next; // p往后走k-1步
       	if(p==NULL)  return 0; // k值太大，超过链表长度，直接跳出函数
       	while(p!=NULL){
       		q=q->next; p=p->next; // p,q同步后移
       	} 
       	p("%d",q->data);  return 1;
       }
       ```

17.    已知两个链表A和B分别表示两个集合，其元素递增有序排列，编写函数，求A和B的交集，并存放于A链表中

       ```
       Linklist Common(Linklist &A,LinKlist &B){
       	LNode *p=A->next; LNode *q=B->next; A->next=Null;
       	LNode *r=A; LNode *u;
       	while(p!=null&&q!=null){
       		if(p->data<q->data) 
       			u=p; p=p->next; free(u); //谁小释放谁
       		else if(p->data>q->data) 
       			u=q; q=q->next; free(u);
       		else if(p->data==q->data) 
       			r->next=p; r=p; p=p->next; u=q; q=q->next; free(u); //将相等的元素尾插入A
       	}
       	while(p!=null){ 
       		u=p; p=p->next; free(u); //若A中有剩余，则释放空间
       	}  
       	r->next=null; return A;
       }
       ```

18.    先序遍历非递归算法

       ```
       void preorder(BTree T){ // 入栈一个立刻出,访问判定右先左
       	InitStack(s); BTNode *p; push(s,p); //先入栈一个元素
       	while(!IsEmpty(s)){//栈不空
       		pop(s,p); visit(p); //出栈一个元素并对其进行访问
       		if(p->rchild!=null)	
       			p=p->rchild; push(s,p); //右孩子不空入栈
       		if(p->lchild!=null) 
       			p=p->lchild; push(s,p); //左孩子不空入栈
       	}	
       }
       ```

         

       

19.    中序遍历非递归算法

       ```
       void inorder(BTree T){ // 入栈向左一直走，出栈访问右子树
       	InitStack(s); BTNode *p;
       	while(p!=NULL||!IsEmpty(s)){
       		if(p!=null) 
       			push(s,p); p=p->lchild; //一路向左走，左孩子不空，则一直向左走
       		else 
       			pop(s,p); visit(p); p=p->rchild;	// 左孩子为空进入else栈顶元素出栈，访问出栈元素，向右孩子走
       	}
       }
       ```

20.    统计二叉树中所有叶子结点的个数

       ```
       int count(BTNode *p){ 
       	int n=0;
       	if(p!=null){
       		if(p->lchild==null&&p->rchild==null)  ++n; //visit(p)
       		count(p->lchild);	 
       		count(p->rchild);
       	}
       }
       ```

21.    判断两棵树是否相等

       ```
       bool isSameTree(BTNode *p, BTNode *q){
       	if(p == NULL && q==NULL)  return true; // 两棵树都为空树，相等
           if(p==NULL || q==NULL)  return false; // 其中一颗为空树，不相等
           if(p->data!=q->data)   return false; // 当p、q都不为空时，判断p、q的值是否相等，不相等返回false  
           return isSameTree(p->lchild,q->lchild) && isSameTree(p->rchild,q->rchild); // 然后再递归遍历左子树和右子树，判断左子树和右子树是不是相同的树
       }
       ```

22.    交换二叉树每个结点的左孩子和右孩子

       ```
       void swap(BTree T){
       	if(T){
       		swap(T->lchild);//递归的交换左子树
       		swap(T->rchild);//递归的交换右子树
       		// 交换左右孩子
       		t=T->lchild; 
       		T->lchild=T->rchild; 
       		T->rchild=t;
       	}
       }
       ```

23.    计算二叉树最大的宽度

       ```
       int  count[100]; // 开辟一个数组count[二叉树高度],遍历每一个节点,然后根据当前节点所在层次i,则执行count[i]++;最后遍历完求出最大的count即为二叉树宽度
       int MAX=-1; //MAX即为所求宽度
       void FindWidth(BTree T,int k){ //k用来记录深度
       	if(T==NULL)   return;
       	count[k]++;
       	if(MAX<count[k]) MAX=count[k];
       	FindWidth(T->lchild,k+1);
       	FindWidth(T->rchild,k+1);
       }      
       ```

       ​    

       

24.     设计二叉树的双序遍历算法

       ```
       DoubleTrave(BTree T){ // 双序遍历即访问结点p，然后递归遍历左子树；再次访问结点p，递归遍历右子树
       	if(T==NULL)  return;
       	else if(T->lchild==NULL&&T->rchild==NULL) 
       		printf(T->data); // 输出叶子结点
       	else{
       		printf(T->data); 
       		DoubleTrave(T->lchild);
       		printf(T->data); 
       		DoubleTrave(T->rchild);
       	}
       }
       ```

25.    用层次遍历二叉树的方法统计树中度为1的结点数目

       ```
       int level(BTNode *p){
       	int num=0; 
       	if(p){
       		QueueInit(Q); EnQueue(Q,p); // Q是以二叉树结点指针为元素的队列
       		while(!isEmpty(Q)){ //只要队列不空, 就继续循环
       			t=DeQueue(Q); printf(t->data); // 出队访问结点
       			if(t->lchild && t->rchild!=NULL || t->lchild!=NULL && t->rchild) num++; //判断访问结点的度是否为1
       			if(t->lchild) EnQueue(Q,t->lchild); // 非空左孩子入队
       			if(t->rchild) EnQueue(Q,t->rchild); // 非空右孩子入队
       		}
       	}  return num;
       }
       ```

26.     求任意二叉树中第一条最长的路径长度，并输出此路径上各结点的值

       ```
       int Depth(BTNode *p) {
           int LD,RD; 
           if(p==NULL) return 0;  
           else {  LD = Depth(p - > lchild); RD = Depth(p - > rchild); return (LD>RD?LD:RD)+1; // 返回树的高度=(左子树和右子树中较大者+根结点高度1) }
       }
       void Path(BTree T){ // 递归打印路径
       	if (T){ 
               printf(T->data); //输出此路径上的结点值
       		if (Depth(T->lchild) > Depth(T->rchild))  
       			Path(T->lchild); // 往下走
       		else Path(T->rchild);
       	} 
       } 
       ```

27.     广度优先遍历（BFS) 类似于层次遍历

       ```
       void BFS(Graph G,int v){ //图G，开始顶点v
       	InitQueue(Q);	//初始化队列
       	for(int i=0;i<G.vexnum,++i)	visited[i]=0; //初始化标记访问数组 
       	visit(v);//访问初始顶点  
       	visited[v]=1;//访问位标记为1  
       	EnQueue(Q,v);	//将v入队
       	while(!isEmpty(Q))	DeQueue(Q,v); //当队不空 出队
       	for(w=FirstAdjVex(G,v);w>=0;w=NextAdjVex(G,v,w))	//检测v的所有邻接点
       		if(visited[w]==0){ //未被访问则访问
       			visit(w); //访问   visited[w]=1; //标记  EnQueue(Q,w); //入队   
       		}	
       }	
       ```

28.    深度优先算法（DFS）类似于先序遍历

       ```
       void DFS(Graph G,int v){ //传入参数，图G和v，从顶点v出发
       	visit(v);  visited[v]=1;
       	for(w=FirstAdjVex(G,v);w>=0;w=NextAdjVex(G,v,w)){ //检测到v的邻接点
       		if(visited[w]==0)	 DFS(G,w); //邻接结点未被访问则递归访问
       	}	
       }
       ```

29.    图的邻接表的存储结构定义

       ```
       typedef struct VNode{ //顶点表
           VexType data;	//顶点表的数值
           ArcNode *firstarc;	//取顶点引出的第一条边
       }VNode;
       typedef struct ArcNode{ //边表
           int adjvex;	//邻接顶点，就是这条边所对应的顶点
           struct ArcNode *nextarc;	//指向下一个边结点的指针
       }ArcNode;
       typedef struct{	//图结构体
       	VNode adjList[maxSize];    //将图的顶点数据放在一个数组中
       	int vexnum, arcnum;  //顶点和边的个数
       }Graph;
       k=p.adjvex;//取p指针指向的结点的值
       p=G->adjList[k].firstarc;//取第k个结点的第一条指针
       ```

30.     计算交错序列1-2/3+3/5-4/7+5/9....的前n项之和

       ```
       double i,item,sum;
       int n,flag=1;
       for(i=1;i<=n;i++){
       	item=flag*i/(2*i-1); sum+=item; flag*=-1;
           printf("%.3lf",sum);
       }
       ```

31.     求组合数

       ```
       double fact(){
       	double fact=1;
       	for(i=1 i<=n i++) fact*=i;
       }
       main{
       	double sum,m,n;  sum = fact(n)/(fact(m)*fact(n-m));
       }
       ```

32.    编写一个函数,由实参传来一个字符串,统计此字符串中字母、数字、空格和其他字符的个数,在主函数中输人字符串以及输出上述的结果

       ```
       int letter, num, space, others;
       void CountStr(char str[]){
       	for (int i = 0; str[i] != '\0'; i++){
       		if ((str[i] >= 'a'&& str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z'))  letter++;
       		else if (str[i] >= '0' && str[i] <= '9') num++;
       		else if (str[i] == ' ') space++;
       		else others++;
       	}
       }
       main(){
       	char text[100]; gets(text); CountStr(text);
       	printf("\nletter:%d\nnum:%d\nspace:%d\nothers:%d\n", letter, num, space, others);
       }
       ```

       

33.     统计素数并求和

       ```
       int main(){
       	int M, N, count = 0, sum = 0, i, j;
       	scanf("%d %d", &M, &N);
       	for (i = M; i <= N; i++) {
       		for (j = 2; j < i; j++) {
       			if (i % j == 0) break;	
       		}
       		if (i == j) count++;  sum += i;
       	} printf("%d %d", count, sum);
       }
       ```

34.     猴子吃桃问题

       ```
       int main(){
       	int n,sum=0,num=1; scanf("%d",&n);
       	for(int i=n-1;i>=1;i--) 
       		sum=(num+1)*2; num=sum;
       	printf("%d",sum);
       }
       ```

35.     兔子繁衍问题

       ```
       int main(){ //斐波那契数列
           int month,N,F1=1,F2=1,F3=0; // F1,F2,F3表示连续三个月的兔子数量
           scanf("%d",&N);
           if(N==1) month=1;
           else{
               month=2;
               while(F3<N){ 
               	F3=F1+F2; 
               	F1=F2;  
               	F2=F3; 
               	month++ 
               }
           printf("%d",month);
       }
       ```

36.     水仙花数

       ```
       int Npower(int x, int N); //计算x的N次方
       int main() {
       	int N, i, temp, result; 
       	scanf("%d", &N);
       	for (i = Npower(10, N - 1); i < Npower(10, N ); i++){
       		result = 0; temp = i;
       		while (temp != 0) { 
       			result += Npower((temp % 10), N);  temp /= 10; 
       			}
       		if (i == result)   printf("%d\n", i);
       	}
       }
       int Npower(int x, int N) { 
       	int Npower = 1;
       	for (int i = 0; i < N; i++) 
       		Npower *= x;
       	return Npower;
       }
       ```

37.     最大公约数和最小公倍数

       ```
       int main() {
       	int M, N, i, gcd = 1, lcm, temp;  scanf("%d %d", &M, &N);
       	if (M > N) temp = M;  M = N;  N = temp; 
       	for (i = 1; i <= N; i++) if (M % i == 0 && N % i == 0) gcd = i;
       	lcm = M * N / gcd;  printf("%d %d", gcd, lcm);
       }
       ```

38.     使用函数输出指定范围内的完数

       ```
       int factorsum( int number ){
           int i,factorsum=0;
           for(i=1;i<number;i++) if(number%i==0) factorsum+=i; 
           return factorsum;
       }
       void PrintPN(int m,int n){
           int i,j,flag=0;
           for(i=m;i<=n;i++){
               if(i==factorsum(i)){
                   printf("%d = 1",i);
                   for(j=2;j<i;j++) if(i%j==0) printf(" + %d",j);
                   printf("\n");  flag=1;
               }
           } if(flag==0) printf("No perfect number");
       }
       ```

39.     使用函数输出一个整数的逆序数

       ```
       int reverse( int number ){
           int i, j, flag = 0, t = 0, sum = 0;
           if(number<0)  flag = 1; number = -number;
           while(number>0){ i = number%10; sum = sum*10+i; number = number/10; }
           if(flag==1) return -sum;
           else return sum;
       }
       ```

40.     递归实现十进制转换二进制

       ```
       void dectobin(int n){
           int sum=0;
           if(n==0) printf("0");
           else if(n==1) printf("1");
           else dectobin(n/2); sum=n%2; printf("%d",sum);
       }
       ```

41.     使用函数统计指定数字的个数

       ```
       int CountDigit( int number, int digit ){
       	if(number<0) number =-number;
           if(number==0){
               if(digit==0) return 1;
               else return 0;
           }  int r,count=0;
       	while(number!=0){
               r=number%10; 
       	    if(r==digit) 
       	   		count++; 
       	   		number=number/10;
       	}
           return count;
       }
       ```

42.     求最大值及其下标

       ```
       int main(){
           int n,i,max,index=0;
           scanf("%d",&n);  int a[n];
           for(i=0;i<n;i++) scanf("%d",&a[i]);
           max=a[0];
           for(i=0;i<n;i++){
               if(a[i]>max) max=a[i]; index=i;
           } printf("%d %d",max,index);
       }
       ```

43.     查找指定字符

       ```
       int main(){
           char ch,c[80]; int i=0,j,flag=0,index;
           ch=getchar();  getchar();
           while((c[i]=getchar())!='\n')i++;
           for(j=0;j<i;j++)
               if(ch==c[j]) index=j; flag=1;
           if(flag==1) printf("index = %d",index);
           else printf("Not Found");
       }
       ```

44.     计算天数

       ```
       int main(){
           int i,year,month,day,n=0,
           a[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
           scanf("%d/%d/%d",&year,&month,&day);
           if((year%4==0&&year%100)||year%400==0) a[2]=29;
           for(i=1;i<month;i++) n+=a[i];
           printf("%d",n+day);
       }
       ```

45.      将数组中的数逆序存放

       ```
       int main(){
           int n,i; scanf("%d",&n); int a[n];
           for(i=n-1;i>=0;i--) scanf("%d",&a[i]);
           for(i=0;i<n-1;i++) printf("%d ",a[i]);
           printf("%d",a[n-1]);
       } 
       ```

46.     时间换算

       ```
       struct time {
           int h, m, s;
       } T;
       int main(){
           int n;
           scanf("%d:%d:%d\n", &T.h, &T.m, &T.s);  scanf("%d", &n); T.s += n;
           if (T.s >= 60) {
               T.s -= 60;  T.m++;
               if (T.m >=60) {
                   T.m -= 60;
                   T.h++;
                   if (T.h==24) T.h = 0;
               }
           }
           printf("%02d:%02d:%02d\n", T.h, T.m, T.s);
       }
       ```
