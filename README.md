# PHY607_Project1

In this repository I have created five separate python files, two for the methods applied to an RC circuit and three for the methods applied to a volume charge distribution. 

To use this repo, navigate to the directory where you want to clone it:

```
cd /path/you/want/repo 
```

then clone the repo and cd into it:

```
 /git clone git@github.com:jrrice5908/PHY607_Project1.git # with ssh
```

```
 cd PHY607_Project1
```

To get the file output, run the corresponding python command:

```
$: python RCcircuit_EulerMethod.py
$: python RCcircuit_4thRungeKutta.py
$: python RiemannSum.py
$: python Simpsonsum.py
$: python TrapSum.py
```

The output of the ODE files is a standard python plot. After the file is ran, a line in this module will save the figure to the pwd, you should be able to identify it by the name of the png. Each module produces solutions for two different sets of initial conditions. 
