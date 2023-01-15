#include<bits/stdc++.h>

using namespace std;

class Solution {
    map<pair<string, string>, bool> user;
    unordered_map<string, bool> login_s;
    vector<string> v = {"register", "login", "logout"};

    string register_(string str)
    {
        int i = 0;
        while(str[i] != ' ')
            i++;
        i++;
        string username, password;
        while(str[i] != ' ')
            username.push_back(str[i++]);
        i++;
        while(i < str.size())
            password.push_back(str[i++]);
        if(user.find({username, password}) != user.end())
            return "Username already exists";
        user[{username, password}] = true;
        return "Registered Successfully";
    }

    string login_(string str)
    {
        int i = 0; 
        while(str[i] != ' ')
            i++;
        i++;
        string username, password;
        while(str[i] != ' ')
            username.push_back(str[i++]);
        i++;
        while(i < str.size())
            password.push_back(str[i++]);
        if(user.find({username, password}) != user.end())
        {
            login_s[username] = true;
            return "Logged in Successfully";
        }
        return "Login Unsuccessful";    
    }

    string logout_(string str){
        int i = 0; 
        while(str[i] != ' ')
            i++;
        i++;
        string username;
        while(str[i] != ' ')
            username.push_back(str[i++]);
        
        if(login_s.find(username) != login_s.end() && login_s[username] == true) 
        {
            login_s.erase(username);
            return "Logged Out Successfully";
        }
        return "Logout Unsuccessful";
    }
public:
    vector<string> function(vector<string>& logs) {
        vector<string> res;
        for(auto it: logs)
        {
            string str;
            int itr = 0;
            while(itr < it.size() && it[itr] != ' ')
                str.push_back(it[itr++]);
            if(str == v[0])
                res.push_back(register_(it));
            else if(str == v[1])
                res.push_back(login_(it));
            else {
                res.push_back(logout_(it));
            }
        }
        return res;
    }
};