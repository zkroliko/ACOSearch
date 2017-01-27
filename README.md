# ACOSearch
Implementation of ACO algorithm optimizing line of sight search of an area.

## Concept

The task is finding a path covering all fields by sight of the (almost)minimal length. The algorithm uses transition pheromone maps over a defined number of iterations.

![Path and pheromone](https://cloud.githubusercontent.com/assets/8882153/22369821/7b604fe2-e48e-11e6-8b9f-c856d831cfbc.png)

## Effects

The algorithm has proven effective, however the Python implemenation is ineffiecient. Problem itself can be parralelized however Python interpreter concurrency leaves much to wish for. Expect > 50x performance increase in a C++ implementation for single core.

![effect](https://cloud.githubusercontent.com/assets/8882153/22370060/b44a5efa-e48f-11e6-9469-2ae748b7f8c8.JPG)

## Organization

Directories are a mess.

## Credits

Designed and implemented as a part of curriculum at AGH Kraków by a student team.
