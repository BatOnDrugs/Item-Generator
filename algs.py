# Python3 program for Bubble Sort Algorithm Implementation from GeekForGeek

# modified to take into account item type and stat to sort by
def bubble_sort_items(items, item_type, sort_by = "main stat"):
    sort_by = sort_by
    n = len(items)
    if item_type == "Armour":
        if sort_by == "main stat":
            sort_by = "defense"
    elif item_type == "Weapons":
        if sort_by == "main stat":
            sort_by = "dmg"
        
    # For loop to traverse through all 
    # elements in an items list
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Range of the items is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if getattr(items[j], sort_by) < getattr(items[j + 1], sort_by):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
                



