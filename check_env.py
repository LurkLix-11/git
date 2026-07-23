import sys
import platform

print("="*50)
print("Python解释器完整路径：")
print(sys.executable)
print("="*50)
print("Python版本：", sys.version)
print("操作系统：", platform.system(), platform.release())

# 尝试检测MindSpore（如果你要用昇思框架）
try:
    import mindspore
    print("\n✅ 检测到MindSpore，版本：", mindspore.__version__)
except ModuleNotFoundError:
    print("\n❌ 当前环境未安装MindSpore")