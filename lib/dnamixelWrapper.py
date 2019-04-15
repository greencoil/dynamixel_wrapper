#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dynamixel_sdk import *

DEVICENAME = '/dev/ttyUSB0'
BAUDRATE = 57600

# Control table address
ADDR_PRO_TORQUE_ENABLE = 64
ADDR_PRO_GOAL_POSITION = 116
ADDR_PRO_PRESENT_POSITION = 132
ADDR_PRO_GOAL_VELOCITY = 104
ADDR_PRO_OPERATING_MODE = 11
ADDR_PRO_LED = 65

# Data Byte Length
LEN_PRO_GOAL_POSITION = 4
LEN_PRO_PRESENT_POSITION = 4

DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold


def set_control_mode(packetHandler, portHandler, ID, MODE):
    if MODE == "VELOCITY":
        VALUE = 1
    if MODE == "POSITION":
        VALUE = 3
    if MODE == "EXTENDED_POSITION":
        VALUE = 4
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, ID, ADDR_PRO_OPERATING_MODE, VALUE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        # print("Dynamixel#%d has been successfully connected" % ID)
        pass


def get_control_mode(packetHandler, portHandler, ID):
    mode, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(
            portHandler, ID, ADDR_PRO_OPERATING_MODE)
    
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        # print("Dynamixel#%d has been successfully connected" % ID)
        pass
    return mode


def set_motor_torque(packetHandler, portHandler, ID, STATUS):
    if STATUS:
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, ID, ADDR_PRO_TORQUE_ENABLE, True)
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, ID, ADDR_PRO_LED, True)
    else:
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, ID, ADDR_PRO_TORQUE_ENABLE, False)
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, ID, ADDR_PRO_LED, False)

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        # print("Dynamixel#%d has been successfully connected" % ID)
        pass

# def set_velocity_PI_Gain(ID, P_gain, I_gain):
#     if read_value(control_mode == VELOCITY):
#         set_value(PIgain)
#     else:
#         print("[ERROR]ID:{0} is not VELOCITY_CONTROL MODE ", ID)


# def set_poisition_PID_Gain(ID, P_gain, I_gain, D_gain):
#     if read_value(control_mode == POSITION):
#         set_value(PIgain)
#     else:
#         print("[ERROR]ID:{0} is not VELOCITY_CONTROL MODE ", ID)


def set_goal_velocity(packetHandler, portHandler, ID, VALUE):
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, ID, ADDR_PRO_GOAL_VELOCITY, VALUE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


# def set_velocity_limit(limit_velocity):
#     set_value(ACTION, ID, limit_velocity)


# def set_acceleration_limit(limit_acceleration):
#     set_value(ACTION, ID, limit_acceleration)


def set_goal_pos(packetHandler, portHandler, ID, angle):
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, ID, ADDR_PRO_GOAL_POSITION, angle)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


def get_moving_status(ID):
    pass
    # なんかステータス読む感じ。この辺マルチ版も必要かなぁ…


def get_present_position(ID):
    dxl_present_position, dxl_comm_result, dxl_error\
        = packetHandler.read4ByteTxRx(
            portHandler, DXL_ID, ADDR_PRO_PRESENT_POSITION)
    
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("PresPos:%03d" % (dxl_present_position))
    return dxl_present_position

def get_present_velocity(ID):
    pass


def get_present_temperature(ID):
    pass


if __name__ == '__main__':
    print("SampleProgram")
    portHandler = PortHandler(DEVICENAME)
    packetHandler = PacketHandler(2.0)
    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        quit()

    # Set port baudrate
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        quit()

    while 1:
        # print("Press any key to continue! (or press ESC to quit!)")
        ID = 1

        # この辺からちょっと便利関数。本当は他のファイルから呼び出したい。
        set_motor_torque(packetHandler, portHandler, ID, True)
        # ----------------------------------------------------------------------------
        # set_control_mode(packetHandler, portHandler, ID, "POSITION")
        # set_control_mode(packetHandler, portHandler, ID, "EXTENDED_POSITION")
        # print(get_control_mode(packetHandler, portHandler, ID))
        set_goal_pos(packetHandler, portHandler, ID, 0)
        # ----------------------------------------------------------------------------
        # set_control_mode(packetHandler, portHandler, ID, "VELOCITY")
        # print(get_control_mode(packetHandler, portHandler, ID))
        # set_goal_velocity(packetHandler, portHandler, ID, 50)  # rpm
        time.sleep(5)
        set_motor_torque(packetHandler, portHandler, ID, False)
        # Close port
        portHandler.closePort()
        print("FINISH")
        exit()