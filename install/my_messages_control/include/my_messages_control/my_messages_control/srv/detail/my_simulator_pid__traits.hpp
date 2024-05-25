// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_messages_control:srv/MySimulatorPID.idl
// generated code does not contain a copyright notice

#ifndef MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__TRAITS_HPP_
#define MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_messages_control/srv/detail/my_simulator_pid__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_messages_control
{

namespace srv
{

inline void to_flow_style_yaml(
  const MySimulatorPID_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: kp
  {
    out << "kp: ";
    rosidl_generator_traits::value_to_yaml(msg.kp, out);
    out << ", ";
  }

  // member: ki
  {
    out << "ki: ";
    rosidl_generator_traits::value_to_yaml(msg.ki, out);
    out << ", ";
  }

  // member: kd
  {
    out << "kd: ";
    rosidl_generator_traits::value_to_yaml(msg.kd, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MySimulatorPID_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: kp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "kp: ";
    rosidl_generator_traits::value_to_yaml(msg.kp, out);
    out << "\n";
  }

  // member: ki
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ki: ";
    rosidl_generator_traits::value_to_yaml(msg.ki, out);
    out << "\n";
  }

  // member: kd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "kd: ";
    rosidl_generator_traits::value_to_yaml(msg.kd, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MySimulatorPID_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_messages_control

namespace rosidl_generator_traits
{

[[deprecated("use my_messages_control::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_messages_control::srv::MySimulatorPID_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_messages_control::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_messages_control::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_messages_control::srv::MySimulatorPID_Request & msg)
{
  return my_messages_control::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_messages_control::srv::MySimulatorPID_Request>()
{
  return "my_messages_control::srv::MySimulatorPID_Request";
}

template<>
inline const char * name<my_messages_control::srv::MySimulatorPID_Request>()
{
  return "my_messages_control/srv/MySimulatorPID_Request";
}

template<>
struct has_fixed_size<my_messages_control::srv::MySimulatorPID_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_messages_control::srv::MySimulatorPID_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_messages_control::srv::MySimulatorPID_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace my_messages_control
{

namespace srv
{

inline void to_flow_style_yaml(
  const MySimulatorPID_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: overshoot
  {
    out << "overshoot: ";
    rosidl_generator_traits::value_to_yaml(msg.overshoot, out);
    out << ", ";
  }

  // member: d
  {
    out << "d: ";
    rosidl_generator_traits::value_to_yaml(msg.d, out);
    out << ", ";
  }

  // member: ess
  {
    out << "ess: ";
    rosidl_generator_traits::value_to_yaml(msg.ess, out);
    out << ", ";
  }

  // member: ts
  {
    out << "ts: ";
    rosidl_generator_traits::value_to_yaml(msg.ts, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MySimulatorPID_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: overshoot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "overshoot: ";
    rosidl_generator_traits::value_to_yaml(msg.overshoot, out);
    out << "\n";
  }

  // member: d
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "d: ";
    rosidl_generator_traits::value_to_yaml(msg.d, out);
    out << "\n";
  }

  // member: ess
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ess: ";
    rosidl_generator_traits::value_to_yaml(msg.ess, out);
    out << "\n";
  }

  // member: ts
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ts: ";
    rosidl_generator_traits::value_to_yaml(msg.ts, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MySimulatorPID_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_messages_control

namespace rosidl_generator_traits
{

[[deprecated("use my_messages_control::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_messages_control::srv::MySimulatorPID_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_messages_control::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_messages_control::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_messages_control::srv::MySimulatorPID_Response & msg)
{
  return my_messages_control::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_messages_control::srv::MySimulatorPID_Response>()
{
  return "my_messages_control::srv::MySimulatorPID_Response";
}

template<>
inline const char * name<my_messages_control::srv::MySimulatorPID_Response>()
{
  return "my_messages_control/srv/MySimulatorPID_Response";
}

template<>
struct has_fixed_size<my_messages_control::srv::MySimulatorPID_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_messages_control::srv::MySimulatorPID_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_messages_control::srv::MySimulatorPID_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_messages_control::srv::MySimulatorPID>()
{
  return "my_messages_control::srv::MySimulatorPID";
}

template<>
inline const char * name<my_messages_control::srv::MySimulatorPID>()
{
  return "my_messages_control/srv/MySimulatorPID";
}

template<>
struct has_fixed_size<my_messages_control::srv::MySimulatorPID>
  : std::integral_constant<
    bool,
    has_fixed_size<my_messages_control::srv::MySimulatorPID_Request>::value &&
    has_fixed_size<my_messages_control::srv::MySimulatorPID_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_messages_control::srv::MySimulatorPID>
  : std::integral_constant<
    bool,
    has_bounded_size<my_messages_control::srv::MySimulatorPID_Request>::value &&
    has_bounded_size<my_messages_control::srv::MySimulatorPID_Response>::value
  >
{
};

template<>
struct is_service<my_messages_control::srv::MySimulatorPID>
  : std::true_type
{
};

template<>
struct is_service_request<my_messages_control::srv::MySimulatorPID_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_messages_control::srv::MySimulatorPID_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__TRAITS_HPP_
