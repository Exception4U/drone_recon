import open3d as o3d
import sys

pcd = o3d.io.read_point_cloud(sys.argv[1])

alpha = 0.03
print(f"alpha={alpha:.3f}")
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
print("mesh generated")

mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)
o3d.io.write_triangle_mesh(sys.argv[1][:-5]+"mesh.ply",mesh)
