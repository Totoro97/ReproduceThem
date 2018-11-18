#include "Tetra.h"

#include <iostream>
#include <vector>

int main() {
  std::vector<Eigen::Vector3d> points;

  for (int i = 0; i < 2; i++)
    for (int j = 0; j < 2; j++)
      for (int k = 0; k < 2; k++) 
        points.emplace_back(static_cast<double>(i), static_cast<double>(j), static_cast<double>(k));
  
  auto tetras = new std::vector<Tetra>();
  Tetrahedralization(points, tetras);
  for (const auto &tetra : *tetras) {
    std::cout << "----------tetra----------\n";
    for (int i = 0; i < 4; i++) {
      std::cout << tetra.points_[i].transpose() << std::endl;
    }
  }
  return 0;
}