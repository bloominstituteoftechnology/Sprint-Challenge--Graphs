
**SOCIAL.PY**
1. To create 100 users with an average of 10 friends each, how many times would you need to call `addFriendship()`? Why? (1pt)

    100^10 times. Because for each user, you need to call the .addFriendship method the avgFriendships number of times. This is of course not accounting for instances where errors occur and the method must be called again (e.g. userID == friendID when randomly generated)

    Exponential time complexity: O(c^n)

    The user number is our constant, and our complexity will increase exponentially with the amount of average friends we need to generate with each user.


2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network? (2pts)

    With 1000 users and 5 random friends each, we're looking at .005% chance of any given friend arriving in the given user's friend list.

    99.5% of all users should be in the extended social network.

    I cannot explain this mathematically, or even ensure that it is correct. It's just what sounds reasonable, and what I can see from running my algorithm (which, again, may be faulty).

    The average degree of separation: 1000 * .005 = 5 degrees of separation. I cannot explain how this works, only that I think it is correct.