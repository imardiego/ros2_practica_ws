// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_messages_control:srv/MySimulatorPID.idl
// generated code does not contain a copyright notice

#ifndef MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__BUILDER_HPP_
#define MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_messages_control/srv/detail/my_simulator_pid__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_messages_control
{

namespace srv
{

namespace builder
{

class Init_MySimulatorPID_Request_kd
{
public:
  explicit Init_MySimulatorPID_Request_kd(::my_messages_control::srv::MySimulatorPID_Request & msg)
  : msg_(msg)
  {}
  ::my_messages_control::srv::MySimulatorPID_Request kd(::my_messages_control::srv::MySimulatorPID_Request::_kd_type arg)
  {
    msg_.kd = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Request msg_;
};

class Init_MySimulatorPID_Request_ki
{
public:
  explicit Init_MySimulatorPID_Request_ki(::my_messages_control::srv::MySimulatorPID_Request & msg)
  : msg_(msg)
  {}
  Init_MySimulatorPID_Request_kd ki(::my_messages_control::srv::MySimulatorPID_Request::_ki_type arg)
  {
    msg_.ki = std::move(arg);
    return Init_MySimulatorPID_Request_kd(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Request msg_;
};

class Init_MySimulatorPID_Request_kp
{
public:
  Init_MySimulatorPID_Request_kp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MySimulatorPID_Request_ki kp(::my_messages_control::srv::MySimulatorPID_Request::_kp_type arg)
  {
    msg_.kp = std::move(arg);
    return Init_MySimulatorPID_Request_ki(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_messages_control::srv::MySimulatorPID_Request>()
{
  return my_messages_control::srv::builder::Init_MySimulatorPID_Request_kp();
}

}  // namespace my_messages_control


namespace my_messages_control
{

namespace srv
{

namespace builder
{

class Init_MySimulatorPID_Response_ts
{
public:
  explicit Init_MySimulatorPID_Response_ts(::my_messages_control::srv::MySimulatorPID_Response & msg)
  : msg_(msg)
  {}
  ::my_messages_control::srv::MySimulatorPID_Response ts(::my_messages_control::srv::MySimulatorPID_Response::_ts_type arg)
  {
    msg_.ts = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Response msg_;
};

class Init_MySimulatorPID_Response_ess
{
public:
  explicit Init_MySimulatorPID_Response_ess(::my_messages_control::srv::MySimulatorPID_Response & msg)
  : msg_(msg)
  {}
  Init_MySimulatorPID_Response_ts ess(::my_messages_control::srv::MySimulatorPID_Response::_ess_type arg)
  {
    msg_.ess = std::move(arg);
    return Init_MySimulatorPID_Response_ts(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Response msg_;
};

class Init_MySimulatorPID_Response_d
{
public:
  explicit Init_MySimulatorPID_Response_d(::my_messages_control::srv::MySimulatorPID_Response & msg)
  : msg_(msg)
  {}
  Init_MySimulatorPID_Response_ess d(::my_messages_control::srv::MySimulatorPID_Response::_d_type arg)
  {
    msg_.d = std::move(arg);
    return Init_MySimulatorPID_Response_ess(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Response msg_;
};

class Init_MySimulatorPID_Response_overshoot
{
public:
  Init_MySimulatorPID_Response_overshoot()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MySimulatorPID_Response_d overshoot(::my_messages_control::srv::MySimulatorPID_Response::_overshoot_type arg)
  {
    msg_.overshoot = std::move(arg);
    return Init_MySimulatorPID_Response_d(msg_);
  }

private:
  ::my_messages_control::srv::MySimulatorPID_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_messages_control::srv::MySimulatorPID_Response>()
{
  return my_messages_control::srv::builder::Init_MySimulatorPID_Response_overshoot();
}

}  // namespace my_messages_control

#endif  // MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__BUILDER_HPP_
