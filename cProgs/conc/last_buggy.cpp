#include <iostream>
#include <algorithm>
#include <thread>
#include <cassert>

struct List
{
    struct Node
    {
        int    _x;
        Node * _next;
        
        Node(int y)
                : _x(y), _next(nullptr) {}
    };
    // List
    Node * _head;
    List() : _head(nullptr) {}
    void insert(int x)
    {
        auto node = new Node(x);
        node->_next = _head;
        _head = node;
    }
    int count() const;
};

void thFun(List & list)
{
    for (int i = 0; i < 100; i++)
        list.insert(i);
}

int main()
{
    List list;
    std::vector<std::thread> workers;
    for (int i = 0; i < 10; ++i) 
    {
        workers.push_back(std::thread(&thFun, std::ref(list)));
    }
    std::for_each(workers.begin(), workers.end(), [](std::thread & th)
    {
        th.join();
    });
    int total = list.count();
}

int List::count() const
{
    int n = 0;
    auto cur = _head;
    while (cur != nullptr)
    {
        ++n;
        cur = cur -> _next;
    }
    return n;
}
