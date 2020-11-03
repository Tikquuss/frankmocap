import os, json

config_dic = {
    #"checkpoint" : [str, ""],
    "checkpoint_body_smpl" : [str, "./extra_data/body_module/pretrained_weights/2020_05_31-00_50_43-best-51.749683916568756.pt"],
    "checkpoint_body_smplx" : [str, "./extra_data/body_module/pretrained_weights/smplx-03-28-46060-w_spin_mlc3d_46582-2089_2020_03_28-21_56_16.pt"],
    "checkpoint_hand" : [str, "./extra_data/hand_module/pretrained_weights/pose_shape_best.pth"],
    
    # input options
    "input_path" : [str, None],         
    "start_frame" : [int, 0], 
    "end_frame" : [float, float('inf')], 
    "pkl_dir" : [str, ""],
    
    # output options
    "out_dir" : [str, None], 
    #"pklout":[],
    "save_bbox_output":[bool, False],
    "save_pred_pkl":[bool, False],
    "save_mesh":[bool, False],
    "save_frame":[bool, False], 

    # Other options
    "single_person":[bool, False],
    "no_video_out":[bool, False], 
    "smpl_dir":[str, "./extra_data/smpl/"],
    "skip":[bool, False], 
    "video_url":[str, None],
    "download":[bool, False], 

    # Body mocap specific options
    "use_smplx":[bool, False], 

    # Hand mocap specific options
    "view_type" :[str, "third_view"],
    "crop_type":[str, "no_crop"],

    # Whole motion capture (FrankMocap) specific options
    "frankmocap_fast_mode":[bool, False],

    # renderer
    "renderer_type": [str, "opengl"]
}

def config_file(args) :
    if os.path.isfile(args.config_file):
        with open(args.config_file) as json_data:
            data_dict = json.load(json_data)
            for key, value in data_dict.items():
                conf = config_dic[key]   
                if value == "False":
                    value = False
                elif value == "True" :
                    value = True
                elif value == "float('inf')" :
                    value = float('inf')
                """
                try :
                    setattr(args, key, conf[0](value))
                except :
                    setattr(args, key, value)
                """
                # Allow to overwrite the parameters of the json configuration file.
                try :
                    value = conf[0](value)
                except :
                    pass
                
                if getattr(args, key, conf[1]) == conf[1] :
                    setattr(args, key, value)
    return args


