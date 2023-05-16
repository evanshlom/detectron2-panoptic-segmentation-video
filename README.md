## Detectron2 Panoptic Segmentation Demo
- Image panoptic segmentation and video panoptic segmentation
- To run:
    1. Clone repository.
    2. Follow environment setup instructions below,
    3. Run "python main.py" in the terminal!

## Environment Setup
- Credit: M. Haroon Shakeel (Medium: https://medium.com/@haroonshakeel/detectron2-setup-on-windows-10-and-linux-407e5382df1)
- Instructions: (estimated time to complete: 5 minutes)
    1. Download and Install Anaconda
    2. Open Anaconda Prompt and create a new virtual environment by using the command: conda create -n detectron_env python=3.8
    3. Activate the environment: conda activate detectron_env
    4. Once done, install cython pip install cython
    5. Install Pytorch and CUDA: conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
    6. Clone Detectron2 repository: git clone https://github.com/facebookresearch/detectron2.git
    7. Got to the downloaded repository folder: cd detectron2
    8. Install dependencies: pip install -e .
    9. Then install OpenCV pip install opencv-python