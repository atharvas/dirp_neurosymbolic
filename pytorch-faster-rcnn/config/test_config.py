class Config:
    model_weights = "/content/dirp_neurosymbolic/pytorch-faster-rcnn/mobilenet_v2-b0353104.pth"
    image_path = "/content/dirp_neurosymbolic/pytorch-faster-rcnn/out.png"
    gpu_id = '2'
    num_classes = 80 + 1
    data_root_dir = " "


test_cfg = Config()
