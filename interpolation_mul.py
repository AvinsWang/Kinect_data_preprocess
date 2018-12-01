# coding:utf-8
import cv2
import numpy as np
import os
from multiprocessing import Pool

# [512, 424] -> [424, 318]
def cut_from_dir(dir):
    img = cv2.imread(dir)[53:371, 44:468, :]
    return img

def cut_from_img(img):
    img = img[53:371, 44:468, :]
    return img

def cut_from_depth(img):
    img = img[53:371, 44:468]
    return img

def mask_from_img(img):
    img = np.array(img)
    mask = np.zeros([img.shape[0], img.shape[1], 1])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] == 0:
                mask[i][j][0] = 255
            else:
                mask[i][j][0] = 0
    mask = mask.astype(np.uint8)
    return mask

def mask_from_depth(img):
    img = np.array(img)
    mask = np.zeros([img.shape[0], img.shape[1]])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] == 0:
                mask[i][j] = 255
            else:
                mask[i][j] = 0
    mask = mask.astype(np.uint8)
    return mask

def interpolate_from_img(img, img_masked):
    dst = cv2.inpaint(img, img_masked, 3, cv2.INPAINT_TELEA)
    return dst

def rgb(dir):
    img = cv2.imread(dir)
    img_masked = mask_from_img(img)
    img_inted = interpolate_from_img(img, img_masked)
    img_cut = cut_from_img(img_inted)
    cv2.imwrite(dir, img_cut)
    print(dir)

def depth(dir):
    imgd = cv2.imread(dir, flags=2)
    depth_masked = mask_from_depth(imgd)
    img_inted = interpolate_from_img(imgd, depth_masked)
    img_cut = cut_from_depth(img_inted)
    cv2.imwrite(dir, img_cut)
    print(dir)

def run(rdir,ddir):
    rdirs = os.listdir(rdir)
    ddirs = os.listdir(ddir)
    process_rgb_dirs = []
    process_dep_dirs = []
    for r in rdirs:
        process_rgb_dirs.append(os.path.join(rdir, r))
    for d in ddirs:
        process_dep_dirs.append(os.path.join(ddir, d))
    p = Pool(12)
    p.map(rgb, process_rgb_dirs)
    p.map(depth, process_dep_dirs)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()


# /* 8bit, color or not */ CV_LOAD_IMAGE_UNCHANGED =-1,
# /* 8bit, gray */ CV_LOAD_IMAGE_GRAYSCALE =0,
# /* ?, color */ CV_LOAD_IMAGE_COLOR =1,
# /* any depth, ? */ CV_LOAD_IMAGE_ANYDEPTH =2,
# /* ?, any color */ CV_LOAD_IMAGE_ANYCOLOR =4

if __name__ == "__main__":
    rdir = "../../map/"
    ddir = "../../depth/"
    run(rdir, ddir)








