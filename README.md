## PowerShellpython激活虚拟环境

```powershell
./.venv/Scripts/Activate.ps1

deactivate
```
## Linux下安装python库

使用linux环境`pip`安装库时可能会被阻止，因为Python 现在阻止直接使用 pip 安装系统级别的包，以防止破坏系统依赖。

### 使用虚拟环境
```bash
sudo apt update
sudo apt install python3-venv

# 创建虚拟环境
python3 -m venv ~/myenv

# 激活虚拟环境
source ~/myenv/bin/activate

# 现在可以安全安装 pytest
pip install pytest

# 验证安装
pytest --version

# 退出虚拟环境
deactivate
```

### 使用包管理器

```bash
sudo apt install python3-pytest
```