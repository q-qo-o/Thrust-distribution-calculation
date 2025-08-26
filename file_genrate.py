import numpy as np


h_file_header = """
#ifndef __THRUST_ALLOCATE_H
#define __THRUST_ALLOCATE_H

#pragma pack(push)
#pragma pack(1)


#include "coordinate_conversion.h"

"""

h_file_struct = """
/**
 * @brief   推力分配\n
 *          将推力分配给电机，考虑广义推力必为一六维向量，推力矩阵必定为6列的。
 *
 */
typedef struct {
    float x_cf;  // X轴上分配推力的参数
    float y_cf;  // Y轴上分配推力的参数
    float z_cf;  // Z轴上分配推力的参数
    float rx_cf; // X轴上分配扭矩的参数
    float ry_cf; // Y轴上分配扭矩的参数
    float rz_cf; // Z轴上分配扭矩的参数
} ThrustAllocate;


"""

h_file_extern = """
#extern ThrustAllocate thrust_matrix
"""


h_file_func = """
void  ThrustAllocate_InitfromParams(ThrustAllocate *p_ta, float x_cf, float y_cf, float z_cf, float rx_cf, float ry_cf, float rz_cf);
float ThrustAllocate_AllocatefromVector6d(ThrustAllocate *p_ta, Vector6d *t);


"""

h_file_end = """
#pragma pack(pop)


#endif
"""


c_file_header = """
#include "thrust_allocate.h"


#include <stdlib.h>
#include <stdio.h>
#include <math.h>


"""


c_file_func = """
/**
 * @brief 根据参数初始化推进器对应的推力分配器
 *
 * @param p_ta 推进器对应的推力分配器
 * @param x_cf X轴上分配推力的参数
 * @param y_cf Y轴上分配推力的参数
 * @param z_cf Z轴上分配推力的参数
 * @param rx_cf X轴上分配扭矩的参数
 * @param ry_cf Y轴上分配扭矩的参数
 * @param rz_cf Z轴上分配扭矩的参数
 */
void ThrustAllocate_InitfromParams(ThrustAllocate *p_ta, float x_cf, float y_cf, float z_cf, float rx_cf, float ry_cf, float rz_cf)
{
    p_ta->x_cf  = x_cf;
    p_ta->y_cf  = y_cf;
    p_ta->z_cf  = z_cf;
    p_ta->rx_cf = rx_cf;
    p_ta->ry_cf = ry_cf;
    p_ta->rz_cf = rz_cf;
}


/**
 * @brief 根据输入的广义力分配扭矩
 *
 * @param p_ta 推进器对应的推力分配器
 * @param t 六维广义力
 * @return float
 */
float ThrustAllocate_AllocatefromVector6d(ThrustAllocate *p_ta, Vector6d *t)
{
    float thrust = 0;

    thrust += t->x * p_ta->x_cf;
    thrust += t->y * p_ta->y_cf;
    thrust += t->z * p_ta->z_cf;
    thrust += t->rx * p_ta->rx_cf;
    thrust += t->ry * p_ta->ry_cf;
    thrust += t->rz * p_ta->rz_cf;

    return thrust;
}
"""


init_func_header = """
/**
 * @brief 推力分配矩阵参数初始化
 *
 */
void ThrustAllocateInit(void)
{

"""

init_func_line_header = ""


init_func_end = """

}
"""


def generate_files(root_path, thrust_matrix):
    # 清空数据
    with open(root_path + "/thrust_allocate.c", "w") as f:
        f.write("")
    with open(root_path + "/thrust_allocate.h", "w") as f:
        f.write("")

    propeller_nums, _ = thrust_matrix.shape

    init_func = init_func_header

    for i in range(propeller_nums):
        init_func += f"ThrustAllocate_InitfromParams(&thrust_matrix[{i}]"
        init_func += f",{thrust_matrix[i][0]:f}"
        init_func += f",{thrust_matrix[i][1]:f}"
        init_func += f",{thrust_matrix[i][2]:f}"
        init_func += f",{thrust_matrix[i][3]:f}"
        init_func += f",{thrust_matrix[i][4]:f}"
        init_func += f",{thrust_matrix[i][5]:f}"
        init_func += ");\n"
    init_func += init_func_end

    with open(root_path + "/thrust_allocate.c", "a+b") as f:
        f.write(c_file_header.encode())
        f.write(f"ThrustAllocate thrust_matrix[MOTOR_NUM];".encode())
        f.write(c_file_func.encode())
        f.write(init_func.encode())

    with open(root_path + "/thrust_allocate.h", "a+b") as f:
        f.write(h_file_header.encode())
        f.write(f"#define MOTOR_NUM {propeller_nums:d} \r\n\r\n".encode())
        f.write(h_file_struct.encode())
        f.write(h_file_func.encode())
        f.write(h_file_end.encode())
