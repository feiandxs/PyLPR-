# 车牌识别系统 (License Plate Recognition System)

## 项目简介 (Project Description)

这是一个基于Python的车牌识别系统，使用OpenCV和机器学习技术实现了对中国车牌的自动识别功能。系统支持对图片和实时视频流中的车牌进行识别，可以识别蓝牌、绿牌、黄牌等多种类型的车牌。

This is a Python-based license plate recognition system that uses OpenCV and machine learning technologies to automatically recognize Chinese license plates. The system supports license plate recognition in both images and real-time video streams, capable of identifying multiple types of plates including blue, green, and yellow plates.

## 功能特点 (Features)

- 支持图片和实时视频流识别 (Support both image and real-time video recognition)
- 支持多种车牌类型 (Support multiple plate types)
- 图形用户界面操作 (Graphical user interface)
- 高精度字符识别 (High-accuracy character recognition)
- 支持车牌颜色识别 (Support plate color recognition)

## 项目结构 (Project Structure)

```
├── main_VLPR.py          # 主程序入口文件 (Main entry file)
├── img_function.py       # 图像处理核心功能 (Core image processing functions)
├── img_math.py           # 图像数学处理函数 (Image mathematical processing)
├── img_recognition.py    # 字符识别实现 (Character recognition implementation)
├── config.py            # 配置文件 (Configuration file)
├── debug.py            # 调试工具 (Debug utilities)
├── delete_files.py     # 文件清理工具 (File cleanup utilities)
├── requirements.txt    # 项目依赖文件 (Project dependencies)
├── svm.dat            # SVM模型文件 (SVM model file)
├── svmchinese.dat     # 中文字符识别模型 (Chinese character recognition model)
├── img/               # 图片资源目录 (Image resources directory)
├── test/              # 测试图片目录 (Test images directory)
│   └── Yes_img/       # 测试结果图片 (Test result images)
└── train/             # 训练数据目录 (Training data directory)
```

## 环境要求 (Requirements)

- Python 3.6+
- OpenCV 4.5.0+
- NumPy 1.19.0+
- scikit-learn 0.24.0+
- Pillow 8.0.0+

## 安装步骤 (Installation)

1. 克隆项目 (Clone the project)
```bash
git clone [repository-url]
cd 车牌识别系统
```

2. 创建并激活虚拟环境 (Create and activate virtual environment)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. 安装依赖 (Install dependencies)
```bash
pip install -r requirements.txt
```

## 使用说明 (Usage)

1. 启动程序 (Start the program)
```bash
python main_VLPR.py
```

2. 功能说明 (Function description)
   - 选择图片文件进行识别 (Select image file for recognition)
   - 启动摄像头实时识别 (Start camera for real-time recognition)
   - 查看识别结果 (View recognition results)

## 识别过程 (Recognition Process)

1. 图像预处理 (Image preprocessing)
   - 灰度化 (Grayscale conversion)
   - 降噪 (Noise reduction)
   - 边缘检测 (Edge detection)

2. 车牌定位 (License plate localization)
   - 轮廓检测 (Contour detection)
   - 矩形矫正 (Rectangle correction)

3. 字符分割 (Character segmentation)
   - 二值化 (Binarization)
   - 连通域分析 (Connected component analysis)

4. 字符识别 (Character recognition)
   - SVM分类 (SVM classification)
   - 字符验证 (Character verification)

## 注意事项 (Notes)

- 确保安装了所有必要的依赖 (Ensure all necessary dependencies are installed)
- 图片要求清晰、光照适中 (Images should be clear with moderate lighting)
- 支持常见的图片格式如jpg、png等 (Supports common image formats like jpg, png)

## 许可证 (License)

本项目采用 MIT 许可证。详情请参见 LICENSE 文件。
This project is licensed under the MIT License. See the LICENSE file for details.
