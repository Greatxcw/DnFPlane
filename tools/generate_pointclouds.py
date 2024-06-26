import numpy as np
import matplotlib.pyplot as plt
# import mcubes
# import trimesh
import os
import configargparse
import open3d as o3d
import cv2
import torch
import imageio
from tqdm import tqdm


name_list = ['cutting', 'pulling', 'pushing', 'tearing', 'thin', 'traction']
<<<<<<< HEAD
<<<<<<< HEAD
place_list = ['data/endonerf_full_datasets/cutting_tissues_twice/close_inf_depth.txt',
              'data/endonerf_full_datasets/pulling_soft_tissues/close_inf_depth.txt',
              'data/endonerf_full_datasets/pushing_tissues/close_inf_depth.txt',
=======
place_list = ['data/endonerf_full_datasets/cutting_tissues_twice/close_inf_depth.txt', 
              'data/endonerf_full_datasets/pulling_soft_tissues/close_inf_depth.txt', 
              'data/endonerf_full_datasets/pushing_tissues/close_inf_depth.txt', 
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
place_list = ['data/endonerf_full_datasets/cutting_tissues_twice/close_inf_depth.txt',
              'data/endonerf_full_datasets/pulling_soft_tissues/close_inf_depth.txt',
              'data/endonerf_full_datasets/pushing_tissues/close_inf_depth.txt',
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
              'data/endonerf_full_datasets/tearing_tissues/close_inf_depth.txt',
              'data/endonerf_full_datasets/thin_structures/close_inf_depth.txt',
              'data/endonerf_full_datasets/traction/close_inf_depth.txt']
'''
Setup
'''

# set cuda
torch.set_default_tensor_type('torch.cuda.FloatTensor')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# this is code for recon pcs from detected depth and rgb images
# for endonerf_dataset
# for edssr
<<<<<<< HEAD
<<<<<<< HEAD
# for endonerf
=======
# for endonerf 
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
# for endonerf
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
# for dnfplane

# hwf = [512, 640, 569.46820041]
# hwf = [512, 640, 1069.46820041] # xy will be miner
hwf = [512, 640, 341.68092024599997]

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

def reconstruct_pointcloud(test_time, nerf_args, vis_rgbd=False, depth_filter=None, verbose=True, crop_size=0):
    rgb_np, disp_np = generate_rgbd(test_time, nerf_args)
    depth_np = 1.0 / (disp_np + 1e-6)

    if crop_size > 0:
        rgb_np = rgb_np[:-crop_size, crop_size:, :]
        depth_np = depth_np[:-crop_size, crop_size:]

    if depth_filter is not None:
        depth_np = cv2.bilateralFilter(
            depth_np, depth_filter[0], depth_filter[1], depth_filter[2])
<<<<<<< HEAD
=======
def reconstruct_pointcloud(test_time, nerf_args, vis_rgbd=False, depth_filter=None, verbose=True, crop_left_size=0):
    rgb_np, disp_np = generate_rgbd(test_time, nerf_args)
    depth_np = 1.0 / (disp_np + 1e-6)
    
    if crop_left_size > 0:
        rgb_np = rgb_np[:, crop_left_size:, :]
        depth_np = depth_np[:, crop_left_size:]

    if depth_filter is not None:
        depth_np = cv2.bilateralFilter(depth_np, depth_filter[0], depth_filter[1], depth_filter[2])
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

    if verbose:
        print('min disp:', disp_np.min(), 'max disp:', disp_np.max())
        print('min depth:', depth_np.min(), 'max depth:', depth_np.max())

    rgb_im = o3d.geometry.Image(rgb_np.astype(np.uint8))
    depth_im = o3d.geometry.Image(depth_np)

<<<<<<< HEAD
<<<<<<< HEAD
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        rgb_im, depth_im, convert_rgb_to_intensity=False)
=======
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(rgb_im, depth_im, convert_rgb_to_intensity=False)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        rgb_im, depth_im, convert_rgb_to_intensity=False)
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

    if vis_rgbd:
        plt.subplot(1, 2, 1)
        plt.title('RGB image')
        plt.imshow(rgbd_image.color)
        plt.subplot(1, 2, 2)
        plt.title('Depth image')
        plt.imshow(rgbd_image.depth)
        plt.colorbar()
        plt.show()

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
<<<<<<< HEAD
<<<<<<< HEAD
        o3d.camera.PinholeCameraIntrinsic(
            hwf[1], hwf[0], hwf[2], hwf[2], hwf[1] / 2, hwf[0] / 2)
=======
        o3d.camera.PinholeCameraIntrinsic(hwf[1],hwf[0], hwf[2], hwf[2], hwf[1] / 2, hwf[0] / 2)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
        o3d.camera.PinholeCameraIntrinsic(
            hwf[1], hwf[0], hwf[2], hwf[2], hwf[1] / 2, hwf[0] / 2)
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    )

    return pcd

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

def load_rgb_images(path):  # uint8 [0, 255]
    return imageio.v2.imread(path)


def load_depth_images(path):  # uint8 [0, 255]
<<<<<<< HEAD
=======
def load_rgb_images(path): # uint8 [0, 255]
    return imageio.v2.imread(path)

def load_depth_images(path): # uint8 [0, 255]
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    # to avoid the outliears, we clip the depth images
    temp = imageio.v2.imread(path)
    temp = np.clip(temp, 0, 255)
    return temp.astype(np.uint8)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

def load_depth_npy(path):  # floate32 [0, max]
    return np.load(path)


<<<<<<< HEAD
=======
def load_depth_npy(path): # floate32 [0, max]
    return np.load(path)

>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
def list_given_ext(dir, ext='.png'):
    # a warpper for os.list dir, only consider given ext
    return [f for f in os.listdir(dir) if f.endswith(ext)]

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

def reconstruct_pointclouds(rgb_np, depth_np, vis_rgbd=False, depth_filter=None, verbose=True, crop_size=0):

    if crop_size > 0:
        rgb_np = rgb_np[:-crop_size, crop_size:, :]
        depth_np = depth_np[:-crop_size, crop_size:]

    if depth_filter is not None:
        depth_np = cv2.bilateralFilter(
            depth_np, depth_filter[0], depth_filter[1], depth_filter[2])
<<<<<<< HEAD
=======
def reconstruct_pointclouds(rgb_np, depth_np, vis_rgbd=False, depth_filter=None, verbose=True, crop_left_size=0):

    if crop_left_size > 0:
        rgb_np = rgb_np[:, crop_left_size:, :]
        depth_np = depth_np[:, crop_left_size:]

    if depth_filter is not None:
        depth_np = cv2.bilateralFilter(depth_np, depth_filter[0], depth_filter[1], depth_filter[2])
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

    if verbose:
        print('min depth:', depth_np.min(), 'max depth:', depth_np.max())

    rgb_im = o3d.geometry.Image(rgb_np.astype(np.uint8))
    depth_im = o3d.geometry.Image(depth_np)

<<<<<<< HEAD
<<<<<<< HEAD
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        rgb_im, depth_im, convert_rgb_to_intensity=False)
=======
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(rgb_im, depth_im, convert_rgb_to_intensity=False)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        rgb_im, depth_im, convert_rgb_to_intensity=False)
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

    if vis_rgbd:
        plt.subplot(1, 2, 1)
        plt.title('RGB image')
        plt.imshow(rgbd_image.color)
        plt.subplot(1, 2, 2)
        plt.title('Depth image')
        plt.imshow(rgbd_image.depth)
        plt.colorbar()
        plt.show()

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
<<<<<<< HEAD
<<<<<<< HEAD
        o3d.camera.PinholeCameraIntrinsic(
            hwf[1], hwf[0], hwf[2], hwf[2], hwf[1] / 2, hwf[0] / 2)
=======
        o3d.camera.PinholeCameraIntrinsic(hwf[1],hwf[0], hwf[2], hwf[2], hwf[1] / 2, hwf[0] / 2)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
        o3d.camera.PinholeCameraIntrinsic(
            hwf[1], hwf[0], hwf[2], hwf[2], hwf[1] / 2, hwf[0] / 2)
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    )
    # vis point clouds
    # o3d.visualization.draw_geometries([pcd])
    return pcd

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

if __name__ == '__main__':
    parser = configargparse.ArgumentParser()
    parser.add_argument('--root_path', type=str,
                        default='/data/ForPlane-main/ForPlane-main/exps/endonerf_cutting_tissues_twice_32k_gt_depth_test_2/endonerf_32k/estm', help='root_path')
    parser.add_argument('--vis_rgbd', action='store_true',
                        help='visualize rgbd')
    parser.add_argument("--depth_smoother", action='store_true',
                        help='apply bilateral filtering on depth maps?')
    parser.add_argument("--depth_smoother_d", type=int, default=32,
                        help='diameter of bilateral filter for depth maps')
    parser.add_argument("--depth_smoother_sv", type=float, default=64,
                        help='The greater the value, the depth farther to each other will start to get mixed')
    parser.add_argument("--depth_smoother_sr", type=float, default=32,
                        help='The greater its value, the more further pixels will mix together')
    parser.add_argument('--verbose', type=bool, default=True, help='verbose')
    parser.add_argument('--crop_size', type=int, default=30, help='crop size')
    parser.add_argument("--no_pc_saved", action='store_true',
                        help='donot save reconstructed point clouds?')
    parser.add_argument('--out_postfix', type=str, default='',
                        help='the postfix append to the output directory name')
    parser.add_argument('--data_type', type=str, default=None,
                        help='the postfix append to the output directory name')
<<<<<<< HEAD
=======
if __name__ == '__main__':
    parser = configargparse.ArgumentParser()
    parser.add_argument('--root_path', type=str, default='/data/ForPlane-main/ForPlane-main/exps/endonerf_cutting_tissues_twice_32k_gt_depth_test_2/endonerf_32k/estm', help='root_path')
    parser.add_argument('--vis_rgbd', action='store_true', help='visualize rgbd')
    parser.add_argument("--depth_smoother", action='store_true', help='apply bilateral filtering on depth maps?')
    parser.add_argument("--depth_smoother_d", type=int, default=32, help='diameter of bilateral filter for depth maps')
    parser.add_argument("--depth_smoother_sv", type=float, default=64, help='The greater the value, the depth farther to each other will start to get mixed')
    parser.add_argument("--depth_smoother_sr", type=float, default=32, help='The greater its value, the more further pixels will mix together')
    parser.add_argument('--verbose', type=bool, default=True, help='verbose')
    parser.add_argument('--crop_left_size', type=int, default=75, help='crop left size')
    parser.add_argument("--no_pc_saved", action='store_true', help='donot save reconstructed point clouds?')
    parser.add_argument('--out_postfix', type=str, default='', help='the postfix append to the output directory name')
    parser.add_argument('--data_type', type=str, default=None, help='the postfix append to the output directory name')
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    args = parser.parse_args()

    # build depth filter
    if args.depth_smoother:
<<<<<<< HEAD
<<<<<<< HEAD
        depth_smoother = (args.depth_smoother_d,
                          args.depth_smoother_sv, args.depth_smoother_sr)
=======
        depth_smoother = (args.depth_smoother_d, args.depth_smoother_sv, args.depth_smoother_sr)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
        depth_smoother = (args.depth_smoother_d,
                          args.depth_smoother_sv, args.depth_smoother_sr)
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    else:
        depth_smoother = None

    # reconstruct pointclouds
    print('Reconstructing point clouds...')

<<<<<<< HEAD
<<<<<<< HEAD
    # for GT
=======

    ## for GT
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
    # for GT
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    # if not args.no_pc_saved:
    #     out_dir = os.path.join(args.root_path, 'pointclouds')
    #     if not os.path.exists(out_dir):
    #         os.makedirs(out_dir)
    #     parser.write_config_file(args, [os.path.join(out_dir, 'args.txt')])
    # img_names = [i for i in sorted(os.listdir(args.root_path + "/images"), key=lambda x: int(x.split('.')[0])) if i.endswith('.png')]
    # depth_names = [i for i in sorted(os.listdir(args.root_path + "/depth"), key=lambda x: int(x.split('.')[0])) if i.endswith('.png')]
    # for i in tqdm(range(len(img_names))):
    #     img = load_rgb_images(os.path.join(args.root_path, 'images', img_names[i]))
    #     depth = load_depth_images(os.path.join(args.root_path, 'depth', depth_names[i]))
    #     # check img data type and depth data type
    #     # print('img data type:', img.dtype, 'depth data type:', depth.dtype)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    #     pcd = reconstruct_pointclouds(img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_size)
    #     if not args.no_pc_saved:
    #         o3d.io.write_point_cloud(os.path.join(out_dir, args.out_postfix+'_'+img_names[i].split('.')[0] + '.ply'), pcd)
    # break
<<<<<<< HEAD
=======
    #     pcd = reconstruct_pointclouds(img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_left_size)
    #     if not args.no_pc_saved:
    #         o3d.io.write_point_cloud(os.path.join(out_dir, args.out_postfix+'_'+img_names[i].split('.')[0] + '.ply'), pcd)
        # break
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

    # # for predicted endo
    # # output directory
    # if not args.no_pc_saved:
    #     out_dir = os.path.join(os.path.dirname(os.path.dirname(args.root_path)), 'pointclouds')
    #     if not os.path.exists(out_dir):
    #         os.makedirs(out_dir)
    #     parser.write_config_file(args, [os.path.join(out_dir, 'args.txt')])
    # img_names = [i for i in sorted(list_given_ext(args.root_path), key=lambda x: int(x.split('.')[0])) if i.endswith('.png')]
    # depth_names = [i for i in sorted(list_given_ext(args.root_path, ext='.npy'), key=lambda x: int(x.split('.')[0])) if i.endswith('.npy')]
    # print(img_names, depth_names)
    # for i in tqdm(range(len(img_names))):
    #     img = load_rgb_images(os.path.join(args.root_path, img_names[i]))
    #     depth = load_depth_npy(os.path.join(args.root_path, depth_names[i])).astype(np.float32)
    #     # check img data type and depth data type
    #     # print('img data type:', img.dtype, 'depth data type:', depth.dtype)
<<<<<<< HEAD
<<<<<<< HEAD
    #     pcd = reconstruct_pointclouds(img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_size)
=======
    #     pcd = reconstruct_pointclouds(img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_left_size)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
    #     pcd = reconstruct_pointclouds(img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_size)
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    #     # break
    #     if not args.no_pc_saved:
    #         o3d.io.write_point_cloud(os.path.join(out_dir, args.out_postfix+'_'+img_names[i].split('.')[0] + '.ply'), pcd)
    #     # break

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    # for dnfplane
    # output directory
    assert args.data_type in name_list

    if not args.no_pc_saved:
        out_dir = os.path.join(os.path.dirname(args.root_path), 'pointclouds')
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        parser.write_config_file(args, [os.path.join(out_dir, 'args.txt')])
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb

    if args.data_type == None:
        assert args.root_path.split('/')[-2].split('_')[-1] in name_list
        # get name list idx
        name_list_idx = name_list.index(
            args.root_path.split('/')[-2].split('_')[-1])
<<<<<<< HEAD
=======
    
    if args.data_type == None:
        assert args.root_path.split('/')[-2].split('_')[-1] in name_list
        # get name list idx
        name_list_idx = name_list.index(args.root_path.split('/')[-2].split('_')[-1])
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    else:
        name_list_idx = name_list.index(args.data_type)
    # get close depth and inf depth from place_list
    close_depth, inf_depth = np.loadtxt(place_list[name_list_idx])
    print(close_depth, inf_depth)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
    img_names = [i for i in sorted(list_given_ext(
        args.root_path), key=lambda x: int(x.split('.')[0])) if i.endswith('.png')]
    depth_names = [i for i in sorted(list_given_ext(
        args.root_path, ext='.npy'), key=lambda x: int(x.split('.')[0][5:])) if i.endswith('.npy')]
    print(img_names, depth_names)
    for i in tqdm(range(len(img_names))):
        img = load_rgb_images(os.path.join(args.root_path, img_names[i]))
        depth = load_depth_npy(os.path.join(
            args.root_path, depth_names[i])).astype(np.float32)
<<<<<<< HEAD
=======
    img_names = [i for i in sorted(list_given_ext(args.root_path), key=lambda x: int(x.split('.')[0])) if i.endswith('.png')]
    depth_names = [i for i in sorted(list_given_ext(args.root_path, ext='.npy'), key=lambda x: int(x.split('.')[0][5:])) if i.endswith('.npy')]
    print(img_names, depth_names)
    for i in tqdm(range(len(img_names))):
        img = load_rgb_images(os.path.join(args.root_path, img_names[i]))
        depth = load_depth_npy(os.path.join(args.root_path, depth_names[i])).astype(np.float32)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
        if close_depth is not None:
            depth *= (inf_depth-close_depth)
        # check img data type and depth data type
        # print('img data type:', img.dtype, 'depth data type:', depth.dtype)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
        pcd = reconstruct_pointclouds(
            img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_size)
        # break
        if not args.no_pc_saved:
            # judge if the img_name is %3d, if it is %3d, just use the img_name as the ply name, else transfer to %3d
            assert int(img_names[i].split('.')[0]
                       ) == i, 'img_names should inline with idx'
            o3d.io.write_point_cloud(os.path.join(
                out_dir, args.out_postfix+'_'+f'{i:03d}.ply'), pcd)
<<<<<<< HEAD
=======
        pcd = reconstruct_pointclouds(img, depth, args.vis_rgbd, depth_smoother, args.verbose, args.crop_left_size)
        # break
        if not args.no_pc_saved:
            # judge if the img_name is %3d, if it is %3d, just use the img_name as the ply name, else transfer to %3d
            assert int(img_names[i].split('.')[0])==i, 'img_names should inline with idx'
            o3d.io.write_point_cloud(os.path.join(out_dir, args.out_postfix+'_'+f'{i:03d}.ply'), pcd)
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
        # break

    # demo script
    # python form_pcs_from_depth_and_image.py --root_path dnfplane/iter2000/full_2000_cutting/estm \
    #                                         --out_postfix lp_recon \
<<<<<<< HEAD
<<<<<<< HEAD
    #                                         --depth_smoother
=======
    #                                         --depth_smoother
>>>>>>> 7b47ab7f3206d9ec6e484f2424448b04149fba99
=======
    #                                         --depth_smoother
>>>>>>> b26eda0cef18828bb6d35a349459deb84f752fbb
