    Author   : Amit Singh Sansoya (@amit3200)
    Github   : https://github.com/Amit3200
    library  : graphq

    #Import  
    	import graphq

    #Introduction
    This is test library for the python which lets you create graph using some functions.
    This library will allow you to create undirected graphs and also provides some of the
    other functionalities. This library is for the beginner programmer who wants to get started
    at the programming with the graphs and want to visualize it easily. It is highly recommended to
    learn the actual code so that one can implement them without using this library at the interviews,
    and competition. This library was designed for the programmers who are studying graph currently.
    This will allow them to have the idea and brute force solution to them which they can further optimize.

    This libary also allow's you to do following things
        1. Create Graph [Undirected]
        2. Detect Cycle [Undirected]
        3. Check Path [Undirected]
        4. Disconnected Components [Undirected]

    #Functions
    1. Create Graph

        Description:

            This function allow you to add the edge between two nodes.
            The use of this function is very simple. One only needs to pass the
            dictionary so called graph,node u and node v where edge will exist between
            u and v. Moreover the edge v and u will be automatically created as this
            is undirected graph.
    

        Function Use : insertuv(dictionary_name,node1,node2)

        Example : graphq.insert_uv(d,1,2)

        Return Type : None

        In above example d is the dictionary (so called graph)

    2. Detect Cycle

        Description:

            As the name suggests, this function will allow you to detect if there is a cycle in graph
            Return type is Boolean [True or False] where True tells that graph has cycle and False depicts
            there is no cycle. This will detect as per the undirected graph.

        Function use : detect_cycle(dictionary_name)

        Example : graphq.detect_cycle(d)

        Return Type : Boolean

        In above example d is the dictionary (so called graph)

    3. Check Path

        Description:

            As the name says this function will tell you if there exists the path between two nodes.
            One only needs to pass dictionary_name (so called graph), the node u and node v. This function
            returns boolean value. True if there is path between u and v else False

        Function use : check_path(dictionary_name,node1,node2)

        Example : graphq.check_path(d,2,8)

        Return Type : Boolean

        In above example d is the dictionary (so called graph)

    4. Disconnected Components

        Description:

            As the name says this function will detect the disconnected components and this will return a dictionary
            having keys as:
            'dis_count': This will give you the values of count of disconnected components in a graph. If the value returned
                         is 1 then there is no disconnected component. [ Makes Sense ;) ]
            'components': Gives the list of containing nodes which are connected together

            Function use : graphq.get_disconnected_components(d)
                           graphq.get_disconnected_components(d)['dis_count']
                           graphq.get_disconnected_components(d)['components']


    #Note
    Remember :  This library resembles undirected graph
                Also Get the logic behind function that is very important


    #Do Support
    Author   : Amit Singh Sansoya (@amit3200)
    Github   : https://github.com/Amit3200

    Keep Coding and Smiling
