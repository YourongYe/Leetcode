//https://leetcode.com/problems/self-dividing-numbers/description/
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> v;
        for (int num=left; num<=right; num++){
            int temp=num;
            bool ok=true;
            while (temp>0){
                int remain = temp%10;
                if (remain==0 || num%remain!=0){
                    ok=false;
                    break;
                }
                temp/=10;
            }
            if (ok==true){
                v.push_back (num);
            }
        }
        return v;
    }
};
