#include <stdio.h>

  int main()
  {
    //const int N = 100000;
    const int N = 100;
    double X[N], Y[N], alpha = 0.5;
    for (int i = 0; i < N; ++i)
    {
      X[i] = i;
      Y[i] = i;
    }

    // Start of daxpy loop
    for (int i = 0; i < N; ++i)
    {
      Y[i] = alpha * X[i] + Y[i];
    }
    // End of daxpy loop

    double sum = 0;
    for (int i = 0; i < N; ++i)
    {
      sum += Y[i];
    }
    printf("%lf\n", sum);
    return 0;
}
