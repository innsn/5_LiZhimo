CUDA_VISIBLE_DEVICES=1
#!/bin/bash
cd /project/train/src_repo
# pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

python train.py --labels_txt=/project/train/models/label.txt --save_model=/project/train/models/detect --batchsize=16 --net_type=yolov5s --epochs=10 --pretrained=coco_pretrained/yolov5s.pth --resume

python export_onnx.py --pth=/project/train/models/detect/best.pth --onnx_path=/project/train/models/detect/best.onnx --labels_txt=/project/train/models/label.txt --net_type=yolov5s
cp /project/train/models/detect/train_log.jpg /project/train/result-graphs/
#python -m onnxsim demobilized_weights/best.onnx demobilized_weights/best_sim.onnx
