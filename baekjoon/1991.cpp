#include <iostream>

using namespace std;

int tree[27][3];
bool mark[27];
int testcase;

void preorder(int root);
void inorder(int root);
void postorder(int root);

void mark_init(void);



int main(void)
{


    char a, b, c;

    for (int i=0;i<27;i++)
        for (int j=0;j<3;j++)
            tree[i][j]=0;

    //A position 1
    tree[1][0]=1;

    cin >> testcase;

    for (int i=0;i<testcase;i++)
    {
        cin >> a >> b >> c;
        if (b!='.')
        {
            tree[a-64][1]=b-64;
            tree[b-64][0]=tree[a-64][0]*2;
        }

        if (c!='.')
        {
            tree[a-64][2]=c-64;
            tree[c-64][0]=tree[a-64][0]*2+1;
        }

    }

    preorder(1);
    cout<<endl;
    inorder(1);
    cout<<endl;
    postorder(1);
    cout<<endl;



    return 0;

}

void preorder(int root)
{
    cout<<(char)(root+64);
    if (tree[root][1]!=0)
        preorder(tree[root][1]);
    if (tree[root][2]!=0)
        preorder(tree[root][2]);
}

void inorder(int root)
{
    if (tree[root][1]!=0)
        inorder(tree[root][1]);
    cout<<(char)(root+64);
    if (tree[root][2]!=0)
        inorder(tree[root][2]);
}
void postorder(int root)
{
    if (tree[root][1]!=0)
        postorder(tree[root][1]);
    if (tree[root][2]!=0)
        postorder(tree[root][2]);
    cout<<(char)(root+64);
}
void mark_init(void)
{
    for (int i=0;i<27;i++)
        mark[i]=false;
}
