
// https://leetcode.com/problems/move-zeroes/submissions/1
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int i=0; i<nums.size(); i++){
            if (nums[i]==0){
                for (int j=i+1; j<nums.size(); j++){
                    if (nums[j]!=0){
                        int m=nums[i];
                        nums[i]=nums[j];
                        nums[j]=m;
                        i++;
                    }
                }
                break;
            }
        }
    }
};
