import subprocess
import time
import os

ADB_PATH = r"C:\Users\lenovo\AppData\Local\Android\Sdk\platform-tools\adb.exe"

class BluetoothLibrary:

    def execute_command(self, command):

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    # -----------------------------------------
    # Validate Android Device Connection
    # -----------------------------------------

    def check_device_connection(self):

        output = self.execute_command(f'"{ADB_PATH}" devices')

        print("\nADB Devices Output:")
        print(output)

        lines = output.splitlines()

        connected_devices = []

        for line in lines[1:]:

            if "\tdevice" in line:
                device_id = line.split("\t")[0]
                connected_devices.append(device_id)

        if len(connected_devices) == 0:
            raise Exception("No Android device connected")

        print(f"\nConnected Devices: {connected_devices}")

        return connected_devices[0]

    # -----------------------------------------
    # Enable Bluetooth
    # -----------------------------------------

    def enable_bluetooth(self):

        print("\nEnabling Bluetooth...")

        command = ( f'"{ADB_PATH}" shell settings put global bluetooth_on 1')

        self.execute_command(command)

        # Wake Bluetooth service
        self.execute_command( f'"{ADB_PATH}" shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE' )

        time.sleep(5)

        print("Bluetooth enable command executed")

    # -----------------------------------------
    # Verify Bluetooth Status
    # -----------------------------------------

    def verify_bluetooth_status(self):

        print("\nVerifying Bluetooth Status...")

        command = ( f'"{ADB_PATH}" shell settings get global bluetooth_on'  )

        output = self.execute_command(command)

        print(f"Bluetooth Raw Status: {output}")

        if output == "1":
            print("Bluetooth is ENABLED")
            return "enabled"

        print("Bluetooth is DISABLED")

        return "disabled"

    # -----------------------------------------
    # Capture Logcat
    # -----------------------------------------

    def capture_logcat(self):

        os.makedirs("logs", exist_ok=True)

        command = (f'"{ADB_PATH}" logcat -d > logs\\bluetooth_log.txt')

        subprocess.run(command, shell=True)

        print("Logs saved to logs/bluetooth_log.txt")

    # -----------------------------------------
    # Disable Bluetooth
    # -----------------------------------------

    def disable_bluetooth(self):

        print("\nDisabling Bluetooth...")

        command = (f'"{ADB_PATH}" shell settings put global bluetooth_on 0')

        self.execute_command(command)

        time.sleep(3)

        print("Bluetooth disabled")