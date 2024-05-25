// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_messages_control:srv/MySimulatorPID.idl
// generated code does not contain a copyright notice

#ifndef MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__STRUCT_H_
#define MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/MySimulatorPID in the package my_messages_control.
typedef struct my_messages_control__srv__MySimulatorPID_Request
{
  /// estructura de la solicitud de servicio del cliente
  float kp;
  float ki;
  float kd;
} my_messages_control__srv__MySimulatorPID_Request;

// Struct for a sequence of my_messages_control__srv__MySimulatorPID_Request.
typedef struct my_messages_control__srv__MySimulatorPID_Request__Sequence
{
  my_messages_control__srv__MySimulatorPID_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_messages_control__srv__MySimulatorPID_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MySimulatorPID in the package my_messages_control.
typedef struct my_messages_control__srv__MySimulatorPID_Response
{
  /// estructura de la respuesta de sercicio del servidor
  float overshoot;
  float d;
  float ess;
  float ts;
} my_messages_control__srv__MySimulatorPID_Response;

// Struct for a sequence of my_messages_control__srv__MySimulatorPID_Response.
typedef struct my_messages_control__srv__MySimulatorPID_Response__Sequence
{
  my_messages_control__srv__MySimulatorPID_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_messages_control__srv__MySimulatorPID_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__STRUCT_H_
