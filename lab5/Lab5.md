# Lab 5: Build Systems

# Part 1:

## Step 1: A Basic Starting Point 

### Code Updates: <br>
![step1_b.png](step1_b.PNG)

### Terminal: <br>
![step1_a.png](step1_a.PNG)


## Step 2: Adding a Library 

### Code Updates: <br>
![step2_b.png](step2_b.PNG)

### Terminal: <br>
![step2_a.png](step2_a.PNG)


## Step 3: Installing and Testing

### Code Updates: <br>
![step3_b.png](step3_b.PNG)

![step3_c.png](step3_c.PNG)

![step3_d.png](step3_d.PNG)

### Terminal: <br>
![step3_a.png](step3_a.PNG)


## Step 4: Adding System Introspection

### Code Updates: <br>
![step4_b.png](step4_b.PNG)

![step4_c.png](step4_c.PNG)

### Terminal: <br>
![step4_a.png](step4_a.PNG)

## Step 5: Adding a Generated File and Generator

### Code Updates: <br>
![step5_b.png](step5_b.PNG)

![step5_c.png](step5_c.PNG)

### Terminal: <br>
![step5_a.png](step5_a.PNG)


# Part 2: 

## MakeFile:
```makefile
all: static_block dynamic_block
block.o: ./source/block.c
	gcc -c ./source/block.c -o ./bin/block.o

libblock_static.a: block.o
	ar rcs ./bin/libblock_static.a ./bin/block.o

libblock_dynamic.so: block.o
	gcc -shared ./bin/block.o -o ./bin/libblock_dynamic.so

program.o: ./program.c
	gcc -c ./program.c -o ./bin/program.o

static_block: program.o libblock_static.a
	gcc ./bin/program.o -L./bin -lblock_static -o ./bin/static_block

dynamic_block: program.o libblock_dynamic.so
	gcc ./bin/program.o -L./bin -l:libblock_dynamic.so -o ./bin/dynamic_block
```

<br>

## CMakeLists.txt:
```cmake
cmake_minimum_required(VERSION 3.0)
project(Lab5-part2)
include_directories(headers)

add_library(static STATIC source/block.c)
add_library(dynamic SHARED source/block.c)

add_executable(dynamic_block program.c)
target_link_libraries(dynamic_block dynamic)

add_executable(static_block program.c)
target_link_libraries(static_block static)
```
<br>

