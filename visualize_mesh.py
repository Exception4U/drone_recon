import open3d as o3d
import sys

pcd = o3d.io.read_triangle_mesh(sys.argv[1])
o3d.visualization.draw_geometries([pcd])