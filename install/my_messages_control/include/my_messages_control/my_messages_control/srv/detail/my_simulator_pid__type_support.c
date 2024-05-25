// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from my_messages_control:srv/MySimulatorPID.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "my_messages_control/srv/detail/my_simulator_pid__rosidl_typesupport_introspection_c.h"
#include "my_messages_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "my_messages_control/srv/detail/my_simulator_pid__functions.h"
#include "my_messages_control/srv/detail/my_simulator_pid__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  my_messages_control__srv__MySimulatorPID_Request__init(message_memory);
}

void my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_fini_function(void * message_memory)
{
  my_messages_control__srv__MySimulatorPID_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_member_array[3] = {
  {
    "kp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Request, kp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ki",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Request, ki),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "kd",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Request, kd),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_members = {
  "my_messages_control__srv",  // message namespace
  "MySimulatorPID_Request",  // message name
  3,  // number of fields
  sizeof(my_messages_control__srv__MySimulatorPID_Request),
  my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_member_array,  // message members
  my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_type_support_handle = {
  0,
  &my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_my_messages_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID_Request)() {
  if (!my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_type_support_handle.typesupport_identifier) {
    my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &my_messages_control__srv__MySimulatorPID_Request__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "my_messages_control/srv/detail/my_simulator_pid__rosidl_typesupport_introspection_c.h"
// already included above
// #include "my_messages_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "my_messages_control/srv/detail/my_simulator_pid__functions.h"
// already included above
// #include "my_messages_control/srv/detail/my_simulator_pid__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  my_messages_control__srv__MySimulatorPID_Response__init(message_memory);
}

void my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_fini_function(void * message_memory)
{
  my_messages_control__srv__MySimulatorPID_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_member_array[4] = {
  {
    "overshoot",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Response, overshoot),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "d",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Response, d),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ess",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Response, ess),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ts",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_messages_control__srv__MySimulatorPID_Response, ts),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_members = {
  "my_messages_control__srv",  // message namespace
  "MySimulatorPID_Response",  // message name
  4,  // number of fields
  sizeof(my_messages_control__srv__MySimulatorPID_Response),
  my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_member_array,  // message members
  my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_type_support_handle = {
  0,
  &my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_my_messages_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID_Response)() {
  if (!my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_type_support_handle.typesupport_identifier) {
    my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &my_messages_control__srv__MySimulatorPID_Response__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "my_messages_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "my_messages_control/srv/detail/my_simulator_pid__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_members = {
  "my_messages_control__srv",  // service namespace
  "MySimulatorPID",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_Request_message_type_support_handle,
  NULL  // response message
  // my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_Response_message_type_support_handle
};

static rosidl_service_type_support_t my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_type_support_handle = {
  0,
  &my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_my_messages_control
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID)() {
  if (!my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_type_support_handle.typesupport_identifier) {
    my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_messages_control, srv, MySimulatorPID_Response)()->data;
  }

  return &my_messages_control__srv__detail__my_simulator_pid__rosidl_typesupport_introspection_c__MySimulatorPID_service_type_support_handle;
}
