#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    sort(nums.begin(), nums.end());

    vector<vector<int>> res;

    for (int i = 0; i < nums.size(); i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        if (nums[i] > 0) break;

        int left = i + 1;
        int right = nums.size() - 1;

        while (left < right) {
            int curr_res = nums[i] + nums[left] + nums[right];
            if (curr_res == 0) {
                res.push_back({nums[i], nums[left], nums[right]});
                left++;
                right--;
                while (left < right && nums[left] == nums[left - 1]) left++;
                while (left < right && nums[right] == nums[right + 1]) right--;
            } else if (curr_res < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    for (int i = 0; i < res.size(); i++) {
        cout << "[" << res[i][0] << ", " << res[i][1] << ", " << res[i][2] << "]" << endl;
    }
}
