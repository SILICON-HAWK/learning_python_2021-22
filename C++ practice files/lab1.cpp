/*Design   a   class   to represent   a   bank   account.   
Include   the   following members.
Data Members
     Name of the depositor
     Account number
     Type of account
     Balance amount in the account
Methods
     To assign initial values
     To deposit an amount
     To withdraw an amount after checking balance
     To display the name and balance Incorporate a constructor to provide initial values.*/

#include<iostream>
#include<string>
using namespace std;
class bank_account{
    public:
    string name, type_of_account;
    int account_number, account_balance;
    
    void info(){
        cout<<"input your name :: ";
        getline(cin,name);

        cout<<"input your account_number :: ";
        cin>>account_number;
        
        cout<<"input your accout type :: ";
        cin>>type_of_account;
        
        cout<<"input your bank balance :: ";
        cin>>account_balance;
        
        cout<<"\n \n";
    };
    
    void display_info(){
        cout<<"account holder name is = "<<name<<endl<<endl;
        cout<<"account number = "<<account_number<<endl<<endl;
        cout<<"account type = "<<type_of_account<<endl<<endl;
        cout<<"your account balance = "<<account_balance<<endl<<endl;
    }
};



int main(){
    bank_account b;
    b.info();
    b.display_info();
}