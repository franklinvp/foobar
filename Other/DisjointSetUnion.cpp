#include <iostream>
#include <vector>
#include <unordered_set>
#include <stack>

using namespace std;

struct dsuNode
{
  int val;
  dsuNode* parent;
  int rank;
  dsuNode(int x) : val(x), parent(nullptr), rank(0) {};
  bool operator ==(const dsuNode & obj) const
  {
    if (val == obj.val)
      return true;
    return false;
  }
};


template<>
struct std::hash<dsuNode>
{
  size_t
  operator()(const dsuNode& obj) const
  {
    return hash<int>()(obj.val);
  }
};


class DSU
{
public:
  unordered_set<dsuNode> subsets;

public:
  void makeSet(dsuNode* x)
  {
    x->parent = x;
    x->rank = 0;
    subsets.insert(*x);
  }

  dsuNode* find(dsuNode* x)
  {
    stack<dsuNode*> toCompress;
    while (x->parent != x)
    {
      toCompress.push(x);
      x = x->parent;
    }
    while (!toCompress.empty())
    {
      toCompress.top()->parent = x;
      toCompress.pop();
    }
    return x->parent;
  }

  void link(dsuNode* x, dsuNode* y)
  {
    if (x->rank > y->rank)
    {
      y->parent = x;
    }
    else
    {
      x->parent = y;
      if (x->rank == y->rank)
      {
        y->rank += 1;
      }
    }
  }

  void makeUnion(dsuNode* x, dsuNode* y)
  {
    link(find(x), find(y));
  }
};


int main()
{
  DSU dsu;
  vector<dsuNode> mynodes;
  for (int i = 0; i < 100; i++)
  {
    mynodes.push_back(i);
  }
  for (auto x : mynodes)
  {
    cout << x.val << ",";
  }
  cout << endl;

  for (int i = 0; i < 100; i++)
  {
    dsu.makeSet(&mynodes[i]);
  }
  cout << "dsu.subsets.size() = " << dsu.subsets.size() << endl;
  for (int i = 0; i < 99; i++)
  {
    dsu.makeUnion(&mynodes[i], &mynodes[i+1]);
  }

  for (int i = 0; i < 100; i++)
  {
    cout << "Class of " << mynodes[i].val << " is " << dsu.find(&mynodes[i])->val << ", rank = " << mynodes[i].rank << endl;
  }

  return 0;
}
