# Insertion Sort

# unlike bubble sort which sorts by comparing adjacent pairs of values
# insertion sort sorts by comparing each value by all of the values before it and then places the value accordingly in its correct position
# toh therefore insertion mai sirf aik dafa order mai parsing hoti hai list ki, unlike bubble jismay bar bar hoti hai


def insertionsort(somelist):

    for index in range(1, len(somelist)):   # from 2nd item to the last item in the list
        tempindex = index   # isliye kiukay neechay index ki value ko decrement karna parh rha hai, so without using a temp variable, for loop kay index mai masla hota

        while (tempindex > 0) and (somelist[tempindex] < somelist[tempindex-1]):   
            somelist[tempindex-1], somelist[tempindex] = somelist[tempindex], somelist[tempindex-1]   # :D aala tariqa hai
            tempindex -= 1   # agr main index variable kay saath kartay toh for loop kharab ho jata
            
    print(somelist)

mylist = [230,43,8,101,5,100,9879,3,56]
insertionsort(mylist)
