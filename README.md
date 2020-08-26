**Problem Description**

We aim to visualize the simulations of a [Single Server
Queueing](https://en.wikipedia.org/wiki/Queueing_theory#Single_queueing_nodes)
(simulation code attached) using the python library **dash**. Our goal
is to visualize the delays of each customer for a given set of
parameters.

**FIFO Single Server model**

There is one server (e.g. an ATM machine) behind which forms a queue
(waiting system for arriving customers). The n^th^ Customer C~n~ arrives
as time t~n~ where

0 = t~0~ \< t~1~ \< t~2~ ..... \< t~n~ \< ................

With lim~n\ -\>\ ∞~ t~n~ = ∞

The interarrival time T~n~ is the length of time between the arrival of
successive customers C~n~ and C~n+1~ i.e.

$$T_{n} = \ t_{n + 1} - t_{n}\ $$

Let $S_{n}$ denote the service time of $C_{n}$

Let $D_{n}$ denote the waiting time of $C_{n}$ then:

$$D_{n + 1} = {max(D}_{n} + S_{n} - T_{n},\ 0)$$

We want to plot the series of $D_{n}$s for different parameters. For our
case we will assume that the service time of $C_{n}\ $is a Poisson
Distribution with mean $\lambda$ and the Interarrival time is a Uniform
distribution with a = 1. The user can choose $\lambda$ from a set of
$\{ 1.0,\ 3.0,\ 5.0\}$ and $b$ from a set of
$\{ 3.0,\ 5.0,\ 7.0,\ 10.0\}$

$$S\ \sim\ Poiss(\lambda)$$

and

$$T\ \sim\ Unif(1,\ b)$$

**Note:** a sim.py file is attached with this test to provide a helper
simulation class. You can simulate the Single Server Queue (SSQ) as
follows

**Expected Output**

![](media/image2.png){width="6.5in" height="2.527083333333333in"}

The title of the dashboard is **Single Server Queue**

The title of the graph is **Delay of a Single Server Queue.** The color
code of the grid lines is \#dddddd with x-gridlines disabled and the
current values in the dropdown selector are disabled i.e. the user
cannot select the current values. The label of the x-axis is **N** and
y-axis is **D~n~.** The Service time (S) dropdown will be used for
selecting $\lambda$ (default: 3.0) and Interarrival Times (T) for
selecting $b$(default: 5.0).

This is the minimum expectation; in fact, you are encouraged to add some
useful features on your own which you believe would make the dashboard
easier for the end-user to understand.

**Submission**

We expect you to create a GitHub repo and submit its link. We will clone
the repo and run it in a fresh python virtual environment. Please do not
forget to add the **requirements.txt** file.

Please submit the test by **August 28, 2020 11:59 PM ET**
