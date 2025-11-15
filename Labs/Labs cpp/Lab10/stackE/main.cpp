#include <iostream>
#include <string>
using namespace std;

class Stack {
    int* arr;
    int size;
    int tos;

public:
    Stack(int size) {
        this->size = size;
        tos = -1;
        arr = new int[size];
    }

    ~Stack() {
        delete[] arr;
    }

    int push(int num) {
        if (tos < size - 1) {
            arr[++tos] = num;
            return 1;
        } else {
            cout << "Stack is Full\n";
            return 0;
        }
    }

    int pop(int& num) {
        if (tos > -1) {
            num = arr[tos--];
            return 1;
        } else {
            return 0;
        }
    }

    int top(int& num) {
        if (tos > -1) {
            num = arr[tos];
            return 1;
        } else return 0;
    }

    bool isEmpty() {
        return tos == -1;
    }
};

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

int applyOp(int a, int b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
    }
    return 0;
}

int evaluate(string expr) {
    Stack values(100);
    Stack ops(100);

    for (int i = 0; i < expr.length(); i++) {
        if (expr[i] == ' ') continue;

        if (isdigit(expr[i])) {
            int val = 0;
            while (i < expr.length() && isdigit(expr[i])) {
                val = (val * 10) + (expr[i] - '0');
                i++;
            }
            values.push(val);
            i--;
        }

        else if (expr[i] == '(') {
            ops.push(expr[i]);
        }

        else if (expr[i] == ')') {
            int op;
            while (ops.top(op) && op != '(') {
                ops.pop(op);
                int val2, val1;
                values.pop(val2);
                values.pop(val1);
                values.push(applyOp(val1, val2, (char)op));
            }
            ops.pop(op);
        }

        else {
            int op;
            while (!ops.isEmpty() && ops.top(op) && precedence(op) >= precedence(expr[i])) {
                ops.pop(op);
                int val2, val1;
                values.pop(val2);
                values.pop(val1);
                values.push(applyOp(val1, val2, (char)op));
            }
            ops.push(expr[i]);
        }
    }

    int op;
    while (!ops.isEmpty() && ops.pop(op)) {
        int val2, val1;
        values.pop(val2);
        values.pop(val1);
        values.push(applyOp(val1, val2, (char)op));
    }

    int result;
    values.pop(result);
    return result;
}

int main() {
    string expr;
    cout << "Enter expression: ";
    getline(cin, expr);

    cout << "Result = " << evaluate(expr) << endl;
    return 0;
}
