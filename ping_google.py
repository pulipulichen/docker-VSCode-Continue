import subprocess

def ping_google():
    """
    嘗試對 Google 的公共 DNS 伺服器 (8.8.8.8) 執行 ping 操作。
    此函數會執行系統的 ping 命令，並檢查其回傳碼以判斷 ping 是否成功。

    回傳:
        bool: 如果 ping 成功，則回傳 True；否則回傳 False。
    """
    try:
        # 執行 ping 命令。在大多數系統上，-c 1 表示只發送一個封包。
        # 在 Windows 上，可能是 -n 1。為了跨平台兼容性，這裡假設為 Linux/macOS。
        # 如果需要支援 Windows，可能需要額外的邏輯來判斷作業系統。
        # timeout 參數確保命令不會無限期等待。
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True, timeout=5)
        
        # 檢查回傳碼。0 通常表示成功。
        if result.returncode == 0:
            print("Ping Google 成功。")
            return True
        else:
            print(f"Ping Google 失敗。回傳碼: {result.returncode}")
            print(f"標準輸出:\n{result.stdout}")
            print(f"標準錯誤:\n{result.stderr}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"執行 ping 命令時發生錯誤: {e}")
        print(f"標準輸出:\n{e.stdout}")
        print(f"標準錯誤:\n{e.stderr}")
        return False
    except FileNotFoundError:
        print("錯誤: 'ping' 命令未找到。請確認您的系統已安裝 ping 工具。")
        return False
    except Exception as e:
        print(f"發生未知錯誤: {e}")
        return False

if __name__ == "__main__":
    if ping_google():
        print("與 Google 的連線正常。")
    else:
        print("無法連線到 Google。")
