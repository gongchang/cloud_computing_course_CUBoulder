hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input apat63_99.txt -output output.txt
