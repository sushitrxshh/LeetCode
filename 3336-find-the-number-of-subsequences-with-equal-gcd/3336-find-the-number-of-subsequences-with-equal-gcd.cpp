class Solution {
    const int mod=1e9+7;
    int dp[200][201][201];
public:
    int countPairs(int index, vector<int>& nums, int gcd1, int gcd2) {
        if (index == nums.size()){
            return (gcd1 && gcd2 && gcd1 == gcd2);
        } 

        if (dp[index][gcd1][gcd2] != -1) return dp[index][gcd1][gcd2];

        int skip = countPairs(index + 1, nums, gcd1, gcd2);

        int takeGcd1 = countPairs(index + 1, nums, gcd(gcd1, nums[index]), gcd2);

        int takeGcd2 = countPairs(index +1 , nums, gcd1, gcd(gcd2, nums[index]));

        return dp[index][gcd1][gcd2]=((long long)skip +takeGcd1 + takeGcd2)%mod;
    }
    int subsequencePairCount(vector<int>& nums){
        memset(dp, -1, sizeof(dp));
        return countPairs(0, nums, 0, 0);
    }
};