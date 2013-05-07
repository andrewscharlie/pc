#include <iterator>
#include <string>
#include <cstdio>
#include <sstream>

template <class T>
std::string toString(T container) {
  std::stringstream ss;
  typename T::iterator first = container.begin(), last = container.end();
  ss << "{";

  while (first != last) {
    ss << (*first);

    if (++first != last) {
      ss << ", ";
    }
  }


  ss << "}";
  return ss.str();
}
