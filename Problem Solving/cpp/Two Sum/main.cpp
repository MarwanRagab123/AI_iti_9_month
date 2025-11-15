#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        for(i=0;i<=nums.sizeof();i++){
            for(j=i+1;j<=nums.sizeof();i++){

                if(nums[i]+nums[j]==target)
                    return i ,j
            }
        }

    }
};
int main()
{

}
