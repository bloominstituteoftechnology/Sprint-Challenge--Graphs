To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why? (1pt)

I made a list of possible users that's length was set by input n in the function
I took the average input and multiplied it by 2
then I get a random number between 0 and that number which over time would give me the average
I also need to make sure that I'm adding a friend to itself or repeating a friendship already given

addFriendship would be therefore be called this many times:

number_of_users * (random_number_for_average - both_random_conditionals)

or O(n^r)

where r is the random number - the conditionals

If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network? (2pts)