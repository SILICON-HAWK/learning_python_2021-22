#include<iostream>
#include<vector>
using namespace std;

void print(vector<string> &vec){
    for(auto &item : vec){
        cout<<item<<" ";
    }
}
void swap_element(vector<string> &vec,string itm,string ritm){
    for(auto i=0;i<vec.size();i++){
        if(vec[i]==itm){
            vec[i]=ritm;
        }
    }
    cout<<"Item not found !";
}
int main(){
    vector<string> shop_list;
    //printing vector
    print(shop_list);
    cout<<endl;
    //appending item
    shop_list.push_back("eggs");
    shop_list.push_back("milk");
    shop_list.push_back("sugar");
    shop_list.push_back("choclate");
    shop_list.push_back("flour");
    print(shop_list);
    cout<<endl;
    //Deleting last item 
    shop_list.pop_back();
    print(shop_list);
    cout<<endl;
    //Appending item
    shop_list.push_back("coffee");
    print(shop_list);
    cout<<endl;
    //Replacing item in vector
    swap_element(shop_list,"sugar","honey");
    print(shop_list);
    cout<<endl;
    //Deleting item from vector
    vector<string>::iterator it;
    while(it!=shop_list.end()){
        if(*it=="milk"){
            shop_list.erase(it);
            break;
        }
        it++;
    }
    print(shop_list);
    return 0;
}