<div>
Author   : Amit Singh Sansoya (@amit3200)<br>
Github   : https://github.com/Amit3200<br>
library  : graphq<br>
</div>

# Import  
```import graphq```

# Introduction
<p>
    This is test library for the python which lets you create graph using some functions.
    This library will allow you to create undirected graphs and also provides some of the
    other functionalities. This library is for the beginner programmer who wants to get started
    at the programming with the graphs and want to visualize it easily. It is highly recommended to
    learn the actual code so that one can implement them without using this library at the interviews,
    and competition. This library was designed for the programmers who are studying graph currently.
    This will allow them to have the idea and brute force solution to them which they can further optimize.
    This libary also allow's you to do following things
    <ul>
        <li> Create Graph [Undirected]</li>
        <li> Detect Cycle [Undirected]</li>
        <li> Check Path [Undirected]</li>
        <li> Disconnected Components [Undirected]</li>
    </ul>
 </p>       
<ul>
    <li>
        <h1>Create Graph</h1>
            <h3>Description:</h3>
                    <p>This function allow you to add the edge between two nodes.
                    The use of this function is very simple. One only needs to pass the
                    dictionary so called graph,node u and node v where edge will exist between
                    u and v. Moreover the edge v and u will be automatically created as this
                    is undirected graph.</p><br>
        <p>
          Function Use : insertuv(dictionary_name,node1,node2)<br>
          Example : graphq.insert_uv(d,1,2)<br>
          Return Type : None<br>
          In above example d is the dictionary (so called graph)<br>
        </p>
    </li>
    <li>
        <h1>Detect Cycle</h1>
        <h3>Description:</h3>
            <p>
            As the name suggests, this function will allow you to detect if there is a cycle in graph
            Return type is Boolean [True or False] where True tells that graph has cycle and False depicts
                there is no cycle. This will detect as per the undirected graph.</p><br>
        <p>
        Function use : detect_cycle(dictionary_name)<br>
        Example : graphq.detect_cycle(d)<br>
        Return Type : Boolean<br>
        In above example d is the dictionary (so called graph)<br>
        </p>
   </li>
   <li> <h1>Check Path</h1>
        <h3>Description:</h3>
      <p>
            As the name says this function will tell you if there exists the path between two nodes.
            One only needs to pass dictionary_name (so called graph), the node u and node v. This function
         returns boolean value. True if there is path between u and v else False</p>
         <br>
      <p>
        Function use : check_path(dictionary_name,node1,node2)<br>
        Example : graphq.check_path(d,2,8)<br>
        Return Type : Boolean<br>
        In above example d is the dictionary (so called graph)<br>
        </p>
   </li>
<li>
   <h1> Disconnected Components</h1>
        <h3>Description:</h3>
      <p>
            As the name says this function will detect the disconnected components and this will return a dictionary
            having keys as:
            'dis_count': This will give you the values of count of disconnected components in a graph. If the value returned
                         is 1 then there is no disconnected component. [ Makes Sense ;) ]
         'components': Gives the list of containing nodes which are connected together</p>
         <br>
         <p>
           Function use : graphq.get_disconnected_components(d)<br>
                           graphq.get_disconnected_components(d)['dis_count']<br>
                           graphq.get_disconnected_components(d)['components']<br>
           Return Type : Dict<br>
   </p>
   </li>
  </ul>
  
# Note
<h5>Remember</h5> 
This library resembles undirected graph<br>
Also Get the logic behind function that is very important<br>
<br>
# Do Support
Author   : Amit Singh Sansoya (@amit3200)<br>
Github   : https://github.com/Amit3200`<br>
<h4> Keep Coding and Smiling</h4>
