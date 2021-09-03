## Test Data

#### Main Menu

```
mx,my = 0,0
```
```
mx,my = 150,215
```
```
mx,my = 190,240
```
```
mx,my = 280,310
```
```
mx,my = 1008,560
```
```
mx,my = 1122,600
```

The chosen test data allows for points one the edge of the buttons, in the buttons (all three to test functionality of all of them), and beyond the buttons. This means the intended purose and locational placement in regards to the UI can be confirmed as correct.

#### Naming Sub-Routine

```
keyboard input: a
```

```
keyboard input: z
```

```
keyboard input: -
```

```
keyboard input: 1
```

```
keyboard input: 9
```

```
keyboard input: 0
```

```
keyboard input: =
```

```
keyboard input: \
```

```
keyboard input: command key
```

```
keyboard input: option key
```

```
keyboard input: apple-123pinaple
```

Each selected test input is important. As we convert from input to ASCII to the letter as a string, we test the limits of the allotted range being a and z for the alphabet, 1 to 9 and 0 for the numbers, and the - as it is an allowed character. We also test = as it is an unallowed input as per the range limit. We further test for the command key and the option key which are keys without ASCII equivalent. We will also test apple-123pinaple to ensure the max character feature is functional.

#### Linear Search

```
list: 1,2,3,5,6,2,7
input: 1
```

```
list: 1,2,3,5,6,2,7
input: 4
```

```
list: 1,2,3,5,6,2,7
input: 7
```

```
list: 1,2,3,5,6,2,7
input: 8
```

```
list: 1,2,3,5,6,2
input: 2
```

We test for specific inputs. To start with we test for 1 which is the first content of the list, and similarly we test for 7 which is at the end of the list. We test for 4 which is within the list. Further we test for 8 which is not within the list. Additionally we test for 2 which is within the list twice. We do this to ensure that the program identifies that it is within the list twice and whereabouts its location is.