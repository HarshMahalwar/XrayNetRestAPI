class Solution{
    int getPalin(int i, string& a)
    {
        int l = i, r = i, res = 1;
        while(l >= 0 && r < a.length())
        {   
            if(a[l] != a[r])
                break;
            else
            {
                l--;
                r++;
                res += 2;
            }
        }
        return res;
    }
public:
    int findEarnings(int n, int m, vector<int>& comedianHumour, vector<int>& charge, vector<int>& tolerence, vector<int>& seriousness, vector<bool>& e)
    {
        for(int i = 0; i < 2 * n; i++)
        {
            
        }
    }
};