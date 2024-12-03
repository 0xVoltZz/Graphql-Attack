
def build_graphql_query(endpoint_type, operation_name, args_names, args_types, return_name, pay):

    args_list = args_names.split(",") if args_names else []
    args_types_list = args_types.split(",") if args_types else []

    query = {
        "query": ""
    }

    if not args_names and not return_name:
        query["query"] = f"""
            {endpoint_type} {{
                {operation_name}
            }}          
        """
    
    elif not args_names and return_name:
        query["query"] = f"""
            {endpoint_type} {{
                {operation_name} {{
                    {return_name}
                }}
            }}          
        """

    elif args_types and args_list and return_name:
        query["query"] = f"""
            {endpoint_type} {{
                {operation_name}({build_args(args_list, args_types_list,pay)}) {{
                    {return_name}
                }}
            }}          
        """

    elif args_names and not return_name:
        query["query"] = f"""
            {endpoint_type} {{
                {operation_name}({build_args(args_list, args_types_list,pay)})
            }}          
        """
    
    elif args_names and args_types != "String" and return_name:
        query["query"] = f"""
            {endpoint_type} {{
                {operation_name}({build_args(args_list, args_types_list,pay)}) {{
                    {return_name}
                }}
            }}          
        """
    else:
        print("[-] Unsupported operation or arguments structure.")
        query = {}

    return query


def build_args(args_list, args_types_list, pay):
    args = []
    
    for arg_type in args_types_list[::-1]:
        for index, arg in  enumerate(args_list[::-1]) :
            if arg_type == "String" and index ==0:
                args.append(f'''{arg}: "{pay}"''')
            elif arg_type == "String" and index ==1:
                args.append(f'''{arg}: "Root"''')
            elif arg_type == "String" and index >1:
                args.append(f'''{arg}: "{index-2}"''')
            elif arg_type == "Int":
                args.append(f'{arg}: 123')
            elif arg_type == "Boolean":
                args.append(f'{arg}: true')
            elif arg_type == "ID":
                args.append(f'{arg}: "1"')
            else:
                args.append(f'{arg}: "Root"') 

    return ", ".join(args)
