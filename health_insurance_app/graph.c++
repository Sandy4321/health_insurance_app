#include <iostream>
#include "bag.h"

using namespace std;


public class Graph {

  private:
    int V, E;
    Bag* adj;
  public:
    
    Graph() 
    {

      cout << "Number of vertices: ";
      cin << V;

      adj = new Bag[V];

      cout << "Number of edges: ";
      cin << E;

      for(int i = 0; i < E; i++)    
      {
      }
    }
  
    void add_edge(int u, int v) 
    {
      
 






int main() {
  
