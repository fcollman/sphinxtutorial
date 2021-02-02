import numpy as np
def repair_nose(verts: np.array, faces: np.array, iters:int=3):
    """function to repair the sphinx's nose

    Args:
        verts (np.array): vertices of sphinx mesh (Nx3 array)
        faces (np.array): faces of sphinx mesh, indices into verts (K,3) triangles
        iters (int): how many iterations of repairs (Default=3) 
    
    Returns:
        verts (np.array): fixed vertices
        faces (np.array): fixed faces
    """
    return verts, faces