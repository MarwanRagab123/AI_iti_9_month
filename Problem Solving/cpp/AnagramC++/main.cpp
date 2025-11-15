#include <iostream>
#include <cctype>   // عشان نستخدم isalnum و tolower
#include <string>
using namespace std;
bool isPalindrome(string s);

int main()
{
        string s;
    cout << "Enter a phrase: ";
    getline(cin, s);

    if (isPalindrome(s)) {
        cout << " It is a palindrome." << endl;
    } else {
        cout << " It is not a palindrome." << endl;
    }
}




bool isPalindrome(string s) {
    string clean = "";

        for (char c : s) {
            if (isalnum(c)) {
                clean += tolower(c);
            }
        int left=0;
        int right=clean.size()-1;

        while(left<right){
            if(left!=right){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
