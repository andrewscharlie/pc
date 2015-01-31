template<typename T>
T **newArray2d(int d1, int d2) {
  T **array = new T*[d1];

  for (int i = 0; i < d1; ++i)
    array[i] = new T[d2];

  return array;
}

template<typename T>
T **newArray2d(int d1, int d2, T initialValue) {
  T **array = newArray2d<T>(d1, d2);

  for (int i = 0; i < d1; ++i)
    for (int j = 0; j < d2; ++j)
      array[i][j] = initialValue;
  
  return array;
}
}
template<typename T>
void deleteArray2d(T **array, int d1) {
  for (int i = 0; i < d1; ++i) {
    delete []array[i];
  }

  delete []array;
}
