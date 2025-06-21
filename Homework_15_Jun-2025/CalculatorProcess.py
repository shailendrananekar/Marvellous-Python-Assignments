import psutil
import subprocess
import schedule
import time


def is_process_running(processname):
    for proc in psutil.process_iter(["name"]):
        if processname in proc.info["name"]:
            return True

    return False


def CalculatorStart(name="CalculatorApp.exe", executable="Calc.exe"):
    if not is_process_running(name):
        print(f"{name} is starting the process...")
        subprocess.Popen([executable], shell=True)


def main():
    schedule.every(1).minutes.do(CalculatorStart)
    # CalculatorStart("Calc.exe")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
