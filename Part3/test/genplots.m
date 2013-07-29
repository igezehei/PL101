ids = gendata('IDS_Statistics.txt');
astar = gendata('ASTAR_Statistics.txt');

plot(ids(:,1),ids(:,2),'r+');
hold on
plot(ids(:,1),astar(:,2),'o');

xlabel('number of cities(nodes)');
ylabel('time takend by bfs and astar(nodes)');
title('Comparision of the time taken by ids and astar with varying numbers of cities');

print -djpeg time.jpg;
hold off;
clear all;
ids_1 = gendata('IDS_Statistics.txt');
astar_1 = gendata('ASTAR_Statistics.txt');

plot(ids_1(:,1),ids_1(:,3),'r+');
hold on
plot(ids_1(:,1),astar_1(:,3),'o');

xlabel('number of cities(nodes)');
ylabel('space takend by bfs and astar(nodes)');
title('Comparision of the space taken by ids and astar with varying numbers of cities');
print -djpeg space.jpg;
hold off

