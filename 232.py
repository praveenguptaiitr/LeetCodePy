"""
#include<stack>
#include<iostream>
using namespace std;

class MyQueue {
        stack<int> s1;
        stack<int> s2;
        bool first = true;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        first = true;
    }

    /** Push element x to the back of queue. */
    void push(int x) {
        if (first == true)
                s1.push(x);
        else
                s2.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int p= 0;
        if (first == true){
                while(!s1.empty()){
                int x = s1.top();
                s1.pop();
                s2.push(x);
                }
                p = s2.top();
                s2.pop();
                while(!s2.empty()){
                int x = s2.top();
                s2.pop();
                s1.push(x);
                }
        }

        return  p;
    }
    /** Get the front element. */
    int peek() {
        int p= 0;
        while(!s1.empty()){
        int x = s1.top();
        s1.pop();
        s2.push(x);
        }
        p = s2.top();
        while(!s2.empty()){
        int x = s2.top();
        s2.pop();
        s1.push(x);
        }

        return  p;
}


    /** Returns whether the queue is empty. */
    bool empty() {
        if (s1.empty() && s2.empty())
                return true;
        else
                return false;
    }
#
"""