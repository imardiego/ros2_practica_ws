// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_messages_control:srv/MySimulatorPID.idl
// generated code does not contain a copyright notice

#ifndef MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__STRUCT_HPP_
#define MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_messages_control__srv__MySimulatorPID_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_messages_control__srv__MySimulatorPID_Request __declspec(deprecated)
#endif

namespace my_messages_control
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MySimulatorPID_Request_
{
  using Type = MySimulatorPID_Request_<ContainerAllocator>;

  explicit MySimulatorPID_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->kp = 0.0f;
      this->ki = 0.0f;
      this->kd = 0.0f;
    }
  }

  explicit MySimulatorPID_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->kp = 0.0f;
      this->ki = 0.0f;
      this->kd = 0.0f;
    }
  }

  // field types and members
  using _kp_type =
    float;
  _kp_type kp;
  using _ki_type =
    float;
  _ki_type ki;
  using _kd_type =
    float;
  _kd_type kd;

  // setters for named parameter idiom
  Type & set__kp(
    const float & _arg)
  {
    this->kp = _arg;
    return *this;
  }
  Type & set__ki(
    const float & _arg)
  {
    this->ki = _arg;
    return *this;
  }
  Type & set__kd(
    const float & _arg)
  {
    this->kd = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_messages_control__srv__MySimulatorPID_Request
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_messages_control__srv__MySimulatorPID_Request
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MySimulatorPID_Request_ & other) const
  {
    if (this->kp != other.kp) {
      return false;
    }
    if (this->ki != other.ki) {
      return false;
    }
    if (this->kd != other.kd) {
      return false;
    }
    return true;
  }
  bool operator!=(const MySimulatorPID_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MySimulatorPID_Request_

// alias to use template instance with default allocator
using MySimulatorPID_Request =
  my_messages_control::srv::MySimulatorPID_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_messages_control


#ifndef _WIN32
# define DEPRECATED__my_messages_control__srv__MySimulatorPID_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_messages_control__srv__MySimulatorPID_Response __declspec(deprecated)
#endif

namespace my_messages_control
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MySimulatorPID_Response_
{
  using Type = MySimulatorPID_Response_<ContainerAllocator>;

  explicit MySimulatorPID_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->overshoot = 0.0f;
      this->d = 0.0f;
      this->ess = 0.0f;
      this->ts = 0.0f;
    }
  }

  explicit MySimulatorPID_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->overshoot = 0.0f;
      this->d = 0.0f;
      this->ess = 0.0f;
      this->ts = 0.0f;
    }
  }

  // field types and members
  using _overshoot_type =
    float;
  _overshoot_type overshoot;
  using _d_type =
    float;
  _d_type d;
  using _ess_type =
    float;
  _ess_type ess;
  using _ts_type =
    float;
  _ts_type ts;

  // setters for named parameter idiom
  Type & set__overshoot(
    const float & _arg)
  {
    this->overshoot = _arg;
    return *this;
  }
  Type & set__d(
    const float & _arg)
  {
    this->d = _arg;
    return *this;
  }
  Type & set__ess(
    const float & _arg)
  {
    this->ess = _arg;
    return *this;
  }
  Type & set__ts(
    const float & _arg)
  {
    this->ts = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_messages_control__srv__MySimulatorPID_Response
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_messages_control__srv__MySimulatorPID_Response
    std::shared_ptr<my_messages_control::srv::MySimulatorPID_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MySimulatorPID_Response_ & other) const
  {
    if (this->overshoot != other.overshoot) {
      return false;
    }
    if (this->d != other.d) {
      return false;
    }
    if (this->ess != other.ess) {
      return false;
    }
    if (this->ts != other.ts) {
      return false;
    }
    return true;
  }
  bool operator!=(const MySimulatorPID_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MySimulatorPID_Response_

// alias to use template instance with default allocator
using MySimulatorPID_Response =
  my_messages_control::srv::MySimulatorPID_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_messages_control

namespace my_messages_control
{

namespace srv
{

struct MySimulatorPID
{
  using Request = my_messages_control::srv::MySimulatorPID_Request;
  using Response = my_messages_control::srv::MySimulatorPID_Response;
};

}  // namespace srv

}  // namespace my_messages_control

#endif  // MY_MESSAGES_CONTROL__SRV__DETAIL__MY_SIMULATOR_PID__STRUCT_HPP_
