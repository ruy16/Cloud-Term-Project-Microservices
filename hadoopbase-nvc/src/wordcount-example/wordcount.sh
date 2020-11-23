#!/usr/bin/env bash
hdfs dfs -mkdir /input
hdfs dfs -mkdir /output
hdfs dfs -put inputtext.txt /input
hadoop jar wordcount.jar wordcount.WordCount /input/* /output/wordcount
hdfs dfs -cat /output/wordcount/part-r-00000