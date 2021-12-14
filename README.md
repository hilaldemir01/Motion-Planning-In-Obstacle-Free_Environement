# Motion-Planning-In-Obstacle-Free_Environement
Specifications:
1. 3 Turtles will move in a single ROS TurtleSim window.
2. All turtles should start moving simultaneously.
3. The first two turtles should execute the motion pattern that is explained in steps 3-6.
4. The third turtle should execute the motion pattern that is explained in step 7.
5. The motion of each turtle proceeds in rounds; round-1, round-2, and round-3. The turtle stops moving
after it executes 3 rounds. In each round, the turtle tosses a fair coin (e.g. 0 refers to a head, and 1 refers
to a tail outcome) to decide its direction. If it tosses head, it moves right and comes back to its initial
location; otherwise, it moves left and then comes back to its initial location. If the previous direction of
the turtle is the same as its current direction, the turtle increases the distance it travels by one unit;
otherwise, it doubles its distance. For example: Assume that the coin tosses of turtle-1 in round 1-3 are
“Head, Head, Tail”, respectively. Then, the turtle moves 1 unit right in round=1, 2 units right in round=2,
and 4 units left in round=3.
6. Before the turtle returns back to its initial location, it should first move 0.3 units down.
7. The motion of turtle-3 also proceeds in rounds. However, unlike the first two turtles, turtle-3 executes
only 2 rounds. In each round, the turtle tosses a fair coin (e.g. 0 refers to a head, and 1 refers to a tail
outcome) to decide its direction. If it tosses head, it moves right; otherwise, it moves left. In each round,
the turtle draws a half circle with radius r. r = 1 in round-1 and r = 2 in round-2.
8. Each turtle should always face the direction it moves.
9. You should create only one python node to control turtle1 or turtle2 and a separate python node to
control turtle3.
10. Create a launch file that will start the ROS Turtlesim also the motion of three turtles simultaneously.
